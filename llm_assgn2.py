from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env")

try:
    message=PromptTemplate.from_template("You are a {role}. Explain {topic} for {audience}")

    model=ChatOpenRouter(
        model="qwen/qwen3.6-plus:free", 
        api_key=api_key,
        temperature=0.7,
        max_tokens=100)

    response= message | model | StrOutputParser()

    data=response.invoke({ "role": "teacher", "topic": "gravity", "audience": "5-years-old" })
    data1=response.invoke({ "role": "software architect", "topic": "gravity", "audience": "developers" }) # response.invoke() is used to execute the model with the specified input values for the placeholders in the message string.
    

    print("teacher: " + data + "\n\n" + "software architect:  " + data1)

except NotImplementedError as e:
    print(f"Error: {e}")