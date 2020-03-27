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
import funciones


bot = telebot.TeleBot("1077001880:AAHmY_d_jkl6fQ3uAX8NqgnZOjz3VSdeGJA")

#lista de comandos
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	funciones.welcome(message, bot)

@bot.message_handler(commands=['ver_cartas'])
def echo_all(message):
	funciones.ver_cartas(message, bot)

@bot.message_handler(commands=['armar_mazo'])
def echo_all(message):
	funciones.armar_mazo(message, bot)


@bot.message_handler(commands=['ver_mis_mazos'])
def echo_all(message):
	bot.reply_to(message, "listar los mazos de tu coleccion para poder compartirlos luego!")

bot.polling()
