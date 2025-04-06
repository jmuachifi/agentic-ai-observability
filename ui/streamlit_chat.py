import sys
import os
import streamlit as st

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.ollama_agent import ask_ollama
from app.helper import load_fake_logs, load_fake_tickets

# --- Page Config ---
st.set_page_config(page_title="Agentic Observability Bot", layout="centered")

# --- Title ---
st.title("🤖 Agentic AI Observability Chat")

# --- Sidebar Settings ---
st.sidebar.header("Settings")
service = st.sidebar.selectbox("Select Source", ["Jira", "Datadog"])

# --- Chat Container ---
with st.chat_message("ai"):
    st.markdown("Hello! I’m your Agentic AI assistant. Ask me about system issues, incidents, or logs.")

# --- Session State ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- User Input ---
with st.container():
    user_prompt = st.text_input("Ask me anything about incidents, services, or logs...", key="input", label_visibility="collapsed")

# --- Process Input ---
if user_prompt:
    # Add user input to session state
    st.session_state.history.append({"role": "user", "message": user_prompt})

    # Display user input in the chat
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Generate AI response using ask_ollama
    with st.spinner("Analyzing..."):
        try:
            ai_response = ask_ollama(user_prompt, source=service)
        except Exception as e:
            ai_response = f"⚠️ Error: {str(e)}"

    # Add AI response to session state
    st.session_state.history.append({"role": "ai", "message": ai_response})

    # Display AI response in the chat
    with st.chat_message("ai"):
        st.markdown(f"💡 **AI Suggestion:** {ai_response}")

# --- Display Chat History ---
for chat in st.session_state.history[::-1]:
    if chat["role"] == "user":
        st.markdown(f"<div class='chatbox alert'>🧑 {chat['message']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chatbox ai-response'>💡 <b>AI Suggestion:</b><br>{chat['message']}</div>", unsafe_allow_html=True)

# --- Expandable Raw Logs ---
with st.expander("🔍 Raw Observability Data"):
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📋 Mock Jira Tickets")
        try:
            tickets = load_fake_tickets()
            st.json(tickets)
        except Exception as e:
            st.error(f"⚠️ Error loading Jira tickets: {str(e)}")

    with col2:
        st.markdown("#### 🧾 Mock Datadog Logs")
        try:
            logs = load_fake_logs()
            st.json(logs)
        except Exception as e:
            st.error(f"⚠️ Error loading Datadog logs: {str(e)}")

# --- Footer ---
st.markdown("---")
st.markdown("🛠️ Developed for local Agentic AI Observability testing with Ollama LLM")

# --- For real API call ---

# import sys
# import os
# import streamlit as st

# # Add the parent directory to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from app.ollama_agent import ask_ollama
# from app.jira_service import fetch_jira_issues
# from app.datadog_service import fetch_datadog_logs

# # --- Page Config ---
# st.set_page_config(page_title="Agentic Observability Bot", layout="centered")

# # --- Title ---
# st.title("🤖 Agentic AI Observability Chat")

# # --- Sidebar Settings ---
# st.sidebar.header("Settings")
# service = st.sidebar.selectbox("Select Source", ["Jira", "Datadog"])

# # --- Chat Container ---
# with st.chat_message("ai"):
#     st.markdown(
#         "Hello! I’m your Agentic AI assistant. Ask me about system issues, incidents, or logs."
#     )

# # --- Session State ---
# if "history" not in st.session_state:
#     st.session_state.history = []

# # --- User Input ---
# with st.container():
#     user_prompt = st.text_input(
#         "Ask me anything about incidents, services, or logs...",
#         key="input",
#         label_visibility="collapsed",
#     )

# # --- Process Input ---
# if user_prompt:
#     # Add user input to session state
#     st.session_state.history.append({"role": "user", "message": user_prompt})

#     # Display user input in the chat
#     with st.chat_message("user"):
#         st.markdown(user_prompt)

#     # Generate AI response using ask_ollama
#     with st.spinner("Analyzing..."):
#         try:
#             ai_response = ask_ollama(user_prompt, source=service)
#         except Exception as e:
#             ai_response = f"⚠️ Error: {str(e)}"

#     # Add AI response to session state
#     st.session_state.history.append({"role": "ai", "message": ai_response})

#     # Display AI response in the chat
#     with st.chat_message("ai"):
#         st.markdown(f"💡 **AI Suggestion:** {ai_response}")

# # --- Display Chat History ---
# for chat in st.session_state.history[::-1]:
#     if chat["role"] == "user":
#         st.markdown(
#             f"<div class='chatbox alert'>🧑 {chat['message']}</div>",
#             unsafe_allow_html=True,
#         )
#     else:
#         st.markdown(
#             f"<div class='chatbox ai-response'>💡 <b>AI Suggestion:</b><br>{chat['message']}</div>",
#             unsafe_allow_html=True,
#         )

# # --- Expandable Raw Logs ---
# # --- Expandable Raw Logs ---
# with st.expander("🔍 Raw Observability Data"):
#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("#### 📋 Jira Tickets")
#         try:
#             # Fetch real Jira tickets
#             tickets = fetch_jira_issues(priority_filter=["High", "Critical"])
#             st.json(tickets)
#         except Exception as e:
#             st.error(f"⚠️ Error loading Jira tickets: {str(e)}")

#     with col2:
#         st.markdown("#### 🧾 Datadog Logs")
#         try:
#             # Fetch real Datadog logs
#             logs = fetch_datadog_logs()
#             st.json(logs)
#         except Exception as e:
#             st.error(f"⚠️ Error loading Datadog logs: {str(e)}")

# # --- Footer ---
# st.markdown("---")
# st.markdown("🛠️ Developed for local Agentic AI Observability testing with Ollama LLM")