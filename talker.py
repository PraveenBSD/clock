from gtts import gTTS 
from datetime import datetime as dt
import os 
import time

def talk(text, lang = "en"):

    taskAudio = gTTS(text=text, lang=lang, slow=False) 
    taskAudio.save("talk.mp3") 
    
    os.system("afplay indian_railway.mp3") 
    os.system("afplay talk.mp3") 

while True:
    message = ""
    if dt.now().minute == 0:
        h = dt.now().hour
        if h == 8:
            message = ".  Good morning Praveen"
        if h == 22:
            message = ".  Good night Praveen"
        
        period = "A M"
        if h > 12:
            h = h - 12
            period = "P M"

        talk("Now the time is"+ str(h) + " " + period+ " " + message)
    time.sleep((59 - dt.now().minute)*60)
