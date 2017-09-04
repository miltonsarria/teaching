#sudo apt-get install mpg321
#pip install gtts
#os.system("google_speech -l es" +" 'Hola, como es su nombre?, bienvenido'")
import os
from gtts import gTTS
import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      
        self.btn = QtGui.QPushButton('Texto a voz: ', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.tts)
        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Convertir de texto a voz')
        self.show()
        
    def tts(self):
         texto = str(self.le.text())
         tts=gTTS(text=texto, lang='es')
         tts.save("good.mp3")
         os.system("mpg321 good.mp3")
         #os.system("google_speech -l es"+" '"+texto+"'")
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
