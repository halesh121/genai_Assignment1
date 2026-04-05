from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import os

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env")

class User(BaseModel):
    linkedin: str = Field(description="write a post for linkedin")
    tweeter: str = Field(description="write a post for tweeter") 
    instagram: str = Field(description="write a caption for instagram")

try:
    parser = PydanticOutputParser(pydantic_object=User)
    
    message = PromptTemplate.from_template(
        "Generate social media content about {topic}. Provide content for LinkedIn, Twitter, and Instagram.\n{format_instructions}"
    )

    model = ChatOpenRouter(
        model="qwen/qwen3.6-plus:free", 
        api_key=api_key,        
        temperature=0.7,
        max_tokens=300)
    
    response = message | model | parser
    
    data = response.invoke({"topic": "AI in healthCare", "format_instructions": parser.get_format_instructions()})
    print("AI in healthCare content generated:")
    print("LinkedIn:", data.linkedin)
    print("Twitter:", data.tweeter)
    print("Instagram:", data.instagram)

except Exception as e:
    print(f"Error: {e}")