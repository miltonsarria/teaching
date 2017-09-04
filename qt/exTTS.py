import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
spanish=voices[20]
engine.setProperty('voice', spanish.id)
#engine.setProperty('voice', "spanish-latin-american")
engine.say("hola mundo")
engine.say("1 2 3")
engine.say("quiero comer")
engine.runAndWait()
