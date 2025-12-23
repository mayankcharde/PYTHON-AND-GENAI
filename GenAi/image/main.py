# from dotenv import load_dotenv
# from openai import OpenAI



# load_dotenv()

# client = OpenAI()

# response = client.chat.completions.create(
#     model="gpt-4.1-mini",
#     messages=[
#         {
#             "role":"user",
#             "content":[
#                 { "type": "text", "text": "Generate a caption for this image in about 50 words" },
#                 { "type": "image_url", "image_url": {"url": "https://images.pexels.com/photos/879109/pexels-photo-879109.jpeg"} }
#             ]
#         }
#     ]
# )


# print("Response:", response.choices[0].message.content)





import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini vision model
model = genai.GenerativeModel("gemini-2.5-flash")

# Image URL
image_url = "https://images.pexels.com/photos/879109/pexels-photo-879109.jpeg"

# Download image
image_bytes = requests.get(image_url).content

# Generate caption
response = model.generate_content(
    [
        "Generate a caption for this image in about 50 words",
        {
            "mime_type": "image/jpeg",
            "data": image_bytes
        }
    ]
)

print("Response:", response.text)
