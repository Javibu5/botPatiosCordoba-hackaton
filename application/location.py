# coding=utf-8
from application import bot
import math
import json
import requests

@bot.message_handler(content_types=['location'])
def handle_location(message):
	latitude = message.location.latitude
	longitude = message.location.longitude
	nombre, imagen = patiocercano(latitude, longitude)
	bot.reply_to(message, nombre)
	bot.reply_to(message, imagen)

def distance(lat1, long1, lat2, long2):
	dist = math.sqrt((lat1-lat2)**2 + (long1-long2)**2)
	print("dist:" + str(dist))
	return dist

def patiocercano(mylatitude, mylongitude):
	url = "http://b.patios.cordoba.es/api/v1/public/{locale}/json/pois_y_zonas"

	headers = {
		'cache-control': "no-cache"
	}

	response = requests.get(url)
	data = response.text
	parsed = json.loads(data)

	distanciaMinima = 999

	for x in range(0, 72):
		latitude = float(parsed['pois'][x]['lat'])
		longitude = float(parsed['pois'][x]['lng'])

		if distance(latitude, longitude, mylatitude, mylongitude) < distanciaMinima:
			nombre = parsed['pois'][x]['nombre']
			imagen = parsed['pois'][x]['imagen']
			distanciaMinima = distance(latitude, longitude, mylatitude, mylongitude)

	return nombre, imagen
