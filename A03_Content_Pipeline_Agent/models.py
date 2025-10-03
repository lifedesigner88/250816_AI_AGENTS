from pydantic import BaseModel
from typing import List


class BlogPost(BaseModel):
    title: str = ""
    subtitle: str = ""
    sections: List[str]


class Tweet(BaseModel):
    content: str = ""
    hashtags: str = ""


class LinkedInPost(BaseModel):
    hook: str = ""
    content: str = ""
    call_to_action: str = ""


class Score(BaseModel):
    score: int = 0
    reason: str = ""


class ContentPipelineState(BaseModel):
    # Inputs
    content_type: str = ""
    topic: str = ""

    # Internal
    max_length: int = 0
    research: str = ""
    score: Score | None = None

    # Content
    blog_post: BlogPost | None = None
    tweet: Tweet | None = None
    linkedin_post: LinkedInPost | None = None