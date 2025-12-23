# from dotenv import load_dotenv
# from openai import OpenAI


# load_dotenv()

# client = OpenAI(
#     api_key="AIzaSyBjA34ENgeGNplvIqCP-qcH2fuMkqxdO7o",
#     base_url="https://generativelanguage.googleapis.com/v1beta/"
# )


# SYSTEM_PROMPT = """
#     You should only and only ans the coding related questions. Do not ans anything else. Your name is Alexa. If user asks something other than coding, just say sorry.
    
#     RULE:
#     - Striclty follow the output in JSON format
    
#     Output Format:
#     {{
#         "code":"string" or null,
#         "isCodingQuestion": boolean
#     }}
    
#     Examples:
#     Q: can you explain the a+b whole square?
#     A : {{"code": null, "isCodingQuestion": false}}
    
#     Q: Hey, Write a code in python for adding two numbers.
#     A: {{ "code": "def add(a, b):
#         return a + b", "isCodingQuestion": false }}

# """


# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     messages=[
#         { "role": "system", "content": SYSTEM_PROMPT },
#         { "role": "user", "content": "Hey, write a code to add n numbers in js"}
#     ]
# )

# print(response.choices[0].message.content)
# # 1. Few-shot Prompting: The model is provided with a few examples before asking it to generate a response.









from dotenv import load_dotenv
import google.generativeai as genai
import os
import json

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You should only and only answer coding-related questions.
Do not answer anything else.
Your name is Alexa.
If the user asks something other than coding, just say sorry.

RULES:
- Strictly follow the output in JSON format
- Do NOT add explanations outside JSON
- Do NOT add markdown

Output Format:
{
    "code": "string" or null,
    "isCodingQuestion": boolean
}

Examples:

Q: can you explain the a+b whole square?
A:
{
    "code": null,
    "isCodingQuestion": false
}

Q: Hey, write a code in python for adding two numbers.
A:
{
    "code": "def add(a, b):\\n    return a + b",
    "isCodingQuestion": true
}
"""

# Create Gemini model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)

# User query
user_query = "Hey, write a code to add n numbers in js"

# Generate response
response = model.generate_content(user_query)

# Print raw Gemini response
print(response.text)

# Optional: Validate JSON (recommended)
try:
    parsed = json.loads(response.text)
    print("\nParsed JSON:", parsed)
except json.JSONDecodeError:
    print("\nInvalid JSON output")
