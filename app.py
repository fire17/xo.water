from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send, join_room, leave_room
from flask import Flask, render_template, redirect, request, jsonify, url_for, send_from_directory
from xo import *

# from flask_jwt_extended import decode_token
# from flask_jwt_extended import JWTManager
# from flask_jwt_extended import jwt_required
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import create_access_token
from flask_cors import CORS, cross_origin
# import os
# from werkzeug.utils import secure_filename
# import shortuuid
# from mock import *
# from whatsappFeed import *
# from c18core import *
# import datetime as dt

# from flask_socketio import SocketIO, send, emit, join_room
# import jwt as pyjwt

# app = Flask(__name__)
# socketio = SocketIO(app, cors_allowed_origins=['http://localhost:8080'])
# socketio = SocketIO(app, cors_allowed_origins=["*",'http://localhost:5050'])
# socketio = SocketIO(app, cors_allowed_origins=['http://localhost:5050'])


import os
import traceback

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
	os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__, template_folder='templates')

cors = CORS(app, resources={r'/*': {"origins": '*'}})
app.config['SECRET_KEY'] = 'LHUIGYFVHbkjlhuytuvbHTDCFGVHBJtydryctvyuhijhuogyift'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_HEADERS'] = 'Authorization'
app.config['CORS_HEADERS'] = "HTTP_AUTHORIZATION"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

MYPORT = 5050  # for nginx
# MYPORT = 5050  # for nginx
# MYPORT = 5050  # for nginx
ssl = True
if ssl:
	# MYPORT = 443
	# MYPORT = int(os.environ.get('PORT', 443))
	ssl = True
	# import eventlet
	# eventlet.monkey_patch() fuck this monkey patch lol
# MYPORT = 5001

# cors = CORS(app, resources={r"/api": {"origins": "http://localhost:{0}".format(MYPORT)}})
# cors = CORS(app, resources={r"/api": {"origins": "https://localhost:{0}".format(MYPORT)}})
socketio = SocketIO(app, cors_allowed_origins='*')
# socketio = SocketIO(app, cors_allowed_origins=f'https://localhost:{MYPORT}')

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "GYRESETDRYTXXXXXFUGYIUHOt7"  # Change this!
app.config['SECRET_KEY'] = 'secret!'
# jwt = JWTManager(app)
@app.route('/')
def index():
	# return render_template('index.html')
	# return redirect("https://chat.whatsapp.com/JmnYDofCd7v0cXzfBgcVDO")
	return redirect("https://akeyo.io")


@socketio.on('connect')
def on_connect():
	print('A user connected')


@socketio.on('disconnect')
def on_disconnect():
	print('A user disconnected')


@socketio.on('send message')
def on_send_message(message):
	print(f'Received message: {message}')

	# Send message back to the client that initiated the event
	xo[request.sid].message = message
	emit('new message', message+"!")
	print(":::", request.sid)
	print(xo)
	# send('new message', message+"!", room=request.sid)


# if __name__ == '__main__':
# 	socketio.run(app, debug=True)



