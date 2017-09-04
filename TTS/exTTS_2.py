#!/usr/bin/env python
#sudo apt-get install mpg321
#pip install gtts

#usando gtts
import os
from gtts import gTTS


texto = " hola mundo,1 2 3, que dia es hoy?"  #definimos el texto
tts=gTTS(text=texto, lang='es')               #se envia el texto a google
tts.save("good.mp3")                          #se guarda la respuesta en mp3
os.system("mpg321 good.mp3")                  #se reproduce el archivo mp3
         
         
