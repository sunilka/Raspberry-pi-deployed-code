from gtts import gTTS
import os
file = open("/home/pi/Desktop/final_year_project/weather/weather_text.txt","r").read()
speech = gTTS(text = str(file),lang = 'en',slow = False)
speech.save("/home/pi/Desktop/final_year_project/weather/weather_voice.mp3")
