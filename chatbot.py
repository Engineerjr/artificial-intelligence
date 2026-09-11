import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph

load_dotenv()


class State(TypedDict):
    messages: list


def create_app():
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing API key. Add GEMINI_API_KEY or GOOGLE_API_KEY to your .env file."
        )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.7,
        google_api_key=api_key,
    )

    def chatbot(state: State):
        response = llm.invoke(state["messages"])
        return {"messages": [response]}

    builder = StateGraph(State)
    builder.add_node("chatbot", chatbot)
    builder.set_entry_point("chatbot")
    builder.add_edge("chatbot", END)

    return builder.compile(checkpointer=MemorySaver())


def main():
    app = create_app()
    thread_config = {"configurable": {"thread_id": "simple-chatbot"}}

    print("Simple LangGraph Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        current_state = app.get_state(thread_config)
        messages = current_state.values.get("messages", []) if current_state.values else []
        messages.append(HumanMessage(content=user_input))

        result = app.invoke({"messages": messages}, config=thread_config)
        assistant_reply = result["messages"][-1].content
        print(f"Bot: {assistant_reply}\n")


if __name__ == "__main__":
    main()
