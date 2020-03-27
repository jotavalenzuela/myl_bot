from sqlalchemy import *

def busqueda_por_nombre_carta(connection, carta_a_buscar):
    #cur = connection.cursor()
    query = 'SELECT Imagen FROM `cartas` WHERE Nombre_Carta = \'{}\''.format(carta_a_buscar)
    result = connection.execute(query)
    print(str(result))
    var = list(result)
    out = [item for v in var for item in v]
    return(out)
    pass

def busqueda_por_id_carta(connection):
   # cur = connection.cursor()
    query = 'SELECT Nombre_Carta FROM `cartas` WHERE ID_Carta = 1276' #por mientras limit 1 de pues por cada token se elimina
    connection.execute(query)
    result = connection.fetchall()
    var = list(result)
    out = [item for v in var for item in v]
    return(out)
    pass
