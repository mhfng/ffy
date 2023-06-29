from flask import Flask
import telegram
import sched
import time
import os

app = Flask(__name__)
bot = telegram.Bot(token=os.environ.get('5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg'))

def send_message():
    chat_id = os.environ.get('373715044')
    message = 'Hello, this is a scheduled message!'
    bot.send_message(chat_id=chat_id, text=message)

def schedule_message():
    s.enter(3 * 60 * 60, 1, schedule_message)
    send_message()

s = sched.scheduler(time.time, time.sleep)
schedule_message()
s.run()
