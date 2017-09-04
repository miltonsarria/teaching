import pyttsx

#usando pyttsx

engine = pyttsx.init()                          #se inicializa un objeto tipo pyttsx
voices = engine.getProperty('voices')           #optenemos la lista de voces
spanish=voices[20]                              #seleccionamos la 20, que es español
#20 spanish
#19 spanish-latin-am
engine.setProperty('voice', spanish.id)         #ponemos español como voz a usar
engine.say("hola mundo")                        #enivar el texto
engine.say("1 2 3")
engine.say("Que dia es hoy?")
engine.runAndWait()                             #ejecutar la sintesis 
