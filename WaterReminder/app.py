#------------------>Drink water Reminder<-------------------#

import time
from gtts import gTTS
import schedule
from plyer import notification
import playsound
import os

#--------------->Generating Drink Water Sound<-----------------------------#

text = "Drink Water now, Stay Hydrated"

def water_break():
    tts = gTTS(text=text, lang='en')
    fn = "water.mp3"
    tts.save(fn)
    notification.notify(message=text, title="Drink Water", timeout=5)
    playsound.playsound(fn) #Gives audio message
    if (os.path.exists(fn)):
        os.remove(fn)

schedule.every(15).seconds.do(water_break)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except KeyboardInterrupt:
    print("Shutting down")