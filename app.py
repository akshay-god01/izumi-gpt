from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your OpenAI GPT-4 API key
OPENAI_API_KEY = "sk-proj-gNesKpQ3dJQJNzZoPCxDT3BlbkFJHhUua0j3QgY15ctGPmYl"

@app.route('/gpt', methods=['GET'])
def chat_with_gpt4():
    user_message = request.args.get('q')

    if not user_message:
        return jsonify({'error': 'No query parameter "q" provided'}), 400

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}',
    }

    payload = {
        'model': 'gpt-4',
        'messages': [
            {'role': 'user', 'content': user_message}
        ]
    }

    response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, json=payload)
    completion = response.json()['choices'][0]['message']['content']

    return jsonify({'response': completion})

if __name__ == '__main__':
    app.run(debug=True)
