import threading
import time


class misHilos(threading.Thread):
      def __init__(self, counter, name, dormir=10):
         threading.Thread.__init__(self)
         self.counter = counter
         self.name = name
         self.sleep = dormir
      def run(self):
         print("iniciar proceso ", self.name)
         
         while self.counter > 0:
             time.sleep(self.sleep)
             print('contador :',self.name, self.counter)
             self.counter=self.counter-1
             
     
hilo1=misHilos(7,'hilo 1')

hilo2=misHilos(10,'hilo 2', 3)

hilo1.start()
hilo2.start()
