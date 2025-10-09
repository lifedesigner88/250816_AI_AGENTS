import vertexai, dotenv, os

dotenv.load_dotenv()

from vertexai.preview import reasoning_engines

from travel_advisor_agent.agent import travel_advisor_agent

PROJECT_ID = "sejongclass"
LOCATION = "asia-northeast1"
BUCKET = "gs://weather_agent_88"

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=BUCKET,
)

app = reasoning_engines.AdkApp(
    agent=travel_advisor_agent,
    enable_tracing=True,
)

remote_app = vertexai.agent_engines.create(
    display_name="Travel Advisor Agent",
    agent_engine=app,
    requirements=[
        "google-cloud-aiplatform[adk,agent-engines]",
        "litellm",
    ],
    extra_packages=[
        "travel_advisor_agent"
    ],
    env_vars={
        "OPENAI_API_KEY": os.environ["OPENAI_API_KEY"],
    }
)
