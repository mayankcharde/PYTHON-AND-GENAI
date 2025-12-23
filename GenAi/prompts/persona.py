# from dotenv import load_dotenv
# from openai import OpenAI


# import json

# load_dotenv()

# client = OpenAI()

# SYSTEM_PROMPT = """
#     You are an AI Persona Assistant named Mayank Charde.
#     You are acting on behalf of Piyush Garg who is 25 years old Tech enthusiatic and 
#     principle engineer. Your main tech stack is JS and Python and You are leaning GenAI these days.

#     Examples:
#     Q. Hey
#     A: Hey, Whats up!

#     (100 - 150 examples)

# """


# response = client.chat.completions.create(
#     model = "gpt-4o",
#     messages = [
#         {"role":"system" , "content":SYSTEM_PROMPT},
#         {"role":"user" , "content":"What is your name?"}
#     ]
# )


# print("Response:" , response.choices[0].message.content)






#  GEMINI INTEGRATED CODE 

from dotenv import load_dotenv
import google.generativeai as genai
import os
import json

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# System prompt (persona)
SYSTEM_PROMPT = """
You are an AI Persona Assistant named Mayank Charde.
You are acting on behalf of Piyush Garg who is 25 years old, tech enthusiastic and
principal engineer. Your main tech stack is JavaScript and Python and you are learning GenAI these days.

Examples:
Q. Hey
A: Hey, What's up!

(100 - 150 examples)
"""

# Create Gemini model with system instruction
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)

# User input
user_question = "What is your name?"

# Generate response
response = model.generate_content(user_question)

# Print output
print("Response:", response.text)
