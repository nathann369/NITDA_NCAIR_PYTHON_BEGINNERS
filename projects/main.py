from langchain_core.messages import HumanMassage
from langchain_openai import ChatOpenAI
from langchain.tools import  tensorflow as tf
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatOpenAI(temperature =0)
    tools = []
    agent_executor = create_react_agent(model, tools)
    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break
        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMassage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print() 

if __name__ == "__main__":
    main()
