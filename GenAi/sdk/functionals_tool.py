from dotenv import load_dotenv
import requests
from typing import Any

from agents import Agent, Runner
from agents import WebSearchTool , function_tool

load_dotenv()

#  IN FUNCTIONAL TOOLS WE CAN GIBVE OUR CUSTOME VARIOUS FUNCTIONS FOR MAKING OUR AGENT STRONGER AND HAVE DIFF VARIATIONS
@function_tool
def get_weather(city: str):
    """
    Fetch the weather for a given city name.  
    Args:
        city: The city to fetch the weather for
    """
    
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong"



#  DEFINE AN AGENT 
hello_agent = Agent[Any](
    name = "Hello world agent",
    instructions = "You are an agent which greets the user and helps tehm ans using emojis and in funny way",
    tools=[
        WebSearchTool(),
        get_weather
    ]
)


result = Runner.run_sync(hello_agent,"what is wikipedia in google?")

print(result.final_output)





# from dotenv import load_dotenv
# from typing import Any

# from agents import Agent, Runner
# from agents import WebSearchTool

# load_dotenv()

# # DEFINE AN AGENT
# hello_agent = Agent[Any](
#     name="Hello world agent",
#     instructions="You are an agent which greets the user and helps them answer using emojis and in a funny way 😄🎉",
#     tools=[
#         WebSearchTool()
#     ]
# )

# #  IN THIS WE ARE GIVING OUR QUESTIONS
# result = Runner.run_sync(hello_agent, "what is wikipedia in google?")
# print(result.final_output)
