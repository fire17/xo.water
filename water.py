#xo.water.py
# Water System
import requests
from tools import *
from wservices import LoadWaterServices
from wa_automate_socket_client import SocketClient
from xo.redis import xoRedis, xo , Expando
from customTextEncoder import *
import emoji


# Basic
import time
import os
import traceback
import json


# Sockets
from tokenize import group

#Extra
from pprint import pprint as pp
from pprint import pformat as pf


# from rich.prompt import Prompt


# Wa Automate Docs: 
# https: // openwa.dev/docs/api/classes/api_Client.Client

# simple Service
# npx @open-wa/wa-automate --socket -p 8085 -k "$WA_KEY"
# python3 simple.py

# from test import *
# water.Simple.send(number="972543610404", msg="Hello from simple.py")
# water.Simple.send(number="972547932000", msg="Hello from simple.py")

######################################    imports and setup    ####################################################



cwd = os.path.dirname(os.path.abspath(__file__))
print(" ::: cwd:", cwd)

water = xoRedis('water', host="localhost", port=6379)
# from xo import *



appServices = None

def getEnvKey(key="WA_KEY"):
	return os.environ.get(key, "Please export the WA_KEY environment variable.")
wa_key = getEnvKey()


if not os.path.exists(f"{cwd}/secrets.json"):
	print("Please set up the secrets file before running the script.")
	print("""{
  "WA_KEY": "your_wa_key"
}""")
else:
	with open(f"{cwd}/secrets.json", "r") as f:
		secrets = json.load(f)
		# Update the environment with the values in the JSON file
		os.environ.update(secrets)
		# Your script code goes here
		# You can access the environment variables using the os.environ dictionary
		wa_key = os.environ["WA_KEY"]
		print(" ::: Loaded secrets from secrets.json ::: WA_KEY=", wa_key)

# sys.exit(1)

host, port = "localhost", 8085
# from common import *
# from dal.utilities.rename_process import set_proc_name
# set_proc_name(b'simple')
defaultNumber = "972547932000@c.us"


