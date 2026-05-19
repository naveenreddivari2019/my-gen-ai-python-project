#open AI client
from openai import OpenAI
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Create an OpenAI client
client = OpenAI()
# Create a chat completion
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku."}
    ]
)
# Print the response
print(response.choices[0].message.content)
