#!/usr/bin/env python
#sudo apt-get install mpg321
#pip install gtts

#usando gtts
import os
from gtts import gTTS


texto = " Cepillo, zapato, cebolla"  #definimos el texto
tts=gTTS(text=texto, lang='es')               #se envia el texto a google
tts.save("audio_de_la_nube.mp3")                          #se guarda la respuesta en mp3
os.system("mpg321 audio_de_la_nube.mp3")                  #se reproduce el archivo mp3
         
         
