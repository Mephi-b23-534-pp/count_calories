import telebot
from parser import *
#ну токен и токен что бубнить то
token = '6435325177:AAETrHUo3CP6J-rnxjN1B8NZhVCMwzbzjuU'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,message)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,"<b>Help</b> <em><u>information</u></em>",parse_mode='html')

@bot.message_handler(commands=['add'])
def start_message(message):
    



bot.infinity_polling()