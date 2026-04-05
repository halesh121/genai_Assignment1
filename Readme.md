# genai_Assignment1

## Overview

This project contains three LangChain examples using the `qwen/qwen3.6-plus:free` model from OpenRouter:

- `llm_assgin1.py`: Basic chat model interaction
- `llm_assgn2.py`: Prompt template example explaining a topic in different roles
- `llm_assign3.py`: Structured output parsing for social media content generation

## Prerequisites

- Python 3.11+ (confirmed 3.14.3 works)
- Virtual environment
- `.env` file with valid API key

## Recommended workspace path

Use an ASCII-only path to avoid Windows/OneDrive Unicode issues:
- `C:\Users\Halesh\Projects\genai_Assignment1`

## Setup

```powershell
# create local project folder
md C:\Users\Halesh\Projects\genai_Assignment1
cd C:\Users\Halesh\Projects\genai_Assignment1

# create and activate venv
python -m venv .genai
. .genai\Scripts\Activate.ps1

# install dependencies (add requirements.txt if needed)
pip install langchain python-dotenv
```

## .env

Create `.env` in the project root:

```
OPENROUTER_API_KEY=your_open_router_api_key_here
```

## Run

```powershell
# Run the basic chat model example
python llm_assgin1.py

# Run the prompt template example
python llm_assgn2.py

# Run the structured output parsing example
python llm_assign3.py
```

## Scripts

### llm_assgin1.py
Basic LangChain chat model example that demonstrates interaction with the OpenRouter API.

### llm_assgn2.py
Uses a PromptTemplate to explain the topic "gravity" in two different roles:
- As a teacher explaining to 5-year-olds
- As a software architect explaining to developers

Outputs explanations from both perspectives.

### llm_assign3.py
Demonstrates structured output parsing using PydanticOutputParser. Generates social media content for LinkedIn, Twitter, and Instagram about "AI in healthCare" with properly formatted JSON output.


