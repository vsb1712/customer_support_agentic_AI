from flask import Flask, request, jsonify
from agent import run_agent

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Agent is running 🚀"

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        return "Use POST with JSON: {'goal': 'your task'}"

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    goal = data.get("goal")

    if not goal:
        return jsonify({"error": "Missing 'goal' field"}), 400

    result = run_agent(goal)

    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
