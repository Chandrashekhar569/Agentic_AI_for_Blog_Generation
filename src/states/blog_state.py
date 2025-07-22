"""
=============================================
            Blog State File
=============================================
* This file defines the structure for maintaining blog-related state data
  across LangGraph workflows using Pydantic and TypedDict.

* Key Responsibilities:
  - Structures the blog payload with title and content fields via `Blog` model
  - Defines `BlogState` to track input topic, generated blog, and target language
  - Enables type-safe manipulation and routing within graph nodes

## Class: Blog (Pydantic Model)
* Schema enforcing content format and descriptions for blog generation

## Class: BlogState (TypedDict)
* Represents flow state with keys:
  - `topic`: input topic used to generate blog
  - `blog`: validated blog output (title + content)
  - `current_language`: language for translation or routing
_____________________________________________
"""


from typing import TypedDict
from pydantic import BaseModel, Field

class Blog(BaseModel):
    title:str=Field(description="The title of the blog post")
    content:str=Field(description="The main content of the blog post")


class BlogState(TypedDict):
    topic:str
    blog:Blog
    current_language:str