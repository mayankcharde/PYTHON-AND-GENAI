# from dotenv import load_dotenv
# from openai import OpenAI

# import json

# load_dotenv()

# client = OpenAI()

# SYSTEM_PROMPT = """
#      You're an expert AI Assistant in resolving user queries using chain of thought.
#     You work on START, PLAN and OUPUT steps.
#     You need to first PLAN what needs to be done. The PLAN can be multiple steps.
#     Once you think enough PLAN has been done, finally you can give an OUTPUT.
    
#     Rules:
#     - Strictly Follow the given JSON output format
#     - Only run one step at a time.
#     - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).
    
#     Output JSON Format:
#     { "step": "START" | "PLAN" | "OUTPUT", "content": "string" }


    
#     Example:
#     START: Hey, Can you solve 2 + 3 * 5 / 10
#     PLAN: { "step": "PLAN": "content": "Seems like user is interested in math problem" }
#     PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method" }
#     PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }
#     PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15" }
#     PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10" }
#     PLAN: { "step": "PLAN": "content": "We must perform divide that is 15 / 10  = 1.5" }
#     PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 1.5" }
#     PLAN: { "step": "PLAN": "content": "Now finally lets perform the add 3.5" }
#     PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans" }
#     OUTPUT: { "step": "OUTPUT": "content": "3.5" }



# """



# print("\n\n\n")


# message_history = [
#     {"role":"system" , "content": SYSTEM_PROMPT},
# ]

# user_query = input("")
# message_history.append({"role":"user" , "content":user_query})

# while True:
#      response = client.chat.completions.create(
#         model="gpt-4o",
#         response_format={"type": "json_object"},
#         messages=message_history
#     )
     
     
#     raw_result = response.choices[0].message.content
#     message_history.append({"role":"assistant" , "content":raw_result})
    
    
#     parsed_result = json.loads(raw_result)
    
    
    
#     if parsed_result.get("step") == "START":
#         print("🔥", parsed_result.get("content"))
#         continue

#     if parsed_result.get("step") == "PLAN":
#         print("🧠", parsed_result.get("content"))
#         continue

#     if parsed_result.get("step") == "OUTPUT":
#         print("🤖", parsed_result.get("content"))
#         break
    
    
# print("\n\n\n")    
    






from dotenv import load_dotenv
import google.generativeai as genai
import os
import json

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
     You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    
    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).
    
    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT", "content": "string" }


    
    Example:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN": "content": "We must perform divide that is 15 / 10  = 1.5" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 1.5" }
    PLAN: { "step": "PLAN": "content": "Now finally lets perform the add 3.5" }
    PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans" }
    OUTPUT: { "step": "OUTPUT": "content": "3.5" }
"""

# Create Gemini model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)

print("\n\n")

# Conversation history (Gemini style)
message_history = []

# Take user input
user_query = input("enter query...")
message_history.append(user_query)

# Loop until OUTPUT step
while True:
    response = model.generate_content(message_history)

    raw_result = response.text
    message_history.append(raw_result)

    # Extract ONLY the last JSON object (NO try-catch)
    json_start = raw_result.rfind("{")
    json_end = raw_result.rfind("}") + 1
    json_text = raw_result[json_start:json_end]

    parsed_result = json.loads(json_text)

    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break

print("\n\n")
