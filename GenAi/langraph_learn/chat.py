from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model


load_dotenv()


llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)
#  WE DEFINED STATE HERE
class State(TypedDict):
    messages: Annotated[list, add_messages]
    

# CHATBOT NODE FIRST NODE FROM START
def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return { "messages": [response] }


# AFTER CHATBOT LLM MESSAGE IT GOES TO SAMPLENODE MSG
#  AND AT LAST PRINT SAMPLE MESSAGE APPENDED
def samplenode(state: State):
    print("\n\nInside samplenode node", state)
    return { "messages": ["Sample Message Appended"] }


#  THROUGH THIS WE CAN BUILD THE GRAPH
graph_buider = StateGraph(State)

graph_buider.add_node("chatbot", chatbot)
graph_buider.add_node("samplenode", samplenode)

graph_buider.add_edge(START, "chatbot")
graph_buider.add_edge("chatbot","samplenode")
graph_buider.add_edge("samplenode", END)


graph = graph_buider.compile()

updated_state =  graph.invoke(State({"messages":["What is my name?"]}))

print("\n\nupdated_state", updated_state)



# (START) -> chatbot -> samplenode -> (END)

# state = { messages: ["Hey there"] }
# node runs: chatbot(state: ["Hey There"]) -> ["Hi, This is a message from ChatBot Node"]
# state = { "messages": ["Hey there", "Hi, This is a message from ChatBot Node"]  }