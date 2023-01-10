#xo.water.py


from gtts import gTTS
from pydub import AudioSegment
import shazi
# from munch import Munch

import speech_recognition as sr
recognizer = sr.Recognizer()

import os


# simple Service
# npx @open-wa/wa-automate --socket -p 8085 -k "$WA_KEY"
# python3 simple.py

# from test import *
# water.Simple.send(number="972543610404", msg="Hello from simple.py")
# water.Simple.send(number="972547932000", msg="Hello from simple.py")

######################################    imports and setup    ####################################################
# Wa Automate Docs: 
# https: // openwa.dev/docs/api/classes/api_Client.Client

import time
from tokenize import group
import traceback
from rich.prompt import Prompt
from wa_automate_socket_client import SocketClient
from xo.redis import xoRedis, xo , Expando
import json
import os
cwd = os.path.dirname(os.path.abspath(__file__))
print(" ::: cwd:", cwd)

water = xoRedis('water')

from pprint import pprint as pp

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


def sendMessage(_message="fresh grass", _number="972547932000@c.us", *a, **kw):
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
		print(
			f" Sending MEssage..... {number} {message} ::: {a} {kw} \n", payload, "\n")
		water._driver.sendText(number, message)
		print(f" Sending MEssage ::: {a} {kw} \n", payload, "\n")
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
from services.googler import Googler
from services.api import *
# from services.warmWinters import WarmWinters

# water.services.warmWinters = WarmWinters()
def loadGroups():
	groups = water.groups()
	if groups == None:
		water.groups = []
		groups = water.groups()
	for group in groups:
		print("GGGGGGGGGGGGGGGGGGG",group)
		water.groups[group]()
		water.groups[group].service()


loadGroups()


def setGroupToService(group, service):
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
		# serviceObject: someService = water.services[service]._service
		serviceObject = water.services[service]._service

		water.sendMessage(f"[Changing Group]\n {group} to service {service} :::",group, water.services[service]._service.title)
		water._driver.setGroupTitle(group, serviceObject.title)
		water._driver.setGroupIconByUrl(group, serviceObject.iconURL)
	else:
		print(f" --- Service {service} is not loaded in water ---")


def loadServices(water):	
	# water.services.googler.api = WaterAPI()
	# water.services.googler = Googler()
	for service in [Googler,]:
		api = WaterAPI(water._driver)
		api.service = service
		water.services[service.name]._api = api
		water.services[service.name]._service = service(api)



	
def main():

	# These are available:
	# water.logs.info('::: Starting simple Service on port')
	number = '972547932000@c.us'
	# secure = "0B2FDC9C-FADF48A9-92E5F3D1-D2CDA55A"
	# secure = "secure_api_key"
	_client = SocketClient(f'http://{host}:{port}/', wa_key)
	water._driver = _client
	print("!!!!!!!!!!!!!!!!!","_driver" in water, water._driver)
	def printResponse(message):
		print(" incoming :::\n", message["data"]["body"],"\n")

	# Listening for events
	# water._driver.onMessage(printResponse)
	# water._driver.onMessage(water.ManageIncoming)
	water._driver.onAnyMessage(water.ManageIncoming)
	water._driver.onPollVote(water.ManagePolls)

	# Executing commands
	water._driver.sendText(number, "fresh waters!!!!!!")

	# Sync/Async support
	print(" ::: CONNECTED! ", water._driver.getHostNumber())  # Sync request
	loadServices(water)
	# water._driver.sendAudio(NUMBER,
	# 				"https://download.samplelib.com/mp3/sample-3s.mp3",
	# 				sync=False,
	# 				callback=printResponse)  # Async request. Callback is optional

	# Finally disconnect
	# client.disconnect()


water._groups = {}
water._apps = {"Google": {"name": " GOOGLE", "icon_url": "",
						   "description": "Google Search", "invite_link": ""}}


# @Simple
def setGroupApp(group_id, app, *args, **kwargs):
	if "_driver" not in water:
		print(" setGroupApp ::: Driver not connected yet :::")
		return False

	if group_id not in water._groups:
		water._groups[group_id] = {}
	# if app not in water._apps:
	# 	water._apps[app] = {}

	water._groups[group_id]["app"] = app

	# Change group name to app name
	water._driver.setGroupTitle(group_id, water._apps[app]["name"])
	# water._driver.setGroupIconByUrl(water._groups[group]["id"], water._apps[app]["icon_url"])
	# water._driver.setGroupDescription(group_id, water._apps[app]["description"])
	print("@@@@@@@@@@@@@@@@@@ setGroupApp: ",
		  group_id, water._apps[app]["name"], water._apps[app]["description"])
	return True


