import os
import sys
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

##################################################################
class ventana1(QtGui.QWidget):    
    def __init__(self):
        super(ventana1, self).__init__()
        
        self.ajustarEntorno()
                
    def ajustarEntorno(self):      

        self.btn = QtGui.QPushButton('nombre boton: ', self)
        
        self.btn.clicked.connect(self.PresionaBoton)
        
        self.label1 = QtGui.QLabel(self)
        self.label1.setText('Nombre:')

        self.text1 = QtGui.QLineEdit(self)
             
        self.label2 = QtGui.QLabel(self)
        self.label2.setText('Apellido:')
        
        self.text2 = QtGui.QLineEdit(self)
                
        self.label3 = QtGui.QLabel(self)
        self.label3.setText('Edad:')
       
        self.text3 = QtGui.QLineEdit(self)
              
        self.label4 = QtGui.QLabel(self)
        self.label4.setText('Cargo:')
        
        self.text4 = QtGui.QLineEdit(self)
               
        
        self.btn2 = QtGui.QPushButton('Siguiente >>', self)
        
        self.btn2.clicked.connect(self.PresionaBoton2)        
        #uso de layoouts verticales y horizontales
        hbox = QHBoxLayout()        
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()
        for w in [self.label1,  self.label2,  self.label3,  self.label4]:
            vbox1.addWidget(w)
            vbox1.setAlignment(w, Qt.AlignVCenter)
            
        for w in [self.text1,  self.text2,  self.text3,  self.text4]:
            vbox2.addWidget(w)
            vbox2.setAlignment(w, Qt.AlignVCenter)
        
        vbox3.addWidget(self.btn); #vbox1.setAlignment(w, Qt.AlignVLeft)
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2) 
        vbox3.addLayout(hbox)
        vbox3.addWidget(self.btn2); #vbox1.setAlignment(w, Qt.AlignVRight)
                    
        self.setLayout(vbox3) 
        
        self.setGeometry(300, 300, 400, 250)
        self.setWindowTitle('Recibir datos')
        
        self.show() #mostrar lo construido
        
    def PresionaBoton(self):
         print('me presiono')
        
    def PresionaBoton2(self):
         print('soy boton 2 me presiono')

def main():    
      
    app = QtGui.QApplication(sys.argv)

    v1 = ventana1()
        
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()




