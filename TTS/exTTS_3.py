import os

lang='-ves-la' #voice espanish latin america

#usando espeak
texto='hola mundo'                              #definimos el texto
comando= 'espeak' + " '" + texto + "' " + lang  #definimos el comando a ejecutar, no cambiar esta parte
os.system(comando)                              #ejecutar el comando


texto='1 2 3'                                   #un nuevo texto
comando= 'espeak' + " '" + texto + "' " + lang  #notar que es la misma linea de definicion de comando
os.system(comando)


texto='que dia es hoy?'                         #nuevo texto...
comando= 'espeak' + " '" + texto + "' " + lang
os.system(comando)
