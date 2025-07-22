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
app.py                         # FastAPI server and API routes
requirements.txt               # Project dependencies
.env                           # Environment variables (not included)
```

---

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/langgraph-blog-api.git
cd langgraph-blog-api

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
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
  -d '{"topic": "AI in Healthcare", "language": "Spanish"}'
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

## 💡 Future Improvements

- ✍️ Add blog tone and length as options  
- 🌍 Enhance multilingual output with translation LLMs  
- 📄 Markdown blog output support  
- 🧪 Add test coverage with Pytest  

---

> Built with 🧠 and ☕ by Chandrashekhar Chaudhari
