#how to comunicate python with Arduino via serial port 
#first install pySerial 
#pip install pyserial

#source code can be found in https://github.com/pyserial/pyserial

import serial
import threading
import time
import matplotlib.pyplot as plt
import numpy as np



#this will read whatever is in the serial port
class comObje(threading.Thread):
      def __init__(self,serPort):
         threading.Thread.__init__(self)
         self.data = 0
         self.read = False
         self.kill = False
         self.serPort = serPort
      def run(self):      
        while not(self.kill):
        
          while self.read:
             self.data=float(self.serPort.readline())
      
      
#######################################################################      
porname='/dev/tty.usbserial' #remember to check the name of your port
puerto = serial.Serial('/dev/ttyACM2', 9600)
muestras=100            
comunicar = comObje(puerto)
X=();
comunicar.start()
for t in np.arange(muestras):
     comunicar.read=True
     value=comunicar.data
     X = np.append(X, value)     
     while value==comunicar.data:
        pass
     print value
comunicar.read=False
comunicar.kill=True     
plt.plot(X)
plt.show()
