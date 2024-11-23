from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load a conversational AI model
chatbot = pipeline('conversational', model='microsoft/DialoGPT-small')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    response = chatbot(user_input)
    return jsonify({"response": response[0]['generated_text']})


if __name__ == '__main__':
    app.run(debug=True)