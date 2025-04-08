from flask import Flask, request, jsonify, redirect
import string
import random
import json
import os

app = Flask(__name__)
URLS_FILE = 'urls.json'

# In-memory dictionary
url_mapping = {}

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def load_urls():
    global url_mapping
    if os.path.exists(URLS_FILE):
        try:
            with open(URLS_FILE, 'r') as f:
                url_mapping = json.load(f)
        except json.JSONDecodeError:
            url_mapping = {}

def save_urls():
    with open(URLS_FILE, 'w') as f:
        json.dump(url_mapping, f, indent=4)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400

    short_code = generate_short_code()
    url_mapping[short_code] = original_url
    save_urls()

    return jsonify({'short_url': request.host_url + short_code})

@app.route('/<short_code>')
def redirect_url(short_code):
    original_url = url_mapping.get(short_code)
    if original_url:
        return redirect(original_url)
    return jsonify({'error': 'Short URL not found'}), 404

if __name__ == '__main__':
    load_urls()
    app.run(host='0.0.0.0', port=5000)