# @Simple
def createGroup(Name=" ::: Test ::: ", participants=["972543610404@c.us"], *args, **kwargs):
	print("Creating group: ,,,,,,,,")
	if "_driver" not in water:
		print(" ::: Driver not connected yet :::")
		return False
	res = water._driver.createGroup(Name, participants)
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
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	try:
		res["invite_link"] = water._driver.getGroupInviteLink(
			res["wid"]["_serialized"])
	except:
		print(" ::: invite_link failed :::")
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
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", res["info"]["groupMetadata"]["id"])
	# water._driver.sendMessage("WELCOME!",res["wid"]["_serialized"])
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	# water._driver.sendMessage("WELCOME!", "120363029005529843@g.us")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
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
		water.sendMessage(warmWintersMsg,res["info"]["groupMetadata"]["id"])
		water._driver.sendPoll(res["wid"]["_serialized"], "*:חורף חם*",["בקשת חימום", "תרומת חימום", "עזרה במסירה", "הרשמה כעמותה/ספק"])

	else:
		water.sendMessage("WELCOME!",res["info"]["groupMetadata"]["id"])
		water._driver.sendPoll(res["wid"]["_serialized"], "How do you like this service?",["good", "great!", "niiccce"])
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


	print("invite link: ", res["invite_link"])
	print("invite link: ", res["invite_link"])
	print("invite link: ", res["invite_link"])
	print("invite link: ", res["invite_link"])
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


# make public web api, with permissions