def ParticipantChanged(data,*a,**kw):
	print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
	print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
	print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
	print(":::::::::::::::::", a)
	pp(data)
	print(":::::::::::::::::", kw)
	print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
	print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
	print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
	origin = data["data"]["chat"]
	user = data["data"]["who"]
	action = data["data"]["action"]
	if action == "add":
		print(" ::: Participant Added ::: ", user)
		if user == defaultNumber:
			print(" ::: Welcome Admin ::: ", user)
		else:
			print(" ::: Welcome New User ::: ", user)

		# Give a second for the service to be ready for the group
		# time.sleep(3)

		timeout, serviceC = 30, 0
		foundService, service = None, None
		print("11111111111111110")
		serviceName = None
		while (origin not in water.groups.value):
			serviceName = water.groups[origin].service.value
			serviceC+=1
			time.sleep(1)
			print("AWAITING SERVICE Name....",serviceC)
		print("1111111111111111",serviceName)
		if origin in water.groups.value:
			timeout, serviceC = 30, 0
			serviceName = water.groups[origin].service.value
			while (serviceName is None and serviceC<timeout):
				serviceName = water.groups[origin].service.value
				serviceC+=1
				time.sleep(1)
				print("AWAITING SERVICE name Final....",serviceC)
			if serviceName != None:
				print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
				print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
				print(f" @@@@@@@@ PARTICIPANT CHANGE IN SERVICE {serviceName} ")
				print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
				print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
				foundService = serviceName
				service = water.services[foundService]._service

				print("S"*40)
				pp(service)
				print("S"*40)
				# water.sendMessage(_message=f"_New USER Participant ADDED - Service: {foundService} User:{user}_ \n_new rolling group in the background {newGroupID} {newFinal['invite_link']}_", _number=origin)
				water.sendMessage(_message=f"_New USER Participant ADDED - Service: {foundService} User:{user}_" , _number=origin)
				water.sendMessage(_message=str(pf(service)), _number=origin)
				if service.welcome and service.welcome != "":
					water.sendMessage(_message=service.welcome, _number=origin)
					# Kick or remove from rolling
					if "throwAfterWelcome" in service.__dir__() and service.throwAfterWelcome and (False or True):
						water.sendMessage(_message=f"*Thanks For Login using {service.title}*\n_DYNAMIC GOODBYE + SEND OAUTH BACK_", _number=origin)
						time.sleep(5)
						water._driver.removeParticipant(origin, user)
					else:
						print("O O O O O O O O O O O O O O O O O O O O O O","throwAfterWelcome" in service.__dir__() and service.throwAfterWelcome)
						print("O O O O O O O O O O O O O O O O O O O O O O")
						print("O O O O O O O O O O O O O O O O O O O O O O")
						print("O O O O O O O O O O O O O O O O O O O O O O")
						print("O O O O O O O O O O O O O O O O O O O O O O")
						print("O O O O O O O O O O O O O O O O O O O O O O")
						print("O O O O O O O O O O O O O O O O O O O O O O")
						targetService = water.rollingGroups[origin].service()
						print(" :::::::::::::: ENTERED ROLLING GROUP of ",foundService, targetService)
						#remove from roling available (if not admin)
						
						# TODO: Change _number = origin to service.admingroup
						if user != defaultNumber:
							# water.rollingGroups[origin]._delete("service")
							# water.rollingGroups._delete(origin)
							######### water.rollingGroups.available[foundService] += [origin]

							# av = water.rollingGroups.available
							if water.rollingGroups.available[foundService].groups() == None:
								water.rollingGroups.available[foundService].groups._setValue([])
								print(" RRRRRRRRRRRRRR CLEARED ROLLING",foundService)
							if water.rollingGroups.available[foundService].groups() is not None and origin in water.rollingGroups.available[foundService].groups():
								water.rollingGroups.available[foundService].groups = water.rollingGroups.available[foundService].groups().remove(origin)
								print(" RRRRRRRRRRRRRR REMOVED FROM ROLLING",foundService)
							else:
								print(" RRRRRRRRRRRRRR NOTTTTTT REMOVED FROM ROLLING",foundService)

							#DO i NEED TO REMOVE LINK> NAH, its not accesible if the origin group isnt in groups
								
							########### water.temp.a = water.temp.a().remove(2)
							#create new group
							
							# create new group in the stack
							# TODO: check isMe istead of defaultNumber (change default number on connected)
							#if user != defaultNumber:
							print(f" ::: NEWWWWWWWW USER JOINED!!!!!!!!!!!! {user} ")
							# TODO: Change _number = origin to service.admingroup
							# thisGroupName = "Get current name"

							#Remove this chat from available rolling groups / or kick out
							#check if there are less availalbe rolling groups for this service then should
							# create a new rolling group and add it to available rolling groups

							
							#add new group to rolling availalbe
							newGroupID, newFinal = "FAILED", {'invite_link':"FAILED"}
							try:
								newGroupID, newFinal = newGroupService(foundService, debug=True, _number = origin, setServiceAdminGroup=True)
							except:
								print(f" FAILED CREATING GROUP ")
								print(f" FAILED CREATING GROUP ")
								print(f" FAILED CREATING GROUP ",foundService)
								print("F F F F F F F F F F F F F F F F F F F F\n"*10)
							# if isMe:
								# groupID, final = newGroupService(body.split(" ")[1], debug=True, _number = origin, setServiceAdminGroup=True)
							# else:
							# 	groupID, final = newGroupService(body.split(
							# 		" ")[1], debug=True, _number=origin, setServiceAdminGroup=True, users=[user, "autoLeave"])
							# 	water.sendMessage(_message=f"/setgroup {groupID} {body.split(' ')[1]}", _number=origin)
							# 	water.sendMessage(
							# 		_message=f"{final['invite_link']}", url=final['invite_link'], _number=origin)
							# return groupID, final
							''' #PREV/OLD
							thisGroupName = water.groups[origin].name
							base64icon = water.groups[origin].base64icon
							newGroupID, newFinal = newGroupService(targetService=targetService, debug=True, addRolling=True, _number = origin, overrideTitle = thisGroupName, overrideBase64Icon = base64icon)
							water.sendMessage(
								_message=f"_New USER Participant ADDED - Service: {targetService} User:{user}_ \n_new rolling group in the background {newGroupID} {newFinal['invite_link']}_", _number=origin)
							'''
							water.sendMessage(
								_message=f"_New USER Participant ADDED - Service: {foundService} User:{user}_ \n_new rolling group in the background {newGroupID} {newFinal['invite_link']}_", _number=origin)
							water.rollingGroups[newGroupID].service = foundService
							if water.rollingGroups.available[foundService].groups() == None:
								water.rollingGroups.available[foundService].groups = []
							if newGroupID == 'FAILED':
								print (" X F X F X F X F X F X F X ")
								print (" X F X F X F X F X F X F X ")
								print (" X F X F X F X F X F X F X ")
								print (" X F X F X F X F X F X F X ")
								print (" X F X F X F X F X F X F X ", newFinal)
							else:
								water.rollingGroups.available[foundService].groups += [newGroupID]
								water.rollingGroups.available[foundService].groups[newGroupID].link = newFinal['invite_link']
							print("O O O O O  !!!!!!!!!!!!!!!!!!!!  O O O O O O",newFinal['invite_link'])
							print("O O O O O  !!!!!!!!!!!!!!!!!!!!  O O O O O O",newFinal['invite_link'])
							print("O O O O O  !!!!!!!!!!!!!!!!!!!!  O O O O O O",newFinal['invite_link'])
							print("O O O O O  !!!!!!!!!!!!!!!!!!!!  O O O O O O",newFinal['invite_link'])
							print("O O O O O  !!!!!!!!!!!!!!!!!!!!  O O O O O O",newFinal['invite_link'])
							print("O O O O O  !!!!!!!!!!!!!!!!!!!!  O O O O O O",newFinal['invite_link'])
							print("O O O O O  !!!!!!!!!!!!!!!!!!!!  O O O O O O",newFinal['invite_link'])
							print("O O O O O  !!!!!!!!!!!!!!!!!!!!  O O O O O O",newFinal['invite_link'])
							print("O O O O O  !!!!!!!!!!!!!!!!!!!!  O O O O O O",water.rollingGroups.available[foundService].groups[newGroupID].link())
							print("O O O O O  !!!!!!!!!!!!!!!!!!!!  O O O O O O",water.rollingGroups.available[foundService].groups[newGroupID].link())
							print("O O O O O  !!!!!!!!!!!!!!!!!!!!  O O O O O O",water.rollingGroups.available[foundService].groups[newGroupID].link())
							print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


		if origin and water.rollingGroups[origin].service() is not None and False:
		# if origin in water.rollingGroups.value:
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			print("O O O O O O O O O O O O O O O O O O O O O O")
			targetService = water.rollingGroups[origin].service()
			print(" :::::::::::::: ENTERED ROLLING GROUP of ",targetService)
			# create new group in the stack
			# TODO: check isMe istead of defaultNumber (change default number on connected)
			if user != defaultNumber:
				print(f" ::: NEWWWWWWWW USER JOINED!!!!!!!!!!!! {user} ")
				# TODO: Change _number = origin to service.admingroup
				# thisGroupName = "Get current name"

				#Remove this chat from available rolling groups / or kick out
				#check if there are less availalbe rolling groups for this service then should
				# create a new rolling group and add it to available rolling groups


				thisGroupName = water.groups[origin].name
				base64icon = water.groups[origin].base64icon
				newGroupID, newFinal = newGroupService(targetService=targetService, debug=True, addRolling=True, _number = origin, overrideTitle = thisGroupName, overrideBase64Icon = base64icon)
				water.sendMessage(
					_message=f"_New USER Participant ADDED - Service: {targetService} User:{user}_ \n_new rolling group in the background {newGroupID} {newFinal['invite_link']}_", _number=origin)
			else:
				print(f" ::: USER AND ORIGIN ARE THE SAME {origin} ")
				water.sendMessage(
					_message=f"_Admin Participant Changed - Service: {targetService}_", _number=origin)
		else:
			print(" ::: Service ::: ", origin, foundService, service)
		
		# TODO: Change _number = origin to service.admingroup
		if user == defaultNumber:
			#TODO: ADD TO ROLLING
			print(" ::: ADMIN FIRST TIME IN GROUP ::: ",foundService)
			water.rollingGroups[origin].service = foundService
			if water.rollingGroups.available[foundService].groups() == None:
				water.rollingGroups.available[foundService].groups._setValue([])
			water.rollingGroups.available[foundService].groups += [origin]
			#TODO: Set chat in available

			print(" ::: Rolling Groups ::: ", origin in water.rollingGroups, water.rollingGroups)
		# water.Simple.send(number=user, msg="Welcome to the group!")
	# PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
	# ::::::::::::::::: ()
	# {'data': {'action': 'add',
	#           'chat': '120363031776520233@g.us',
	#           'who': '972547932000@c.us'},
	#  'event': 'onGlobalParticipantsChanged',
	#  'id': '88bc2dcc-5e1c-48bf-b5e4-bdbcbcd053ba',
	#  'sessionId': 'session',
	#  'ts': 1673970719200}
	# ::::::::::::::::: {}
	# PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
	# PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
		

water.ParticipantChanged = ParticipantChanged

def manage_polls(data,*a,**kw):
	print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
	print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
	print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
	print(":::::::::::::::::", a)
	pp(data)
	print(":::::::::::::::::", kw)
	print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
	print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
	print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
	

water.ManagePolls = manage_polls


