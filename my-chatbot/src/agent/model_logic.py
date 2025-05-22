from datetime import datetime, UTC
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="phi", 
    base_url="http://localhost:11434",
    temperature=0.7
)

PROMPT = """
If the user asks about the current time, always respond strictly with:
"The current UTC time is YYYY-MM-DDThh:mm:ssZ".

Otherwise, answer normally.
"""

def get_chat_response(message: str) -> str:
    try:
        if "time" in message.lower():
            now = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
            return f"The current UTC time is {now}"

        response = llm.invoke([
            SystemMessage(content=PROMPT),
            HumanMessage(content=message)
        ])
        return str(response.content).strip()

    except Exception as e:
        return f"Error: {e}"
