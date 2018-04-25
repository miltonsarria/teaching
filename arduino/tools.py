#Milton Orlando Sarria
#USC - Cali
#some tools to test and do graphs.....
import serial
import threading
import time
import numpy as np
import matplotlib.pyplot as plt



#######################################################################
#this will read whatever is in the serial port
class comObj(threading.Thread):
      def __init__(self,portName,portRate):
         threading.Thread.__init__(self)         
         self.raw_data  = '0\r\n'  #initial value
         self.dataCount = 0        #no data
         self.read      = False    #flag to read from serial port
         self.stop      = False    #flag to stop the whole process
         self.portName  = portName 
         self.portRate  = portRate        
         self.num_data  = np.array([])
         self.tRead     = 10/1e3
         
      def run(self):   
         #create the port instance
         self.serPort = serial.Serial(self.portName, self.portRate) 
         while not(self.stop):
          while self.read:                       
             self.raw_data     =self.serPort.readline()
             #if it only reads '\r\n' or less, there is no data
             if len(self.raw_data)>2:
                try:                   
                   self.num_data=np.append(self.num_data,float(self.raw_data[:-2]))
                   self.dataCount+=1
                except:
                   print('Error: no data')
         #if stop the process, close the port before leaving        
         self.serPort.close()
         return     
        
      def kill(self):
          self.read=False
          self.stop=True
          return
      def save(self,name_file):
          x_data=np.arange(self.num_data.size)
          X=np.vstack((x_data,self.num_data))
          X=X.transpose()
          np.savetxt(name_file, X, fmt='%5.5f', delimiter='\t', newline='\n', header='', footer='', comments='# ')
          return    
        


