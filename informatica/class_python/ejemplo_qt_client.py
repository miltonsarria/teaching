import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np
import threading
import time

##########################################################
##########################################################    
            
########################################################## 
########### main window frame ###########################       
##########################################################       
class ClientForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle('Main: ventana principal cliente')
        self.create_main_frame()
    #function when close event.... ask yes or no? 
    def closeEvent(self, event):        
        reply = QMessageBox.question(self, 'Message',
            "Exit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()        
        else:
            event.ignore()        

    #function apply layout, crear el entorno completo (lo visual)    
    def create_main_frame(self):
        self.main_frame = QWidget()
                    
        self.label_port = QLabel("Puerto: ")
        self.label_server = QLabel("Servidor: ")        
        self.edit_port    = QLineEdit()
        self.edit_server  = QLineEdit()        
        self.start_button = QPushButton("Conectar a servidor")
        self.dialog =QTextEdit()
        self.edit_line  = QLineEdit()
        self.send_button = QPushButton("Enviar")
        
                        
        hbox1 = QHBoxLayout()        
        for w in [  self.label_port, self.edit_port, self.label_server, self.edit_server, self.start_button]:
            hbox1.addWidget(w)
            hbox1.setAlignment(w, Qt.AlignVCenter)
            
        hbox2 = QHBoxLayout()    
        for w in [ self.edit_line, self.send_button]:
            hbox2.addWidget(w)
            hbox2.setAlignment(w, Qt.AlignVCenter)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addWidget(self.dialog)
        vbox.addLayout(hbox2)

        
        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)
##########################################################
##########################################################
def main():
    app = QApplication(sys.argv)
    form = ClientForm()
    form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    
    
    
    
#self.axes2.spines['right'].set_visible(False)

