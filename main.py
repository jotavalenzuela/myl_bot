#funciones pendientes
##menu de comandos bot
###ver carta por codigo o nombre
###agregar mazo
###ver cartas de mazo de otros users
###arrojar estadisticas de mazos segun id?
### ver mis mazos guardados


import telebot

bot = telebot.TeleBot("1077001880:AAHmY_d_jkl6fQ3uAX8NqgnZOjz3VSdeGJA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "hola jake puto queri consultar cartas maldito qlo?")

bot.polling()
