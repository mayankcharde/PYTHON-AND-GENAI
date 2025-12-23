# Ollama is a tool that lets you run large language models (LLMs) locally on your own computer instead of using cloud APIs.

from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client = Client(
    host="http://localhost:11434",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/contact-us")
def read_root():
    return {"email": "mayankcharde2@gmail.com"}

@app.post("/chat")
def chat(
        message: str = Body(..., description="The Message")
):
    response = client.chat(model="gemma:2b", messages=[
        { "role": "user", "content":message  }
    ])

    return { "response": response.message.content }
