#how to comunicate python with Arduino via serial port 
#first install pySerial 

#pip install pyserial

#source code can be found in https://github.com/pyserial/pyserial

import serial
import threading
import time
import matplotlib.pyplot as plt
import numpy as np


#######################################################################
#this will read whatever is in the serial port
class comObje(threading.Thread):
      def __init__(self,portName,portRate):
         threading.Thread.__init__(self)         
         self.data      = '0\r\n'  #initial value
         self.dataCount = 0        #no data
         self.read      = False    #flag to read from serial port
         self.stop      = False    #flag to stop the whole process
         self.portName  = portName 
         self.portRate  = portRate        
         
      def run(self):   
        #create the port instance
        self.serPort = serial.Serial(self.portName, self.portRate) 
        while not(self.stop):
          while self.read:                       
             self.data     =self.serPort.readline()
             #if it only reads '\r\n' or less, there is no data
             if len(self.data)>2:
                self.dataCount+=1
        #if stop the process, close the port before leaving        
        self.serPort.close()
        return     
      
      
#######################################################################      
portname        = '/dev/ttyACM0' #remember to check the name of your port
portrate        = 9600
num_samples     = 1000            
arduinoData     = comObje(portname,portrate)

################
X=np.array([]);        #empty array
arduinoData.start()    #start the thread for reading data
arduinoData.read=True  #flag to read data from usb port as True
hf = open('data.txt','w')
item=0;
for t in np.arange(num_samples):
     #stop and wait until data count increases     
     while item==arduinoData.dataCount:
         pass
     item =arduinoData.dataCount
     #conver data to float
     value=float(arduinoData.data[:-2]) #discard '\r\n'     
     line=str(item)+'\t'+str(value)+'\n'
     hf.write(line)
     X=np.append(X,value)
     
hf.close()
arduinoData.read=False #stop reading
arduinoData.stop=True  #stop the process   
plt.plot(X)
plt.show()

#######################################################################
#arduino code
'''
float angle = 0;
double value = 0;

void setup() {
   Serial.begin(9600);
}

void loop() { 
  
  value=sin(angle);
  Serial.println(value,5);
  angle+=0.0314;
  delay(100);  
}
'''


