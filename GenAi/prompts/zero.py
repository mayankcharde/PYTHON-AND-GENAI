# from doctenv import load_dotenv
# from openai import OpenAI

# load_dotenv()

# client = OpenAI(
#     api_key="AIzaSyBjA34ENgeGNplvIqCP-qcH2fuMkqxdO7o",
#     base_url="https://generativelanguage.googleapis.com/v1beta/"
# )


# SYSTEM_PROMPT = "You should only and only ans the coding related questions. Do not ans anything else. Your name is Alexa. If user asks something other than coding, just say sorry."

# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     messages=[
#         { "role": "system", "content": SYSTEM_PROMPT },
#         { "role": "user", "content": "Hey, Can you write a python code to translate the word hello to Hindi"}
#     ]
# )

# print(response.choices[0].message.content)


# # 1. Zero-shot Prompting: The model is given a direct question or task without prior examples.







from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# System prompt
SYSTEM_PROMPT = (
    "You should only and only answer coding-related questions. "
    "Do not answer anything else. Your name is Alexa. "
    "If the user asks something other than coding, just say sorry."
)

# Create Gemini model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)

# User query
user_query = "Hey, can you write a Python code to translate the word hello to Hindi?"

# Generate response
response = model.generate_content(user_query)

# Print response
print(response.text)

# 1. Zero-shot Prompting:
# The model is given a direct question or task without prior examples.
