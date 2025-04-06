# Agentic Observability

Agentic Observability is a Streamlit-based application that integrates with JIRA and Datadog to fetch data, process it using OpenAI's API(or meta ai API or other), and provide actionable insights via a chatbot interface.

---

## Installation

### Step 1: Set Up Ollama (Required for Local LLM Testing)

1. **Install Ollama**:
   Follow the [Ollama installation guide](https://ollama.ai/download) for Linux. Typically, you can use the following command:
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

2. **Verify Installation**:
   Check that Ollama is installed correctly:
   ```bash
   ollama --version
   ```

3. **Pull the `phi3` Model**:
   The `phi3` model is lightweight and suitable for local testing. Pull it using:
   ```bash
   ollama pull phi3
   ```

4. **Run Ollama**:
   Start the Ollama service:
   ```bash
   ollama serve
   ```

5. **Verify Ollama Service**:
   Ensure the service is running on port `11434`:
   ```bash
   curl http://localhost:11434
   ```

---

### Step 2: Test Locally with Fake Data (Recommended for First-Time Setup)

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/agentic-ai-observability.git
   cd agentic-ai-observability
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add the following:
   ```env
   OPENAI_API_KEY=your-openai-api-key
   JIRA_BASE_URL=https://your-jira-instance.atlassian.net
   JIRA_EMAIL=your-email@example.com
   JIRA_API_TOKEN=your-jira-api-token
   DATADOG_API_KEY=your-datadog-api-key
   DATADOG_APP_KEY=your-datadog-app-key
   OLLAMA_MODEL_NAME=phi3
   OLLAMA_HOST=http://localhost:11434
   ```

5. **Run the Application**:
   ```bash
   streamlit run ui/streamlit_chat.py
   ```

6. **Access the Application**:
   Open your browser and navigate to:
   ```
   http://localhost:8502
   ```

---

### Step 3: Transition to Real APIs (Optional)

> **Important Note**:  
> To test with real APIs, you need to **comment out the code for fake data** and **uncomment the code for real API calls** in the following files:
> - [`app/jira_service.py`](app/jira_service.py)
> - [`app/datadog_service.py`](app/datadog_service.py)
> - [`app/ollama_agent.py`](app/ollama_agent.py)


Once you have tested the application with fake data, you can configure it to use real APIs for JIRA and Datadog.

1. **Update the `.env` File**:
   Ensure your `.env` file contains valid API keys and credentials for JIRA and Datadog.

2. **Run the Application**:
   ```bash
   streamlit run ui/streamlit_chat.py
   ```

3. **Verify the APIs**:
   - Ensure that your JIRA and Datadog credentials are valid.
   - Check that the application fetches real data from the APIs.

---

### Docker/Docker Compose Setup

1. **Ensure Docker and Docker Compose Are Installed**:
   - Install [Docker](https://docs.docker.com/get-docker/).
   - Install [Docker Compose](https://docs.docker.com/compose/install/).

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/agentic-ai-observability.git
   cd agentic-observability
   ```

3. **Set Up the `.env` File**:
   Create a `.env` file in the root directory with the following:
   ```env
   OPENAI_API_KEY=your-openai-api-key
   JIRA_BASE_URL=https://your-jira-instance.atlassian.net
   JIRA_EMAIL=your-email@example.com
   JIRA_API_TOKEN=your-jira-api-token
   DATADOG_API_KEY=your-datadog-api-key
   DATADOG_APP_KEY=your-datadog-app-key
   OLLAMA_MODEL_NAME=phi3
   OLLAMA_HOST=http://ollama:11434
   ```

4. **Build and Start the Services**:
   ```bash
   docker-compose up --build
   ```

5. **Verify the Services**:
   - Check that the `chat-ui` service is running on port `8501`.
   - Check that the `ollama` service is running on port `11434`.

6. **Access the Application**:
   Open your browser and navigate to:
   ```
   http://localhost:8502
   ```

---

## Troubleshooting

### Common Issues

1. **Error: Port Already in Use**:
   - Stop any process using the conflicting port:
     ```bash
     netstat -ano | findstr :8501  # Replace 8501 with the conflicting port
     taskkill /PID <PID> /F       # Replace <PID> with the process ID
     ```
     > Another solution is to change the mapped port in the `docker-compose.yml` file.

2. **Error: Failed to Connect to Ollama**:
   - Ensure the `ollama` service is running:
     ```bash
     docker-compose up -d ollama
     ```
   - Verify the `phi3` model is available:
     ```bash
     docker exec -it <ollama-container-id> ollama list
     ```
     If not, download it:
     ```bash
     docker exec -it <ollama-container-id> ollama pull phi3
     ```

3. **Error: File Not Found**:
   - Ensure the `data` directory and its files (`sample_jira_tickets.json`, `sample_datadog_logs.json`) are present in the project.

---
## Author

- **Jodionísio Muachifi** - [GitHub Profile](https://github.com/jmuachifi/)
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.