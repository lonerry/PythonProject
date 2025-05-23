# LangGraph ChatBot – Stateless Tool-Using Agent

A simple LangGraph-powered agent that answers user messages statelessly and calls a tool `get_current_time()` when the user asks about the current UTC time.

---

## 🔧 How to Run It

```bash
git clone <repo>
cd your_repo
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

---

## ⚙️ Requirements

- Python 3.9+
- [Ollama](https://ollama.com) installed locally with the model `phi` pulled

---

## 🚀 Ollama Setup (Required)

### 🐧 Linux:

1. **Install Ollama**:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

2. **Start the Ollama server** (runs on `localhost:11434` by default):
```bash
ollama serve
```

3. **Pull the model**:
```bash
ollama pull phi
```

---

### 🍎 macOS:

1. **Install Ollama** (choose one):

- via Homebrew:
```bash
brew install ollama
```

- or via install script:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

2. **Start the Ollama server**:
```bash
ollama serve
```

3. **Pull the model**:
```bash
ollama pull phi
```

---

## ▶️ Start the Project

```bash
langgraph dev
```

---

## 🛠️ Development Notes

You can customize logic in:

- `model_logic.py`: LLM prompt and tool routing
- `graph.py`: defines the flow (start → call_model → end)

To test the graph visually:

```
https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

---

## 🌍 Environment (optional)

Copy the environment example file and configure LangSmith:

```bash
cp .env.example .env
```

`.env`:
```env
LANGSMITH_PROJECT=your_project_name
LANGSMITH_API_KEY=your_langsmith_key
```
