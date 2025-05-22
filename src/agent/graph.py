from typing import TypedDict

from langgraph.graph import END, StateGraph

from src.agent.model_logic import get_chat_response


class State(TypedDict):
    input: str
    output: str


def call_model(state: State) -> State:
    user_input = state["input"]
    response = get_chat_response(user_input)
    return {"input": user_input, "output": response}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("call_model", call_model)
    graph.set_entry_point("call_model")
    graph.add_edge("call_model", END)
    return graph.compile()


graph = build_graph()
