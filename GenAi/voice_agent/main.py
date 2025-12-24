# import asyncio

# from dotenv import load_dotenv

# import speech_recognition as sr
# from openai import OpenAI
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
        

# def main():
#     r = sr.Recognizer() # Speech to Text

#     with sr.Microphone() as source: # Mic Access
#         r.adjust_for_ambient_noise(source)
#         r.pause_threshold = 2

#         SYSTEM_PROMPT = f"""
#                 You're an expert voice agent. You are given the transcript of what
#                 user has said using voice.
#                 You need to output as if you are an voice agent and whatever you speak
#                 will be converted back to audio using AI and played back to user.
#             """

#         messages = [
#             { "role": "system", "content": SYSTEM_PROMPT },
#         ]

#         while True:

#             print("Speak Something...")
#             audio = r.listen(source)

#             print("Processing Audio... (STT)")
#             stt = r.recognize_google(audio)

#             print("You Said:", stt)

#             messages.append({ "role": "user", "content": stt })

#             response = client.chat.completions.create(
#                 model="gpt-4.1-mini",
#                 messages=messages
#             )

#             print("AI Response", response.choices[0].message.content)
#             asyncio.run(tts(speech=response.choices[0].message.content))

# main()







import speech_recognition as sr
import google.generativeai as genai
import pyttsx3
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="""
    You are an expert cheerful voice assistant.
    Always respond in a happy, delightful, and friendly tone.
    """
)

# Text-to-Speech engine
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 175)
tts_engine.setProperty("volume", 1.0)

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        recognizer.pause_threshold = 2

        print("🎤 Voice Agent Started (Gemini)")

        chat = model.start_chat(history=[])

        while True:
            try:
                print("\nSpeak something...")
                audio = recognizer.listen(source)

                print("Processing (STT)...")
                user_text = recognizer.recognize_google(audio)

                print("You said:", user_text)

                # Send to Gemini
                response = chat.send_message(user_text)

                ai_text = response.text
                print("Gemini:", ai_text)

                # Speak response
                speak(ai_text)

            except sr.UnknownValueError:
                print("❌ Could not understand audio")

            except KeyboardInterrupt:
                print("\n👋 Exiting Voice Agent")
                break

main()
