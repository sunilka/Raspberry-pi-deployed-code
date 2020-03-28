import pygame
import random
import os



def pmusic(file):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        print("Playing...")
        clock.tick(1000)

def stopmusic():
    pygame.mixer.music.stop()


def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan


def initMixer():
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

try:
	pmusic("/home/pi/Desktop/final_year_project/extravoices/music_welcome.mp3")
	path = "/home/pi/Desktop/final_year_project/music"
	all_mp3 = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp3')]
	initMixer()
	file = random.choice(all_mp3)
	pmusic(file)
    #file = '/home/pi/Desktop/final_year_project/music/Kedam - Shy Girl.mp3'
    
except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
    stopmusic()
    print("\nPlay Stopped by user")
except Exception:
    print("unknown error")

print("Done")
