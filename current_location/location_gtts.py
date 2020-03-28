from gtts import gTTS
import os
file = open("//home//pi//Desktop//final_year_project//current_location//location.txt","r").read().replace("\n"," ")
speech = gTTS(text = str(file),lang = 'en',slow = False)
speech.save("//home//pi//Desktop//final_year_project//current_location//cur_loc.mp3")
