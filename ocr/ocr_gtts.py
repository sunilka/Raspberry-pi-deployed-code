from gtts import gTTS
import os
file = open("//home//pi//Desktop//final_year_project//ocr//ocr_text.txt","r").read().replace("\n"," ")
if os.stat("//home//pi//Desktop//final_year_project//ocr//ocr_text.txt").st_size > 0:
	speech = gTTS(text = str(file),lang = 'en',slow = False)
else:
	speech = gTTS(text = "Image not captured properly, please try again. Program complete",lang = 'en',slow = False)
speech.save("//home//pi//Desktop//final_year_project//ocr//ocr_voice.mp3")