def Process(contact, factored=False):

	if not factored:
		message = Munch(contact)
		# for m in message:
		# 	print(m,":::",message[m])
		message.chat = Munch(message.chat)
		message.sender = Munch(message.sender)

	else:
		# message = contact
		pass
	# for message in contact.messages:
	if True:
		# print("MMMMMMMMMM",message.content)
		# {"123":"123"}.get_j
		if factored:
			mChatID = message.chat_id
			mSenderID = message.sender.id
			mSenderName = message.get_js_obj()["chat"]["contact"]["formattedName"]
			mType = message.type
		else:
			mChatID = message.chat.id
			message.chat_id = message.chat.id
			if "clientUrl" in message:
				message.client_url = message.clientUrl
			if "mediaKey" in message:
				message.media_key = message.mediaKey

			message.chat_id = message.chat.id
			message.get_js_obj = message

			mSenderID = message.sender.id

			# mSenderName = message.get_js_obj()["chat"]["contact"]["formattedName"]
			mSenderName = message["chat"]["contact"]["formattedName"]
			mType = message.type

		LAST[0] = message

		if "ptt" in mType.lower() or "audio" in mType:
			print("PPPPPTTTTTTTTTT")
			print("PPPPPTTTTTTTTTT")
			print("PPPPPTTTTTTTTTT")

			# for k in message:
			# 	print(k," ::: ", message[k])
			mContent = self.AnalyzeAudio(message, factored= factored)
		else:
			print(mType)
			print(mType)
			print(mType)
			print(mType)
			print(mType)
			if factored:
				mContent = message.content
			else:
				mContent = message["content"]

		if mContent is not None and len(mContent) > 0:

			# if runLocal and False: ## FOR FIREFOX
			# 	chatID = message.chat_id["_serialized"]
			# else:
			# 	chatID = mChatID
			chatID = mChatID

			try:
				chat = self.driver.get_chat_from_id(chatID)
			except Exception as e:
				print(" ::: ERROR - _serialized chatID ::: "+chatID+" ::: ", "\n",e,e.args,"\n")

			''' incoming from: '''
			''' Personal Chat  '''
			senderName = mSenderName
			senderID = mSenderID
			fromGroup = False
			if "c" in chatID:
				print("FFFFFFFFFF")
				# print(message.get_js_obj())
				# pp(message.get_js_obj())
				# self.driver.chat_reply_message(message.id, "awesome")
				# self.driver.privateReply(message.id, "awesome",chatID)
				if factored:
					self.driver.privateReply(message.id, mContent, "972512170493-1612427003@g.us")
				else:
					self.driver.privateReply(message["id"], mContent, "972512170493-1612427003@g.us")
				# self.driver.forward_messages("972512170493-1612427003@g.us",message.id,False)
				print(
										'''
				===================================
				Incoming Messages from '''+senderID+" "+senderName+'''
				===================================
				'''
				)

				''' SEND TO MASTER SERVICE '''
				self.masterService.ProcessChat(message)

				# self.driver.remove_participant_group()
				# if message.type == "chat":
				# 	text = message.content
				#
				# 	print("TTTTTXXXXXXXXXTTTTTTT",text)
				# 	''' subscribe to service '''
				#
				# 	''' SENT FROM GROUP CHAT '''
				#
				# 	if "%%%!%%%" in text:
				# 		target = text.split(u"%%%!%%%")[1]
				# 		self.driver.sendMessage(chatID,"Adding Service to DB: "+target)
				# 		self.db["services"][target] = {"dbID":None,"incomingTarget":None}
				# 		ServiceLoader.LoadService(service = target, send = self.send, backup = self.backupService, genLink = self.genLink)
				# 		# self.LoadServices()
				# 		# self.serviceFuncs["services"][target] = None
				#
				# 		self.backup(now = True)
				# 	else:
				# 		print("XXXXXXXXXXXXXXXXXXX")
				# 		print("XXXXXXXXXXXXXXXXXXX")
				# 		print("XXXXXXXXXXXXXXXXXXX")
				#
				# 	if text[0] is "/":
				# 		# "//div[@class='VPvMz']/div/div/span[@data-testid='menu']"
				# 		print("##################################")
				# 		print("##################################")
				# 		print("#####                      #######")
				# 		print("##################################")
				# 		print("##################################", text)
				# 		dotsSide = self.driver.tryOut(self.driver.driver.find_element_by_xpath,text,click=True)
				#
				# 	if text[0] is "-":
				# 	''' person unsubscribing service with -'''
				# 	target = text[1:]
				# 	dbChanged = False
				# 	now = False
				#
				# 	''' check target service in db '''
				# 	serviceFound = False
				# 	for service in self.services:
				# 		print("______________ ----------"+service)
				# 		print("")
				# 		if not serviceFound and target.lower() == service.lower():
				# 			target = service
				#
				# 			''' service found '''
				# 			serviceFound = True
				#
				# 			if chatID not in self.db["users"]:
				# 				self.db["users"][chatID] = {}
				# 				dbChanged = True
				# 				''' first time user '''
				# 				# self.db["users"][senderID] = {'services': {'Reminders': {'groupID': None}}}
				# 			else:
				# 				pass
				# 				''' known user '''
				#
				#
				# 			foundChat = None
				# 			if chatID in self.db["groups"]:
				# 				if "service" in self.db["groups"][chatID]:
				# 					self.db["groups"][chatID]["service"] = None
				#
				# 			if service in self.db["users"][chatID]:
				# 				serviceChat = self.db["users"][chatID][service]
				#
				# 				# self.driver.sendMessage(senderID,"You are already subscirbed to: "+target+" \nYou can unsubscribe with -"+target.lower())
				# 				if serviceChat is not None:
				# 					try:
				# 						self.db["users"][chatID].pop(service)
				# 						self.driver.sendMessage(chatID,"Unsubscribing from: *"+service+"*")
				# 						print("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
				# 						print("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
				# 						print("UUUUUUU    UNSUBSCRIBING       UUUUUUUUUUUU")
				# 						print("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
				# 						print("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
				# 						print("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",chatID,service)
				# 						dbChanged = True
				# 						now = True
				#
				# 					except:
				# 						print('chat could not be found')
				# 	if not serviceFound:
				# 		self.driver.sendMessage(chatID,"you are not subscirbed to: *"+service+"*")
				#
				#
				# if text[0] is "=":
				# 	''' person registering service with ='''
				# 	target = text[1:]
				# 	dbChanged = False
				# 	now = False
				#
				# 	''' check target service in db '''
				# 	serviceFound = False
				#
				# 	serviceChat = ""
				# 	for service in self.services:
				# 		print("______________ ----------"+service)
				# 		print("")
				# 		if not serviceFound and target.lower() == service.lower():
				# 			target = service
				#
				# 			''' service found '''
				# 			serviceFound = True
				#
				# 			if chatID not in self.db["users"]:
				# 				self.db["users"][chatID] = {}
				# 				dbChanged = True
				# 				''' first time user '''
				# 				# self.db["users"][senderID] = {'services': {'Reminders': {'groupID': None}}}
				# 			else:
				# 				pass
				# 				''' known user '''
				#
				#
				# 			foundChat = None
				# 			if service in self.db["users"][chatID]:
				#
				# 				serviceChat = self.db["users"][chatID][service]
				#
				# 				# self.driver.sendMessage(senderID,"You are already subscirbed to: "+target+" \nYou can unsubscribe with -"+target.lower())
				# 				if serviceChat is not None:
				# 					try:
				# 						foundChat = self.driver.get_chat_from_id(serviceChat)
				# 					except:
				# 						print('chat could not be found')
				#
				#
				# 			chatName = target
				# 			welcome = "Thank you for Subscribing to "+target
				# 			try:
				# 				chatName = self.services[service]["obj"].name
				# 				welcome = "Thank you for Subscribing to "+chatName
				# 				welcome = self.services[service]["obj"].welcome
				# 			except:
				# 				pass
				#
				# 			if foundChat is not None:
				# 				check_participents = False
				# 				if check_participents:
				# 					if senderID in foundChat.get_participants_ids() or True:
				# 						'''##### check that user is participant '''
				# 						self.driver.sendMessage(senderID,"You are already subscirbed to: "+chatName+" \nYou can unsubscribe with -"+target.lower())
				# 						self.driver.sendMessage(serviceChat,"subscirbed to: "+chatName)
				# 					else:
				# 						foundChat = None
				# 				else:
				# 					gotLink = False
				# 					groupName = service
				# 					path = self.download_image()
				# 					inviteLink = ""
				#
				# 					print("$$$$$$$$$$$$$$$$$$$$$$$")
				# 					print(serviceChat, self.db["groups"][serviceChat]  )
				# 					if serviceChat in self.db["groups"] and self.db["groups"][serviceChat] is not None and "invite" in self.db["groups"][serviceChat]:
				# 						if self.db["groups"][serviceChat]["invite"] is not None:
				# 							inviteLink = self.db["groups"][serviceChat]["invite"]
				# 							gotLink = True
				# 							if service in self.services and "obj" in self.services[service] and self.services[service]["obj"] is not None:
				# 								groupName = self.services[service]["obj"].name
				# 								imageurl = self.services[service]["obj"].imageurl
				# 								if imageurl is not None:
				# 									path = self.download_image(service=service,pic_url=imageurl)
				#
				#
				# 					content = "You are already subscirbed to:\n"+chatName+" \n"
				# 					if gotLink:
				# 						content+= inviteLink
				# 					content+="\n"+"You can unsubscribe with -"+target.lower()
				#
				# 					if gotLink:
				# 						res = self.driver.send_message_with_thumbnail(path,senderID,url=inviteLink,title="Open  "+groupName,description="xxx",text=content)
				# 					else:
				# 						self.driver.sendMessage(senderID,content)
				# 					self.driver.sendMessage(serviceChat,"subscirbed to: "+chatName)
				#
				#
				# 			''' create new group '''
				# 			if foundChat is None:
				# 				print(
				# 				'''
				# 				===============================================
				# 				 ''' + senderID +" CREATING NEW GROUP "+ target +" :D "+'''
				# 				===============================================
				# 				'''
				# 				)
				# 				groupName = service
				# 				path = self.download_image()
				# 				if service in self.services and "obj" in self.services[service] and self.services[service]["obj"] is not None:
				# 					groupName = self.services[service]["obj"].name
				# 					imageurl = self.services[service]["obj"].imageurl
				# 					if imageurl is not None:
				# 						path = self.download_image(service=service,pic_url=imageurl)
				#
				#
				#
				# 				imagepath = path
				# 				newGroup, groupInvite = self.driver.newGroup(newGroupName = groupName, number = "+"+senderID.split("@")[0], local = runLocal, image=imagepath)
				# 				newGroupID = newGroup.id
				#
				# 				self.newG = newGroupID
				#
				# 				self.db["users"][chatID][service] = newGroupID
				# 				self.db["groups"][newGroupID] = {"service":target, "invite":groupInvite}
				# 				dbChanged = True
				# 				now = True
				# 				print(
				# 				'''
				# 				===============================================
				# 				 ''' + senderID +" is NOW SUBSCRIBED TO "+ target +" :D "+'''
				# 				===============================================
				# 				'''
				# 				)
				#
				# 				res = self.driver.send_message_with_thumbnail(path,senderID,url=groupInvite,title="Open  "+groupName,description="BBBBBBBB",text="Thank you! you are now subscribed to: "+chatName+" \n"+str(groupInvite)+"\nPlease check your new group :)")
				# 				# self.driver.sendMessage(senderID,"Thank you! you are now subscribed to: "+chatName+" \n"+str(groupInvite)+"\nPlease check your new group :)")
				# 				self.driver.sendMessage(newGroupID,welcome)
				# 				# self.driver.sendMessage(serviceChat,"subscirbed to: "+target)
				#
				# 	if not serviceFound:
				# 		self.driver.sendMessage(chatID,target+" : is not recognized as a service "+target)
				# 		print(
				# 		'''
				# 		===============================================
				# 		  SERVICE '''+ target +" IS NOT AVAILABLE"+'''
				# 		===============================================
				# 		'''
				# 		)
				# 	if dbChanged:
				# 		self.backup(now=now)
				#

			# ''' Group Chat '''
			elif "g" in chatID:
				fromGroup = True

				# self.driver.privateReply(message.id, mContent,"972512170493-1612427003@g.us")
				# self.driver.privateReply(message.id, mContent,senderID)

				print(
										'''
				===============================================
					Incoming Messages in Group \"'''+mChatID+" "+senderName+" from "+senderID+'''
				===============================================
				'''
				)
				if message.type == "chat" or True:
					text = mContent


					# ''' GOT REGISTRATION COMMAND '''
					# if text[0] is "=":
					# 	foundService = None
					# 	target = text[1:]
					#
					# 	''' register group to service '''
					# 	for service in self.services:
					# 		if target.lower() == service.lower():
					# 			foundService = service
					#
					# 			foundChat = False
					# 			if chatID in self.db["groups"]:
					# 				if "service" not in self.db["groups"][chatID]:
					# 					invite = None
					# 					if "invite" in self.db["groups"][chatID]:
					# 						invite = self.db["groups"][chatID]["invite"]
					# 					link = None
					# 					if "link" in self.db["groups"][chatID]:
					# 						link = self.db["groups"][chatID]["link"]
					# 					self.db["groups"][chatID] = {"service":service,"invite":invite, "link":link}
					#
					# 				targetService = self.db["groups"][chatID]["service"]
					# 				print("TTTTTTTTTTTTTTTTTTTT")
					# 				print(targetService, service)
					# 				if targetService is not None:
					# 					if targetService.lower() == service.lower():
					# 						foundChat = True
					# 						self.driver.sendMessage(chatID,"You are already subscirbed to: "+target+" \nYou can unsubscribe with -"+target.lower())
					#
					# 			if not foundChat:
					# 				print("SSSSSSSSSSSSSSSSSSSSSSsxxxxx")
					# 				print("SSSSSSSSSSSSSSSSSSSSSSsxxxxx")
					# 				print("SSSSSSSSSSSSSSSSSSSSSSsxxxxx")
					# 				self.driver.sendMessage(chatID,"Subscribing to service: "+self.services[service]["obj"].name)
					# 				self.driver.sendMessage(chatID,self.services[service]["obj"].welcome)
					# 				link = self.genLink(api = self.services[service]["api"],service=service,chatID=chatID,answer="")
					# 				self.db["groups"][chatID] = {"service":service, "invite":None, "link":link}
					# 				self.backup()
					#
					# 	if foundService is None:
					# 		self.driver.sendMessage(chatID,"service: "+target+" Not Found")

					''' Chat is not registered first time'''
					if chatID not in self.db["groups"]:
						# print("SSSSSSSSSSSSSSSSSSSSSS")
						# self.driver.sendMessage(chatID,"This chat is not registered with any service yet\nYou can register it by sending =service_name")
						# print("JJJJJJJJJJJJJJ")
						self.db["groups"][chatID] = {"service": None, "invite":None, "link":None}
						# print("SSSSSSSSSSSSSSSSSSSSSS")
						self.backup()

					if self.db["groups"][chatID] is not None:
						''' Chat is known '''
						if "service" not in self.db["groups"][chatID] or self.db["groups"][chatID]["service"] is None:
							invite = None
							if "invite" in self.db["groups"][chatID]:
								invite = self.db["groups"][chatID]["invite"]
							# self.db["groups"][chatID] = {"service":self.db["groups"][chatID],"invite":invite}
							link = None
							if "link" in self.db["groups"][chatID]:
								link = self.db["groups"][chatID]["link"]
							self.db["groups"][chatID] = {"service": None,"invite":invite, "link":link}
							# self.driver.sendMessage(chatID,"This chat is not registered with any service yet\nYou can register it by sending =service_name")

						target = self.db["groups"][chatID]["service"]
						print("MMMMMMMMMMMMMMMM", target)

						if target is not None:
							foundService = None
							for service in self.services:
								if target.lower() == service.lower():
									foundService = service

									''' CHAT IS REGISTERED TO SERVICE! '''
									''' PROCESS INCOMNG MESSAGE in SERVICE '''
									if foundService is not None:

										''' this is where the magic happens - send to service'''

										if "obj" in self.services[foundService]:
											obj = self.services[foundService]["obj"]
											if obj is not None:
												#Get Nicknames
												quoted = None
												if factored:
													j = message.get_js_obj()
												else:
													j = message
													# pass #j = message.get_js_obj()
												if "quotedMsg" in j:
													quoted = j["quotedMsg"]
												self.ProcessServiceAsync(obj, {"origin":chatID, "user":senderID, "content":text, "mID":message.id, "mType":mType, "quotedMsg":quoted})
												# obj.process({"origin":chatID, "user":senderID, "content":text})

										# self.ProcessServiceAsync(service,chatID,text)

							if foundService is None:
								self.driver.sendMessage(chatID, target+" : is not recognized as a service "+target)

