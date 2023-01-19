# from googlesearch.googlesearch import GoogleSearch
# from services.api import incomingEvent, poll, question, someService, WaterAPI, WaterService
from services.api import incomingEvent, poll, question, WaterAPI, WaterService
# from wservices import 

# class Googler(someService):
class Googler(WaterService):
	title = "Google"
	name = "googler"
	# iconURL = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
	iconURL = "https://cdn.iconscout.com/icon/free/png-128/google-photos-square-3771029-3147646.png"
	welcome = "Welcome to Google Service! \n any thing you send here will turn into a google search"
	sessions = {}

	def __init__(self, api: WaterAPI, *args, **kwargs):
		self._api = api
	
	
	def on_init_group(self, groupUID, *args, **kwargs ):

		self._api.send(self.Welcome)
		# self._api.sendPoll(groupUID, self.rootPoll)
		# send welcome
		pass 
		print("@@@@@@@@@@ googler group init", groupUID, args, kwargs)



	def on_incoming(self, data:incomingEvent, *args, **kwargs):
		# if data.eventType == "poll":
		# print("!!!!!!!!!!!!!!!",data.data, args, kwargs)
		print("!!!!!!!!!!!!!!!!!", data.origin,)
		query = data.data["data"]["body"]
		# self._api.send(data.origin, "https://www.google.com/search?q="+str(data.data))
		max_results = 5
		maxWordsDesc = 10
		# search_results = [res for res in googlesearch.search(query)[:max_results]]
		search_results = []
		resC = 0
		# looking =  search(query)
		looking = []
		tries = 0
		while tries < 3:
			try:
				looking =  Search(query).results
			except:
				print("FAILED TO SEARCH", query)
				pass
			if len(looking) > 0:
				break
			tries += 1

		for result in looking:
			print("!!!!!!!!!!!!!!!!",result)
			search_results.append(result)
			resC += 1
			if resC > max_results:
				break

		final = "[Search Results]\n"
		c = 1
		for result in search_results:
			final += str(c) + ". *" + result.title+"* "+" ".join(result.description.split(" ")[:maxWordsDesc])+"\n" + result.url + "\n"
			c+=1

		self._api.send(data.origin, str(final))
		print("::::::::::::::::::::::::: DONE GOOGLER INCOMING")
		print("::::::::::::::::::::::::: DONE GOOGLER INCOMING")
		print("::::::::::::::::::::::::: DONE GOOGLER INCOMING")
		print("::::::::::::::::::::::::: DONE GOOGLER INCOMING")
		print("::::::::::::::::::::::::: DONE GOOGLER INCOMING")
		print("::::::::::::::::::::::::: DONE GOOGLER INCOMING")
		print("::::::::::::::::::::::::: DONE GOOGLER INCOMING")
		print("::::::::::::::::::::::::: DONE GOOGLER INCOMING")
	
# from googlesearch import search

# from googleapi import google
# num_page = 3
# search = google.search

from googlesearch import Search


# from google import google
# import googlesearch
