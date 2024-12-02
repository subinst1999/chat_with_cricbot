import json
from models import agent
from flask import Flask, request, jsonify, render_template, Blueprint
import requests
from models import agent
app = Flask(__name__)

# Replace with your actual backend URL and authentication details
BACKEND_URL = "https://your-backend-api.com"
BACKEND_AUTH_TOKEN = "your_backend_auth_token"

# Replace with your desired port number
PORT_NUMBER = 5001
cricbot = Blueprint('cricbot', __name__, url_prefix='/cricbot')


@app.route('/login', methods=['POST'])
def login():
    print("hiiiii")
    username =request.form.get('username')
    password =request.form.get('password')
    # Replace with your actual authentication logic
    if username == "user" and password == "password":
        return render_template('dashboard.html')
    else:
        return jsonify({'error': 'Invalid credentials'}), 401


@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/query', methods=['POST'])
def query():
    # token = request.headers.get('Authorization')

    # Replace with your actual backend query logic
    # headers = {'Authorization': f'Bearer {token}'}
    try:
        data = json.loads(request.data)
        if data.get("query") and len(data["query"])>5:
            answer = agent.process_user_query(data['query'])
        else:
            answer = "Please enter a valid query"
        return jsonify({"answer":answer}),200
    except Exception:
        return jsonify({'answer': 'Sorry, some error occured. Please try after sometime!'}), 500


if __name__ == '__main__':
    app.run(debug=True,port=PORT_NUMBER,host = '0.0.0.0')