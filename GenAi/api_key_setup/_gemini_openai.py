from dotenv import load_dotenv
from openai import OpenAi


load_dotenv()


client = OpenAi(
    api_key="AIzaSyCbztrpuiKBX8s_PcLrf9KYb-PJ0tGXv7A",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    models = "gemini-2.5-flash",
    messages=[
        {"role":"system", "content":"You are an expert in Maths and only and only ans maths realted questions. That if the query is not related to maths. Just say sorry and do not ans that."},
        { "role": "user", "content": "Hey, can you help me solve the a + b whole square"}
    ]
)

print(reponse.choices[0].message.content)