def send(self, chatID, content, thumbnail = None, service = "test", autoPreview = False):
	print("SSSSSSSSSSSSSSSSSS sending", chatID, content, autoPreview)
	if autoPreview and "http" in content:
		if thumbnail is None or "dict" not in type(thumbnail) or len(thumnbnail)==0:
			thumbnail = {}
		url = str(re.search("(?P<url>https?://[^\s]+)", content).group("url"))
		preview = self.GetWebpagePreview(url)
		if "image" in preview:
			print("!!!!!!!",thumbnail,type(preview))
			thumbnail["imageurl"] = preview["image"]
		else:
			thumbnail["imageurl"] = ""
		if "title" in preview:
			thumbnail["title"] = preview["title"]
		if "description" in preview:
			thumbnail["desc"] = preview["description"]
		thumbnail["link"] = url


	if "/" in content:
		if "image" == content.split("/")[0]:
			imagepath = "/".join(content.split("\n")[0].split("/")[1:])
			sendBack = ""
			if "\n" in content:
				sendBack = "\n".join(content.split("\n")[1:])
			return self.driver.send_media(imagepath,chatID,sendBack)
				# self.driver.send_media(imagepath,chatID,content)
	if thumbnail is not None:
		imageurl = "https://media1.tenor.com/images/7528819f1bcc9a212d5c23be19be5bf6/tenor.gif"
		title = "AAAAAAAAAA"
		desc = "BBBBBBB"
		link = imageurl
		path = ""
			#
			# pT = Thread(target = self.sendPreview, args = [[chatID, url, content]])
			# pT.start()
			# return True

		sendAttachment = False
		if "imageurl" in thumbnail:
			if thumbnail["imageurl"] is None:
				thumbnail["imageurl"] = ""
				imageurl = ""
			else:
				imageurl = thumbnail["imageurl"]
			path = self.download_image(service = service, pic_url=imageurl)
			print("PPPPPPPPPPPPPPPPPPP",path)
			if "title" in thumbnail and thumbnail["title"] is not None:
				title = thumbnail["title"]
				if "desc" in thumbnail and thumbnail["desc"] is not None:
					desc = thumbnail["desc"]
					if "link" in thumbnail and thumbnail["link"] is not None:
						link = thumbnail["link"]
						sendAttachment = True

		if sendAttachment:
			res = self.driver.send_message_with_thumbnail(path,chatID,url=link,title=title,description=desc,text=content)
			print(res)
			print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT", path, "LINK",link,"TEXT",content)
			return res

	return self.driver.sendMessage(chatID, content)


def sendMessage(_message="fresh grass", _number="972547932000@c.us", url = None, *a, **kw):
	if "_xo" in kw:
		_message = kw["_xo"].value
	if isinstance(_message, dict):
		_number, _message = _message["number"], _message["message"]
	elif isinstance(_message, list):
		if len(_message) == 1:
			_message = _message[0]
			if isinstance(_message, str):
				_message = _message
			else:
				_number, _message = _message["number"], _message["message"]
		elif len(_message) == 2:
			_message, _number,  = _message
	# print(":::!!!!!!!send::::::::::::::", _message, _number)
	payload = None
	# print(payload)
	# if isinstance(payload, list):
	# 	if len(payload) == 1:
	# 		payload = payload[0]
	# 		if isinstance(payload, str):
	# 			_message = payload
	# 		else:
	# 			_number, _message = payload["number"], payload["message"]
	# 	elif len(payload) == 2:
	# 		_number, _message = payload
	# 	payload = None
	# elif isinstance(payload, str):
	# 	_message = payload
	# 	payload = None
			
	print(":::::::::::::::::", payload, _number, _message)
	number = payload["number"] if payload else _number
	message = payload["message"] if payload else _message
	print(":::!!!!!!!send::::::::::::::", message, number)
	if "_driver" in water:
		print(f" Sending Message..... {number} {message} ::: {a} {kw} \n", payload, "\n")
		
		# else:
		if url is not None:
			print("WITH AUTO PREVIEW!!!!!!!!!!!")
			print("WITH AUTO PREVIEW!!!!!!!!!!!")
			print("WITH AUTO PREVIEW!!!!!!!!!!!")
			print("WITH AUTO PREVIEW!!!!!!!!!!!")
			# water._driver.sendLinkWithAutoPreview(number, url, text = message)
			water._driver.sendLinkWithAutoPreview(number, url, message)
		else:
			print("FFFFFFFFFFFFFF",number, "OOOOOOOOOOOO",message)
			water._driver.sendText(number, message)
		print(f" Message Sent ::: {a} {kw} \n", payload, "\n")
	else:
		print(" ::: Driver not connected yet :::")


water.sendMessage = sendMessage

_client = None

class flow(Expando):
	
	def load(**kw):
		pass
	def addStep(**kw):
		pass
	def newResponse(*a,**kw):
		pass 
	def nextPhase():
		pass 
	def runFlow(**kw):
		pass



# water.newContact = lambda payload, *a,**kw : water.addContact(payload)
# water.newMedia = lambda payload, *a,**kw : water.sendMedia(payload)
# water.newLocation = lambda payload, *a,**kw : water.sendLocation(payload)
# water.newSticker = lambda payload, *a,**kw : water.sendSticker(payload)
# from services.googler import Googler
from services.api import *
# from services.warmWinters import WarmWinters

# water.services.warmWinters = WarmWinters()
def loadGroups():
	groups = water.groups()
	if groups == None:
		water.groups._setValue([])
		groups = water.groups()
	for group in groups:
		water.groups[group]()
		water.groups[group].service()
		print(" ::: Loaded Group", group, water.groups[group].service.value)


loadGroups()


def setGroupToService(group, service, setServiceAdminGroup = False, groupName = None, overrideIconURL = None, overrideBase64Icon = None):
	if service in water.services:
		print(f" ::: SETTING GROUP {group} to service {service}")
		print(f" ::: SETTING GROUP {group} to service {service}")
		print(f" ::: SETTING GROUP {group} to service {service}")
		print(f" ::: SETTING GROUP {group} to service {service}")
		print(f" ::: SETTING GROUP {group} to service {service}")
		print(f" ::: SETTING GROUP {group} to service {service}")
		print(f" ::: SETTING GROUP {group} to service {service}")
		print(f" ::: SETTING GROUP {group} to service {service}")
		print(f" ::: SETTING GROUP {group} to service {service}")
		print(f" ::: SETTING GROUP {group} to service {service}")
		water.groups += [group]
		water.groups[group].service = service
		water.services[service].groups[group]
		serviceObject = water.services[service]._service
		if groupName is None:
			groupName = serviceObject.title

		water.groups[group].name = groupName
		# serviceObject: someService = water.services[service]._service
		if setServiceAdminGroup:
			serviceObject.SuperAdminGroup = group
		water._driver.setGroupTitle(group, groupName+"!!!")
		
		if overrideBase64Icon is None:
			icon_url = serviceObject.iconURL
			if overrideIconURL is not None:
				icon_url = overrideIconURL

			

			if "path:" in icon_url:
				imageData = open(icon_url.replace("path:",""), "rb").read()
				imageDataB64 = base64.b64encode(imageData)
			else:
				image = requests.get(icon_url).content
				imageDataB64 = base64.b64encode(image)

			# water._driver.setGroupIconByUrl(group, serviceObject.iconURL)
			# open image from 
			# imageDataB64 = base64.b64encode(image)
			print(str(imageDataB64))
			# finalBase64 = f"data:image/jpeg;base64,{str(imageDataB64)[2:-1]}"
			
			image_type = "png"
			if ".jpg" in icon_url or ".jpeg" in icon_url:
				image_type = "jpeg"
			finalBase64 = f"data:image/{image_type};base64,{str(imageDataB64)[2:-1]}"
		else:
			finalBase64 = overrideBase64Icon
		water.groups[group].base64icon = finalBase64
		print("=====================")
		print(finalBase64)
		print("=====================")
		water._driver.setGroupIcon(group, finalBase64)

		water.sendMessage(f"[Changing Group]\n {group} to service {service} :::",group, water.services[service]._service.title)
	else:
		print(f" --- Service {service} is not loaded in water ---")
water.setGroupToService = setGroupToService


