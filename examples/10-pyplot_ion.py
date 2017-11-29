import sys
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
 
import numpy as np
import threading
import time


class dataObj(threading.Thread):
      def __init__(self):
        threading.Thread.__init__(self)          
        self.stop       = False
        self.buffersize = 256
        self.Ts         = 0.02
        self.y_buffer   = np.array([])
        self.x_buffer   = np.array([])
        self.count      = 0
          
      def run(self):
        timer= time.time()
        while not(self.stop):
              while (time.time()-timer)<self.Ts:
                 pass
              n=self.count
              y_data=np.sin(2*np.pi*n*self.Ts)
              x_data=n*self.Ts
              if n<self.buffersize:
                 self.y_buffer=np.append(self.y_buffer,y_data)
                 self.x_buffer=np.append(self.x_buffer,x_data)
                 
                 self.y_buffer[n]=y_data
                 self.x_buffer[n]=x_data
              else:
                 self.y_buffer=np.append(self.y_buffer[1:],y_data)
                 self.x_buffer=np.append(self.x_buffer[1:],x_data)
              self.count=n+1
              timer=time.time()
        return

class callTimer(threading.Thread):
      def __init__(self,obj,data,timer):
        threading.Thread.__init__(self)          
        self.stop = False
        self.obj  = obj
        self.data = data
        self.Ts   = timer
      def run(self):
        timer= time.time()
        while not(self.stop):
              while (time.time()-timer)<self.Ts:
                 pass
              self.obj.data=self.data.y_buffer
              self.obj.run() 
              timer=time.time()
        return
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'Ejemplo usando pyplot'
        self.width = 640
        self.height = 400
        self.data=dataObj()
        self.initUI()
        
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
         
        self.m = PlotCanvas(self, width=5, height=4)
        self.m.move(0,0)
        self.updatePlot=callTimer(self.m,self.data,0.2)
                 
        button = QPushButton('Iniciar', self)
        button.setToolTip('plot')
        button.move(500,350)
        button.resize(90,30)
        button.clicked.connect(self.buttonClicked)
   
        self.show()
    def buttonClicked(self):
        if self.data.count==0:
           self.data.start()
           self.updatePlot.start()

        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Seguro que quiere salir?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.data.stop=True
            self.updatePlot.stop=True
            event.accept()
        else:
            event.ignore()        
            
 
class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        self.data = np.array([]);
        self.ts=0.2
        self.stop = False
        self.ax = self.figure.add_subplot(111)
        self.run()
 
    def run(self):
     
        
        self.ax.clear()
        self.ax.plot(self.data, 'r-')
        self.ax.set_title('Ejemplo')
        self.draw()
     
              
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
