import json
import ollama
from app.jira_service import fetch_jira_issues
from app.datadog_service import fetch_datadog_logs
from app.config import OLLAMA_MODEL_NAME

def ask_ollama(user_input: str, source: str = "Datadog") -> str:
    try:
        # Fetch data based on the selected source
        if source == "Jira":
            high_priority_tickets = fetch_jira_issues(priority_filter=["High", "Critical"])
            context_data = f"""
📋 High Priority Jira Tickets:
{json.dumps(high_priority_tickets, indent=2)}
            """
        elif source == "Datadog":
            recent_logs = fetch_datadog_logs()
            context_data = f"""
📈 Recent Observability Logs:
{json.dumps(recent_logs, indent=2)}
            """
        else:
            return "🚨 Invalid source selected. Please choose either 'Jira' or 'Datadog'."

        # System behavior prompt
        system_prompt = """
You are an AI assistant helping IT support and service desk agents analyze observability data.
Use the provided data to generate a useful summary including:

🔧 Issue Summary
🔍 Possible Root Cause
✅ Recommended Action

If no relevant issues are detected, respond politely that nothing critical is found.
Always use concise and clear explanations.
        """

        # Inject context
        context_prompt = f"""
{context_data}

💬 User Query:
{user_input}
        """

        # LLM conversation structure
        messages = [
            {"role": "system", "content": system_prompt.strip()},
            {"role": "user", "content": context_prompt.strip()}
        ]

        # Call local Ollama
        response = ollama.chat(
            model=OLLAMA_MODEL_NAME,  # from config.py (e.g. "phi3")
            messages=messages
        )

        return response['message']['content']

    except Exception as e:
        if "more system memory" in str(e):
            return "🚨 Ollama model error: The selected model requires more memory than available. Try a smaller model like `phi3` or enable swap memory."
        return f"🚨 Error while querying Ollama: {str(e)}"

# ----------------- for real API call -----------------
# import json
# import ollama
# from app.jira_service import fetch_jira_issues
# from app.datadog_service import fetch_datadog_logs
# from app.config import OLLAMA_MODEL_NAME

# def ask_ollama(user_input: str, log_service: str = "checkout-api") -> str:
#     try:
#         # Fetch real data from Jira and Datadog APIs
#         high_priority_tickets = fetch_jira_issues(priority_filter=["High", "Critical"])
#         recent_logs = fetch_datadog_logs()

#         # System behavior prompt
#         system_prompt = """
# You are an AI assistant helping IT support and service desk agents analyze observability data from Jira and Datadog.
# Use the provided data to generate a useful summary including:

# 🔧 Issue Summary
# 🔍 Possible Root Cause
# ✅ Recommended Action

# If no relevant issues are detected, respond politely that nothing critical is found.
# Always use concise and clear explanations.
#         """

#         # Inject context
#         context_prompt = f"""
# 📋 High Priority Jira Tickets:
# {json.dumps(high_priority_tickets, indent=2)}

# 📈 Recent Observability Logs:
# {json.dumps(recent_logs, indent=2)}

# 💬 User Query:
# {user_input}
#         """

#         # LLM conversation structure
#         messages = [
#             {"role": "system", "content": system_prompt.strip()},
#             {"role": "user", "content": context_prompt.strip()}
#         ]

#         # Call local Ollama
#         response = ollama.chat(
#             model=OLLAMA_MODEL_NAME,  # from config.py (e.g. "phi3")
#             messages=messages
#         )

#         return response['message']['content']

#     except Exception as e:
#         if "more system memory" in str(e):
#             return "🚨 Ollama model error: The selected model requires more memory than available. Try a smaller model like `phi3` or enable swap memory."
#         return f"🚨 Error while querying Ollama: {str(e)}"