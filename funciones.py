import re
import sql_worker

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='127.0.0.1', database= 'myldb', user ='usr_tokendb', password = 'passdelostoken7172')
except Exception as e:
    print(e)
    raise

text_responses = {
	'welcome' :
		u'Hola {username}!\n\n'
		u'En este bot puedes hacer las siguientes cositas relacionadas con el TCG Mitos y Leyendas :3 \n\n'
		u'Revisar cartas: puedes buscar cartas con el comando /ver_cartas y el nombre de la carta que busques o el codigo coleccionista (ES = espada sagrada HE = helenica DR = Dominios de RA HD = Hijos de Daana)\nEjemplos: /ver_cartas rey arturo pendragon /ver_cartas ES001 (WORK IN PROGRESS)\n\n'
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
	pass
