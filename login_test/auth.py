import time
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

socketio = SocketIO(app)

users = {'user1': generate_password_hash('password1'),'user2': generate_password_hash('password1')}

@app.route('/generate_hash', methods=['POST'])
def generate_hash():
    print("B: generate_hash")
    print(request.json)
    
    data = request.json
    username = data['username']
    session_id = data['session_id']
    
    user_hash = generate_password_hash(username + session_id)
    print()
    print("B: username = ", username)
    print("B: user_hash = ", user_hash)
    print("B: session_id = ", session_id)
    print()

    # Check if the user exists
    if username not in users:
        print("xxxxxxxx1")
        return jsonify({'error': 'Invalid username'}), 401

    # Check if the hash matches
    if not check_password_hash(users[username], user_hash) and False:
        print("xxxxxxxx2")
        return jsonify({'error': 'Invalid credentials'}), 401

    print("xxxxxxxx3")
    # time.sleep(2)
    # Emit a Socket.IO event for successful login

    
    jwt_token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
    print("B: JWT",jwt_token)
    return jsonify({'jwt_token': jwt_token.decode('utf-8')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
