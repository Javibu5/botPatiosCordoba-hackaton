# coding=utf-8
from application import bot

latitude = float('nan')
longitude = float('nan')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)
