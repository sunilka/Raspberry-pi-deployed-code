from gtts import gTTS
import os
file = open("/home/pi/Desktop/final_year_project/horoscope/h.txt","r").read()
speech = gTTS(text = str(file),lang = 'en',slow = False)
speech.save("/home/pi/Desktop/final_year_project/horoscope/h_voice.mp3")
