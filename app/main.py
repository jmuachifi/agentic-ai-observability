from flask import Flask, request, jsonify
from app.ollama_agent import ask_ollama

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt")
    response = ask_ollama(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)