def loadServices(water):	
	# v0.0.1
	# water.services.googler.api = WaterAPI()
	# water.services.googler = Googler()

	# v0.1
	# for service in [Googler,]:
	# 	api = WaterAPI(water._driver)
	# 	api.service = service
	# 	water.services[service.name]._api = api
	# 	water.services[service.name]._service = service(api)
	
	# v0.2
	all_services = LoadWaterServices(water)
	for service in all_services:
		print(" ::: Loaded Service", service)
		# api = WaterAPI(water._driver)
		# api.service = service
		Service = all_services[service]
		water.services[Service.name]._service = Service
		water.services[Service.name]._api = Service._api
		
	print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
	print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
	print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
	print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
	for service in water.services:
		print(" :::::::::: service ", service, " ::: ", water.services[service])
		# water.services[service.name]._service = service(api)




water._groups = {}
# water._apps = {"Google": {"name": " GOOGLE", "icon_url": "",
# 						   "description": "Google Search", "invite_link": ""}}


# # @Simple
# def setGroupApp(group_id, app, *args, **kwargs):
# 	if "_driver" not in water:
# 		print(" setGroupApp ::: Driver not connected yet :::")
# 		return False

# 	if group_id not in water._groups:
# 		water._groups[group_id] = {}
# 	# if app not in water._apps:
# 	# 	water._apps[app] = {}

# 	water._groups[group_id]["app"] = app

# 	# Change group name to app name
# 	water._driver.setGroupTitle(group_id, water._apps[app]["name"])
# 	# water._driver.setGroupIconByUrl(water._groups[group]["id"], water._apps[app]["icon_url"])
# 	# water._driver.setGroupDescription(group_id, water._apps[app]["description"])
# 	print("@@@@@@@@@@@@@@@@@@ setGroupApp: ",
# 		  group_id, water._apps[app]["name"], water._apps[app]["description"])
# 	return True


# @Simple
def createGroup(Name=" ::: Test ::: ", participants=["972543610404@c.us"], debug=False, *args, **kwargs):
	print("Creating group: ,,,,,,,,")
	if "_driver" not in water:
		print(" ::: Driver not connected yet :::")
		return False
	res = water._driver.createGroup(Name, participants)
	if "Error: " in res:
		print(" ::: createGroup failed  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX :::\n"*10,res)
		return None
	print("Created group: ", res)
	time.sleep(1)
	# res2 = "FAILED"
	# try:
	# 	res2 = water._driver.removeParticipant(
	# 		res["wid"]["_serialized"], participants[0])
	# except:
	# 	print(" ::: remove_participant failed :::")
	# 	traceback.print_exc()
	# water._driver.setGroupTitle(res["wid"]["_serialized"], "XXXXXXXXXXXXXXX")
	water._driver.setGroupTitle(res["wid"]["_serialized"], " ::: "+Name.upper()+" ::: ")
		
	# print("removed participant: ", res2)
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",res["wid"]["_serialized"])
	foundInvite, inviteCount, maxCount = False,0,10
	while not foundInvite and inviteCount < maxCount:
		inviteCount += 1
		try:
			res["invite_link"] = water._driver.getGroupInviteLink(res["wid"]["_serialized"])
			if "error" not in res["invite_link"]:
				foundInvite = True
			else:
				print("i x i x i x i x i x i x i x i x i ")
				print("i x i x i x i x i x i x i x i x i ")
				print("i x i x i x i x i x i x i x i x i ")
				print("i x i x i x i x i x i x i x i x i ")
				print("i x i x i x i x i x i x i x i x i ")
				print("i x i x i x i x i x i x i x i x i ")
		except:
			print(" ::: invite_link failed :::",inviteCount)
			traceback.print_exc()

	print("invite link: ", res["invite_link"])
	try:
		res["info"] = water._driver.inviteInfo(res["invite_link"])
	except:
		print(" ::: inviteInfo failed :::")
		traceback.print_exc()
		
	print("info : ", res["info"])
	# time.sleep(3)
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

	# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", res["info"]["groupMetadata"]["id"])
	# water._driver.sendMessage("WELCOME!",res["wid"]["_serialized"])
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	# water._driver.sendMessage("WELCOME!", "120363029005529843@g.us")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	groupID = res["wid"]["_serialized"]
	if "winter" in Name:
		# water._driver.sendImage("https://i.ibb.co/1dZj8pT/winter.jpg", res["wid"]["_serialized"], "WELCOME!")
		water._driver.setGroupTitle(res["wid"]["_serialized"], " ::: *חורף חם* ::: ")
		warmWintersMsg = """*חורף חם:*
		שלום ותורה רבה שפניתם אלינו!
		המשימה שלנו היא לוודא שאין אף אחד שקר לו החורף.
		אם אתם או מישהו שאתם מכירים צריכים פטרון חימום , לחצו על "בקשה לחימום"
		לכל מי שמעוניין לעזור לחצו על הכפתורים המתאימים...

		תודה רבה על ההשתתפות!
		שיהיה לכולנו *חורף חם!*"""
		# water.sendMessage(warmWintersMsg,res["info"]["groupMetadata"]["id"])
		water.sendMessage(warmWintersMsg,groupID)
		water._driver.sendPoll(res["wid"]["_serialized"], "*:חורף חם*",["בקשת חימום", "תרומת חימום", "עזרה במסירה", "הרשמה כעמותה/ספק"])

	else:
		water.sendMessage("[WELCOME!]", groupID)
		water._driver.setGroupTitle(groupID, "XXXXXXXXXXX")

		# water._driver.sendPoll(res["wid"]["_serialized"], "How do you like this service?",["good", "great!", "niiccce"])
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


	print("invite link: ", res["invite_link"])
	print("invite link: ", res["invite_link"])
	print("invite link: ", res["invite_link"])
	print("invite link: ", res["invite_link"])
	if debug:
		water.sendMessage(_message=f"GROUP CREATED {res}", _number=groupID)
	return res

water.createGroup = createGroup

# @Simple
def listGroups(search="*", *args, **kwargs):
	if "_driver" not in water:
		print(" ::: Driver not connected yet :::")
		return False
	res = water._driver.getAllGroups()
	final = {}
	for group in res:
		if search is "*" or search in group["name"]:
			print("group: ", group)

			print()
			final[group["id"]] = {"name": group["name"], "id": group["id"],
						 "participants": group["groupMetadata"]["participants"],
						 "full_data": group, }
			if "desc" in group["groupMetadata"]:
				final[group["id"]]["desc"] = group["groupMetadata"]["desc"]
			# getGroupInviteLink(group["id"])
			# final[group["id"]] = group
		# elif search in group["name"]:
		# 	final[group["id"]] = group

	for key in final:
		print("key: ", key, " group: ", final[key]["name"], final[key]["id"])
	# print("list groups: ", final)
	return {"groups": final}

# wa setup in readme
# wa api docs

# run protocol docs
# run user stories:
# 1. user can send a message to a group
# 2. user can send a message to a contact
# 3. user can send a message to a contact and get a response
# 4. user can send a message to a group and get a response
# fucking run it already
# make dynamic groups
# make rolling groups
# make fire.io links for groups


# add graphana and prometheus
# add logging ?
# add tests
# add CI/CD
# add docker
# add kubernetes
# add terraform
# add ansible
# add aws
# add vercel
# add github
# add gitlab
# add bitbucket



