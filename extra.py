########OLD CODE########

def xProcess(contact, factored=False):

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
								self.driver.sendMessage(
									chatID, target+" : is not recognized as a service "+target)

########################