# importing packages and necessary dependencies
from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

# A function that takes our voice and give back answers
def talkToMe(audio):
	print(audio)
	tts = gTTS(text = audio , lang ='en',slow=False)
	tts.save('audio.mp3')
	os.system('mpg123 audio.mp3')

# A function that listens to our commands
def mycommand():

	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("What is my next command?")
		r.pause_threshhold = 1
		r.adjust_for_ambient_noise(source, duration = 1)
		audio = r.listen(source)

	try:
		command = r.recognize_google(audio)
		print('You said ' + command + '\n')
	
	#loop back to continue to listen for commands
	
	except sr.UnknownValueError:
		print("I didn't get you.")
		assistant (mycommand())

	return command

# if statements for executing the commands
def assistant(command):
	if 'open Reddit python' in command:
		chrome_path = '/usr/bin/google-chrome'
		url = 'https://www.reddit.com/r/python'
		webbrowser.get(chrome_path).open(url)
	if "what's up?" in command:
		talkToMe("what do you want mdrfckr")
	
	if "mail" in command:
		talkToMe('who is the recipent')
		recipent = mycommand()

	if recipent is 'karanvir':
		talkToMe("What should I say?")
		content = mycommand()
	#init gmail
	mail = smtplib.SMTP('stmp.gmail.com',587)

	#identify the server
	mail.ehlo()

	#encrypt session
	mail.starttls()

	#login
	mail.login('username', 'password')

	#send mail
	mail.sendmail('PERSON NAME', 'email@whatever.com',content)

	#close connection
	mail.close()
	
	talkToMe('email sent')

talkToMe('What is my next command?')

while True:
	assistant(mycommand())	
