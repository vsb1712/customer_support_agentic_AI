from flask import Flask, request, jsonify
from coordinator import process_query

app = Flask(__name__)

# Home route (browser test)
@app.route("/")
def home():
    return "✅ Multi-Agent Support AI is running. Use POST /chat"

# GET route so browser doesn't show 405
@app.route("/chat", methods=["GET"])
def chat_get():
    return "ℹ️ This endpoint only accepts POST requests with JSON body."

# MAIN API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400

    user_message = data["message"]
    reply = process_query(user_message)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
