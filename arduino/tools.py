#Milton Orlando Sarria
#USC - Cali
#some tools to test and do graphs.....
import serial
import threading
import time
import numpy as np
#import matplotlib
#matplotlib.use('agg')
import matplotlib.pyplot as plt
plt.ion()


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
###################################
#define a class to read from a file every X ms
class reader(threading.Thread):
      def __init__(self,datafile,tRead=100):
         threading.Thread.__init__(self) 
         self.fh=open(datafile,'r')
         self.rawdata   = '0\t0\n'
         self.tRead     = tRead/1e3
         self.read      = False
         self.num_data  = np.array([])
         self.dataCount = 0
      def run(self):
      
         for line in self.fh:
            while not(self.read):
               pass
            self.rawdata=line
            self.num_data=np.append(self.num_data,float(self.rawdata[:-1].split('\t')[1]))
            self.dataCount+=1
            time.sleep(self.tRead)
         self.fh.close()
         return
      
      def kill(self):
          self.read=False
          return
          
###################################   
class DynamicPlot():
    def __init__(self,ran_x=[],ran_y=[]):
        #if we know the x  and y  range, must provide two
        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None
        if len(ran_x)>1:
          self.min_x = ran_x[0]
          self.max_x = ran_x[1]
        if len(ran_y)>1:
          self.min_y = ran_y[0]
          self.max_y = ran_y[1]
        #Set up plot
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([],[],'k')
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        if not(self.min_x==None):
           self.ax.set_xlim(self.min_x, self.max_x)
        if not(self.min_y==None):
           self.ax.set_ylim(self.min_y, self.max_y)
        #grid on
        self.ax.grid()
    def on_running(self, xdata, ydata):
        #Update data (with the new _and_ the old points)
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        #Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        #We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

###################################
class GetDisplay(threading.Thread):
    '''
    Class to display data using two objects, a data object and a display object
    needs either a reader object or a comObj object, and a DynamicPlot object, optional an update time
    when it finishes, saves all colected data
    '''
    def __init__(self,comObj,DynPlotObj,update=0.5):
        threading.Thread.__init__(self) 
        self.comObj  = comObj
        self.DyPlot  = DynPlotObj
        self.update  = update
        self.stop    = False
        self.save    = True
        self.fileName= 'newfile.txt'
        self.buffersize=256
    def run(self):
        y_buffer  = np.zeros(self.buffersize)
        x_buffer  = np.zeros(self.buffersize)
        p_in = 0
        p_fin= 0
        timer= time.time()
        while not(self.stop):
            y_data=self.comObj.num_data
            x_data=np.arange(y_data.size)            
            if not(p_fin==self.comObj.dataCount):
               p_fin=self.comObj.dataCount
               if y_data.size>self.buffersize:
                   p_in=y_data.size-self.buffersize
                   y_buffer = y_data[p_in:]
                   x_buffer = x_data[p_in:]            
               else:
                   y_buffer = y_data[p_in:]
                   x_buffer = x_data[p_in:]
                   
            if (time.time()-timer)>self.update:
                self.DyPlot.on_running(x_buffer,y_buffer)
                timer=time.time()
        #if save, then save all data to a txt file
        if self.save:        
            X=np.vstack((x_data,y_data))
            X=X.transpose()
            np.savetxt(self.fileName, X, fmt='%5.5f', delimiter='\t', newline='\n', header='', footer='', comments='# ')
        return    
    
    def kill(self):
        self.comObj.kill()
        self.stop=True
        return


