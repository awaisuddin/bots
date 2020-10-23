import os
import time
import random
import send2trash
import time
from datetime import datetime
from IAPIbotAwaZ import Bot
from os import listdir
from os.path import isfile, join
from random import randint
import requests as req

i=0
bot = Bot() 
PhotoPath = "C:/PythonBots/Instagram/res/jarvis.awazcafe" # Change Directory to Folder with Pics that you want to upload
IGUSER = "jarvis.awazcafe" 
PASSWD = "z78692969" 
#PhotoHashtag
IGCaption = " "
os.chdir(PhotoPath)
ListFiles = sorted([f for f in listdir(PhotoPath) if isfile (join(PhotoPath, f))])



while(1):
    now = datetime.now()
    dtcode = now.strftime("%H%M")
    photo = ListFiles[i]
    print("Progress :" + str([i + 1]) + " of " + str(len(ListFiles)))
    print("Now Uploading this photo to instagram: " + photo)
    print("Time =", dtcode)
    bot.login(username=IGUSER,password=PASSWD)
    bot.upload_photo(photo,caption=IGCaption)
    send2trash.send2trash(photo+str("REMOVE_ME"))
    r = req.get('https://maker.ifttt.com/trigger/awazcafe/with/key/fjUKTebijTWWbwEXB8-_kjolCPuTvBhASMRAIPeHJP-')
    time.sleep(43200)
    i=i+1
    time.sleep(20)



