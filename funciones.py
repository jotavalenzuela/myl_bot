import re
import sql_worker
from sqlalchemy import *
import pandas as pd
import telebot
from telebot.types import *


engine = create_engine('mysql://root:unapassquenoseteolvidepoaweonao123.@35.223.9.17/myldb')

connection = engine.connect()

text_responses = {
	'welcome' :
		u'Hola {username}!\n\n'
		u'En este bot puedes hacer las siguientes cositas relacionadas con el TCG Mitos y Leyendas :3 \n\n'
		u'Revisar cartas: puedes buscar cartas con el comando /ver_cartas y el nombrde de la carta que busques o el codigo coleccionista (ES = espada sagrada HE = helenica DR = Dominios de RA HD = Hijos de Daana)\nEjemplos: /ver_cartas rey arturo pendragon /ver_cartas ES001 (WORK IN PROGRESS)\n\n'
		u'Armar mazos: puedes agregar cartas a un mazo con el comando /armar_mazo para consultarlo o compartir la lista de cartas de forma privada o publica! (WORK IN PROGRESS)\n\n'
		u'Ver mis mazos: con este comando /ver_mis_mazos puedes listar los mazos que tengas para obtener el id y poder compartirlo ;) (WORK IN PROGRESS)\n\n'
}

def listtostring(original_list):
	final_string = ""
	for index in original_list:
		final_string += index
	return final_string

def welcome(message, bot):
	bot.reply_to(message, text_responses['welcome'].format(username=message.chat.username))
	pass

def ver_cartas(message, bot):
	#leer la carta ingresada
	regex_carta = "(?<=ver_cartas ).*"
	carta_a_buscar = re.findall(regex_carta, message.text)
	carta_a_buscar = listtostring(carta_a_buscar)
	imagen_carta = sql_worker.busqueda_por_nombre_carta(connection, carta_a_buscar)
	if imagen_carta:
		bot.reply_to(message, "link provisorio de imagen de la carta... " + str(imagen_carta))
		pass
	else:
		bot.reply_to(message, "UPS!... Esa carta no existe :( (WORK IN PROGRESS : Dar sugerencia de posible carta a buscar)")
		pass
	#falta hacer la consulta a la base de imagenes?
	pass

def armar_mazo(message, bot):
    mazo = pd.DataFrame(columns=['carta', 'cantidad'])
    bot_async = telebot.AsyncTeleBot("1077001880:AAHmY_d_jkl6fQ3uAX8NqgnZOjz3VSdeGJA")
    task = bot_async.get_me()
    print("test armado de mazo")
    while mazo['cantidad'].sum() < 49:
        bot.reply_to(message, "llevas " + str(mazo['cantidad'].sum()) + " cartas... recuerda son 49 (sin contar oro inicial)")
        #print de pregunta de cartas
        forzar_respuesta = types.ForceReply(selective=False)
        bot_async.send_message(message.chat.id, "favor ingresa el nombre de la carta que quieres agregar al mazo: ",reply_markup=forzar_respuesta)
        #print de cantidad de cartas
        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn1 = types.KeyboardButton('0')
        itembtn2 = types.KeyboardButton('1')
        itembtn3 = types.KeyboardButton('2')
        itembtn4 = types.KeyboardButton('3')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
        bot_async.send_message(message.chat.id, "cuantas copias de [insertar nombre de carta] (0 para arrepentirse):", reply_markup=markup)
        result = task.wait()
        print(result)
        pass
    print(mazo)
    pass
