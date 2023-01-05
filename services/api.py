
class incomingEvent():
	def __init__(self, eventType:str, data:object, origin:str, user:str, *args, **kwargs):
		self.eventType = eventType
		self.data = data
		self.origin = origin
		self.user = user
	eventType:str
	data:object
	origin:str
	user:str

class poll():
	pass
class question():
	pass

class WaterAPI():

	def __init__(self, driver) -> None:
		self._driver = driver

	def respond(*args, **kwargs):
		print(" ::::::::: RESPONDING ? API ::::::::::::", *args, **kwargs)
		
	def send(self,origin, data, *args, **kwargs):

		print(" ::::::::: SENDING SOMETHING API ::::::::::::",origin, data, args, kwargs)
		if self._driver is not None:
			self._driver.sendText(origin, "[Results]\n" + str(data) )
			print("DONE")

		
	# def sendPoll(self, title, options, callback = None):
	def sendPoll(self, poll:poll, *args, **kwargs):
		print(" ::::::::: SENDING POLL API ::::::::::::", poll, args, kwargs)

	def sendQuestion(self, question, callback = None, filter=None, filterResponse=None , *args, **kwargs):
		print(" ::::::::: SENDING Question API ::::::::::::",question, callback , filter, filterResponse, args, kwargs)
		
class someService(object):
	name="someService"
	title = " ::: Some Service :::"
	iconURL = ""
	_api = None
	state = {} # use xo.redis ?

	def __init__(self, api:WaterAPI,*args,**kwargs):
		self._api = api
		
	def on_incoming(self, *args, **kwargs):
		# handle logic for new information
		pass 
	def on_init_group(self, *args, **kwargs):
		# send welcome
		pass

	def live(self, *args, **kwargs):
		pass 