def registerCallbacks():

	# water._driver = openwa.driver

	# Create lambda functions for each method in the whatsapp driver
	water.newGroup @= lambda payload, *a,**kw : water.createGroup(payload, *a,**kw)
	water.message @= lambda payload, *a,**kw : water.sendMessage(payload, *a,**kw)
	water.newLink @= lambda payload, *a,**kw : water.createLink(payload)
	water.silence @= lambda payload, *a,**kw : water.silenceGroup(payload)
	water.unsilence @= lambda payload, *a,**kw : water.unsilenceGroup(payload)
	water.poll @= lambda payload, *a,**kw : water.createPoll(payload)
	# water.onMessage @= lambda payload, *a,**kw : water.ManageIncoming(payload)

	# water.timedMessage = lambda payload, *a,**kw : water.sendTimedMessage(payload)
	# water.onAck @= lambda payload, *a,**kw : water.onMessageAck(payload)
	# water.onParticipantsChanged @= lambda payload, *a,**kw : water.handle.onGroupParticipantsChanged(payload)
	# water.onAddedToGroup @= lambda payload, *a,**kw : water.handle.onAddedToGroup(payload)
	# water.onRemovedFromGroup @= lambda payload, *a,**kw : water.handle.onRemovedFromGroup(payload)
	# water.onGroupCreated @= lambda payload, *a,**kw : water.handle.onGroupCreated(payload)
	# water.onGroupUpdated @= lambda payload, *a,**kw : water.handle.onGroupUpdated(payload)
	# water.onGroupDeleted @= lambda payload, *a,**kw : water.handle.onGroupDeleted(payload)
	# water.onGroupSettingsChanged @= lambda payload, *a,**kw : water.handle.onGroupSettingsChanged(payload)
	# water.onGroupParticipantIsTyping @= lambda payload, *a,**kw : water.handle.onGroupParticipantIsTyping(payload) # ghost effect
	# water.onGroupParticipantIsRecordingVoice @= lambda payload, *a,**kw : water.handle.onGroupParticipantIsRecordingVoice(payload) # ghost effect
	# water.onGroupParticipantIsPlayingVoice @= lambda payload, *a,**kw : water.handle.onGroupParticipantIsPlayingVoice(payload) # ghost effect
	# water.getGroupAdmins @= lambda payload, *a,**kw : water.Get.GroupAdmins(payload)
	# water.getGroupMembers @= lambda payload, *a,**kw : water.Get.GroupMembers(payload)
	# water.getGroupInviteLink @= lambda payload, *a,**kw : water.Get.GroupInviteLink(payload)
	# water.getGroupInfo @= lambda payload, *a,**kw : water.Get.GroupInfo(payload)
	# water.getGroupMetadata @= lambda payload, *a,**kw : water.Get.GroupMetadata(payload)
	# water.getGroupParticipantIDs @= lambda payload, *a,**kw : water.Get.GroupParticipantIDs(payload)
	# water.getGroupParticipants @= lambda payload, *a,**kw : water.Get.GroupParticipants(payload)
	# water.getGroupPicture @= lambda payload, *a,**kw : water.Get.GroupPicture(payload)
	# water.getGroupSettings @= lambda payload, *a,**kw : water.Get.GroupSettings(payload)
	# water.getGroupStats @= lambda payload, *a,**kw : water.Get.GroupStats(payload)
	# water.getGroupWelcomeMessage @= lambda payload, *a,**kw : water.Get.GroupWelcomeMessage(payload)
	# water.getGroupDescription @= lambda payload, *a,**kw : water.Get.GroupDescription(payload)
	# water.getGroupRules @= lambda payload, *a,**kw : water.Get.GroupRules(payload)
	# water.getGroupAnnouncements @= lambda payload, *a,**kw : water.Get.GroupAnnouncements(payload)
	# water.getMessage @= lambda payload, *a,**kw : water.Get.Message(payload)
	# water.getMessages @= lambda payload, *a,**kw : water.Get.Messages(payload)
	# water.getProfilePicFromServer @= lambda payload, *a,**kw : water.Get.ProfilePicFromServer(payload)
	# water.getProfilePicFromUser @= lambda payload, *a,**kw : water.Get.ProfilePicFromUser(payload)
	# water.getProfilePicThumb @= lambda payload, *a,**kw : water.Get.ProfilePicThumb(payload)
	# water.getProfilePicUrl @= lambda payload, *a,**kw : water.Get.ProfilePicUrl(payload)
	# water.getBatteryLevel @= lambda payload, *a,**kw : water.Get.BatteryLevel(payload)
	# water.getWAVersion @= lambda payload, *a,**kw : water.Get.WAVersion(payload)
	# water.getChatById @= lambda payload, *a,**kw : water.Get.ChatById(payload)
	# water.getChatByName @= lambda payload, *a,**kw : water.Get.ChatByName(payload)
	# water.getChatIds @= lambda payload, *a,**kw : water.Get.ChatIds(payload)
	# water.getChats @= lambda payload, *a,**kw : water.Get.Chats(payload)
	# water.getCommonGroups @= lambda payload, *a,**kw : water.Get.CommonGroups(payload)
	# water.getContact @= lambda payload, *a,**kw : water.Get.Contact(payload)
	# water.getContactIds @= lambda payload, *a,**kw : water.Get.ContactIds(payload)
	# water.getContacts @= lambda payload, *a,**kw : water.Get.Contacts(payload)
	# water.getMe @= lambda payload, *a,**kw : water.Get.Me(payload)
	# water.getMyGroups @= lambda payload, *a,**kw : water.Get.MyGroups(payload)
	# water.getMyStatus @= lambda payload, *a,**kw : water.Get.MyStatus(payload)
	# water.getMessageViews @= lambda payload, *a,**kw : water.Get.MessageViews(payload)
	# water.createQuote @= lambda payload, *a,**kw : water.create.Quote(payload)
	# water.createContact @= lambda payload, *a,**kw : water.create.Contact(payload)
	# water.deleteChat @= lambda payload, *a,**kw : water.Delete.Chat(payload)
	# water.deleteMessages @= lambda payload, *a,**kw : water.Delete.Messages(payload)
	# water.deleteProfilePic @= lambda payload, *a,**kw : water.Delete.ProfilePic(payload)
	# water.deleteStatus @= lambda payload, *a,**kw : water.Delete.Status(payload)
	# water.demoteParticipants @= lambda payload, *a,**kw : water.group.demoteParticipants(payload)
	# water.elevateParticipants @= lambda payload, *a,**kw : water.group.elevateParticipants(payload)
	# water.forwardMessages @= lambda payload, *a,**kw : water.forwardMessages(payload)
	# water.reply @= lambda payload, *a,**kw : water.reply(payload)
	# water.changeGroupService @= lambda payload, *a,**kw : water.change.GroupService(payload)
	# water.changeGroupDescription @= lambda payload, *a,**kw : water.change.GroupDescription(payload)
	# water.changeGroupRules @= lambda payload, *a,**kw : water.change.GroupRules(payload)
	# water.changeGroupAnnouncements @= lambda payload, *a,**kw : water.change.GroupAnnouncements(payload)
	# water.changeGroupPicture @= lambda payload, *a,**kw : water.change.GroupPicture(payload)
	# # water.changeGroupWelcomeMessage @= lambda payload, *a,**kw : water.change.GroupWelcomeMessage(payload)
	# water.changeGroupSettings @= lambda payload, *a,**kw : water.change.GroupSettings(payload)
	# water.changeMyName @= lambda payload, *a,**kw : water.change.MyName(payload)
	# water.changeMyStatus @= lambda payload, *a,**kw : water.change.MyStatus(payload)
	# water.changeMyProfilePic @= lambda payload, *a,**kw : water.change.MyProfilePic(payload)
	# water.changeGroupAdmins @= lambda payload, *a,**kw : water.change.GroupAdmins(payload)
	# water.changeGroupSubject @= lambda payload, *a,**kw : water.change.GroupSubject(payload)
	# water.changeGroupDescription @= lambda payload, *a,**kw : water.change.GroupDescription(payload)
	# water.changeGroupName @= lambda payload, *a,**kw : water.change.GroupName(payload)
	# water.transcribeAudio @= lambda payload, *a,**kw : water.transcribe.Audio(payload)
	# water.sendContact @= lambda payload, *a,**kw : water.send.Contact(payload)
	# water.sendFile @= lambda payload, *a,**kw : water.send.File(payload)
	# water.sendImage @= lambda payload, *a,**kw : water.send.Image(payload)
	# water.sendImageAsSticker @= lambda payload, *a,**kw : water.send.ImageAsSticker(payload)
	# water.sendLinkWithAutoPreview @= lambda payload, *a,**kw : water.send.LinkWithAutoPreview(payload)
	# water.sendLinkWithCustomThumb @= lambda payload, *a,**kw : water.send.LinkWithCustomThumb(payload)
	# water.sendLinkWithDescription @= lambda payload, *a,**kw : water.send.LinkWithDescription(payload)
	# water.sendLinkWithDescriptionAndThumbnail @= lambda payload, *a,**kw : water.send.LinkWithDescriptionAndThumbnail(payload)
	# water.sendLinkWithThumbnail @= lambda payload, *a,**kw : water.send.LinkWithThumbnail(payload)
	# water.summerizeChat @= lambda payload, *a,**kw : water.summerize.Chat(payload)
	# water.summerizeUser @= lambda payload, *a,**kw : water.summerize.User(payload)
	# water.summerizeGroup @= lambda payload, *a,**kw : water.summerize.Group(payload)
	# water.sendGroupInvite @= lambda payload, *a,**kw : water.send.GroupInvite(payload)
	# water.sendGroupStats @= lambda payload, *a,**kw : water.send.GroupStats(payload)
	# water.sendGroupWelcomeMessage @= lambda payload, *a,**kw : water.send.GroupWelcomeMessage(payload)
	# water.sendGroupDescription @= lambda payload, *a,**kw : water.send.GroupDescription(payload)
	# water.sendGroupRules @= lambda payload, *a,**kw : water.send.GroupRules(payload)
	# water.sendGroupAnnouncements @= lambda payload, *a,**kw : water.send.GroupAnnouncements(payload)
	# water.setGroupToAdminsOnly @= lambda payload, *a,**kw : water.Set.GroupToAdminsOnly(payload)
	# water.setGroupToEveryone @= lambda payload, *a,**kw : water.Set.GroupToEveryone(payload)
	# water.setGroupToMembersOnly @= lambda payload, *a,**kw : water.Set.GroupToMembersOnly(payload)
	# water.setGroupToNewMembersOnly @= lambda payload, *a,**kw : water.Set.GroupToNewMembersOnly(payload)
	# water.setGroupToPrivate @= lambda payload, *a,**kw : water.Set.GroupToPrivate(payload)
	# water.setGroupToPublic @= lambda payload, *a,**kw : water.Set.GroupToPublic(payload)
	# water.setGroupToRestricted @= lambda payload, *a,**kw : water.Set.GroupToRestricted(payload)
	# water.setGroupToUnrestricted @= lambda payload, *a,**kw : water.Set.GroupToUnrestricted(payload)
	# water.setProfilePic @= lambda payload, *a,**kw : water.Set.ProfilePic(payload)
	# water.setGroupPicture @= lambda payload, *a,**kw : water.Set.GroupPicture(payload)
	# water.sendServicePublicLink @= lambda payload, *a,**kw : water.send.ServicePublicLink(payload)
	# water.sendServicePrivateLink @= lambda payload, *a,**kw : water.send.ServicePrivateLink(payload)
	# water.setGroupService @= lambda payload, *a,**kw : water.Set.GroupService(payload)
	# water.silenceUser @= lambda payload, *a,**kw : water.silence.User(payload)
	# water.unsilenceUser @= lambda payload, *a,**kw : water.unsilence.User(payload)
	# water.pauseGroup @= lambda payload, *a,**kw : water.pause.Group(payload)
	# water.unpauseGroup @= lambda payload, *a,**kw : water.unpause.Group(payload)
	# water.connectGroups @= lambda payload, *a,**kw : water.connect.Groups(payload)
	# water.disconnectGroups @= lambda payload, *a,**kw : water.disconnect.Groups(payload)
	# water.sendGroupInvite @= lambda payload, *a,**kw : water.send.GroupInvite(payload)
	# water.addAI @= lambda payload, *a,**kw : water.add.AI(payload)
	# water.removeAI @= lambda payload, *a,**kw : water.remove.AI(payload)
	# water.addUserToGroup @= lambda payload, *a,**kw : water.add.UserToGroup(payload)
	# water.removeUserFromGroup @= lambda payload, *a,**kw : water.remove.UserFromGroup(payload)
	water.privateGroup @= lambda payload, *a,**kw : water.private.Group(payload)
	water.publicGroup @= lambda payload, *a,**kw : water.public.Group(payload)
	water.getPortal @= lambda payload, *a,**kw : water.Get.Portal(payload)