@app.route('/<path:text>', methods=['GET', 'POST'])
def all_routes(text):
	print("all_routes")
	print("all_routes")
	print("all_routes")
	print("all_routes", text)

	data = request.json
	final = jsonify({"msg": "HELLO WORLD :D"}), 200
	print(data)
	# print(request.args)
	if data is not None:
		# print(request.json)
		pass
		# if "checkUsername" in data:
		# 	res = checkUsername(data["checkUsername"])
		# 	final = jsonify({"result":res[0], "msg":res[1]}), 200
	# return final[0], final[1]

	# master = Master.shares[0]
	# requestOrigin = {'ip': request.remote_addr, "location": getIpLocation(request.remote_addr)}
	if text.split("/")[0] == "send":
		try:
			number = text.split("/")[1].replace("+", "")
			if "@" not in number:
				if "-" not in number:
					number += "@c.us"
				else:
					number += "@g.us"

			contentAt = 2
			content = ""
			# if len(text.split("/")) > 3:
			# 	content = "_From *"+text.split("/")[contentAt]+":*_ \n"
			# 	content = content.replace("+"," ")
			# 	contentAt +=1

			content += "/".join(text.split("/")[contentAt:])
			content = content.replace("+", " ")
			withVerify = False
			print("MSG:", content)
			if withVerify:
				for v in verifiedNumbers:
					if number in v:
						xo.wa.send(v, content)
						# master.sendMessage(v,content)
						# master.driver.sendMessageQuick(v,content)
						return redirect("https://cdn0.iconfinder.com/data/icons/dashboard-vol-1-flat/48/Dashboard_Vol._1-16-512.png")
			else:
				xo.wa.send(number, content)
				# master.sendMessage(number,content)
				# master.driver.sendMessageQuick(number,content)
				return redirect("https://cdn0.iconfinder.com/data/icons/dashboard-vol-1-flat/48/Dashboard_Vol._1-16-512.png")
		except:
			traceback.print_exc()
		return redirect("https://cdn0.iconfinder.com/data/icons/dashboard-vol-1-flat/48/Dashboard_Vol._1-18-512.png")
	#
	# if "exit" in text:
	# 	print("EXITTT")
	# 	print("EXITTT")
	# 	print("EXITTT")
	# 	print("EXITTT")
	# 	text = text.split("exit/")[1]
	# 	return
	# 	return redirect("https://chat.whatsapp.com/JmnYDofCd7v0cXzfBgcVDO")
	# 	return render_template("exit.html", user_image = "full_filename", status = "s")
	#
	if "join" == text:
		print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
		print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
		print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
		print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
		print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
		print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
	
	if "join" in text:
		print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJ",text,len(text))
		if False:
			master.runningSubscriptions+=1
			place = master.runningSubscriptions
			service = "Master"
			if len(text.split("/")) > 1 and len(text.split("/")[1]) > 0:
				afterSlash = text.split("/")[1]
				foundService = None
				for serv in master.services:
					if afterSlash.lower() == serv.lower():
						foundService = serv
				if foundService is not None:
					service = foundService
		
			while("availableChats" not in master.db):
				print("NO AVAILABLE CHATS")
				time.sleep(0.1)
		
			while(len(master.db["availableChats"][service]) == 0 or place < master.runningSubscriptions):
				time.sleep(0.5)
				# print("NEW USER WAITING FOR MASTER GROUP")
		
			firstKey = list(master.db["availableChats"][service])[0]
			return redirect(master.db["availableChats"][service][firstKey])
		else:
			service = text.split("join/")[1]
			final = jsonify({"msg": f"Should join {service} and enter group..."}), 200
			return final[0],final[1]
			firstKey = list(master.db["availableChats"][service])[0]

			return redirect(master.db["availableChats"][service][firstKey])
		#
		# master.backup(now = True)
		# runningSubscriptions-=1
		#
	return final[0], final[1]

	if text.split("/")[0] in master.links:
		print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
		print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
		print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
		print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
		print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
		print("SERVING LINK "+text)
		linkData = master.links[text.split("/")[0]]
		foundCmd = False
		if len(text.split("/")) > 1:
			data = None
			cmd = "/".join(text.split("/")[:2])
			print("CCCCCCCCCCCCCCCCCCCCCC", master.links)
			print("CCCCCCCCCCCCCCCCCCCCCC")
			print("CCCCCCCCCCCCCCCCCCCCCC")
			print("CCCCCCCCCCCCCCCCCCCCCC")
			print("CCCCCCCCCCCCCCCCCCCCCC", cmd)
			if cmd in master.links:
				linkData = master.links[cmd]
				foundCmd = True

		requestOrigin = {'ip': request.remote_addr,
						"location": getIpLocation(request.remote_addr)}
		if text.split("/")[0] == "send":
			print("OOOOOOOOOOOOOOOOOOOOo")
			print("OOOOOOOOOOOOOOOOOOOOo")
			print("OOOOOOOOOOOOOOOOOOOOo")
			print("OOOOOOOOOOOOOOOOOOOOo")
			print("OOOOOOOOOOOOOOOOOOOOo")
			print("OOOOOOOOOOOOOOOOOOOOo")
			print("OOOOOOOOOOOOOOOOOOOOo SENDING PROXY")
			try:
				number = text.split("/")[1].replace("+", "")
				if "@" not in number:
					if "-" not in number:
						number += "@c.us"
					else:
						number += "@g.us"

				contentAt = 2
				content = ""
				# if len(text.split("/")) > 3:
				# 	content = "_From *"+text.split("/")[contentAt]+":*_ \n"
				# 	content = content.replace("+"," ")
				# 	contentAt +=1

				content += "/".join(text.split("/")[contentAt:])
				content = content.replace("+", " ")
				withVerify = False
				print("MSG:", content)
				if withVerify:
					for v in verifiedNumbers:
						if number in v:
							master.sendMessage(v, content)
							# master.driver.sendMessageQuick(v,content)
							return redirect("https://cdn0.iconfinder.com/data/icons/dashboard-vol-1-flat/48/Dashboard_Vol._1-16-512.png")
				else:
					master.sendMessage(number, content)
					# master.driver.sendMessageQuick(number,content)
					return redirect("https://cdn0.iconfinder.com/data/icons/dashboard-vol-1-flat/48/Dashboard_Vol._1-16-512.png")
			except:
				traceback.print_exc()
			return redirect("https://cdn0.iconfinder.com/data/icons/dashboard-vol-1-flat/48/Dashboard_Vol._1-18-512.png")

		if linkData is not None and "service" in linkData and "chatID" in linkData and "answer" in linkData and "invite" in linkData:
			# service = linkData["service"]
			service, chatID, answer, invite = linkData["service"], linkData[
				"chatID"], linkData["answer"], linkData["invite"]
			user = chatID
			if "user" in linkData and linkData["user"] is not None:
				user = linkData["user"]
			if "obj" in master.services[service]:
				obj = master.services[service]["obj"]
				if obj is not None:
					# Get Nicknames

					toSend = ""
					if foundCmd:
						toSend += answer
						if len(text.split("/")) > 2:
							toSend += "/" + "/".join(text.split("/")[2:])
					else:
						if len(text.split("/")) > 1:
							toSend += "/".join(text.split("/")[1:])

					if toSend in obj.examples:
						print("EEEEEXXXXXXAMMMPLEEEEEE XMPL")
						if "answer" in obj.examples[toSend]:
							toSend = obj.examples[toSend]["answer"]

						master.sendMessage(chatID, toSend)
						time.sleep(1)

					master.ProcessServiceAsync(
						obj, {"origin": chatID, "user": user, "content": toSend})

				print("RRRRRRRRRRRRRRRRRRRRRedirecting")
				print("RRRRRRRRRRRRRRRRRRRRRedirecting")
				print("RRRRRRRRRRRRRRRRRRRRRedirecting")
				print("RRRRRRRRRRRRRRRRRRRRRedirecting")
				print("RRRRRRRRRRRRRRRRRRRRRedirecting")
				print("RRRRRRRRRRRRRRRRRRRRRedirecting", invite)
				return redirect(invite)

	if text in refs:
		return redirect(refs[text])
	else:
		return redirect("/")


