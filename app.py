from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load a conversational AI model
chatbot = pipeline('text-generation', model='sshleifer/tiny-gpt2')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    if len(user_input) > 100:  # Limit to 100 characters
        return jsonify({"error": "Message too long, please shorten your input"}), 400
        
    response = chatbot(user_input, max_length=50)
    return jsonify({"response": response[0]['generated_text']})


if __name__ == '__main__':
    app.run(debug=True)
