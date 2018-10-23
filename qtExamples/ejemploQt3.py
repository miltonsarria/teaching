import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np
import threading
import time

##########################################################
##########################################################    
class secWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
                
        #Generar el entorno grafico
        self.setWindowTitle('Un titulo')
        self.sec_frame = QWidget()                
        
        self.button = QPushButton("Boton salir ocultar")
        self.connect(self.button, SIGNAL('clicked()'), self.closeEvent)
       
        vbox = QVBoxLayout()
        vbox.addWidget(self.button)     
        
        self.sec_frame.setLayout(vbox)
        self.setCentralWidget(self.sec_frame)
        
    
    #function do not destroy window, just hide it, and do not waste time ploting  
    def closeEvent(self):
        self.hide()
            
            
########################################################## 
########### main window frame ###########################       
##########################################################       
class AppForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle('Main: ventana principal')
        self.create_main_frame()
        self.secW  = secWindow(self.main_frame)
      
    
    #function when value in spinbox changes update values
    def valuechange(self):
        """Updates y=mx+b
        """
        
        return
    #function when close event.... ask yes or no? 
    def closeEvent(self, event):        
        reply = QMessageBox.question(self, 'Message',
            "Exit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            pass
        else:
            event.ignore()        
    def funcionBoton(self):
        pass
    def iniciar(self):
        '''shows result of adjusting image
        '''
        self.secW.show()        
        return
    #function apply layout    
    def create_main_frame(self):
        self.main_frame = QWidget()
        
        # Create the mpl Figure and FigCanvas objects. 
        # 5x4 inches, 100 dots-per-inch
        #
            
        self.label_pendiente = QLabel("un label: ")
        self.label_m = QLabel('otro label')
         

        self.label_intercepto = QLabel("Otro label: ")
        self.label_b = QLabel('otro')        
       
        self.adjust_button = QPushButton("Boton Ajustar")
        self.connect(self.adjust_button, SIGNAL('clicked()'), self.funcionBoton)
        Lspace1 = QLabel("\t\t\t")
        Lspace2 = QLabel("\t\t\t\t\t\t\t\t\t\t\t\t\t")
        Lspace3 = QLabel("\t\t\t\t\t\t\t\t\t\t\t\t\t")              
        self.l1 = QLabel("Min:")
        self.sp1 = QSpinBox()
        self.sp1.setMinimum(0)
        self.sp1.setMaximum(255)
        self.sp1.setValue(0)
        self.sp1.valueChanged.connect(self.valuechange)

        self.l2 = QLabel("Max:")
        self.sp2 = QSpinBox()
        self.sp2.setMinimum(0)
        self.sp2.setMaximum(255)
        self.sp2.setValue(255)
        self.sp2.valueChanged.connect(self.valuechange)

        self.l3 = QLabel("Niveles: ")
        self.e1_levels = QLineEdit()
        self.e1_levels.setText('6')
        self.l4 = QLabel("Filter size: ")
        self.e2_filter = QLineEdit()
        self.e2_filter.setText('5')
        
        self.mask_cb = QCheckBox("Mascara")
        self.mask_cb.setChecked(True)

        self.filter_cb = QCheckBox("Filtro")
        self.filter_cb.setChecked(True)
        
        self.start_button = QPushButton("Iniciar")
        self.connect(self.start_button, SIGNAL('clicked()'), self.iniciar)
                  
        #
        # Layout with box sizers
        # 
        hbox1 = QHBoxLayout()        
        for w in [  self.label_pendiente, self.label_m, self.label_intercepto, self.label_b]:
            hbox1.addWidget(w)
            hbox1.setAlignment(w, Qt.AlignVCenter)
            
        hbox2 = QHBoxLayout()    
        for w in [ self.l1, self.sp1, self.l2, self.sp2, self.l3, self.e1_levels, self.l4,
                self.e2_filter,self.mask_cb,self.filter_cb]:
            hbox2.addWidget(w)
            hbox2.setAlignment(w, Qt.AlignVCenter)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.adjust_button); hbox3.addWidget(Lspace2); 
        
        hbox4 = QHBoxLayout()          
        hbox4.addWidget(self.start_button); hbox4.addWidget(Lspace3);
         
        vbox = QVBoxLayout()


        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        
        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)
##########################################################
##########################################################
def main():
    app = QApplication(sys.argv)
    form = AppForm()
    form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    
    
    
    
#self.axes2.spines['right'].set_visible(False)