def AnalyzeAudioFile(self, path, defLanguage = 'iw-IL'):
	text = ""
	try:
		# audio.export(path, format="wav")
		''' speech to '''
		# notSent = False
		with sr.AudioFile(path) as source:
			rec = recognizer.record(source)
			text = recognizer.recognize_google(rec)
			# self.sendMessage(message.chat_id, "Got from Speech:\n*"+text+"*")
	except:
		traceback.print_exc()
		# notSent = True
	return text
	
def AnalyzeAudio(message, factored = False):
	if message is None:
		return None
	shortRec = 3.5
	text = ""
	try:
		# LAST[0] = message
		# LAST["o"] = {}
		# if factored:
		# 	jobj = message.get_js_obj()
		# else:
		# 	jobj = message
		jobj = message["data"]
		origin = message["data"]["chat"]["id"] 
		ok = origin == message["data"]["sender"]["id"]
		print("JJJJJJJJJJJJ",origin,ok)
		print()
		# water._driver.sendMessage(origin, "_Analyzing Audio Please Wait..._")
		water.sendMessage(_message="_Analyzing Audio Please Wait..._", _number=defaultNumber)
		jobj["clientUrl"] = jobj["deprecatedMms3Url"]

		# ptt = water._driver.download_media(jobj)
		ptt = water._driver.download(jobj["clientUrl"])
		print("\n"*5)
		print("PTT: ", ptt)
		print("\n"*4)
		# audio = AudioSegment.from_file(ptt)
		audio = AudioSegment.from_file(jobj["filePath"])
		

		length = len(audio)
		# audio = AudioSegment.from_file(ptt)
		# path = "rec.wav"
		# path = "recs/"+message.chat_id.split("@")[0]+"_rec"+".wav"
		path = "recs/"+origin.split("@")[0]+"_rec"+".wav"
		# if True:
		audio.export(path, format="wav")
		''' speech to '''
		print("path: ", path)
		print("path: ", path)
		print("path: ", path)
		print("path: ", path)
		print("path: ", path)
		print("path: ", path)
		print("path: ", path)
		print("path: ", path)
		print("path: ", path)
		notSent = False
		try:
			with sr.AudioFile(path) as source:
				rec = recognizer.record(source)

				text = recognizer.recognize_google(rec, language = 'iw-IL')
				water.sendMessage(_message="Got from Speech:\n*"+text+"*", _number=defaultNumber)

				# water._driver.sendMessage(origin, "Got from Speech:\n*"+text+"*")
		except:
			traceback.print_exc()
			notSent = True

		shazamLimit = 22
		if length > shortRec * 1000:
			''' shazam '''
			o = shazi.shazam(path)
			tx = time.time()
			while "title" not in o and time.time()-tx < shazamLimit:
				time.sleep(1)
			# water._driver.sendMessage(message.chat_id, "Got from Shazam:\n*"+str(o["title"]+" - "+o["artist"])+"*")
			water.sendMessage(_message= "Got from Shazam:\n*"+str(o["title"]+" - "+o["artist"])+"*", _number=defaultNumber)

			text = str(o["title"]+" - "+o["artist"])
	except:
		traceback.print_exc()
	return text

