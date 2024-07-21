from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Your OpenAI API key
openai.api_key = "sk-proj-XpG97QycmFmLohGuvkrST3BlbkFJUaX9kyyLP4WbBnlHFYjr"

@app.route('/gpt', methods=['GET'])
def chat():
    query = request.args.get('chat')
    if not query:
        return jsonify({"error": "No query provided"}), 400

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        max_tokens=150
    )

    answer = response.choices[0].text.strip()
    return jsonify({"response": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
