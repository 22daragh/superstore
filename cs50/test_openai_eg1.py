from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    input="yes",
    model="gpt-4.1-mini"
)

print(response.output_text)