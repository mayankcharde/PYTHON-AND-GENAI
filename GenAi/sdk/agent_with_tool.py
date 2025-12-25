# from dotenv import load_dotenv

# from agents import Agent, Runner
# from agents import WebSearchTool

# load_dotenv()


# #  DEFINE AN AGENT 
# hello_agent = Agent[Any](
#     name = "Hello world agent",
#     instructions = "You are an agent which greets the user and helps tehm ans using emojis and in funny way",
#     tools=[
#         WebSearchTool()
#     ]
# )


# result = Runner.run_sync(hello_agent,"what is wikipedia in google?")

# print(result.final_output)





from dotenv import load_dotenv
from typing import Any

from agents import Agent, Runner
from agents import WebSearchTool

load_dotenv()

# DEFINE AN AGENT
hello_agent = Agent[Any](
    name="Hello world agent",
    instructions="You are an agent which greets the user and helps them answer using emojis and in a funny way 😄🎉",
    tools=[
        WebSearchTool()
    ]
)

#  IN THIS WE ARE GIVING OUR QUESTIONS
result = Runner.run_sync(hello_agent, "what is wikipedia in google?")
print(result.final_output)
