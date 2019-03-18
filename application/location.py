# coding=utf-8
from application import bot

@bot.message_handler(content_types=['location'])
def handle_location(message):
	latitude = message.location.latitude
	longitude = message.location.longitude
	bot.reply_to(message, "{0}, {1}".format(latitude, longitude))