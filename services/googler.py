from services.api import incomingEvent, poll, question, someService, WaterAPI

class Googler(someService):
    title = "Google"
    name = "googler"
    iconURL = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
    welcome = "Welcome to Google Service! \n any thing you send here will turn into a google search"
    sessions = {}
    
    
def on_init_group(self, groupUID, *args, **kwargs ):

    self._api.send(self.Welcome)
    # self._api.sendPoll(groupUID, self.rootPoll)
    # send welcome
    pass 
    print("@@@@@@@@@@ googler group init", groupUID, args, kwargs)



def on_incoming(self, data:incomingEvent, *args, **kwargs):
    # if data.eventType == "poll":
    print("!!!!!!!!!!!!!!!",data, args, kwargs)
    self._api.send(data.origin, "https://www.google.com/search?q="+str(data.data))
    print("::::::::::::::::::::::::: DONE GOOGLER INCOMING")
    