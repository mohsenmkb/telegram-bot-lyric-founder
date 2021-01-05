import time
import telebot
from googlesearch import search
from bs4 import BeautifulSoup
import requests

TOKEN = "YOUR TOKEN"
bot = telebot.TeleBot(token=TOKEN)

def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, "let's find some lyric")

@bot.message_handler(commands=['help']) # help message handler
def send_welcome(message):
    bot.reply_to(message, 'import with this format: \n singer name song name')

@bot.message_handler(func=lambda msg: msg.text is not None)
# lambda function finds messages with the '@' sign in them
# in case msg.text doesn't exist, the handler doesn't process it
def at_converter(message):
    query = message.text + ' lyrics genius'
    for j in search(query, tld="com", num=10, stop=1, pause=2): 
        html = j
        
    if 'genius' not in html:
        html = ''
    try:
        lyric='Produced by'
        while len(lyric) <= 30:
            res = requests.get(html)
            soup = BeautifulSoup(res.text,"lxml")
            body = soup.find_all('p')
            lyric = body[0].text
        bot.reply_to(message, lyric)
    except:
        bot.reply_to(message, 'the song or singer name is wrong')

while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)
