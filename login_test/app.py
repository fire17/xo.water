from flask import Flask, render_template, request, redirect, session, url_for
from flask_socketio import SocketIO
import requests
import json
import os
import time, threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

auth_url = 'http://localhost:5001'
backend_url = 'http://localhost:5002'

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/auth')
def auth():
    def login_success():
        # time.sleep(3)
        print("login_success")
        socketio.sleep(5)
        socketio.emit('login_success', {"success":True})
        print("login_success 2")
    # t = threading.Thread(target=login_success)
    socketio.start_background_task(target=login_success)
    isMobile = request.user_agent.platform == 'android' or request.user_agent.platform == 'ios'
    groupLink = 'https://chat.whatsapp.com/JEFnj7I25kF1jnmUzzxDqP'
    print("whatsapp: ",groupLink)
    # return redirect(url_for('whatsapp'))
    # return render_template('whatsapp.html', wa_url = groupLink)
    if isMobile:
        return redirect(groupLink)
    return render_template('wa.html', wa_url = groupLink)
    return render_template('loginWindow.html', wa_url = groupLink)
    # t.start()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session_id = os.urandom(16).hex()

        # Send request to Auth (B) to generate a hash
        response = requests.post(f'{auth_url}/generate_hash', json={'username': username, 'session_id': session_id})
        
        if response.status_code == 200:
            data = response.json()
            session['jwt_token'] = data['jwt_token']
             # Open a new window for login
            # script = f'''
            #     var loginWindow = window.open('{url_for('login')}', '_blank', 'height=400,width=600,resizable=yes,scrollbars=yes');
            #     function checkLoginStatus() {{
            #         if (loginWindow.closed) {{
            #             window.location.href = '{url_for('dashboard')}';
            #         }} else {{
            #             setTimeout(checkLoginStatus, 1000);
            #         }}
            #     }}
            #     checkLoginStatus();
            # '''
            # return f'<script>{script}</script>'
            # return render_template('loginWindow.html')
            return redirect(url_for('auth'))
            return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'jwt_token' not in session:
        return redirect(url_for('login'))

    jwt_token = session['jwt_token']
    user_details = requests.post(f'{backend_url}/get_user', json={'jwt_token': jwt_token}).json()
    return render_template('dashboard.html', jwt_token=jwt_token, user_details = user_details, **user_details)

@socketio.on('connect')
def handle_connect():
    if 'jwt_token' not in session:
        return False
    
    jwt_token = session['jwt_token']
    user_details = requests.post(f'{backend_url}/get_user', json={'jwt_token': jwt_token}).json()
    socketio.emit('user_details', user_details, room = request.sid)

if __name__ == '__main__':
    print("Starting app")
    socketio.run(app, host='0.0.0.0', port=5000)
