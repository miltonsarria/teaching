import threading
import time


class misHilos(threading.Thread):
      def __init__(self, counter, name,sleep):
         threading.Thread.__init__(self)
         self.counter = counter
         self.name = name
         self.sleep = sleep
      def run(self):
         print "iniciar proceso ", self.name
         
         while self.counter > 0:
             time.sleep(self.sleep)
             print 'contador ', self.name, self.counter
             self.counter=self.counter-1
             
     
hilo1=misHilos(7,'hilo 1', 2)
hilo2=misHilos(10,'hilo 2', 3)

hilo1.start()
hilo2.start()
