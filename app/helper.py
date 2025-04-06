import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  

def load_fake_tickets(priority=None):
    file_path = os.path.join(BASE_DIR, "data", "sample_jira_tickets.json")
    with open(file_path, "r") as f:
        tickets = json.load(f)
    if priority:
        return [t for t in tickets if t["priority"] == priority]
    return tickets

def load_fake_logs(service=None):
    file_path = os.path.join(BASE_DIR, "data", "sample_datadog_logs.json")
    with open(file_path, "r") as f:
        logs = json.load(f)
    if service:
        return [log for log in logs if service in log["message"].lower()]
    return logs
