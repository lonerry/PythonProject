# New LangGraph Project
## Getting Started

1. **Запусти Ollama**, если он ещё не запущен (локальный LLM-сервер):

```bash
ollama serve
```

2. **Загрузи модель `phi`** (можно добавить другую модель):

```bash
ollama pull phi
```

> По умолчанию LangGraph будет подключаться к Ollama на `http://localhost:11434`.

3. **Установи зависимости**, включая [LangGraph CLI](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/):

```bash
cd path/to/your/app
pip install -e .
```

4. (Опционально) Создай `.env`, если нужны секреты или токены:

```bash
cp .env.example .env
```

Если хочешь включить LangSmith для трассировки:

```text
# .env
LANGSMITH_API_KEY=lsv2...
LANGSMITH_PROJECT=...
```

5. **Запусти LangGraph сервер:**

```bash
langgraph dev
```

Теперь сервер будет доступен по адресу:

- 🧠 UI: [http://127.0.0.1:2024](http://127.0.0.1:2024)
- 📚 API Docs: [http://127.0.0.1:2024/docs](http://127.0.0.1:2024/docs)
- 🎨 Studio: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024

---

## How to customize

1. **Настрой параметры**: измени `Configuration` в `graph.py`, если нужно указать системный prompt или другую модель.

2. **Расширь граф**: логика работы графа — в [graph.py](./src/agent/graph.py). Добавляй новые узлы, ветвления и кастомную обработку.

---