from customTextEncoder import *
import emoji

def processRootCommands(message):
	origin = message["data"]["chatId"]
	user = message["data"]["from"]
	msgType =  message["data"]["type"]
	messageID = message["data"]["id"]
	text = None
	if "chat" in msgType:
		text = message["data"]["content"]
	# isMe = message["data"]["sender"]["isMe"]

	body = text if text is not None else ""
	if "ECHO" in body:
		print(" ::: ACK ECHO :::", text)
	elif body.startswith("/poll"):
		poll = water._driver.sendPoll(origin, "How do you like this service?", [
			"good", "great!", "niiccce"])

	elif body.startswith("/group"):
		groupName = "......"
		groupName = body.split("/group")[1].strip()
		res = " ::: creating new group group :::" + groupName
		# water.sendMessage(_message=res, _number=defaultNumber)
		# final = water._driver.createGroup(groupName, ["972543610404@c.us"])
		final = water.createGroup(groupName, ["972543610404@c.us"])
		# water.sendMessage(_message=f"GROUP CREATED {final}", _number=defaultNumber)
		water.sendMessage(_message=f"GROUP CREATED {final}", _number=origin)
		groupID = final["wid"]["_serialized"]
		if len(body.split(" ")) > 0:
			setGroupToService(groupID, body.split(" ")[1])
		inviteURL = "TODO invite url"
		print(" ::: DONE CREATING GROUP :::", groupID, inviteURL)
	elif body.startswith("/secret "):
		secret = "......"
		secret = body.split("/secret")[1].strip()
		# secret_wrapped = wrapSecret(emoji.emojize(secret), post = "🔐")
		splitSecret = secret.split(" ")
		post = ""
		if len(splitSecret) > 1:
			secret = splitSecret[0]
			secret_wrapped = wrapSecret(emoji.emojize(secret), post = splitSecret[1])
			if len(splitSecret) > 2:
				post = " ".join(splitSecret[2:])
			

		# if 		secret = body.split("/secret")[1].strip()
		secret_wrapped = wrapSecret(emoji.emojize(secret))

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
		water.sendMessage(_message=str(emoji.demojize(secret_wrapped)), _number=origin)
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
	isMe = False
	if "data" in message and "sender" in message["data"] and message["data"]["sender"] is not None:
		isMe = message["data"]["sender"]["isMe"]
	print()
	print("::::::::incoming :::::::::", origin, user, msgType, text, a, kw)
	if isMe and user == origin:
		print(f"This is the root manager isMe:{isMe}",origin)
		processRootCommands(message)
	elif isMe and origin in water.groups.value:
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
			
	elif isMe:
		print("????????????????????")
		print(">>> origin",origin)
		for knownGroup in water.groups:
			print(" -",knownGroup)
		print("????????????????????")


	data = {}
	if message:
		print(message["data"]["chat"]["id"], a, kw)
		print(":::::::::::::::::")
		pp(message)
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
			mContent = AnalyzeAudio(message)#, factored=factored)
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



	




# have raw ability to change icon and name

# create rolling empty groups, which are accessible via rest api

# create an abstract class for a service, which can be used to create a service
# it will have a name, a description, an icon, a list of event hooks, and an api to the user (obfuscated)

# water.services.warmWinters.users["master"].groups["origin_uid"]
# water.services.warmWinters.groups["origin_uid"].users["master"]
# water.groups["origin_uid"].service = "warmWinters"
# water.groups["origin_uid"].service.api = water.services.warmWinters.api

# water.users

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
