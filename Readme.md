# genai_Assignment1

## Overview

This project runs a LangChain chat model example using the `qwen/qwen3.6-plus:free` model from OpenRouter.

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
python llm_assgin1.py
```

## Notes

- If you see `venvlauncher.exe` copy errors, you're likely in a Unicode path (e.g., `文档`). Move to ASCII path as above.
- `llm_assgin1.py` now uses `temperature` and checks `OPENROUTER_API_KEY`.
