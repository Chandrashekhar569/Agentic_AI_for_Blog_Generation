from typing import TypedDict
from pydantic import BaseModel, Field

class Blog(BaseModel):
    """
    Blog post structure with title and content.

    Attributes:
        title (str): The blog post's headline.
        content (str): The body of the blog post.
    """
    title: str = Field(description="The title of the blog post")
    content: str = Field(description="The main content of the blog post")


class BlogState(TypedDict):
    """
    Represents the state during blog generation and processing.

    Attributes:
        topic (str): The input topic used to generate the blog.
        blog (Blog): The validated blog post with title and content.
        current_language (str): The language to be used for translation or routing.
    """
    topic: str
    blog: Blog
    current_language: str
