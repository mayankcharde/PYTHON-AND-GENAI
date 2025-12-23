from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# -------- OPENAI SETUP --------
from openai import OpenAI

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -------- GEMINI SETUP --------
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

gemini_model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=(
        "You are an expert in Maths and only answer maths-related questions. "
        "If the question is not related to maths, say sorry."
    )
)

# -------- SWITCH HERE --------
USE_MODEL = "gemini"   # change to "openai"

question = "Solve (a + b) whole square"

# -------- GEMINI RESPONSE --------
if USE_MODEL == "gemini":
    response = gemini_model.generate_content(question)
    print("Gemini response:\n", response.text)

# -------- OPENAI RESPONSE --------
elif USE_MODEL == "openai":
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert in Maths and only answer maths-related questions. "
                    "If the question is not related to maths, say sorry."
                )
            },
            {"role": "user", "content": question}
        ]
    )
    print("OpenAI response:\n", response.choices[0].message.content)

else:
    print("Invalid model selection")
