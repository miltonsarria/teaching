"""
Milton Orlando Sarria Paja
USC
Kinect and camera use
"""
import sys, os, random
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import cv2
import threading
import time
##
#sys.path.append('/usr/local/lib/python2.7/dist-packages/')
#import freenect

def read_img():
        file_name =  '/home/sarria/data/images_kinect/im3.npz'
        npzfile = np.load(file_name)
        img0 = (npzfile['arr_0']).astype(float)
        return img0
##########################################################
##########################################################
class kinect_cam():
    def __init__(self):
        self.isopen        = False
        self.rgb           = np.array([])
        self.depth         = np.array([])
        self.convert_rgb   = True
        self.convert_depth = True

    #function to get RGB image from kinect    
    def _get_video(self):
        self.rgb,_ = freenect.sync_get_video()
        if self.convert_rgb:
            self.rgb = cv2.cvtColor(self.rgb,cv2.COLOR_RGB2BGR)
        return 
    #function to get depth image from kinect
    def _get_depth(self):
        self.depth,_ = freenect.sync_get_depth()
        if self.convert_depth:        
            self.depth = self.depth.astype(np.uint8)
        return
    #function is open??
    def isOpened(self):
        data = freenect.sync_get_depth()
        if data is None:
            self.isopen  = False
            return False
        else:
            return True
            self.isopen  = True            
    #function read depth camera    
    def read(self):
        if self.isopen:
            self._get_depth()
            return self.depth
        else:
            return np.array([])
    #function read rgb camera
    def read_rgb(self):
        if self.isopen:
            self._get_video()
            return self.rgb
        else:
            return np.array([])
##########################################################
class capture(threading.Thread):
    def __init__(self,source=0,tRead=70):
      threading.Thread.__init__(self) 
      # Create the VideoCapture object and define default values
      self.cam    = cv2.VideoCapture(source)
      self.m      = 1.0
      self.b      = 0.0
      self.read   = True
      self.stop   = False
      self.tRead  = tRead/1e3
      self.window = None
      self.filterSize = 5
      self.ap_mask=True
      self.filter =True
      if not self.cam.isOpened():
        print "Video device or file couldn't be opened"
        exit()
      retval, img = self.cam.read()
      self.img_g   = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      self.img_rgb = img
      #
      self.mask = 255*np.ones(self.img_g.shape)     
      self.process()
      return
    #pre-process image
    def process(self):
        if self.ap_mask:
          self.img_g = self.mask - self.img_g
        self.img_g = self.img_g*self.m+self.b
        self.img_g[self.img_g<0]=0
        self.img_g[self.img_g>255]=255
        if self.filter:
           self.img_g = cv2.blur(self.img_g,(self.filterSize,self.filterSize))                
        return
        
    def run(self):
      #read from camera
      while True:
            while not(self.read):
                 pass
            retval, img = self.cam.read()
            self.img_g   = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            self.img_rgb = img
            #img=read_img()
            #
            self.process()           
            
            if not(self.window == None) :
                self.window.on_draw(self.img_g)
            time.sleep(self.tRead)           
            ###########
            if self.stop:
               break
      return 
    #function kill process  
    def kill(self):
       self.stop=True
       return
##########################################################
##########################################################    
class secWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        #Grid para graficar la imagen de forma apropiada
        self.X      = None
        self.Y      = None
        self.grid   = False
        self.showImg= False
        self.contour= True
        self.cmap   = 'jet'
        #Generar el entorno grafico
        self.setWindowTitle('Resultado')
        self.sec_frame = QWidget()                
        self.dpi = 100
        self.fig = Figure((8.0, 6.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.sec_frame)
        
        self.axes = self.fig.add_subplot(111)
        self.axes.set_autoscaley_on(True)
        self.axes.get_yaxis().set_visible(False)
        self.axes.get_xaxis().set_visible(False)
        self.axes.set_yticklabels([])
        self.axes.set_xticklabels([])
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.canvas)     
        
        self.sec_frame.setLayout(vbox)
        self.setCentralWidget(self.sec_frame)
    #function draws image including contour    
    def on_draw(self,img_g):
      """ Redraws image
      """
      if self.showImg:
        if not(self.grid):
           x = np.linspace(255, 0, img_g.shape[1])
           y = np.linspace(255, 0, img_g.shape[0])
           self.X, self.Y = np.meshgrid(x, y)
           self.grid=True
        
        self.axes.clear()
        if self.contour:
          self.axes.contour(self.X, self.Y,img_g, self.levels, colors='black')            
        self.axes.imshow(img_g,cmap=self.cmap, extent=[255,0,0, 255])            
        self.canvas.draw()
      return
    #function do not destroy window, just hide it, and do not waste time ploting  
    def closeEvent(self, event):
        self.showImg=False
        self.hide()
            
            
