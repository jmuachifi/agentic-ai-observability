import json
import os


def fetch_jira_issues(priority_filter=["High", "Critical"]):
    try:
        file_path = os.path.join(
            os.path.dirname(__file__), "../data/sample_jira_tickets.json"
        )
        with open(file_path, "r") as f:
            issues = json.load(f)

        filtered = [i for i in issues if i["priority"] in priority_filter]
        return filtered

    except Exception as e:
        return [{"error": str(e)}]


# ----------------- for real API call -----------------

# import requests
# import os

# JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
# JIRA_EMAIL = os.getenv("JIRA_EMAIL")
# JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

# def fetch_jira_issues(priority_filter=["High", "Critical"]):
#     try:
#         # Validate environment variables
#         if not JIRA_BASE_URL or not JIRA_EMAIL or not JIRA_API_TOKEN:
#             raise ValueError("Missing required Jira environment variables (JIRA_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN)")

#         # Construct the API URL and headers
#         url = f"{JIRA_BASE_URL}/rest/api/2/search"
#         headers = {"Content-Type": "application/json"}
#         auth = (JIRA_EMAIL, JIRA_API_TOKEN)

#         # Construct the JQL query
#         query = {
#             "jql": f'priority in ({",".join(priority_filter)})',
#             "fields": ["key", "summary", "status", "priority", "created"]
#         }

#         # Make the API request
#         response = requests.get(url, headers=headers, auth=auth, params=query)
#         response.raise_for_status()

#         # Parse the response
#         issues = response.json().get("issues", [])
#         return [
#             {
#                 "key": issue["key"],
#                 "summary": issue["fields"]["summary"],
#                 "status": issue["fields"]["status"]["name"],
#                 "priority": issue["fields"]["priority"]["name"],
#                 "created": issue["fields"]["created"]
#             }
#             for issue in issues
#         ]

#     except requests.exceptions.HTTPError as http_err:
#         return [{"error": f"HTTP error occurred: {http_err}"}]
#     except requests.exceptions.RequestException as req_err:
#         return [{"error": f"Request error occurred: {req_err}"}]
#     except ValueError as val_err:
#         return [{"error": str(val_err)}]
#     except Exception as e:
#         return [{"error": f"An unexpected error occurred: {str(e)}"}]
