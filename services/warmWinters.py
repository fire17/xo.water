from api import *

class WarmWinters(someService):
	title = ""
	welcome = ""
	sessions = {}
	
	def on_init_group(self, groupUID, *args, **kwargs ):

		self._api.send(self.Welcome)
		self._api.sendPoll(groupUID, self.rootPoll)
		# send welcome
		pass 
		print("@@@@@@@@@@ group init", groupUID, args, kwargs)
	


	def on_incoming(self, data:incomingEvent, *args, **kwargs):
		# if data.eventType == "poll":
		print("!!!!!!!!!!!!!!!",data, args, kwargs)


	def onRoot1(self, group:str, data:incomingEvent):
		#save user prefs
		self._api.send("We will get you heating asap! please provide us with more details to complete the request")
		self._api.sendPoll(group, self.lastQuestion)
		pass

	def requestHeating1(self, group:str, data:incomingEvent):
		#save user prefs
		self._api.send("Last Question")
		self._api.sendQuestion(group, self.lastQuestion)
		
	def onLastQuestion(self, group:str, data:incomingEvent):
		# sessionData = self.xo_store.get(group, {})
		sessionData = {} # get from db
		self.done(group, data, sessionData)

	def requestHeating2(self, group:str, data:incomingEvent):
		pass

	def onRoot2(self, group:str, data:incomingEvent):
		#save user prefs
		pass
	def done(self, group:str, data:incomingEvent, sessionData:dict):
		pass
	rootPoll = poll("Choose 1-4", ("option 1",onRoot1),("option 2",onRoot2))
	requestHeatingPoll = poll("How many people", ("1-2",requestHeating1),("3-8",requestHeating1),("3-8",requestHeating1))
	lastQuestion = question("Choose 1-4", onLastQuestion, lambda *a,**kw: True if len(a) > 0 and type(a[0]) == str else False , "Please enter valid answer (str)")



	# def onRoot3(self, group:str, data:_incomingEvent):
	# 	#save user prefs
	# 	pass
	# def onRoot4(self, group:str, data:_incomingEvent):
	# 	#save user prefs
	# 	pass

	
	

		

# water.services.warmWinters.users["master"].groups["origin_uid"]
# water.services.warmWinters.groups["origin_uid"].users["master"]
def waterFlowDesc(water):
	warmWinters = water.services.warmWinters
	warmWinters.icon = "🌱" 
	warmWinters.iconURL = ""
	warmWinters.name = "Warm Winters 🔥❄️"
	warmWinters.description = "A service to help everybody stay warm during the winter."
	warmWinters.welcome = "*Welcome to Warm Winters* 🔥❄️\nWe are here to help make sure everyone stays warm during the winter.\n" + \
		"\n*How it works? What are the options*:\n" + \
		"1. You can send an anonymous request to get heating for you or someone else.\n" + \
		"2. Anyone can volenteer to donate either some heating equiptment or money to buy new ones.\n" + \
		"3. If you'd like to help in other ways, there other options, such as with deliveries.\n" + \
		"4. If you are (or you know of) a local supplier/non-profit organization, and would like to get involved .\n"
	warmWinters.welcome[1] = "@poll", "*Warm Winters* 🔥❄️", ["1. Request heating", "2. Give/Donate heating", "3. Help with deliveries/others", "4. Join as a supplier/non-profit organization"]
	
	warmWinters.welcome[1].on[1][1] = "*Request heating* 🔥"
	warmWinters.welcome[1].on[1][2] = "@poll", "*How many people* need heating?", ["1-2 People","3-8 People"," Over 8+ People"]
	warmWinters.welcome[1].on[1][3] = "@question", "What is the *Delivery address* ? (Full address or location)", "location"
	warmWinters.welcome[1].on[1][4] = "@question", "Write down *anything else you would like us to know* when handleing your request:", str
	warmWinters.welcome[1].on[1].done = "@handleHeatingRequest","*Done!* You request is saved:", "We will get back to you as soon as we have "

	warmWinters.welcome[1].on[2][1] = "@poll","*Give or Donate heating* 🔥", ["*I have equiptment* to donate","Donate *money for heating equiptment*"]
	warmWinters.welcome[1].on[2][1].on[1][1] = "That is amazing!"
	warmWinters.welcome[1].on[2][1].on[1][2] = "@poll", "Are you mobile? Can you deliver in your are?", ["Yes","No"]
	warmWinters.welcome[1].on[2][1].on[1][3] = "@question", "What equiptment do you have to give (good condition only):"
	warmWinters.welcome[1].on[2][1].on[1].done = "@handleGiveaway"

	warmWinters.welcome[1].on[2][1].on[2][1] = "*Incredible - Thank you! in the link below you can choose how much you'd like to donate"
	warmWinters.welcome[1].on[2][1].on[2][2] = "@paymentLink"
	warmWinters.welcome[1].on[2][1].on[2].done = "@paymentHandle"
	
	
	warmWinters.welcome[1].on[3][1] = "@poll", "*Help with deliveries/others* 🔥\nAre you mobile? Can you help deliver in your are?", ["Yes, I Can Deliver :)","Id like to help in other matters :)"]
	warmWinters.welcome[1].on[3][1].on[1] = "@question", "Where can you make deliveries?\nWrite All the areas, seperated by comma - or send a location:", "location"
	warmWinters.welcome[1].on[3][1].on[1].done = "@deliveryVolenteer"
	warmWinters.welcome[1].on[3][1].on[2] = "@inviteToCommunity"

	
	warmWinters.welcome[1].on[4][1] = "@poll", "*Register as:* ", ["I am heating supplier", "I work with a non-profit organization"]
	warmWinters.welcome[1].on[4][1].on[1] = "@question", "Where can you make deliveries?\nWrite All the areas (seperated by comma), or send a location:", "location"
	warmWinters.welcome[1].on[4][2] = "@question", "What is the *name of the Organization* ?:"
	warmWinters.welcome[1].on[4][3] = "@question", "What is *your name* ? (for follow ups):"
	warmWinters.welcome[1].on[4][3].done = "@registerEntity"
	
	
	
	# warmWinters.polls.welcome[1] = "*Request heating* 🔥"]
	
	# water._driver.sendPoll(res["wid"]["_serialized"], "*:חורף חם*",["בקשת חימום", "תרומת חימום", "עזרה במסירה", "הרשמה כעמותה/ספק"])
