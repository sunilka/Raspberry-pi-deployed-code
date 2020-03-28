from gtts import gTTS
import os
file = open("/home/pi/Desktop/final_year_project/jokes/result.txt","r").read()
speech = gTTS(text = str(file),lang = 'en',slow = False)
speech.save("/home/pi/Desktop/final_year_project/jokes/joke_voice.mp3")
