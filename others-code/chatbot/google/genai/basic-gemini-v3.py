# This code borrowed from:
# @CodeW1thAlex
# https://www.youtube.com/shorts/hW1-H1RgRsA

from google import genai

client=genai.Client(api_key="MY_SECRET_GOOGLE_API_KEY") # get your own key here: https://aistudio.google.com/api-keys

chat=client.chats.create(model="gemini-3.5-flash")

while True:
    message=input("You: ")
    if message.lower() in ("exit","quit"):
       break
    response=chat.send_message(message=message)
    print(f"Bot: {response.text}\n")


