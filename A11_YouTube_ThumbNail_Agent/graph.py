import base64
import operator, textwrap, dotenv

dotenv.load_dotenv()

from langchain.chat_models import init_chat_model
from langgraph.types import Send, interrupt
from typing_extensions import Annotated

from langgraph.graph import END, START, StateGraph
from typing import TypedDict
import subprocess

# 오픈 AI 직접 사용 하는 방식.
from openai import OpenAI

llm = init_chat_model("openai:gpt-4o-mini")


class State(TypedDict):
    video_file: str
    audio_file: str
    transcription: str
    summaries: Annotated[list[str], operator.add]
    thumbnail_prompt: Annotated[list[str], operator.add]
    thumbnail_sketches: Annotated[list[str], operator.add]
    mega_summarys: str
    user_feedback: str
    chosen_prompt: str


def extract_audio(state: State):
    output_file = state["video_file"].replace(".mp4", ".mp3")
    command = [
        "ffmpeg",
        "-i",
        state["video_file"],
        "-filter:a",
        "atempo=2.0",
        "-y",
        output_file,
    ]
    subprocess.run(command)
    return {
        "audio_file": output_file,
    }


def transcribe_audio(state: State):
    client = OpenAI()
    with open(state["audio_file"], "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            response_format="text",
            file=audio_file,
            language="ko",
            prompt="유발하라리, 넥서스, 책 요약"
        )
        return {
            "transcription": transcription
        }


def dispatch_summarizers(state: State):
    transcription = state["transcription"]
    chunks = []
    for i, chunk in enumerate(textwrap.wrap(transcription, 500)):
        chunks.append({
            "id": i + 1,
            "chunk": chunk
        })
    return [Send("summarize_chunk", chunk) for chunk in chunks]


def summarize_chunk(chunk):
    chunk_id = chunk["id"]
    chunk_text = chunk["chunk"]
    response = llm.invoke(
        f"""
        이 텍스트들을 보기좋게 요약을 해주세요. 한국어 입니다.
        텍스트: {chunk_text}
        """
    )
    summary = f"[Chunk {chunk_id}] {response.content}"
    return {
        "summaries": [summary]
    }


def mega_summary(state: State):
    all_summaries = "/n".join(state["summaries"])
    prompt = f"""
    요약본을 바탕으로 핵심키워드를 추출해서 요약본을 설명하는 요약본을 만들어줘 약 500자 내외면 좋겠어.
    요약본:{all_summaries}
    """
    response = llm.invoke(prompt)
    return {"mega_summarys": response.content}


def dispatch_artists(state: State):
    return [
        Send(
            "generate_thumbnail", {
                "id": i,
                "summary": state["mega_summarys"]
            }
        ) for i in [1, 2, 3]
    ]


def generate_thumbnail(args):
    concept_id = args["id"]
    summary = args["summary"]

    prompt = f"""
    이 요약본을 바탕으로, GPT images 생성기에 입력할 유튜브 썸네일을 만들기 위한 프롬프트를 만들어줘,
    - 핵심적인 시각적 요소가 2~3개 포함되어야 하고 너무 많은 요소가 들어가지 않도록 해줘,
    - 색상의 균형이 중요해,
    - 타이틀이 들어갈 위치에 핵심키워드를 넣어줘.
    요약본 : {summary}
    """

    response = llm.invoke(prompt)

    thumbnail_prompt = response.content

    client = OpenAI()

    result = client.images.generate(
        model="gpt-image-1",
        prompt=thumbnail_prompt,
        quality="low",
        moderation="low",
        size="auto"
    )

    image_bytes = base64.b64decode(result.data[0].b64_json)
    filename = f"thumbnail_{concept_id}.jpg"

    with open(filename, "wb") as file:
        file.write(image_bytes)

    return {
        "thumbnail_prompt": [thumbnail_prompt],
        "thumbnail_sketches": [filename],
    }


def human_feedback(state: State):
    answer = interrupt(
        {
            "chosen_thumbnail": "어떤 썸네일이 제일 마음에 드시나요? ",
            "feedback": "최종 썸네일을 제작하기 위한 피드백을 주세요"
        }
    )
    user_feedback = answer["user_feedback"]
    chosen_prompt = answer["chosen_prompt"]
    return {
        "user_feedback": user_feedback,
        "chosen_prompt": state["thumbnail_prompt"][chosen_prompt - 1],
    }


def generate_hd_thumbnail(state: State):
    chosen_prompt = state["chosen_prompt"]
    user_feedback = state["user_feedback"]

    prompt = f"""
    당신은 전문 유튜브 썸네일 디자이너입니다. 원본 썸네일 프롬프트를 가지고 사용자의 구체적인 피드백을 통합하여 개선된 버전을 만드세요.

    **원본 프롬프트 (ORIGINAL PROMPT):**
    {chosen_prompt}

    **통합할 사용자 피드백 (USER FEEDBACK TO INCORPORATE):**
    {user_feedback}

    다음과 같은 내용을 담아 개선된 프롬프트를 만드세요:
    1.  원본 프롬프트의 **핵심 개념을 유지**합니다.
    2.  사용자가 요청한 피드백을 **구체적으로 다루고 구현**합니다.
    3.  전문 유튜브 썸네일 제작 사양을 추가합니다:
        * **고대비** 및 **굵고 선명한 시각적 요소**
        * 시선을 사로잡는 **명확한 초점**
        * **전문적인 조명과 구도**
        * 가장자리에서 충분히 떨어지도록 **여백(패딩)을 넉넉하게 적용**한 **최적의 텍스트 배치 및 가독성**
        * **주목을 끄는 톡톡 튀는 색상**
        * **작은 썸네일 크기에서도 잘 작동하는 요소**
        * **중요:** **항상** 텍스트와 이미지 경계 사이에 **충분한 여백/패딩을 확보**하세요.
    """

    hd_response = llm.invoke(prompt)

    final_thumbnail_prompt = hd_response.content

    client = OpenAI()

    result = client.images.generate(
        model="gpt-image-1",
        prompt=final_thumbnail_prompt,
        quality="high",
        moderation="low",
        size="auto",
    )

    image_bytes = base64.b64decode(result.data[0].b64_json)

    with open("thumbnail_final.jpg", "wb") as file:
        file.write(image_bytes)


graph_builder = StateGraph(State)

(
    graph_builder

    .add_node("extract_audio", extract_audio)
    .add_node("transcribe_audio", transcribe_audio)
    .add_node("dispatch_summarizers", dispatch_summarizers)
    .add_node("summarize_chunk", summarize_chunk)
    .add_node("mega_summary", mega_summary)
    .add_node("dispatch_artists", dispatch_artists)
    .add_node("generate_thumbnail", generate_thumbnail)
    .add_node("human_feedback", human_feedback)
    .add_node("generate_hd_thumbnail", generate_hd_thumbnail)

    .add_edge(START, "extract_audio")
    .add_edge("extract_audio", "transcribe_audio")
    .add_conditional_edges("transcribe_audio", dispatch_summarizers, ["summarize_chunk"])
    .add_edge("summarize_chunk", "mega_summary")
    .add_conditional_edges("mega_summary", dispatch_artists, ["generate_thumbnail"])
    .add_edge("generate_thumbnail", "human_feedback")
    .add_edge("human_feedback", "generate_hd_thumbnail")
    .add_edge("generate_hd_thumbnail", END)
)

graph = graph_builder.compile(name="mr_thumbs")