if __name__ == '__main__' and False:
		print("1111111111111111111")
		print("1111111111111111111")
		print("1111111111111111111, port:", MYPORT)
		# socketio.run(app, host='0.0.0.0', port=MYPORT, certfile="ssl/cert.pem",
		# keyfile="ssl/key.pem", server_side=True, debug=True, use_reloader=False)
		socketio.run(app, host='0.0.0.0', port=MYPORT,
					 server_side=True, debug=True, use_reloader=False)
else:
	print("2222222222222222222")
	print("2222222222222222222")
	print("2222222222222222222!!!!!!!!!", MYPORT)

	# socketio.run(app)
	# socketio.run(app, port = MYPORT, use_reloader=False)
	# print(f"MY PORT {MYPORT}")
	# # socketio.run(app, port = MYPORT, use_reloader=False)

	# THIS WAS WORKING!!!!!!!!!!!!!!!!!!
		# socketio.run(app, host='0.0.0.0', port = MYPORT, certfile="cert.pem", keyfile="key.pem", server_side=True, debug=True, use_reloader=False)
		# socketio.run(app, host='0.0.0.0', port = MYPORT, ssl_context='adhoc', server_side=True, debug=True, use_reloader=False)
		# socketio.run(app, host='0.0.0.0', port=MYPORT, certfile="ssl/cert.pem",
		# 			 keyfile="ssl/key.pem", server_side=True, debug=True, use_reloader=False)
	# socketio.run(app, host='0.0.0.0', port=MYPORT, debug=True, use_reloader=False)
	socketio.run(app, host='0.0.0.0', port=MYPORT, debug=True, use_reloader=True)
