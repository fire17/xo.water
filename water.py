#xo.water.py



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
from xo.redis import xoRedis, xo 

water = xoRedis('water')


def getEnvKey(key="WA_KEY"):
    return os.environ.get(key, "Please export the WA_KEY environment variable.")
wa_key = getEnvKey()
host, port = "localhost", 8085
# from common import *
# from dal.utilities.rename_process import set_proc_name
# set_proc_name(b'simple')
defaultNumber = "972547932000@c.us"
def manage_incoming(message, *a,**kw):
	print(":::::::::::::::::")
	if message:
		print(message["data"]["chat"]["id"],a,kw)
		print(":::::::::::::::::")
		print(message)
	print(":::::::::::::::::")
	if message:
		body = "________________________empty body________________________"
		if "data" in message and "body" in message["data"]:
			body = message["data"]["body"]


		origin = message["data"]["chat"]["id"]
		print(f" incoming ::: {a} {kw} \n", message["data"]["sender"]["id"], origin, "\n",body, "\n")
		useEcho = True
		
		response = "ECHO!\n" +body
		if message["data"]["sender"]["isMe"]:
			# print(" ::: message from me :::")
			response += "\n\n ::: message from me :::"
			if "ECHO" in body:
				print(" ::: ACK ECHO :::")
			elif body.startswith("/group"):
				groupName = "......"
				groupName = body.split("/group")[1].strip()
				res = " ::: creating new group group :::"+ groupName
				# water.sendMessage(_message=res, _number=defaultNumber)
				# final = water._driver.createGroup(groupName, ["972543610404@c.us"])
				final = water.createGroup(groupName, ["972543610404@c.us"])
				water.sendMessage(_message=f"GROUP CREATED {final}", _number=defaultNumber)
			else:
				if useEcho:
					
					if "g.us" in origin:
						print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
						water._driver.setGroupTitle(origin, body + "TTTTTTTTT")
						poll = water._driver.sendPoll(origin, "How do you like this service?", [
	                       "good", "great!", "niiccce"])
						
						print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",poll)
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
	print(":::!!!!!!!send::::::::::::::", _message, _number)
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

	# Executing commands
	water._driver.sendText(number, "fresh waters!!!!!!")

	# Sync/Async support
	print(" ::: CONNECTED! ", water._driver.getHostNumber())  # Sync request
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
	water.sendMessage("WELCOME!",res["info"]["groupMetadata"]["id"])
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	# water._driver.sendMessage("WELCOME!", "120363029005529843@g.us")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	water._driver.sendPoll(res["wid"]["_serialized"], "How do you like this service?",["good", "great!", "niiccce"])
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

	water._driver.setGroupTitle(res["wid"]["_serialized"], "XXXXXXXXXXXXXXX")

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
# water.timedMessage = lambda payload, *a,**kw : water.sendTimedMessage(payload)
water.onMessage @= lambda payload, *a,**kw : water.ManageIncoming(payload)
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






# water.newContact = lambda payload, *a,**kw : water.addContact(payload)
# water.newMedia = lambda payload, *a,**kw : water.sendMedia(payload)
# water.newLocation = lambda payload, *a,**kw : water.sendLocation(payload)
# water.newSticker = lambda payload, *a,**kw : water.sendSticker(payload)

if __name__ == "__main__":
	main()
