#funciones pendientes
##menu de comandos bot
###ver carta por codigo o nombre
###agregar mazo
###ver cartas de mazo de otros users
###arrojar estadisticas de mazos segun id?
### ver mis mazos guardados


import telebot
import sql_worker
import re

def listtostring(original_list):
	final_string = ""
	for index in original_list:
		final_string += index
	return final_string

def welcome(message):
	bot.reply_to(message, "hola " + message.chat.username + " que paaaaaaaaaaaaaaaaaaaaaaaaaaaasa")
	pass

def ver_cartas(message):
	search_card = "(?<=ver_cartas ).*"
	card = re.findall(search_card, message.text)
	card = listtostring(card)
	bot.reply_to(message, "asi que queri buscar la carta ... " + str(card))
	pass

bot = telebot.TeleBot("1077001880:AAHmY_d_jkl6fQ3uAX8NqgnZOjz3VSdeGJA")

#lista de comandos
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	welcome(message)

@bot.message_handler(commands=['ver_cartas'])
def echo_all(message):
	ver_cartas(message)

@bot.message_handler(commands=['armar_mazo'])
def echo_all(message):
	print(message)
	bot.reply_to(message, "crea y guarda tu mazo para luego consultar las cartas que tiene")

@bot.message_handler(commands=['ver_mis_mazos'])
def echo_all(message):
	print(message)
	bot.reply_to(message, "listar los mazos de tu coleccion para poder compartirlos luego!")

bot.polling()
