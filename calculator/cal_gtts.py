from gtts import gTTS
import os
file = open("/home/pi/Desktop/final_year_project/calculator/result.txt","r").read()
speech = gTTS(text = str(file),lang = 'en',slow = False)
speech.save("/home/pi/Desktop/final_year_project/calculator/cal_voice.mp3")
