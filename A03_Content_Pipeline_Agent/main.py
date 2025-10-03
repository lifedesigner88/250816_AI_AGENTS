from crewai.flow.flow import Flow, listen, start, router, and_, or_
from crewai import Agent
from crewai import LLM
from models import BlogPost, Tweet, LinkedInPost, ContentPipelineState

from tools import web_search_tool
from seo_crew import SeoCrew
from virality_crew import ViralityCrew


class ContentPipelineFlow(Flow[ContentPipelineState]):

    @start()
    def init_content_pipeline(self):
        if self.state.content_type not in ["tweet", "blog", "linkedin"]:
            raise ValueError("The content type is wrong.")

        if self.state.topic == "":
            raise ValueError("The topic cant't be blank.")

        if self.state.content_type == "tweet":
            self.state.max_length = 150
        elif self.state.content_type == "blog":
            self.state.max_length = 800
        elif self.state.content_type == "linkedin":
            self.state.max_length = 500

    @listen(init_content_pipeline)
    def conduct_research(self):

        researcher = Agent(
            role="Head Researcher",
            backstory="You're like a digital detective who loves digging up fascinationg facts and insights, You have a knack for finding the good stuff that others miss.",
            goal=f"Find the most interesting and useful info about {self.state.topic}",
            tools=[web_search_tool]
        )
        self.state.research = researcher.kickoff(
            f"Find the most interesting and useful info about {self.state.topic}"
        ).raw
        return True

    @router(conduct_research)
    def conduct_research_router(self):
        content_type = self.state.content_type
        if content_type == "blog":
            return "make_blog"
        elif content_type == "tweet":
            return "make_tweet_post"
        else:
            return "make_linkedin_post"

    @listen(or_("make_blog", "remake_blog"))
    def handle_make_blog(self):

        blog_post = self.state.blog_post

        llm = LLM(model="openai/o4-mini", response_format=BlogPost)

        if blog_post is None:
            response = llm.call(
                f"""
                You are a science blogger.
                Write a blog post on the topic: {self.state.topic}
    
                Use the following research as your source material:
                <research>
                ===================
                {self.state.research}
                ===================
                </research>
    
                Requirements:
                1. Length: around 800 length
                2. Tone: friendly and accessible, for a high school audience
                3. Structure: introduction → main explanation → examples → conclusion
                4. Format: Markdown
                5. At the end, include 3 bullet-point key takeaways
                """
            )
        else:
            response = llm.call(
                f"""
                You previously wrote a blog post on the topic: {self.state.topic}.  
                However, it has a low SEO score because of the following issue: {self.state.score.reason}.  

                Your task is to **revise and improve the blog post** to achieve a better SEO score, while keeping it clear and engaging.

                Here is the current blog post:
                <blog_post>
                {self.state.blog_post.model_dump_json()}
                </blog_post>

                Use the following research as supporting material:
                <research>
                ================
                {self.state.research}
                ================
                </research>

                Requirements:
                1. Improve SEO (e.g., keyword placement, headings, meta description, internal/external linking suggestions).
                2. Maintain readability for a general audience.
                3. Keep the structure: introduction → main body → conclusion.
                4. Output in Markdown format.
                5. At the end, include a short list of suggested SEO keywords.
                """
            )
        self.state.blog_post = BlogPost.model_validate_json(response)

    @listen(or_("make_tweet_post", "remake_tweet"))
    def handle_make_tweet_post(self):
        tweet = self.state.tweet
        llm = LLM(model="openai/o4-mini", response_format=Tweet)

        if tweet is None:
            response = llm.call(
                f"""
                You are a best tweeter specialized in viral.
                Write a tweet on the topic: {self.state.topic}

                Use the following research as your source material:
                <research>
                ===================
                {self.state.research}
                ===================
                </research>

                Requirements:
                1. Length: around 150 length
                2. Tone: friendly and accessible, for a high school audience
                """
            )
        else:
            response = llm.call(
                f"""
                You previously wrote a tweet on the topic: {self.state.topic}.  
                However, it has a low virality score because of the following reason: {self.state.score.reason}.  

                Your task is to **revise and improve the tweet** to achieve a better viral score, while keeping it clear and engaging.

                Here is the current tweet post:
                <tweet>
                {self.state.tweet.model_dump_json()}
                </tweet>

                Use the following research as supporting material:
                <research>
                ================
                {self.state.research}
                ================
                </research>

                Requirements:
                1. Improve virality (e.g., Hook strength, Emotional resonance, Shareability factor).
                2. Maintain readability for a general audience.
                """
            )

        self.state.tweet = Tweet.model_validate_json(response)

    @listen(or_("make_linkedin_post", "remake_linkedin_post"))
    def handle_make_linkedin_post(self):
        linkedin_post = self.state.linkedin_post
        llm = LLM(model="openai/o4-mini", response_format=LinkedInPost)

        if linkedin_post is None:
            response = llm.call(
                f"""
                You are a best in linkedin postiong specialized in trusting content.
                Write a linkedin_post on the topic: {self.state.topic}

                Use the following research as your source material:

                <research>
                ===================
                {self.state.research}
                ===================
                </research>

                Requirements:
                1. Length: around 150 length
                2. Tone: friendly and accessible, for a high school audience
                """
            )
        else:
            response = llm.call(
                f"""
                You previously wrote a linkedin_post on the topic: {self.state.topic}.  
                However, it has a low virality score because of the following reason: {self.state.score.reason}.  

                Your task is to **revise and improve the linkedin_post** to achieve a better viral score, while keeping it clear and engaging.

                Here is the current linkedin_post post:
                <linkedin_post>
                {self.state.linkedin_post.model_dump_json()}
                </linkedin_post>

                Use the following research as supporting material:
                <research>
                ================
                {self.state.research}
                ================
                </research>

                 Requirements:
                 1. Improve virality (e.g., Hook strength, Emotional resonance, Shareability factor).
                 2. Maintain readability for a general audience.
                 """
            )
        self.state.linkedin_post = LinkedInPost.model_validate_json(response)

    @listen(handle_make_blog)
    def check_seo(self):
        result = SeoCrew().crew().kickoff(
            inputs={
                "topic": self.state.topic,
                "blog_post": self.state.blog_post.model_dump_json()
            }
        )
        self.state.score = result.pydantic

    @listen(or_(handle_make_tweet_post, handle_make_linkedin_post))
    def check_virality(self):
        result = ViralityCrew().crew().kickoff(
            inputs={
                "topic": self.state.topic,
                "content_type": self.state.content_type,
                "content": self.state.tweet.model_dump_json() if self.state.content_type == "tweet" else self.state.linkedin_post.model_dump_json()
            }
        )
        self.state.score = result.pydantic

    @router(or_(check_virality, check_seo))
    def score_router(self):
        content_type = self.state.content_type
        score = self.state.score.score

        if score >= 7:
            return "check_passed"

        if content_type == "blog":
            return "remake_blog"
        elif content_type == "linkedin":
            return "remake_linkedin_post"
        else:
            return "remake_tweet"

    @listen("check_passed")
    def finalize_content(self):
        """Finalize the content"""
        print("🎉 Finalizing content...")

        if self.state.content_type == "blog":
            print(f"📝 Blog Post: {self.state.blog_post}")
            print(f"🔍 SEO Score: {self.state.score.score}/100")
        elif self.state.content_type == "tweet":
            print(f"🐦 Tweet: {self.state.tweet}")
            print(f"🚀 Virality Score: {self.state.score.score}/100")
        elif self.state.content_type == "linkedin":
            print(f"💼 LinkedIn: {self.state.linkedin_post}")
            print(f"🚀 Virality Score: {self.state.score.score}/100")

        print("✅ Content ready for publication!")
        return (
            self.state.linkedin_post
            if self.state.content_type == "linkedin"
            else (
                self.state.tweet
                if self.state.content_type == "tweet"
                else self.state.blog_post
            )
        )


flow = ContentPipelineFlow()

flow.kickoff(
    inputs={
        "content_type": "tweet",
        "topic": "Chat GPT and K-culture"
    }
)
flow.kickoff(
    inputs={
        "content_type": "blog",
        "topic": "Chat GPT and K-culture"
    }
)

flow.kickoff(
    inputs={
        "content_type": "linkedin",
        "topic": "Chat GPT and K-culture"
    }
)

# flow.plot()

