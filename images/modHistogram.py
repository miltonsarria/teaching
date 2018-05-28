"""
Milton Orlando Sarria Paja
USC

"""
import sys, os, random
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import cv2

class AppForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle('Modificar histograma')
        self.m      = 1.0
        self.b      = 0.0
        self.minV   = 0.0
        self.maxV   = 255.
        
        self.create_main_frame()
      
        self.read_img()
        self.on_draw()

    def read_img(self):

        file_name =  '/home/sarria/data/images_kinect/im2.npz'
        npzfile = np.load(file_name)
        self.img0 = (npzfile['arr_0']).astype(float)
        mask = 255*np.ones(self.img0.shape)
        self.img0 = mask - self.img0
        self.img0 = cv2.blur(self.img0,(7,7))    
                 
        self.img1 = self.img0*self.m+self.b
         
               
    def on_draw(self):
        """ Redraws the histogram
        """
       
        self.img1 = self.img0*self.m+self.b
        self.img1[self.img1<0]=0
        self.img1[self.img1>255]=255
        
        # clear the axes and redraw the plot
        #
        self.axes.clear()        
        self.axes.hist(self.img1.ravel(), 255, density=False, facecolor='g')
        self.axes.grid(True)
        self.axes.set_xlim(0, 255)
        self.canvas.draw()      
        
    def valuechange(self):
        """Updates y=mx+b
        """
        self.minV = self.sp1.value()
        self.maxV = self.sp2.value()
        self.m=255./(self.maxV-self.minV)
        self.b=-(self.m*self.minV)
        self.label_m.setText(str(self.m))
        self.label_b.setText(str(self.b))
           
    def closeEvent(self, event):        
        reply = QMessageBox.question(self, 'Message',
            "Exit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
                
    def show_result(self):
        '''shows result of adjusting image
        '''
        levels  = 10
        x = np.linspace(255, 0, self.img0.shape[1])
        y = np.linspace(255, 0, self.img0.shape[0])

        X, Y = np.meshgrid(x, y)
        
        plt.figure(1)
        plt.subplot(121)
        contours = plt.contour(X, Y, self.img0, levels, colors='black')
        plt.imshow(self.img0, extent=[255,0,0, 255])
        plt.title('Original')

        plt.subplot(122)
        contours = plt.contour(X, Y, self.img1, levels, colors='black')
        plt.imshow(self.img1, extent=[255,0,0, 255])
        plt.title('Ajuste')
        
        plt.show()
    def create_main_frame(self):
        self.main_frame = QWidget()
        
        # Create the mpl Figure and FigCanvas objects. 
        # 5x4 inches, 100 dots-per-inch
        #
        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        
        # Since we have only one plot, we can use add_axes 
        # instead of add_subplot, but then the subplot
        # configuration tool in the navigation toolbar wouldn't
        # work.
        #
        self.axes = self.fig.add_subplot(111)
        self.axes.set_autoscaley_on(True)
        self.axes.set_ylim(-1, 1)

        # Other GUI controls
        # 
                
        self.label_pendiente = QLabel("pendiente: ")
        self.label_m = QLabel(str(self.m))
         

        self.label_intercepto = QLabel("Intercepto: ")
        self.label_b = QLabel(str(self.b))        
       
        self.draw_button = QPushButton("Ajustar")
        self.connect(self.draw_button, SIGNAL('clicked()'), self.on_draw)
               
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

        self.show_button = QPushButton("Mostrar")
        self.connect(self.show_button, SIGNAL('clicked()'), self.show_result)
                  
        #
        # Layout with box sizers
        # 
        hbox1 = QHBoxLayout()        
        for w in [  self.label_pendiente, self.label_m, self.label_intercepto, self.label_b,
                   self.draw_button]:
            hbox1.addWidget(w)
            hbox1.setAlignment(w, Qt.AlignVCenter)
            
        hbox2 = QHBoxLayout()    
        for w in [ self.l1, self.sp1, self.l2, self.sp2,self.show_button]:
            hbox2.addWidget(w)
            hbox2.setAlignment(w, Qt.AlignVCenter)

      
        vbox = QVBoxLayout()
        vbox.addWidget(self.canvas)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        
        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)


def main():
    app = QApplication(sys.argv)
    form = AppForm()
    form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
