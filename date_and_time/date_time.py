import time
import os
import pytesseract  
import pyttsx3   
from PIL import Image              
from googletrans import Translator       
from gtts import gTTS 
from playsound import playsound
from datetime import datetime
from datetime import date
from datetime import date

f = open("/home/pi/Desktop/final_year_project/date_and_time/date_time_text.txt",'w')
today = date.today()
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)
f.write("Today's date is : ")
f.write(d2)
f.write("\n")
t = time.localtime()
current_time = time.strftime("%H:%M:%S",t)
print(current_time)
f.write("Current time is : ")
f.write(current_time)
f.write("\n")
print("Have a nice day")
f.write("Have a nice day")
f.close()
