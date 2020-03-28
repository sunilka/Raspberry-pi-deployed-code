from gtts import gTTS
import os
file = open("//home//pi//Desktop//final_year_project//news_headlines//news_text.txt","r").read()
speech = gTTS(text = str(file),lang = 'en',slow = False)
speech.save("//home//pi//Desktop//final_year_project//news_headlines//news_voice.mp3")
