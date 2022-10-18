#coder : Bruno Perelli S. (Hackspawn)

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO
import os

#LED
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
# to use the function ffplay that reproduce a video file using ffplay
def ffplay():
    os.system("ffplay " + ' -fs ' + 'video.mp4' + ' -an -autoexit')
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: %s' % command)

    if command == 'hi':
       bot.sendMessage(chat_id, on(11) & off (13))
       bot.sendMesagge(chat_id, 'hola')
    elif command =='bye':
       bot.sendMessage(chat_id, off(11) & on(13))
    elif command =='video':
        bot.sendMessage(chat_id, ffplay())

bot = telepot.Bot('TELEGRAM_TOKEN_HERE')
bot.message_loop(handle)
print ('I am listening...')

while 1:
     time.sleep(10)
