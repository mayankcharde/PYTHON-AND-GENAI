# from openai import OpenAI
# from dotenv import load_dotenv
# import requests

# load_dotenv()

# client = OpenAI()

# def get_weather(city:str):
#         url = f"https://wttr.in/{city.lower()}?format=%C+%t"
      
#     if response.status_code == 200:
#         return f"the weather in {city} is {response.text}"    
    
#     return "something went wrong "


# def main():
#     user_query = input("> ")
    
#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             { "role": "user", "content": user_query }
#         ]
#     )

#     print(f"🤖: {response.choices[0].message.content}")
    
# main()    









from dotenv import load_dotenv
import google.generativeai as genai
import os
import requests

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Weather function
def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong while fetching weather."


# Create Gemini model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="""
You are a helpful AI assistant.
If the user asks about weather, respond normally.
"""
)

def main():
    user_query = input("> ")

    # Ask Gemini
    response = model.generate_content(user_query)

    print(f"🤖: {response.text}")


main()
