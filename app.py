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
        'model': 'davinci-codex',
        'messages': [
            {'role': 'user', 'content': user_message}
        ]
    }

    try:
        response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes

        data = response.json()

        # Check if 'choices' exists in the JSON response
        if 'choices' in data and len(data['choices']) > 0:
            completion = data['choices'][0]['message']['content']
            return jsonify({'response': completion})
        else:
            return jsonify({'error': 'Unexpected response format from GPT-4 API.'}), 500

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Request to GPT-4 API failed: {str(e)}'}), 500
    except KeyError as e:
        return jsonify({'error': f'KeyError: {str(e)}'}), 500

if __name__ == '__main__':
    # Run Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
