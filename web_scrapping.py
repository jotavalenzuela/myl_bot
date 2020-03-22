import request
import wget
import os
#import shutil
#eg https://api.myl.cl/static/cards/19/064.png

dicc = []
enca = "https://api.myl.cl/static/cards/21/"
fin = ".png"
i = 99
while i != 350:
    carta = str(enca) +str(i) + str(fin)
    print(carta)
    saves = str(i)+ fin
    os.system('wget '+ carta + ' --no-check-certificate')
    #local_image_filename = wget.download(carta)
    #with open(saves, 'wb') as localfile:
    #    localfile.write(image.read())
    #    pass
    i = i + 1
    pass
