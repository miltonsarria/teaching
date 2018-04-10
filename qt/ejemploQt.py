
import os
import sys
from PyQt4 import QtGui

###########################################################################################   
class datos(object):
    def __init__(self):
        self.nombre=''
        self.apellido=''
        self.edad=0
        self.cargo=''
#objeto=datos()
##################################################################
class ventana1(QtGui.QWidget):    
    def __init__(self,objeto):
        super(ventana1, self).__init__()
        
        self.initUI()
        self.objeto=objeto

        
    def initUI(self):      

        self.btn = QtGui.QPushButton('Borrar datos: ', self)
                     #columna, fila
        self.btn.move(20, 10)
        self.btn.clicked.connect(self.borrarDatos)
        
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
        
        
        self.btn = QtGui.QPushButton('Siguiente >>', self)
                     #columna, fila
        self.btn.move(200, 150)
        self.btn.clicked.connect(self.mostrarv2)        
        
        self.setGeometry(300, 300, 400, 250)
        self.setWindowTitle('Recibir datos')
        
        self.show() #mostrar lo construido
        
    def borrarDatos(self):
         self.text1.setText('')
         self.text2.setText('')
         self.text3.setText('')
         self.text4.setText('')
         self.objeto.nombre=''
         self.objeto.apellido=''
         self.objeto.edad=0
         self.objeto.cargo=''
        
    def mostrarv2(self):
         self.objeto.nombre = self.text1.text()
         self.objeto.apellido = self.text2.text()
         self.objeto.edad = self.text3.text()
         self.objeto.cargo = self.text4.text()
         #self.ventana2.objeto=self.objeto
         
         self.close()
         self.secundario.show()  
###########################################################################################    
class ventana2(QtGui.QWidget):    
    def __init__(self,objeto):
        
        super(ventana2, self).__init__() 
        self.initUI()
        self.objeto=objeto
        
    def initUI(self):      

        self.btn = QtGui.QPushButton('mostrar Datos: ', self)                     
        self.btn.move(20, 10)
        self.btn.clicked.connect(self.mostrarDatos)
        
        self.label1 = QtGui.QLabel(self)
        self.label1.move(20, 45); self.label1.setText('Nombre:               ')
                
        self.label2 = QtGui.QLabel(self)
        self.label2.move(20, 70); self.label2.setText('Apellido:             ')
        
        self.label3 = QtGui.QLabel(self)
        self.label3.move(20, 95); self.label3.setText('Edad:       ')
        
        self.label4 = QtGui.QLabel(self)
        self.label4.move(20, 120); self.label4.setText('Cargo:             ')
        
        self.setGeometry(400, 400, 400, 250)
        self.setWindowTitle('mostrar datos')
        
        self.btn = QtGui.QPushButton('<< Atras', self)
                     #columna, fila
        self.btn.move(200, 150)
        self.btn.clicked.connect(self.mostrarv1)        
        

        
    def mostrarDatos(self):
     
        self.label1.setText('Nombre: '+ str(self.objeto.nombre)); 
        self.label2.setText('Apellido: '+ str(self.objeto.apellido))
        self.label3.setText('Edad: '+ str(self.objeto.edad))
        self.label4.setText('Cargo: '+ str(self.objeto.cargo))               
            
    def mostrarv1(self):
         self.close()
         self.principal.show()      
         
###########################################################################################    
        
def main():    
    data=datos()
    app = QtGui.QApplication(sys.argv)

    v1 = ventana1(data)
    v2 = ventana2(data)
    
        
    v1.secundario = v2    
    v2.principal = v1
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
