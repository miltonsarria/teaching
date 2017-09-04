#!/usr/bin/env python
#sudo apt-get install mpg321
#pip install gtts

import os
from gtts import gTTS

texto = "1 2 3, hola mundo, que dia es hoy?"
tts=gTTS(text=texto, lang='es')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
         
         
