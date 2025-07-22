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
        self.graph.add_node("hindi_translation",lambda state: self.blog_node_object.translation({**state, "current_language":"hindi"}))
        self.graph.add_node("gujarati_translation",lambda state: self.blog_node_object.translation({**state, "current_language":"gujarati"}))
        self.graph.add_node("route",self.blog_node_object.route)

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
                "gujarati":"gujarati_translation"
            }
        )

        # Edges
        self.graph.add_edge("hindi_translation",END)
        self.graph.add_edge("gujarati_translation",END)

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