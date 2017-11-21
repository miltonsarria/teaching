#Milton Orlando Sarria
#USC - Cali
#some tools to test and do graphs.....

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style
import numpy as np
import threading
import time



#######################################################################
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
   
obj=dataObj()
obj.start()

fig = plt.figure()
ax  = fig.add_subplot(1,1,1)

def update(i):
    ax.clear()
    ax.plot(obj.x_buffer,obj.y_buffer) 


ani = FuncAnimation(fig, update, interval=100)
#                    init_func=init, blit=True)
plt.show()

obj.stop=True

