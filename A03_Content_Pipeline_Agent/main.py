from crewai.flow.flow import Flow, listen, start, router, and_, or_
from crewai import Agent
from pydantic import BaseModel


class ContentPipelineState(BaseModel):

    # Inputs
    content_type: str = ""
    topic: str = ""

    # Internal
    max_length: int = 0


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
        print("Researching....")
        return True

    @router(conduct_research)
    def router(self):

        content_type = self.state.content_type

        if content_type == "blog":
            return "make_blog"
        elif content_type == "tweet":
            return "make_tweet_post"
        else:
            return "make_linkedin_post"

    @listen("make_blog")
    def handle_make_blog(self):
        print("Making blog post ...")

    @listen("make_tweet_post")
    def handle_make_tweet_post(self):
        print("Making tweet post ...")

    @listen("make_linkedin_post")
    def handle_make_linkedin_post(self):
        print("Making linkedin post ...")



    @listen(handle_make_blog)
    def check_seo(self):
        print("Checking Blog SEO")

    @listen(or_(handle_make_tweet_post, handle_make_linkedin_post))
    def check_virality(self):
        print("Checking Virality")


    @listen(or_(check_virality, check_seo))
    def finlize_content(self):
        print("Finalizing content")

flow = ContentPipelineFlow()


flow.plot()