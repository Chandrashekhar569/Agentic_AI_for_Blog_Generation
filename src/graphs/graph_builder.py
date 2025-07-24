from langgraph.graph import StateGraph, START, END
from src.llms.groq_llm import GroqLLM
from src.states.blog_state import BlogState
from src.nodes.blog_node import BlogNode


class GraphBuilder:
    """
    Builds LangGraph workflows for blog generation based on user input.

    Attributes:
        llm: An LLM instance used for generation and translation.
        graph: A StateGraph object managing the workflow.
    """

    def __init__(self, llm):
        """
        Initializes the GraphBuilder with a given LLM.

        Args:
            llm: A language model instance for generating blog content.
        """
        self.llm = llm
        self.graph = StateGraph(BlogState)

    def buld_topic_graph(self):
        """
        Build a basic blog generation graph based on a given topic.

        Nodes:
            - title_creation
            - content_generation

        Flow:
            START → title_creation → content_generation → END

        Returns:
            A configured StateGraph object.
        """
        self.blog_node_object = BlogNode(self.llm)

        # Add nodes
        self.graph.add_node("title_creation", self.blog_node_object.title_creation)
        self.graph.add_node("content_generation", self.blog_node_object.content_generation)

        # Define linear edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)

        return self.graph

    def build_language_graph(self):
        """
        Build a graph with conditional translation based on selected language.

        Nodes:
            - title_creation
            - content_generation
            - route (decides target language)
            - translation nodes (Hindi, Gujarati, French, Spanish)

        Flow:
            START → title_creation → content_generation → route → conditional translation → END

        Returns:
            A configured StateGraph object with translation routing.
        """
        self.blog_node_object = BlogNode(self.llm)

        # Add core generation nodes
        self.graph.add_node("title_creation", self.blog_node_object.title_creation)
        self.graph.add_node("content_generation", self.blog_node_object.content_generation)
        self.graph.add_node("route", self.blog_node_object.route)

        # Add translation nodes via lambdas to inject language context
        self.graph.add_node("hindi_translation", lambda state: self.blog_node_object.translation({**state, "current_language": "hindi"}))
        self.graph.add_node("gujarati_translation", lambda state: self.blog_node_object.translation({**state, "current_language": "gujarati"}))
        self.graph.add_node("french_translation", lambda state: self.blog_node_object.translation({**state, "current_language": "french"}))
        self.graph.add_node("spanish_translation", lambda state: self.blog_node_object.translation({**state, "current_language": "spanish"}))

        # Define main path
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", "route")

        # Add conditional branching based on detected language
        self.graph.add_conditional_edges(
            "route",
            self.blog_node_object.route_decision,
            {
                "hindi": "hindi_translation",
                "gujarati": "gujarati_translation",
                "french": "french_translation",
                "spanish": "spanish_translation"
            }
        )

        # Final step to END
        self.graph.add_edge("hindi_translation", END)
        self.graph.add_edge("gujarati_translation", END)
        self.graph.add_edge("french_translation", END)
        self.graph.add_edge("spanish_translation", END)

        return self.graph

    def setup_graph(self, usecase):
        """
        Compiles and returns the graph based on a specified use case.

        Args:
            usecase (str): Either "topic" or "language".

        Returns:
            A compiled LangGraph object.
        """
        if usecase == "topic":
            self.buld_topic_graph()
        if usecase == "language":
            self.build_language_graph()

        return self.graph.compile()


# ─────────────── LangGraph Studio Integration Example ───────────────

# Instantiate LLM
llm = GroqLLM().get_llm()

# Build and compile the language-specific blog graph
graph_builder = GraphBuilder(llm)
graph = graph_builder.build_language_graph().compile()