registerCallbacks()

# make public web api, with permissions

def newGroupService(targetService, debug = False, _number=defaultNumber, addRolling = False, overrideTitle = None, setServiceAdminGroup = False, users = None, autoLeave = False, overrideIconURL = None, overrideBase64Icon = None):
		groupName = targetService
		if users == None:
			users = ["972543610404@c.us"]
		elif "autoLeave" in users :
			users.pop(users.index("autoLeave"))
			autoLeave = True
			
		res = " ::: creating new group :::" + groupName
		# water.sendMessage(_message=res, _number=defaultNumber)
		# final = water._driver.createGroup(groupName, ["972543610404@c.us"])
		# targetService = None
		# if len(body.split(" ")) > 0:
		# 	targetService = body.split(" ")[1]
		serviceObject = None
		if targetService in water.services:
			serviceObject = water.services[targetService]._service
			groupName = serviceObject.title

		if overrideTitle is not None:
			groupName = overrideTitle
		final = water.createGroup(groupName, users, debug = debug)
		
		groupID = final["wid"]["_serialized"]

		water.groups[groupID].service = targetService
		water.sendMessage(_message=f"_Group {groupName} was created_", _number=_number)

		# water.sendMessage(_message=f"GROUP CREATED {final}", _number=defaultNumber)
		print("....................",water.groups[groupID].service)
		print("....................",targetService)
		print("....................")
		print("....................")
		print("....................")
		print("....................")
		print("....................")
		pp(final)
		print("....................")
		print("....................")
		print("....................")

		if serviceObject is not None:
			if addRolling:
				if water.rollingGroups() == None:
					water.rollingGroups._setValue([])
				water.rollingGroups += [groupID]
				water.rollingGroups[groupID].service = targetService

			setGroupToService(groupID, targetService,
							  setServiceAdminGroup=setServiceAdminGroup, groupName = groupName, overrideIconURL = overrideIconURL, overrideBase64Icon = overrideBase64Icon)

		water.sendMessage(
			_message=f"{final['invite_link']}", _number=_number, url=final["invite_link"])
		inviteURL = final['invite_link']
		print(" ::: DONE CREATING GROUP :::", groupID, inviteURL)
		water.groups[groupID].link = inviteURL

		if autoLeave:
			# check docs
			# water._driver.leaveGroup(groupID)
			pass
		return groupID, final

