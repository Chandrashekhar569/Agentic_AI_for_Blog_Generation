from src.states.blog_state import BlogState
from langchain_core.messages import SystemMessage, HumanMessage
from src.states.blog_state import Blog


class BlogNode:
    """
    A class that defines the core nodes for LangGraph blog generation flow.

    This class contains logic for generating a title, full content, language translation,
    and routing decisions for translation workflows.

    Attributes:
        llm: The language model used for content generation and translation.
    """

    def __init__(self, llm):
        """
        Initialize BlogNode with a language model.

        Args:
            llm: A language model instance with `.invoke()` method.
        """
        self.llm = llm

    def title_creation(self, state: BlogState):
        """
        Generate a title for the blog based on the input topic.

        Args:
            state (BlogState): The current blog state containing the topic.

        Returns:
            dict: A dictionary with the generated blog title under the "blog" key.
        """
        if "topic" in state and state["topic"]:
            prompt = """
                You're a title creation agent. Given a topic, generate 1 impactful, 
                audience-targeted title suitable for digital platforms (blogs, videos, presentations). 
                The title should be clear, concise, and SEO-friendly. Rotate between styles—listicle, 
                question-based, innovation-driven, or emotionally resonant—depending on topic context. 
                Format the output using markdown. Topic: {topic}
            """

            system_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)

            return {"blog": {"title": response.content}}

    def content_generation(self, state: BlogState):
        """
        Generate full blog content based on the input topic.

        Args:
            state (BlogState): The current blog state with topic and title.

        Returns:
            dict: A dictionary with the generated blog title and content.
        """
        if "topic" in state and state["topic"]:
            system_prompt = """
            You are an expert blog writer specializing in engaging, well-researched digital content.
            Use Markdown formatting throughout.

            Task:
            Generate a comprehensive blog post on the topic: "{topic}".

            Requirements:
            - Structure the post with a clear introduction, main content, and conclusion.
            - Include headings, subheadings, bullet points, and examples where relevant.
            - Ensure the tone is informative, accessible, and tailored for digital readers.
            - Optimize readability with short paragraphs and clean formatting.

            Audience:
            General readers with interest in the topic but no technical background.

            Output:
            A complete blog post in Markdown format.
            """
            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)

            return {
                "blog": {
                    "title": state.get("blog", {}).get("title", "Untitled"),
                    "content": response.content.strip()
                }
            }

    def translation(self, state: BlogState):
        """
        Translate the blog content to the language specified in the state.

        Args:
            state (BlogState): Blog state with `blog.content` and `current_language`.

        Returns:
            dict: A dictionary containing the translated blog content.
        """
        translation_prompt = """
        Please translate the content below into {current_language}, ensuring the following:

        - Retain the original tone, style, and formatting throughout.
        - Adapt cultural references, idiomatic expressions, and contextual nuances to suit {current_language}.
        - Prioritize clarity and readability in the translated version without losing authenticity.

        ORIGINAL CONTENT:
        {blog_content}
        """

        blog_content = state["blog"]["content"]
        message = [
            HumanMessage(
                translation_prompt.format(
                    current_language=state["current_language"],
                    blog_content=blog_content
                )
            )
        ]

        # Structured output ensures the translated result adheres to Blog schema
        translation_content = self.llm.with_structured_output(Blog).invoke(message)

        return {"blog": {"content": translation_content.content}}

    def route(self, state: BlogState):
        """
        Pass through current_language for routing decisions.

        Args:
            state (BlogState): The current blog state.

        Returns:
            dict: A dictionary with the current_language value.
        """
        return {"current_language": state['current_language']}

    def route_decision(self, state: BlogState):
        """
        Determine which translation path to follow based on current_language.

        Args:
            state (BlogState): The current blog state.

        Returns:
            str: The key representing the chosen translation node.
        """
        if state['current_language'] == "hindi":
            return "hindi"
        elif state["current_language"] == "gujarati":
            return "gujarati"
        elif state["current_language"] == "french":
            return "french"
        elif state["current_language"] == "spanish":
            return "spanish"
        else:
            return state["current_language"]
