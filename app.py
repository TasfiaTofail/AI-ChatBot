from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_response(message):
    message = message.lower()

    if "hi" in message or "hello" in message:
        return "Hello 👋 I am working now!"
    elif "how are you" in message:
        return "I'm doing great 😄"
    elif "name" in message:
        return "I am your AI chatbot 🤖"
    elif "joke" in message:
        return "Why did the computer sit alone? Because it had no cache 😂"
    else:
        return "I got your message 👍 but I'm still learning."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    reply = get_response(message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)