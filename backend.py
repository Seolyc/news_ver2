import os
import requests
from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')  # 환경변수에서 가져오도록 설정
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/news')
def get_news():
    params = {
        'country': 'kr',
        'apiKey': NEWS_API_KEY
    }
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
