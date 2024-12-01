from flask import Flask, request, jsonify
from openai import OpenAI

history = []
base_url = "https://api.aimlapi.com/v1"
api_key = "7ae3a9a75e99458cb771a2e52134e8cb"
system_prompt = "Be descriptive and helpful."
app = Flask(__name__)
api = OpenAI(api_key=api_key, base_url=base_url)
history.append(system_prompt)


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400
    completion = api.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ],
        temperature=0.7,
        max_tokens=256,
    )

    response = completion.choices[0].message.content
    history.append(user_input)
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=True)
