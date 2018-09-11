#Milton Orlando Sarria
#USC - Cali
#visualizar datos provenientes de arduino de forma grafica
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import serial
import threading
import time


#######################################################################
#######################################################################
portname        = '/dev/ttyACM0' #verficar el nombre de su puerto
portrate        = 9600           #velocidad baudrate
#######################################################################
#######################################################################

#######################################################################      
#######################################################################      
#######################################################################      
#######################################################################      

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
        
#######################################################################      
#######################################################################      
#######################################################################      


def update(i):
    buffersize = 256
    y_b   = np.array([])
    x_b   = np.array([])
    if readObj.dataCount>0:    
       y_data=readObj.num_data
       x_data=np.linspace(0,readObj.dataCount*readObj.tRead,y_data.size)
       if y_data.size<buffersize:
          y_b=y_data
          x_b=x_data
       else:
          y_b=y_data[y_data.size-buffersize:]
          x_b=x_data[x_data.size-buffersize:]
   
    ax.clear()
    ax.plot(x_b,y_b) 
    
#definir el objeto que permite comunicacipn y tratamiento de datos provenientes de arduino
readObj     = comObj(portname,portrate)
readObj.read=True  #iniciar la lectura 
 
#inicializar la grafica
fig = plt.figure()
ax  = fig.add_subplot(1,1,1)
ax.set_autoscaley_on(True)
ax.set_ylim(-1, 1)

readObj.start() #iniciar hilo para lectura de datos
ani = FuncAnimation(fig, update, interval=500)
plt.show()

readObj.kill()

#######################################################################
#######################################################################
#######################################################################
#arduino code
'''
//sumar tres sinusoidales
float t  = 0;  //valor de la variable independiente
double value = 0;  //resultado que se va a transmitir al pc
int t_sample = 10; //tiempo de muestreo, en ms. Separacion entre muestras, cada cuanto tiempo
                   //se transmite una nueva muestra al pc
const float pi=3.141592;

void setup() {
   Serial.begin(9600);
}

void loop() { 
  //sumar tres componentes frecuenciales
  value=sin(2*pi*1*t)+0.7*sin(2*pi*2*t)+0.3*sin(2*pi*4*t);
  Serial.println(value,4);
  t=t+float(t_sample)/1000;
  delay(t_sample);  
}
'''
#######################################################################
'''
//generar una onda cuadrada sumando diferentes armonicos usando las series de Fourier
float t  = 0;  //valor de la variable independiente
double value = 0;  //resultado que se va a transmitir al pc
int t_sample = 10; //tiempo de muestreo, en ms. Separacion entre muestras, cada cuanto tiempo
                   //se transmite una nueva muestra al pc
const float pi=3.141592;
const float f = 2;
void setup() {
   Serial.begin(9600);
}

void loop() { 
  //sumar tres componentes frecuenciales
  float w;
  int MAX=4;

  if(t>5)   MAX=10;
  if(t>10)  MAX=20;
  if(t>15)  MAX=40;
  
  value=0;    
  for(int i=1;i<MAX;i+=2)
  {
   w=2*pi*f*i;
   value=value+2/(i*pi)*sin(w*t);
  }
    
  Serial.println(value,4);
  t=t+float(t_sample)/1000;
  delay(t_sample);  
}
'''
#######################################################################
'''
//generar una onda triangular sumando diferentes armonicos usando las series de Fourier
float t  = 0;  //valor de la variable independiente
double value = 0;  //resultado que se va a transmitir al pc
int t_sample = 10; //tiempo de muestreo, en ms. Separacion entre muestras, cada cuanto tiempo
                   //se transmite una nueva muestra al pc
const float pi=3.141592;
const float f = 2;
void setup() {
   Serial.begin(9600);
}

void loop() { 
  //sumar tres componentes frecuenciales
  float w;
  int MAX=3;

  if(t>5)   MAX=5;
  if(t>10)  MAX=8;
  if(t>15)  MAX=10;
  if(t>20)  MAX=50;
  
  value=0;    
  for(int i=1;i<MAX;i++)
  {
   w=2*pi*f*i;
   value=value+2/(pow(i,2)*pow(pi,2))*(cos(i*pi)-1)*cos(w*t);
  }
  value=2*value;
  Serial.println(value,4);
  t=t+float(t_sample)/1000;
  delay(t_sample);  
}

'''
