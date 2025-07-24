from fastapi import FastAPI, Request
import uvicorn
from src.graphs.graph_builder import GraphBuilder
from src.llms.groq_llm import GroqLLM

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Set LangSmith environment variables for observability and tracking
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_PROJECT"] = "Blog Generator"

@app.post("/blogs")
async def create_blogs(request: Request):
    """
    API endpoint to generate a blog in the specified language.

    Expects:
        JSON body with keys:
            - topic (str): The topic to generate the blog on.
            - language (str, optional): The target language for translation.

    Returns:
        dict: Blog state including title and content (possibly translated).
    """
    data = await request.json()
    topic = data.get("topic", "")
    language = data.get("language", "")

    # Initialize LLM instance
    groq_llm = GroqLLM()
    llm = groq_llm.get_llm()

    # Build graph based on input
    graph_builder = GraphBuilder(llm)
    
    if language and topic:
        # Generate and translate blog
        graph = graph_builder.setup_graph(usecase="language")
        state = graph.invoke({"topic": topic, "current_language": language.lower()})
    elif topic:
        # Generate blog without translation
        graph = graph_builder.setup_graph(usecase="topic")
        state = graph.invoke({"topic": topic})
    else:
        state = {"error": "Missing topic in request."}

    return {"data": state}


# Run the app using uvicorn
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

