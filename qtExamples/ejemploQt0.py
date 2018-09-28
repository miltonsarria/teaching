import os
import sys
from PyQt4 import QtGui


##################################################################
class ventana1(QtGui.QWidget):    
    def __init__(self):
        super(ventana1, self).__init__()
        
        self.ajustarEntorno()
                
    def ajustarEntorno(self):      

        self.btn = QtGui.QPushButton('nombre boton: ', self)
                     #columna, fila
        self.btn.move(20, 10)
        self.btn.clicked.connect(self.PresionaBoton)
        
        self.label1 = QtGui.QLabel(self)
        self.label1.move(20, 45); self.label1.setText('Nombre:')

        self.text1 = QtGui.QLineEdit(self)
        self.text1.move(150, 45)
        
        
        self.label2 = QtGui.QLabel(self)
        self.label2.move(20, 70); self.label2.setText('Apellido:')
        
        self.text2 = QtGui.QLineEdit(self)
        self.text2.move(150, 70)
        
        self.label3 = QtGui.QLabel(self)
        self.label3.move(20, 95); self.label3.setText('Edad:')
       
        self.text3 = QtGui.QLineEdit(self)
        self.text3.move(150, 95)
        
        
        self.label4 = QtGui.QLabel(self)
        self.label4.move(20, 120); self.label4.setText('Cargo:')
        
        self.text4 = QtGui.QLineEdit(self)
        self.text4.move(150, 120)
        
        
        self.btn2 = QtGui.QPushButton('Siguiente >>', self)
                     #columna, fila
        self.btn2.move(200, 150)
        self.btn2.clicked.connect(self.PresionaBoton2)        
        
        
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('ventana principal')
        
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
    
