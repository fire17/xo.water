# from googlesearch.googlesearch import GoogleSearch
# from services.api import incomingEvent, poll, question, someService, WaterAPI, WaterService
from services.api import incomingEvent, poll, question, WaterAPI, WaterService
from pprint import pprint as pp

class Shush(WaterService):
	# def __init__(self, water):
	#     super().__init__(water)
	#     self.water = water
	#     self.shush = False
	#     self.shushers = []
	#     self.shushers.append("
	def __init__(self, water, *args, **kwargs):
		super().__init__(water)
		# print("ssssssssssssssssssssssssssss",water)
		self.setWater(water)
		# print(self._water)

	title = " ::: Shush Business Solutions ::: "
	name = "shush"
	# iconURL = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
	# iconURL = "https://cdn.iconscout.com/icon/free/png-128/google-photos-square-3771029-3147646.png"
	# iconURL = "https://images.squarespace-cdn.com/content/v1/5fb956af9747262983c8dd1a/1605982191381-24FICDGBYPHEHZV8UU83/shush.png?format=128w"
	iconURL = "https://images.squarespace-cdn.com/content/v1/5fb956af9747262983c8dd1a/1605982191381-24FICDGBYPHEHZV8UU83/shush.png?format=3000w"
	welcome = "Welcome to Shush Admin Service! \n You can open a shop with /shop [shop_name]"

	SuperAdminGroup = None
	shops = None
	cache = {}
	# load existing
	# if not exists:
		# create shush manager group

	def newShop(self, shopName, origin = None):
		if origin is None:
			origin = self.SuperAdminGroup
		pass
		groupName = shopName
		shopID = None
		# create shop manager group
		res = " ::: creating new group group :::" + groupName
		# water.sendMessage(_message=res, _number=defaultNumber)
		# final = water._driver.createGroup(groupName, ["972543610404@c.us"])
		if False:
			final = self.water.createGroup(groupName + " ::: Shush ", ["972543610404@c.us"])
			# water.sendMessage(_message=f"GROUP CREATED {final}", _number=defaultNumber)
			groupID = final["wid"]["_serialized"]
			# if len(body.split(" ")) > 0:
			self.water.sendMessage(
				_message=f"_Group {groupID} was created_", _number=origin)

			self.water.setGroupToService(groupID, "shush")
		else:
			groupID, final = self.water.newGroupService(
				"shush", debug=True, addRolling=True, _number = origin, overrideTitle = groupName + " ::: Shush ")

		inviteURL = final["invite_link"]
		print(" ::: DONE CREATING SHOP MANAGER GROUP :::", groupID, inviteURL)
		shopID = groupID
		
		if shopID:
			# create shopID, save
			if self.water.shush.managerGroups() == None:
				self.water.shush.managerGroups = []
			self.water.shush.managerGroups += [shopID]
			self.water.shush.managerGroups[shopID].name = shopName
		
		# Send info to manager group
		self.water.sendMessage(_message=f"{shopName} SHOP - MANAGER GROUP CREATED {shopID} {final}", _number=shopID)

		return groupID, final
		# create rolling group for new user



	def getShops(self):
		pass
		# get all shops and show them in the shush manager group

	def changeShop(self, shopIDorName):
		pass

	def findShop(self, shopIDorName):
		# check available shops 
		# return "shopManager" if origin is shop manaager group
		return False, None

	def handle_shush_super_admin(self, incomingEvent:incomingEvent, *args, **kwargs):
		print(" ::: MESSAGE FROM SHUSH SUPER ADMIN GROUP! ::: ")
		print(" ::: MESSAGE FROM SHUSH SUPER ADMIN GROUP! ::: ")
		print(" ::: MESSAGE FROM SHUSH SUPER ADMIN GROUP! ::: ")
		print(" ::: MESSAGE FROM SHUSH SUPER ADMIN GROUP! ::: ")
		print(" ::: MESSAGE FROM SHUSH SUPER ADMIN GROUP! ::: ")
		print(" ::: MESSAGE FROM SHUSH SUPER ADMIN GROUP! ::: ")
		print(" ::: MESSAGE FROM SHUSH SUPER ADMIN GROUP! ::: ")
		print(" ::: MESSAGE FROM SHUSH SUPER ADMIN GROUP! ::: ")
		print(" ::: MESSAGE FROM SHUSH SUPER ADMIN GROUP! ::: ")
		print(" ::: MESSAGE FROM SHUSH SUPER ADMIN GROUP! ::: ")
		print(" ::: MESSAGE FROM SHUSH SUPER ADMIN GROUP! ::: ")
		print(" ::: MESSAGE FROM SHUSH SUPER ADMIN GROUP! ::: ")
		print(" ::: MESSAGE FROM SHUSH SUPER ADMIN GROUP! ::: ")
		pp(incomingEvent.data)

		body = str(incomingEvent.data["data"]["body"])
		if "/shop" in body:
			imageIncludedInMessage = False
			if imageIncludedInMessage:
				pass # add image
			shopName = " ".join(body.strip().split(' ')[1:])
			
			# create Shop Manager Group
			groupID, finalData, = self.newShop(shopName, incomingEvent.origin)
			# get Invite link
			inviteLink = finalData["invite_link"]
			self.water.sendMessage(_message=f"{shopName} SHOP - {groupID} \n{inviteLink}", _number=incomingEvent.origin, url = inviteLink)
			# self.water.sendLinkWithAutoPreview(
			# 	incomingEvent.origin,inviteLink, f"{shopName} SHOP - {groupID} invite: {inviteLink}")

 
			# create rolling group for shop
			# Send the rolling link for the shop
			
			# make and example product and send an invite link with context to the manager group
			self.water.sendMessage(_message=f"This is an example Product", _number=groupID)
			# add an image
			self.water.sendMessage(_message=f"/product Chocolate Box #1", _number=groupID)
			


			# context = f"?context={body.split(' ').strip()[1:].replace(' ','+')}&so=wa"


	def handle_shop_manager(self, incomingEvent:incomingEvent, *args, **kwargs):
		print(" ::: MESSAGE FROM SHOP MANAGER GROUP/USER ::: ")
		print(" ::: MESSAGE FROM SHOP MANAGER GROUP/USER ::: ")
		print(" ::: MESSAGE FROM SHOP MANAGER GROUP/USER ::: ")
		print(" ::: MESSAGE FROM SHOP MANAGER GROUP/USER ::: ")
		print(" ::: MESSAGE FROM SHOP MANAGER GROUP/USER ::: ")
		print(" ::: MESSAGE FROM SHOP MANAGER GROUP/USER ::: ")
		print(" ::: MESSAGE FROM SHOP MANAGER GROUP/USER ::: ")
		print(" ::: MESSAGE FROM SHOP MANAGER GROUP/USER ::: ")
		print(" ::: MESSAGE FROM SHOP MANAGER GROUP/USER ::: ")
		pp(incomingEvent.data)
		origin = incomingEvent.origin
		# body = str(data)
		body = incomingEvent.data["data"]["body"]

		if "/product" in body:
			imageIncludedInMessage = False
			if imageIncludedInMessage:
				pass # add image
			# Get the rolling link for the shop
			context = f"?context={' '.join(body.strip().split(' ')[1:]).replace(' ','+')}&so=wa"
			inviteLink = "{rolling invite link}"
			# send with auto preview
			self.water.sendMessage(_message=f"{inviteLink}/{context}", _number=origin)


	def shop_msg_incoming(shopData, incomingEvent: incomingEvent, *args, **kwargs):
		print(" ::: MESSAGE FROM SHOP ! ::: ")
		print(" ::: MESSAGE FROM SHOP ! ::: ")
		print(" ::: MESSAGE FROM SHOP ! ::: ")
		print(" ::: MESSAGE FROM SHOP ! ::: ")
		print(" ::: MESSAGE FROM SHOP ! ::: ")
		print(" ::: MESSAGE FROM SHOP ! ::: ")
		print(" ::: MESSAGE FROM SHOP ! ::: ")
		print(" ::: MESSAGE FROM SHOP ! ::: ",shopData)
		# forward msg to manager group

		pp(incomingEvent.data["data"])

	def on_participant_changed(self, data, *args, **kwargs):
		print(" ::: on_participant_changed ! SHUSH ! ::: ")
		# if self.shushSuperAdminGroup is None:
			# self.shushSuperAdminGroup = data["origin"]
		

	def on_incoming(self, incomingEvent:incomingEvent, *args, **kwargs):
		print("!@!@!@!@!@!@!@!@!@!@!@ on_incoming SHUSH")

		if self.SuperAdminGroup is None:
			print("XXXXXXXXXXXXXX No manager group id")
			self.SuperAdminGroup = "120363048398073497@g.us"
			self.SuperAdminGroup = "120363047537890730@g.us"
			# TODO: load from db

			# return 
		elif incomingEvent.origin is None:
			print("XXXXXXXXXXXXXX origin is None")
			return 
		else:
			print("XXXXXXXXXXXXXX manager group id", self.SuperAdminGroup)
			print("XXXXXXXXXXXXXX manager group id", self.SuperAdminGroup)
			print("XXXXXXXXXXXXXX manager group id", self.SuperAdminGroup)
			print("XXXXXXXXXXXXXX manager group id", self.SuperAdminGroup)
			print("XXXXXXXXXXXXXX manager group id", self.SuperAdminGroup)
			print("XXXXXXXXXXXXXX manager group id", self.SuperAdminGroup)

		if incomingEvent.origin == self.SuperAdminGroup:
			print("!@!@!@!@!@!@!@!@!@!@!@ on_incoming SHUSH Super Admin Group")
			return self.handle_shush_super_admin(incomingEvent, *args, **kwargs)

		if incomingEvent.origin in self.water.shush.managerGroups():
			print("!@!@!@!@!@!@!@!@!@!@!@ on_incoming SHUSH SHOP MANAGER")
			return self.handle_shop_manager(incomingEvent, *args, **kwargs)
		
		exists, shopData = self.findShop(incomingEvent.origin)
		if exists:
			print("!@!@!@!@!@!@!@!@!@!@!@ on_incoming SHUSH  ---- shop: ",shopData)
			# if "shopManager" in shopData and shopData["shopManager"]:
			#     return self.handle_shop_manager(data, *args, **kwargs)
			return self.shop_msg_incoming(shopData, incomingEvent, *args, **kwargs)
			# if "shopManage" in shopData and shopData["shopManager"]:

		else:
			print("XXXXXXXXXXXXXX findShop did not find matching origin ",incomingEvent["origin"])
			return 