########################################################## 
############## main window frame #########################
##########################################################       
class AppForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle('Main: Modificar histograma')
        self.minV       = 0.0
        self.maxV       = 255.
        self.m          = 1.0
        self.b          = 0.0
            
        self.img_obj    = capture()
        self.img0       = self.img_obj.img_g
        self.img_obj.start() 
               
        self.create_main_frame()
        self.secW           = secWindow(self.main_frame)
        self.secW.levels    = 6
        self.img_obj.window = self.secW
        
        
        self.thirdW         = secWindow(self.main_frame)
        self.thirdW.cmap    = 'Greys'
        self.thirdW.contour = False
        self.timerStart     = False
        self.timer          = QTimer()
        self.timer.timeout.connect(self.iniciar_faces)
        
    #function update histogram using current image    
    def updateHist(self):        
        self.axes1.clear()
        self.axes1.axes.hist(self.img0.ravel(), 255, density=False, facecolor='g')            
        self.axes1.set_xlim(0, 255)
        self.canvas.draw()
    #function ubdate image in main frame using current image    
    def updateImg(self):
        self.axes2.clear()
        self.axes2.imshow(self.img0,cmap = 'jet', extent=[255,0,0, 255])    
        self.canvas.draw()  
    #function adjust parameters, apply mask, filter, slope, intercept, 
    #levels for contour plot.......           
    def adjustImg(self):
        """ Update image
        """
        self.img_obj.ap_mask=self.mask_cb.isChecked()
        self.img_obj.filter=self.filter_cb.isChecked()                          
        self.img_obj.m=self.m
        self.img_obj.b=self.b
        self.secW.levels= int(str(self.e1_levels.text()))    
        self.img_obj.filterSize =int(str(self.e2_filter.text()))

        time.sleep(0.070)
        self.img0   = self.img_obj.img_g       
        self.updateHist()
        self.updateImg()
        return
    #function when value in spinbox changes update values
    def valuechange(self):
        """Updates y=mx+b
        """
        self.minV = self.sp1.value()
        self.maxV = self.sp2.value()
        self.m=255./(self.maxV-self.minV)
        self.b=-(self.m*self.minV)
        self.label_m.setText(str(self.m))
        self.label_b.setText(str(self.b))
        return
    #function when close event.... ask yes or no? 
    def closeEvent(self, event):        
        reply = QMessageBox.question(self, 'Message',
            "Exit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.img_obj.stop=True
            self.secW.close()
            event.accept()
        else:
            event.ignore()        
    #function start the secondary window and show the image            
    def iniciar(self):
        '''shows result of adjusting image
        '''
        self.secW.showImg=True
        self.secW.show()        
        return
    def iniciar_faces(self):
        if not(self.timerStart):
            self.timer.start(70)
            self.timerStart = True
            self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            self.eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        gray    = self.img0
        imshow  = self.img0
        faces   = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            imshow = cv2.rectangle(imshow,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = imshow[y:y+h, x:x+w]
            eyes = self.eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
        if not(self.thirdW.showImg):
            self.thirdW.showImg = True
            self.thirdW.show()
        
        self.self.thirdW.on_draw(imshow)
        
    #function apply layout    
    def create_main_frame(self):
        self.main_frame = QWidget()
        
        # Create the mpl Figure and FigCanvas objects. 
        # 5x4 inches, 100 dots-per-inch
        #
        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        
        #
        self.axes1 = self.fig.add_subplot(121)
        self.axes1.set_autoscaley_on(True)
        self.axes1.grid(True) 
        self.updateHist()
      
        self.axes2 = self.fig.add_subplot(122)
        self.axes2.set_ylim(-1, 1)
        # Turn off tick labels
        self.axes2.get_yaxis().set_visible(False)
        self.axes2.get_xaxis().set_visible(False)
        self.axes2.set_yticklabels([])
        self.axes2.set_xticklabels([])
        self.updateImg()
        # Other GUI controls
        # 
                
        self.label_pendiente = QLabel("pendiente: ")
        self.label_m = QLabel(str(self.m))
         

        self.label_intercepto = QLabel("Intercepto: ")
        self.label_b = QLabel(str(self.b))        
       
        self.adjust_button = QPushButton("Ajustar")
        self.connect(self.adjust_button, SIGNAL('clicked()'), self.adjustImg)
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
        self.e2_filter.setText('7')
        
        self.mask_cb = QCheckBox("Mascara")
        self.mask_cb.setChecked(True)

        self.filter_cb = QCheckBox("Filtro")
        self.filter_cb.setChecked(True)
        
        self.start_button = QPushButton("Iniciar")
        self.connect(self.start_button, SIGNAL('clicked()'), self.iniciar)
        
        self.faces_button = QPushButton("Rostro")
        self.connect(self.faces_button, SIGNAL('clicked()'), self.iniciar_faces)
                  
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
        
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.faces_button); hbox5.addWidget(Lspace1);
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.canvas)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        
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

