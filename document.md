# Frameworks & Libraries for Agentic AI

## The key frameworks and libraries used to build agentic AI systems and autonomous agents

### These tools help in developing AI agents, managing workflows and integrating language models with external data sources

They include:

* Hugging Face Transformers
* LangChain
* LangGraph
* Langflow
* LlamaIndex
* Integration of Langchain with Llama-Index

## API Integration Security

When integrating APIs, it is important to keep sensitive credentials such as API keys, tokens, and other secrets out of source code.

* Store keys in a `.env` file locally
* Load them with a library such as `python-dotenv` in Python or `dotenv` in JavaScript
* Add `.env` to `.gitignore` so it is never committed to Git
* Never hardcode secrets directly into project files, notebooks, or logs

This helps prevent accidental exposure and protects the project from security issues such as push protection violations and leaked credentials.

