"""
=============================================
            Graph Builder File
=============================================
* This file defines the `GraphBuilder` class, responsible for constructing LangGraph workflows
  for blog generation using dynamic language-specific nodes and transitions.

* Key Responsibilities:
  - Initializes a graph with blog-specific state (`BlogState`)
  - Adds nodes for title creation, content generation, and multilingual translation
  - Builds two types of graphs:
    • Topic-based blog generation
    • Language-aware blog translation flows via conditional routing

## Class: GraphBuilder
* Manages graph construction based on chosen use-case ("topic" or "language")
* Leverages BlogNode functions for modular node logic

## Function: buld_topic_graph()
* Constructs basic graph with title and content generation nodes

## Function: build_language_graph()
* Builds graph with routing node and conditional edges for translating blog content
  into Hindi, Gujarati, French, or Spanish

## Function: setup_graph(usecase)
* Compiles and returns the graph based on selected usecase

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
"""

from langgraph.graph import StateGraph,START,END
from src.llms.groq_llm import GroqLLM
from src.states.blog_state import BlogState
from src.nodes.blog_node import BlogNode



class GraphBuilder:
    def __init__(self,llm):
        self.llm=llm
        self.graph=StateGraph(BlogState)

    def buld_topic_graph(self):
        """
        Build a graph to generate blogss based on topic 
        """

        self.blog_node_object=BlogNode(self.llm)

        ## Nodes
        self.graph.add_node("title_creation",self.blog_node_object.title_creation)
        self.graph.add_node("content_generation",self.blog_node_object.content_generation)

        ## Edges
        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation","content_generation")
        self.graph.add_edge("content_generation", END)

        return self.graph
    
    def build_language_graph(self):
        """Build a graph for blog generation with inputs language"""

        self.blog_node_object=BlogNode(self.llm)

        ## Nodes
        self.graph.add_node("title_creation",self.blog_node_object.title_creation)
        self.graph.add_node("content_generation",self.blog_node_object.content_generation)
        self.graph.add_node("route",self.blog_node_object.route)
        self.graph.add_node("hindi_translation",lambda state: self.blog_node_object.translation({**state, "current_language":"hindi"}))
        self.graph.add_node("gujarati_translation",lambda state: self.blog_node_object.translation({**state, "current_language":"gujarati"}))
        self.graph.add_node("french_translation",lambda state: self.blog_node_object.translation({**state, "current_language":"french"}))
        self.graph.add_node("spanish_translation",lambda state: self.blog_node_object.translation({**state, "current_language":"spanish"}))        

        # Edges
        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation","content_generation")
        self.graph.add_edge("content_generation", "route")

        ## conditional Edge
        self.graph.add_conditional_edges(
            "route",
            self.blog_node_object.route_decision,
            {
                "hindi":"hindi_translation",
                "gujarati":"gujarati_translation",
                "french":"french_translation",
                "spanish":"spanish_translation"
            }
        )

        # Edges
        self.graph.add_edge("hindi_translation",END)
        self.graph.add_edge("gujarati_translation",END)
        self.graph.add_edge("french_translation",END)
        self.graph.add_edge("spanish_translation",END)

        return self.graph


    def setup_graph(self,usecase):
        if usecase=="topic":
            self.buld_topic_graph()

        if usecase=="language":
            self.build_language_graph()

        return self.graph.compile()



## Below code for langgraph studeo
llm = GroqLLM().get_llm()

# get the graph
graph_builder=GraphBuilder(llm)
graph = graph_builder.buld_topic_graph().compile()