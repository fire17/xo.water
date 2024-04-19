from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

users = {'user1': {'name': 'User One', 'email': 'user1@example.com'},'user2': {'name': 'User Two', 'email': 'user2@example.com'}}

@app.route('/get_user', methods=['POST'])
def get_user():
    data = request.json
    jwt_token = data['jwt_token']

    try:
        decoded = jwt.decode(jwt_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        username = decoded['username']

        if username in users:
            return jsonify(users[username])
        else:
            return jsonify({'error': 'User not found'}), 404
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