water.newGroupService = newGroupService

def processRootCommands(message):
	origin = message["data"]["chatId"]
	user = message["data"]["from"]
	msgType =  message["data"]["type"]
	messageID = message["data"]["id"]
	text = None
	if "chat" in msgType:
		text = message["data"]["content"]

	isMe = False
	if "data" in message and "sender" in message["data"] and message["data"]["sender"] is not None:
		isMe = message["data"]["sender"]["isMe"]

	# isMe = message["data"]["sender"]["isMe"]

	body = text if text is not None else ""
	if "ECHO" in body:
		print(" ::: ACK ECHO :::", text)
	elif body.startswith("/poll"):
		poll = water._driver.sendPoll(origin, "How do you like this service?", [
			"good", "great!", "niiccce"])

	elif body.startswith("/group") and len(body.split(" ")) > 1:
		# groupName = "......"
		if isMe:
			groupID, final = newGroupService(body.split(" ")[1], debug=True, _number = origin, setServiceAdminGroup=True)
		else:
			groupID, final = newGroupService(body.split(
				" ")[1], debug=True, _number=origin, setServiceAdminGroup=True, users=[user, "autoLeave"])
			water.sendMessage(_message=f"/setgroup {groupID} {body.split(' ')[1]}", _number=origin)
			water.sendMessage(
				_message=f"{final['invite_link']}", url=final['invite_link'], _number=origin)
		return groupID, final
		
	elif body.startswith("/secret "):
		secret = "......"
		secret = body.split("/secret")[1].strip()
		# secret_wrapped = wrapSecret(emoji.emojize(secret), post = "🔐")
		splitSecret = secret.split(" ")
		print("SSSSSSSSSSSSSSSSS")
		print("SSSSSSSSSSSSSSSSS")
		print("SSSSSSSSSSSSSSSSS", splitSecret)
		post = ""
		if len(splitSecret) > 1:
			secret = splitSecret[0]
			secret_wrapped = wrapSecret(emoji.demojize(secret), post = splitSecret[1])
			if len(splitSecret) > 2:
				post = " "+" ".join(splitSecret[2:])
			

		# if 		secret = body.split("/secret")[1].strip()
		else:
			secret_wrapped = wrapSecret(emoji.demojize(secret))

		# res = " ::: creating new group group :::" + secret
		# water.sendMessage(_message=res, _number=defaultNumber)
		# final = water._driver.createGroup(groupName, ["972543610404@c.us"])
		# final = water.createGroup(groupName, ["972543610404@c.us"])
		# water.sendMessage(_message=f"GROUP CREATED {final}", _number=defaultNumber)

		water.sendMessage(_message=secret_wrapped+post, _number=origin)
	elif body.startswith("/detect "):
		secret = "......"
		secret = body.split("/detect")[1].strip()
		secret_wrapped, freeText = recoverSecret(secret)
		# res = " ::: creating new group group :::" + secret
		# water.sendMessage(_message=res, _number=defaultNumber)
		# final = water._driver.createGroup(groupName, ["972543610404@c.us"])
		# final = water.createGroup(groupName, ["972543610404@c.us"])
		# water.sendMessage(_message=f"GROUP CREATED {final}", _number=defaultNumber)
		# water.sendMessage(_message=str(emoji.demojize(secret_wrapped))+" "+str(freeText), _number=origin)
		water.sendMessage(_message=str(emoji.emojize(secret_wrapped)), _number=origin)
		# groupID = final["wid"]["_serialized"]
		# if len(body.split(" ")) > 0:
		# 	setGroupToService(groupID, body.split(" ")[1])
		# inviteURL = "TODO invite url"
		# print(" ::: DONE CREATING GROUP :::", groupID, inviteURL)


def manage_incoming(message, *a, **kw):
	origin = message["data"]["chatId"]
	user = message["data"]["from"]
	msgType =  message["data"]["type"]
	messageID = message["data"]["id"]
	text = None
	if "chat" in msgType:
		text = message["data"]["content"]
	if "text" in kw:
		text = kw["text"]
		message["data"]["body"] = text
		message["data"]["content"] = text
	isMe = False
	if "data" in message and "sender" in message["data"] and message["data"]["sender"] is not None:
		isMe = message["data"]["sender"]["isMe"]
	print()
	print("::::::::incoming :::::::::", origin, user, msgType, text, a, kw,'\n')#,message)
	SuperAdminGroups = [] # Todo: add admin groups
	SuperAdminUsers = ["972547932000@c.us"] # Todo: add admin groups
	if isMe and user == origin or origin in SuperAdminGroups or origin in SuperAdminUsers:
		print(f"This is the root manager isMe:{isMe}",origin,user)
		processRootCommands(message)
	# elif isMe and origin in water.groups.value:
	elif origin in water.groups.value:
		serviceName = water.groups[origin].service.value
		print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
		print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
		print(f" @@@@@@@@ INCOMING MESSAGE TO SERVICE {serviceName} ")
		print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
		print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
		
		if isMe and text and str(text).startswith("/adduser") and len(str(text).split(" "))>1:
			targetUser = str(text).split(" ")[1]
			payload = {"data":{"chat":origin,"who":targetUser, "action":"add"}}
			ParticipantChanged(payload)
		

		# should pass message data to service 
		if text and not text.startswith("[") and not isMe:
			# water.sendMessage(_message=f"[will be handled by {serviceName} service]", _number=origin)
			targetService = water.services[serviceName]._service
			event = incomingEvent("message",message, origin, user)
			targetService.on_incoming(event)
			
	elif isMe:
		print("????????????????????")
		print(">>> origin",origin)
		for knownGroup in water.groups:
			print(" -",knownGroup)
		print("????????????????????")
		if origin in water.groups:
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! found group",origin)
		if origin in water.groups.value:
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! found group",origin)
		serviceName = "Not Found"
		if origin in water.groups.value:
			serviceName = water.groups[origin].service.value
			print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
			print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
			print(f" @@@@@@@@ INCOMING MESSAGE TO SERVICE {serviceName} ")
			print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
			print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
		
			# should pass message data to service 
			if text and not text.startswith("["):
				water.sendMessage(_message=f"[will be handled by {serviceName} service]", _number=origin)
				targetService = water.services[serviceName]._service
				event = incomingEvent("message",message, origin, user)
				targetService.on_incoming(event)
		else:
			print(" SERVICE NOT FOUND")
			print(" SERVICE NOT FOUND")
			print(" SERVICE NOT FOUND")
			print(" SERVICE NOT FOUND")
			print(" SERVICE NOT FOUND")
			print(" SERVICE NOT FOUND")
			print(" SERVICE NOT FOUND")


	data = {}
	if message and text is None:
		print(message["data"]["chat"]["id"], a, kw)
		print(":::::::::::::::::")
		# pp(message)
		data["origin"] = message["data"]["chatId"]
		data["sender"] = message["data"]["from"]
		data["type"] = message["data"]["type"]  # "chat" or "poll_creation" or
		if "chat" in data["type"]:
			data["content"] = message["data"]["content"]
		data["id"] = message["data"]["id"]

		if "ptt" in data["type"].lower() or "audio" in data["type"]:
			print("PPPPPTTTTTTTTTT")
			print("PPPPPTTTTTTTTTT")
			print("PPPPPTTTTTTTTTT")
			print("PPPPPTTTTTTTTTT")
			print("PPPPPTTTTTTTTTT")
			print("PPPPPTTTTTTTTTT")
			print("PPPPPTTTTTTTTTT")
			print("PPPPPTTTTTTTTTT")
			print("PPPPPTTTTTTTTTT")

			# for k in message:
			# 	print(k," ::: ", message[k])
			mContent = AnalyzeAudio(message, water=water)#, factored=factored)
			print("TRANSCRIBED!!!!!!!! ",mContent)
			return manage_incoming(message, text=mContent.strip("*").replace("\u200f",""), *a, **kw)
	print(":::::::::::::::::")
	if message:
		body = "________________________empty body________________________"
		if "data" in message and "body" in message["data"]:
			body = message["data"]["body"]

		origin = message["data"]["chat"]["id"]
		print(f" incoming ::: {a} {kw} \n",
					user, origin, "\n", body, "\n")
		useEcho = True
		useEcho = False

		response = "ECHO!\n" + body
		if isMe and origin == defaultNumber:
			# print(" ::: message from me :::")
			response += "\n\n ::: message from me :::"
			if "ECHO" in body:
				print(" ::: ACK ECHO :::", text)
			else:
				if useEcho:

					if "g.us" in origin:
						print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
						water._driver.setGroupTitle(origin, body + "TTTTTTTTT")
						# poll = water._driver.sendPoll(origin, "How do you like this service?", [
						#    "good", "great!", "niiccce"])

						# print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",poll)
						print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
						print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
					else:
						print("XXXXXXXXXXXXXXXXXXXXXXXXX")
					time.sleep(1)
					water.sendMessage(_message=response, _number=origin)
		else:
				# water.sendMessage(_message=response, _number=message["data"]["sender"]["id"])
			print("33333333333333333")
			if useEcho:
				water.sendMessage(_message=response, _number=defaultNumber)


