from dotenv import load_dotenv
import google.generativeai as genai
import requests
import os
import json

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ---------------- TOOLS ----------------

def run_command(cmd: str):
    return os.system(cmd)

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong"

available_tools = {
    "get_weather": get_weather,
    "run_command": run_command
}

# ---------------- SYSTEM PROMPT ----------------

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    You can also call a tool if required from the list of available tools.
    for every tool call wait for the observe step which is the output from the called tool.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool": "string", "input": "string" }

    Available Tools:
    - get_weather(city: str)
    - run_command(cmd: str)
"""

# ---------------- GEMINI MODEL ----------------

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)

print("\n\n")

message_history = []

# ---------------- MAIN LOOP ----------------

while True:
    user_query = input("👉🏻 ")
    message_history.append(user_query)

    while True:
        response = model.generate_content(message_history)
        raw_result = response.text
        message_history.append(raw_result)

        # Extract last JSON object safely
        json_start = raw_result.rfind("{")
        json_end = raw_result.rfind("}") + 1
        json_text = raw_result[json_start:json_end]

        parsed = json.loads(json_text)

        step = parsed.get("step")

        if step == "START":
            print("🔥", parsed.get("content"))
            continue

        if step == "PLAN":
            print("🧠", parsed.get("content"))
            continue

        if step == "TOOL":
            tool_name = parsed.get("tool")
            tool_input = parsed.get("input")

            print(f"🛠️ Calling tool: {tool_name}({tool_input})")

            tool_response = available_tools[tool_name](tool_input)

            print(f"🛠️ Result: {tool_response}")

            # OBSERVE step injected back
            observe_payload = json.dumps({
                "step": "OBSERVE",
                "tool": tool_name,
                "input": tool_input,
                "output": tool_response
            })

            message_history.append(observe_payload)
            continue

        if step == "OUTPUT":
            print("🤖", parsed.get("content"))
            break

print("\n\n")
