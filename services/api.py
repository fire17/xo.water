
class incomingEvent():
	eventType:str
	data:dict
	origin:str
	user:str

class poll():
	pass
class question():
	pass

class WaterAPI():
	def respond(*args, **kwargs):
		print(" ::::::::: RESPONDING ? API ::::::::::::", *args, **kwargs)
		
	def send(origin, data, *args, **kwargs):
		print(" ::::::::: SENDING SOMETHING API ::::::::::::",origin, data, args, kwargs)
		
	# def sendPoll(self, title, options, callback = None):
	def sendPoll(self, poll:poll, *args, **kwargs):
		print(" ::::::::: SENDING POLL API ::::::::::::", poll, args, kwargs)

	def sendQuestion(self, question, callback = None, filter=None, filterResponse=None , *args, **kwargs):
		print(" ::::::::: SENDING Question API ::::::::::::",question, callback , filter, filterResponse, args, kwargs)
		
class someService():
	_api = None
	state = {} # use xo.redis ?
	def __init__(self, api:WaterAPI,*args,**kwargs):
		self._api = api
		
	def on_incoming():
		# handle logic for new information
		pass 
	def on_init_group():
		# send welcome
		pass

	def live():
		pass 
