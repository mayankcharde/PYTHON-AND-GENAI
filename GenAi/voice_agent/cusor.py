# # Chain Of Thought Prompting
# from dotenv import load_dotenv
# from openai import OpenAI
# import requests
# from pydantic import BaseModel, Field
# from typing import Optional
# import json
# import os

# import asyncio
# import speech_recognition as sr
# from openai.helpers import LocalAudioPlayer
# from openai import AsyncOpenAI

# load_dotenv()

# client = OpenAI()
# async_client = AsyncOpenAI()

# async def tts(speech: str):
#     async with async_client.audio.speech.with_streaming_response.create(
#         model="gpt-4o-mini-tts",
#         voice="coral",
#         instructions="Always speak in cheerfull manner with full of delight and happy",
#         input=speech,
#         response_format="pcm",
#     )as response:
#         await LocalAudioPlayer().play(response)


# def run_command(cmd: str):
#     result = os.system(cmd)
#     return result



# def get_weather(city: str):
#     url = f"https://wttr.in/{city.lower()}?format=%C+%t"
#     response = requests.get(url)

#     if response.status_code == 200:
#         return f"The weather in {city} is {response.text}"
    
#     return "Something went wrong"

# available_tools = {
#     "get_weather": get_weather,
#     "run_command": run_command
# }


# SYSTEM_PROMPT = """
#     You're an expert AI Assistant in resolving user queries using chain of thought.
#     You work on START, PLAN and OUPUT steps.
#     You need to first PLAN what needs to be done. The PLAN can be multiple steps.
#     Once you think enough PLAN has been done, finally you can give an OUTPUT.
#     You can also call a tool if required from the list of available tools.
#     for every tool call wait for the observe step which is the output from the called tool.

#     Rules:
#     - Strictly Follow the given JSON output format
#     - Only run one step at a time.
#     - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

#     Output JSON Format:
#     { "step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool": "string", "input": "string" }

#     Available Tools:
#     - get_weather(city: str): Takes city name as an input string and returns the weather info about the city.
#     - run_command(cmd: str): Takes a system linux command as string and executes the command on user's system and returns the output from that command
    
#     Example 1:
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

#     Example 2:
#     START: What is the weather of Delhi?
#     PLAN: { "step": "PLAN": "content": "Seems like user is interested in getting weather of Delhi in India" }
#     PLAN: { "step": "PLAN": "content": "Lets see if we have any available tool from the list of available tools" }
#     PLAN: { "step": "PLAN": "content": "Great, we have get_weather tool available for this query." }
#     PLAN: { "step": "PLAN": "content": "I need to call get_weather tool for delhi as input for city" }
#     PLAN: { "step": "TOOL": "tool": "get_weather", "input": "delhi" }
#     PLAN: { "step": "OBSERVE": "tool": "get_weather", "output": "The temp of delhi is cloudy with 20 C" }
#     PLAN: { "step": "PLAN": "content": "Great, I got the weather info about delhi" }
#     OUTPUT: { "step": "OUTPUT": "content": "The cuurent weather in delhi is 20 C with some cloudy sky." }
    
# """

# class MyOutputFormat(BaseModel):
#     step: str = Field(..., description="The ID of the step. Example: PLAN, OUTPUT, TOOL, etc")
#     content: Optional[str] = Field(None, description="The optional string content for the step")
#     tool: Optional[str] = Field(None, description="The ID of the tool to call.")
#     input: Optional[str] = Field(None, description="The input params for the tool")

# message_history = [
#     { "role": "system", "content": SYSTEM_PROMPT },
# ]

# r = sr.Recognizer() # Speech to Text
# with sr.Microphone() as source: # Mic Access
#     r.adjust_for_ambient_noise(source)
#     r.pause_threshold = 2

#     while True:
#         print("Speak Something...")
#         audio = r.listen(source)

#         print("Processing Audio... (STT)")
#         user_query = r.recognize_google(audio)
#         message_history.append({ "role": "user", "content": user_query })

