import requests
import json
import pygame



def jokes(f):
    
    data = requests.get(f)
    tt = json.loads(data.text)
    return tt



pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Desktop/final_year_project/extravoices/joke_welcome.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
f = r"https://official-joke-api.appspot.com/jokes/programming/random"
a = jokes(f)

for i in (a):
    f = open("/home/pi/Desktop/final_year_project/jokes/result.txt","w")
    f.write(i["type"])
    f.write("\n")
    f.write(i["setup"])
    f.write("\n")
    f.write(i["punchline"]+"\n")
    f.write("Done")
    f.close()
    print(i["type"])
    print(i["setup"])
    print(i["punchline"], "\n")
