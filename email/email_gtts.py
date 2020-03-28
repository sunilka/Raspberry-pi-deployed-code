from gtts import gTTS
import os
file = open("//home//pi//Desktop//final_year_project//email//emailemail_text.txt","r").read()
speech = gTTS(text = str(file),lang = 'en',slow = False)
speech.save("//home//pi//Desktop//final_year_project//email//email_voice.mp3")
