# # from google import genai
# import google.generativeai as genai

# client = genai.Client(
#     api_key="AIzaSyCbztrpuiKBX8s_PcLrf9KYb-PJ0tGXv7A"
# )
# reponse = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Explain how AI works in a few words"
# )
# print(reponse.text)




import google.generativeai as genai

genai.configure(api_key="AIzaSyCbztrpuiKBX8s_PcLrf9KYb-PJ0tGXv7A")

model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content("who is mayank and its meaning")

print(response.text)
