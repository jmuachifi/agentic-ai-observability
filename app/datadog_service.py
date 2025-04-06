import json
import os


def fetch_datadog_logs():
    try:
        file_path = os.path.join(
            os.path.dirname(__file__), "../data/sample_datadog_logs.json"
        )
        with open(file_path, "r") as f:
            logs = json.load(f)
        return logs
    except Exception as e:
        return [{"error": str(e)}]


# ----------------- for real API call -----------------
# import requests
# import os

# DATADOG_API_KEY = os.getenv("DATADOG_API_KEY")
# DATADOG_APP_KEY = os.getenv("DATADOG_APP_KEY")

# def fetch_datadog_logs():
#     try:
#         url = "https://api.datadoghq.com/api/v2/logs/events"
#         headers = {
#             "Content-Type": "application/json",
#             "DD-API-KEY": DATADOG_API_KEY,
#             "DD-APPLICATION-KEY": DATADOG_APP_KEY
#         }
#         query = {
#             "query": "status:error OR status:critical",
#             "time": {
#                 "from": "now-1h",
#                 "to": "now"
#             }
#         }

#         response = requests.post(url, headers=headers, json=query)
#         response.raise_for_status()
#         logs = response.json().get("data", [])
#         return [
#             {
#                 "timestamp": log["attributes"]["timestamp"],
#                 "message": log["attributes"]["message"],
#                 "level": log["attributes"]["status"]
#             }
#             for log in logs
#         ]
#     except Exception as e:
#         return [{"error": str(e)}]
