from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
import os


load_dotenv()


api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env")
try:
    model = ChatOpenRouter(
    model="qwen/qwen3.6-plus:free",
    api_key=api_key,
    temperature=0.7,
    max_tokens=100,
    )

    question=input("Enter your question: ")
    print("Generating response..."+question)
    response = model.invoke(question)
    print(response.content)
except Exception as e:
    print(f"Error: {e}")
    print("\nNote: If you see a 502 error, the OpenRouter API or upstream model is temporarily unavailable.")