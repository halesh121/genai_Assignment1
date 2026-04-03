from langchain.chat_models import init_chat_model
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env")

model = ChatOpenRouter(
    model="qwen/qwen3.6-plus:free",
    api_key=api_key,
    temperature=0.7,
    max_tokens=100,
)

response = model.invoke("What is the capital of France?")
print(response)