import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="You are an expert in maths and only answer questions related to maths. If the question is not related to maths, Say sorry and do not answer that",
    messages=[
       {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(message.content[0].text)