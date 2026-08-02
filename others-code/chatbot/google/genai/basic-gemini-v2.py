
from google import genai

client=genai.Client(api_key="MY_SECRET_API-KEY")

message=input("You: ")

response=client.models.generate_content(
    model="gemini-3.5-flash",
    contents=message
)

print(response.text)
