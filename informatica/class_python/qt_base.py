import os
import sys
from PyQt4 import QtGui
###############################################
class ventana1(QtGui.QWidget):    
    def __init__(self):
        super(ventana1, self).__init__()
        
        self.generar()
    def generar(self):
       self.label1 = QtGui.QLabel(self)    
       self.label1.move(20, 45); self.label1.setText('Nombre:')
       
       self.label2 = QtGui.QLabel(self)
       self.label2.move(20, 70); self.label2.setText('ID:')
        
       self.text1 = QtGui.QLineEdit(self)
       self.text1.move(150, 45)
       
       self.text2 = QtGui.QLineEdit(self)
       self.text2.move(150, 70)
       
       self.btn2 = QtGui.QPushButton('Aceptar >>', self)
       self.btn2.move(200, 150)
       self.btn2.clicked.connect(self.PresionaBoton2)        
       
       self.setGeometry(100, 100, 400, 200)
       self.setWindowTitle('ventana principal')
        
       self.show() #mostrar lo construido
        
    def PresionaBoton2(self):  
        pass   
    
###############################################
def main():    
    app = QtGui.QApplication(sys.argv)

    v1 = ventana1()
        
    sys.exit(app.exec_())
    
###############################################
if __name__ == '__main__':
    main()
    
