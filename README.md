# artificial-intelligence

## Simple Chatbot with LangGraph

This project contains a minimal LangGraph chatbot powered by Gemini.

### Setup

1. Create a `.env` file from `.env.example`.
2. Add your Gemini API key:
   `GEMINI_API_KEY=your_api_key_here`
3. Install dependencies:
   `pip install -r requirements.txt`

### Run the chatbot

```bash
python langgraph.py
```

Type `exit` to quit the chat.

## Gemini LangGraph Chatbot (Python)

Quick steps to run the example that uses Google Gemini:

1. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

2. Create a `.env` file from the example:

```powershell
copy .env.example .env
```

3. Edit `.env` and set your Gemini API key:

```
GEMINI_API_KEY=your_real_api_key_here
```

4. Run the Gemini chatbot script with a prompt:

```powershell
python langgraph_gemini_chatbot.py "Hello from LangGraph + Gemini"
```

Notes:
- The example uses the `google-generative-ai` client; if your environment
   requires a different package name or version, adjust `requirements.txt`.
- The script prints helpful errors if the SDK or API key is missing.