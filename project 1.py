import os
import pyttsx3
import time

pyttsx3.speak("hii myself alexa whats your name?")

name=input("enter your name:-")
print()
print(name,"do u wannt to know about your system:-",end="")
about_me=input()
if about_me=="yes":
	os.system("start ms-settings:about") 
	print()
else:
	print("u can continue your work :) ...")
	print()
time.sleep(1)

while True:
	print(name,"how can i help u:-",end=(""))
	str=input()
	print()
	x=(str.lower())
	word="alexa" 
	first_word=x.split()[0]
	if word==first_word:  #wake word ALEXA 
		
		if("run" in x) or ("start" in x) or ("launch" in x) or ("open" in x) or ("execute" in x) or ("play" in x) or ("show" in x) or ("tell" in x) or ("what" in x) or ("set" in x):   #launch words   
			if "notepad" in x or "editor" in x:  #default text editor
				pyttsx3.speak("running notepad")
				os.system("notepad")
			elif ("bluetooth" in x) :
				print("enable it if not enabled")
				time.sleep(2)
				os.system("start ms-settings:bluetooth")
				time.sleep(4.7)
				os.system(" start fsquirt")
			elif ("browser" in x) or ("chrome" in x):  #default browser
				pyttsx3.speak("launching chrome")
				os.system("chrome")
			elif "firefox" in x:
				pyttsx3.speak("launching firefox")
				os.system("firefox")
			elif "google" in x:
				pyttsx3.speak("opening google search engine website in chrome")
				os.system("chrome google.com")
			elif "yahoo" in x:
				pyttsx3.speak("opening yahoo search engine website in chrome")
				os.system("chrome yahoo.com")
			elif "bing" in x:
				pyttsx3.speak("opening bing search engine website in chrome")
				os.system("chrome bing.com")
			elif "vlc" in x:  
				pyttsx3.speak("running vlc")  
				os.system("vlc")
			elif "shareit" in  x:
				pyttsx3.speak("here you go")
				os.system("shareit")
			elif "virtualbox" in  x:
				pyttsx3.speak("here you go for virtulization")
				os.system("virtualbox")
			elif ("pdf reader" in  x) or ("pdf viewer" in x):
				pyttsx3.speak("start reading")
				os.system("pdfreader")
			elif "calculator" in  x:
				pyttsx3.speak("launching calculator")
				os.system("calc")
			elif "drawboard" in  x:
				pyttsx3.speak("here you go")
				os.system("start drawboardpdf:")
			elif "time" in  x:
				os.system("time")
			elif "date" in  x:
				os.system("date")
			elif "paint" in  x:
				pyttsx3.speak("start painting")
				os.system("start ms-paint:")
			elif "onenote" in  x:
				pyttsx3.speak("here you go")
				os.system("start onenote")
			elif "outlook" in  x:
				pyttsx3.speak("here you go")
				os.system("start outlook")
			elif "sublime" in  x:
				pyttsx3.speak("running sublime text editor")
				os.system("subl.exe")
			elif ("powerpoint" in  x) or ("ms-powerpoint" in x):
				pyttsx3.speak("opening powerpoint")
				os.system("start powerpnt")
			elif ("word" in  x) or ("ms-word" in x):
				pyttsx3.speak("launching ms word")
				os.system("start winword")
			elif ("ms-excel" in  x) or ("excel" in x):
				pyttsx3.speak("launching ms excel")
				os.system("start excel")
			elif ("ms-access" in  x) or ("access" in x):
				pyttsx3.speak("launching ms access")
				os.system("start access")
			elif ("avast" in  x) or ("anti-virus" in x) or ("anti virus" in x):
				pyttsx3.speak("here you go")
				os.system("avastui")
			elif "obs" in x:
				pyttsx3.speak("executing OBS")
				os.system("obs64")
			elif ("music" in  x) or ("gaana" in x) or ("groove" in x):
				pyttsx3.speak("start playing music")
				os.system("start mswindowsmusic:")
			elif ("camera" in  x) or ("webcam" in x) or ("camcorder" in x):
				pyttsx3.speak("opening your camera")
				os.system("start microsoft.windows.camera:")
			elif ("3dbuilder" in  x) or ("builder3d" in x):
				pyttsx3.speak("here you go")
				os.system("start com.microsoft.builder3d:")
			elif ("messaging" in  x) or ("chatbox" in x) or ("chat" in x) or ("chatting" in x):
				pyttsx3.speak("start messaging")
				os.system("start ms-chat:")
			elif ("store" in  x) or ("window-store" in x):
				pyttsx3.speak("opening window store")
				os.system("start ms-windows-store:")
			elif "whatsapp" in  x:
				pyttsx3.speak("start chatting in whatsapp")
				os.system("whatsapp")
			elif ("network" in  x) or ("networks" in x) or ("connections" in x):
				pyttsx3.speak("your available networks are")
				os.system("start ms-availablenetworks:")
			elif "calendar" in  x:
				pyttsx3.speak("here you go")
				os.system("start outlookcal:")
			elif ("candy crush" in  x) or ("soda saga" in x):
				pyttsx3.speak("start playing ")
				os.system("start candycrushsodasaga:")
			elif "projection" in x:
				pyttsx3.speak("here you go")
				os.system("start ms-projection:")
			elif "cortana" in  x:
				pyttsx3.speak("start interacting with cortana ")
				os.system("start ms-cortana:")
			elif "feedback" in  x:
				pyttsx3.speak("launching feedback hub")
				os.system("start feedback-hub:")
			elif "help" in  x:
				pyttsx3.speak("opening your help center")
				os.system("start ms-contact-support:")
			elif ("mail" in  x) or ("email" in x):
				pyttsx3.speak("here you go")
				os.system("start outlookmail:")
			elif "maps" in  x:
				pyttsx3.speak("here you go")
				os.system("start ms-drive-to:")
			elif "edge" in  x:
				pyttsx3.speak("launching edge")
				os.system("start microsoft-edge:")
			elif "news" in  x:
				pyttsx3.speak("latest news are here for you")
				os.system("start bingnews:")
			elif "solitaire" in  x:	
				pyttsx3.speak("start playing")
				os.system("start xboxliveapp-1297287741:")
			elif ("media" in x) or ("player" in x):
				pyttsx3.speak("launching windows media player")
				os.system("wmplayer")		
			elif "whiteboard" in x:
				pyttsx3.speak("here you go")
				os.system("start ms-whiteboard-cmd:")
			elif "people" in  x:
				pyttsx3.speak("here you go")
				os.system("start ms-people:")
			elif ("photos" in  x) or ("picture" in x) or ("gallary" in x) or ("album" in x):
				pyttsx3.speak("your gallary")
				os.system("start ms-photos:")
			elif "tips" in  x:
				pyttsx3.speak("here you go")
				os.system("start ms-get-started:")
			elif "twitter" in  x:
				pyttsx3.speak("start twitting")
				os.system("start twitter:")
			elif ("3dviewer" in  x) or ("3dpreview" in x):
				pyttsx3.speak("here you go")
				os.system("start com.microsoft.3dviewer:")
			elif ("record" in  x) or ("call recording" in x):
				pyttsx3.speak("start recording")
				os.system("start ms-callrecording:")
			elif "weather" in  x:
				pyttsx3.speak("here's your update")
				os.system("start bingweather:")
			elif ("defender" in  x) or ("windowsdefender" in x):
				pyttsx3.speak("start securing your windows")
				os.system("start windowsdefender:")
			elif ("clock" in  x) or ("alarm" in x):
				pyttsx3.speak("here you go")
				os.system("start ms-clock:")
			elif ("xbox" in  x) and ("friend" in x):
				os.system("start xbox-friendfinder:")
			elif ("xbox" in  x) and ("profile" in x):
				os.system("start xbox-profile:")
			elif ("xbox" in  x) and ("settings" in x):
				os.system("start xbox-settings:")
			elif ("xbox" in  x) and ("smartglass" in x):
				os.system("start smartglass:")
			elif "xbox" in  x:
				pyttsx3.speak("launching xbox")
				os.system("start xbox:")
			elif "settings" in  x:
				pyttsx3.speak("start settings")
				os.system("start ms-settings:")		
			else:
				print("please elaborate your statement...")
		elif ("exit" in  x) or ("quit" in x) or ("close" in x) or ("stop" in x) or ("turn off" in x) or ("shut down" in x):  #this will let u go out of alexa 
			break
		else:
			print("please elaborate your statement...")
	else:
		print("Wake me up by writing the first word of your statement---alexa---")
		print()
