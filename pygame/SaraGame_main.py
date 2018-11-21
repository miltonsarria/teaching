import pygame
import sys, os, random
import numpy as np
import cv2
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
import freenect
import imutils
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# Define some colors
from juego import *


#######################################
#class AppForm(QMainWindow):
class AppForm(QWidget):
    def __init__(self, game, parent=None):
        super(AppForm, self).__init__()
        #QMainWindow.__init__(self, parent)
        self.setWindowTitle('Main: ventana principal')
        self.create_main_frame()
        self.game = game
    def closeEvent(self, event):        
        reply = QMessageBox.question(self, 'Message',
            "Exit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.game.stop=True
            event.accept() 
        else:
            event.ignore()  
                  
    def create_main_frame(self):
        self.main_frame = QWidget()
        self.l1 = QLabel("Nombre del jugador: ")
        self.e1 = QLineEdit()
        self.e1.setText('')
   
        self.l2 = QLabel("Edad: ")
        self.e2 = QLineEdit()
        self.e2.setText('')
        self.start_button = QPushButton("Iniciar")
        self.connect(self.start_button, SIGNAL('clicked()'), self.iniciar)
        vbox = QVBoxLayout()
        for w in [self.l1,self.e1,  self.l2,  self.e2,  self.start_button]:
            vbox.addWidget(w)
            vbox.setAlignment(w, Qt.AlignVCenter)
        
        #self.main_frame.setLayout(vbox)
        #self.setCentralWidget(self.main_frame)
        self.setLayout(vbox) 
        
        self.setGeometry(300, 300, 400, 450)
        self.show() #mostrar lo construido   
    def iniciar(self):
        #self.close()
        if self.game.stop:
            self.game.start()
            
        else:
            self.game.doneSesion=False
            
        
def main():    
    
    game=mainGame(screen_width =  1200, screen_height = 800,N=10, image='Globo2.png')
    app = QApplication(sys.argv)
    form = AppForm(game)
    game.MainWindow=form
    
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()        
