

import traceback
import base64
# from gtts import gTTS
from pydub import AudioSegment
import shazi
# from munch import Munch

import speech_recognition as sr
recognizer = sr.Recognizer()


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
		print("..............")
		print("..............")
		dec = water._driver.decryptMedia(jobj)
		print("..............",dec)
		print("\n"*5)
		print("PTT: ", ptt)
		pp(jobj)
		print("\n"*4)
		print("################################")
		print("################################")
		print(dec)
		print("################################")
		print("################################")
		# audio = AudioSegment.from_file(ptt)
		if "filePath" not in jobj or True:
			# audio = AudioSegment.from_file(jobj["filePath"])
			with open(origin.split("@")[0]+"_recX"+".wav", "wb") as file:
				file.write(base64.b64decode(dec.split(";base64,")[1]))
			audioFile = origin.split("@")[0]+"_recX"+".wav"
		else:
			audioFile = jobj["filePath"]

		audio = AudioSegment.from_file(audioFile)
		

		length = len(audio)
		# audio = AudioSegment.from_file(ptt)
		# path = "rec.wav"
		# path = "recs/"+message.chat_id.split("@")[0]+"_rec"+".wav"
		# path = "recs/"+origin.split("@")[0]+"_rec"+".wav"
		path = audioFile
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
