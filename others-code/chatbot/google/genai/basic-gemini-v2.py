
from google import genai

client=genai.Client(api_key="MY_SECRET_GOOGLE_API_KEY") # get your own key here: https://aistudio.google.com/api-keys

message=input("You: ")

response=client.models.generate_content(
    model="gemini-3.5-flash",
    contents=message
)

print(response.text)
