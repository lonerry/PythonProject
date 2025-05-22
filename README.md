# LangGraph ChatBot – Stateless Tool-Using Agent

A simple LangGraph-powered agent that answers user messages statelessly and calls a tool `get_current_time()` when the user asks about the current UTC time.

---

## 🔧 How to Run It

```bash
git clone <repo>
cd your_repo
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

---

## ⚙️ Requirements

- Python 3.9+
- [Ollama](https://ollama.com) installed locally with model `phi` pulled.

---

## 🚀 Ollama Setup (Required)

1. **Start the Ollama server** (runs on `localhost:11434` by default):

```bash
ollama serve
```

2. **Pull the model** used by this agent (e.g. `phi`):

```bash
ollama pull phi
```
3. **Start Project**
```bash
langgraph dev
```
---

## 🛠️ Development Notes

You can customize logic in:

- `model_logic.py`: LLM prompt and tool routing
- `graph.py`: defines the flow (start → call_model → end)

To test the graph visually, open:

```
https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

---

## 🌍 Environment

Optional: copy example environment file and fill in LangSmith API key if needed:

```bash
cp .env.example .env
```

`.env`:

```env
LANGSMITH_PROJECT=your_project_name
LANGSMITH_API_KEY=your_langsmith_key
```

---
