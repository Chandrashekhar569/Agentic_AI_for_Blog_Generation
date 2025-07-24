# 🧠 LangGraph Blog Generator API

A lightweight FastAPI application that generates blog content using advanced LLM pipelines powered by [LangGraph](https://www.langchain.com/langgraph) and [LangChain](https://www.langchain.com/). This project dynamically constructs LLM workflows based on a given topic and optional language input.

---

## 🚀 Features

- ⚡ Asynchronous REST API with FastAPI  
- 🧩 Dynamically structured LangGraph pipelines  
- 💬 LLM integration via Groq (Mixtral/LLama3 support)  
- 🌐 Topic & multilingual blog generation  
- 🔒 .env-based secure API key handling  

---

## 📦 Tech Stack

- **Framework**: FastAPI, Uvicorn  
- **LLM Orchestration**: LangGraph, LangChain, Groq LLM  
- **Environment**: Python 3.10+  
- **Deployment**: Easily containerizable or deploy via Uvicorn/Gunicorn  

---

## 📁 Project Structure

```
src/
├── graphs/
│   └── graph_builder.py       # Builds LangGraph workflows based on use case
├── llms/
│   └── groq_llm.py            # Groq LLM wrapper for LangChain
├── nodes/
│   └── blog_node.py           # Node logic for title, content, and multilingual blog workflows.
├── states/
│   └── blog_state.py.py       # Defines schema and state types for topic-based blog generation.
app.py                         # FastAPI server and API routes
requirements.txt               # Project dependencies
.env                           # Environment variables (not included)
```

---

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/Chandrashekhar569/Agentic_AI_for_Blog_Generation.git

# Create a virtual environment
uv venv
.venv\Scripts\activate  # or venv\Scripts\activate on Windows

# Install dependencies
uv add -r requirements.txt
```

---

## 🛠️ Environment Variables

Create a `.env` file in the root directory and include:

```env
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

---

## 🚦 Running the Server

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

API will be accessible at: `http://localhost:8000`

---

## 📨 API Usage

### POST `/blogs`

#### Request Body:

```json
{
  "topic": "Artificial Intelligence",
  "language": "English"  // optional
}
```

#### Response:

```json
{
  "data": {
    "generated_blog": "...",
    "summary": "...",
    ...
  }
}
```

---

## 📌 Example

```bash
curl -X POST http://localhost:8000/blogs \
  -H "Content-Type: application/json" \
  -d '{"topic": "AI in Healthcare", "language": "spanish"}'
```

---

## 🧪 Development

Enable hot-reloading:

```bash
uvicorn app:app --reload
```

Log file changes with:

```bash
watchmedo auto-restart --patterns="*.py" --recursive -- uvicorn app:app --reload
```

---

## 🙌 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)  
- [LangGraph](https://github.com/langchain-ai/langgraph)  
- [Groq](https://console.groq.com/)  
- [FastAPI](https://fastapi.tiangolo.com/)  

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for more info.

---


## 👤 About Me

Hey there! I’m **Chandrashekhar Chaudhari**—a former Data Analyst now actively transitioning into AI/ML engineering. This project reflects my passion for building intelligent workflows with LangGraph and LLMs, exploring how agentic architectures can produce multilingual blog content at scale.

I specialize in:
- 🧠 Generative AI workflows using LangChain, LangGraph, and Hugging Face
- 🛠️ Backend engineering with FastAPI and cloud platforms like AWS & Azure
- 📈 Data analysis and visualization using Python, SQL, and Power BI
- 🤖 Deploying modular, agent-driven pipelines with technologies like Streamlit, Docker, and MLOps tools

I believe in open-source collaboration and solving real-world problems with structured, scalable AI systems.

Want to connect or check out more of my work? [Visit my GitHub](https://github.com/Chandrashekhar569)

---

