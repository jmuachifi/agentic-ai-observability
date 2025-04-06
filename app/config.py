import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
DATADOG_API_KEY = os.getenv("DATADOG_API_KEY")
OLLAMA_MODEL_NAME = "phi3"  # Or "llama3", "mistral", etc.