#         while True:
#             response = client.chat.completions.parse(
#                 model="gpt-4.1",
#                 response_format=MyOutputFormat,
#                 messages=message_history
#             )

#             raw_result = response.choices[0].message.content
#             message_history.append({"role": "assistant", "content": raw_result})
            
#             parsed_result = response.choices[0].message.parsed

#             if parsed_result.step == "START":
#                 print("🔥", parsed_result.content)
#                 continue

#             if parsed_result.step == "TOOL":
#                 tool_to_call = parsed_result.tool
#                 tool_input = parsed_result.input
#                 print(f"🛠️: {tool_to_call} ({tool_input})")

#                 tool_response = available_tools[tool_to_call](tool_input)
#                 print(f"🛠️: {tool_to_call} ({tool_input}) = {tool_response}")
#                 message_history.append({ "role": "developer", "content": json.dumps(
#                     { "step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response}
#                 ) })
#                 continue



#             if parsed_result.step == "PLAN":
#                 print("🧠", parsed_result.content)
#                 continue

#             if parsed_result.step == "OUTPUT":
#                 print("🤖", parsed_result.content)
#                 asyncio.run(tts(speech=parsed_result.content))
#                 break





















import os
import json
import requests
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
import google.generativeai as genai

# =========================
# ENV & GEMINI SETUP
# =========================
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="""
You are an expert AI assistant that strictly follows Chain-of-Thought reasoning.

Rules:
- Respond ONLY in valid JSON
- Follow steps: START → PLAN → TOOL → OBSERVE → OUTPUT
- Execute only ONE step per response
- Never skip steps
- Never explain outside JSON

JSON FORMAT:
{
  "step": "START | PLAN | TOOL | OUTPUT",
  "content": "string | null",
  "tool": "string | null",
  "input": "string | null"
}

Available Tools:
1. get_weather(city: str)
2. run_command(cmd: str)
"""
)

chat = model.start_chat(history=[])

# =========================
# TTS SETUP
# =========================
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 170)

def speak(text: str):
    tts_engine.say(text)
    tts_engine.runAndWait()

# =========================
# TOOLS
# =========================
def run_command(cmd: str):
    return os.popen(cmd).read()

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    r = requests.get(url)
    if r.status_code == 200:
        return f"The weather in {city} is {r.text}"
    return "Weather service unavailable"

TOOLS = {
    "get_weather": get_weather,
    "run_command": run_command
}

# =========================
# STT SETUP
# =========================
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("\n🎤 Speak now...")
        audio = recognizer.listen(source)
        return recognizer.recognize_google(audio)

# =========================
# MAIN LOOP
# =========================
def main():
    print("🎙️ Gemini Voice Agent Started")

    while True:
        try:
            user_input = listen()
            print("🧑 You:", user_input)

            chat.send_message(
                json.dumps({
                    "step": "START",
                    "content": user_input,
                    "tool": None,
                    "input": None
                })
            )

            while True:
                response = chat.send_message("Continue")
                raw = response.text.strip()

                try:
                    data = json.loads(raw)
                except Exception:
                    print("❌ Invalid JSON from model:\n", raw)
                    break

                step = data.get("step")

                if step == "PLAN":
                    print("🧠 PLAN:", data.get("content"))
                    continue

                if step == "TOOL":
                    tool = data.get("tool")
                    tool_input = data.get("input")
                    print(f"🛠️ TOOL CALL → {tool}({tool_input})")

                    result = TOOLS[tool](tool_input)

                    chat.send_message(json.dumps({
                        "step": "OBSERVE",
                        "content": result,
                        "tool": tool,
                        "input": tool_input
                    }))
                    continue

                if step == "OUTPUT":
                    answer = data.get("content")
                    print("🤖 OUTPUT:", answer)
                    speak(answer)
                    break

        except KeyboardInterrupt:
            print("\n👋 Exiting")
            break
        except Exception as e:
            print("❌ Error:", e)

main()