water.ManageIncoming = manage_incoming


water.wa.send @= lambda *a, **kw: water.sendMessage(*a, **kw)


	




# have raw ability to change icon and name

# create rolling empty groups, which are accessible via rest api

# create an abstract class for a service, which can be used to create a service
# it will have a name, a description, an icon, a list of event hooks, and an api to the user (obfuscated)

# water.services.warmWinters.users["master"].groups["origin_uid"]
# water.services.warmWinters.groups["origin_uid"].users["master"]
# water.groups["origin_uid"].service = "warmWinters"
# water.groups["origin_uid"].service.api = water.services.warmWinters.api

# water.users


def main():

	# These are available:
	# water.logs.info('::: Starting simple Service on port')
	number = '972547932000@c.us'
	# secure = "0B2FDC9C-FADF48A9-92E5F3D1-D2CDA55A"
	# secure = "secure_api_key"
	_client = SocketClient(f'http://{host}:{port}/', wa_key)
	water._driver = _client
	print("!!!!!!!!!!!!!!!!!", "_driver" in water, water._driver)

	def printResponse(message):
		print(" incoming :::\n", message["data"]["body"], "\n")

	# Listening for events
	# water._driver.onMessage(printResponse)
	# water._driver.onMessage(water.ManageIncoming)
	# water._driver.onAnyMessage(print)
	water._driver.onAnyMessage(water.ManageIncoming)
	water._driver.onPollVote(water.ManagePolls)
	water._driver.onGlobalParticipantsChanged(water.ParticipantChanged)
	water._driver.onReaction(water.ParticipantChanged)


	# Executing commands
	water._driver.sendText(number, "fresh waters!!!!!!")

	# Sync/Async support
	print(" ::: CONNECTED! ", water._driver.getHostNumber())  # Sync request
	loadServices(water)
	# appServices = loadServices(water)

	# water._driver.sendAudio(NUMBER,
	# 				"https://download.samplelib.com/mp3/sample-3s.mp3",
	# 				sync=False,
	# 				callback=printResponse)  # Async request. Callback is optional

	# Finally disconnect
	# client.disconnect()
	while(True):
		time.sleep(1)

if __name__ == "__main__":
	main()


## small
# [] save invite link
# [] onParticipantAdded
# [] onPollVote
# [] /portal command load service
# [] send links with auto preview
# [] fire.io -> server integration



## medium
# [] give state/memory to services - functional programming
# []  
# [] run service events, init - welcome, 
# [] make rolling groups
# [] make links to join/service
# [] make service api more robust and secure (one way, obfuscated users)
# [] make service api more robust and secure (one way, obfuscated users)
# [] send custome quote
# [] onboarding events using xo @= 

## serious
# [] in-service purchases
# [] stable host on server
# [] get a nother number



## vision
#? [] make a service that can be used to create services - master tools service
# [] partnership with open-wa
# [] free opensource services
# [] commisions on free hosted in-service purchases
# [] paid master services (excluding spamming)
# [] premium custom whatsapp service by us (no spamming allowed)



# To open-wa:
# Dear open wa team,
# For a while now I've been working on a advanced project, called Water - it's a platform and marketplace for whatsapp tools and services
# Think of it like a Vercel for whatsapp. The platforms allows users to easily create Functional* whatsapp services, and give/sell them to other users.

# Interested: read more here:
# The platform will host for free - open source services (verified and unreported).
# each service is given: state machine (with integrated db), api to the user, and a list of events that can be hooked into.
# Each Service will get out of the box: Personal Invite Link for users (like this service), Managment Portal for admins, and a bunch of other features.
# Services can have in-service purchases and subscriptions, and the platform will take a small cut from the purchase. 
# The Services will be super easy to share, and also searchable (if not set to private).
# The services are annonimous by default, and the users are obfuscated, so user's personal information is not exposed (unless the user agrees to share)
# Since you guys are, in my opinion, the best whatsapp api, I would love to have a partnership with you.
# From my side, I will host the generic platform (open-source).
# I hope we can create together a new tier of license key, which will allow users/buisnesses to create these applications.
# 
# 

## service:
# user was added to group
# welcome message and instructions (init)
# 


# personal app bank:
# akeyo beta (tags subscription) (chatgpt data/event manager)
# wholesomeTinders 
# WarmWinters
# Googler
# Music
# wishbook
# Sarale's Channel (Multi Services Channel)
# Text To Image
# payment request
# 




# upnext:
# - finalise the rolling groups
# - open links to rolling groups with context - imitate using local links
# - /shop shopid shop-title override
# - change name and icon of rolling groups
# - /shop with image and description


# - auto join group on invite link from admin user (burn numbers to create groups without overlimiting the main number)
