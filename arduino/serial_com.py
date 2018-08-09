#Milton Orlando Sarria
#USC - Cali

from tools import comObj
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

#######################################################################      
portname        = '/dev/ttyACM0' #verficar el nombre de su puerto
portrate        = 9600           #velocidad baudrate
'''
#esta parte del codigo solo corre usando IPython
arduinoData     = comObj(portname,portrate)
figObj = DynamicPlot(ran_y=[-1,1]) #create figure to plot data
dispObj= GetDisplay(arduinoData,figObj,update=0.2)#create object to update plot with arduino data
arduinoData.start()    #iniciar el hilo que permite leer datos del arduino
dispObj.start()        #iniciar el hilo que permite mostrar los datos
arduinoData.read=True  #iniciar la lectura 
'''
#si esta en IPython, debe finalizar el objeto que muestra datos
#dispObj.kill()
#los datos quedan guardados en un archivo de texto 
#data=np.loadtxt('newfile.txt')
#plt.plot(data[:,0],data[:,1])
#plt.show()
#######################################################################

#### evaluar el codigo con un lector de texto
#codigo solo corre en IPython
readObj= reader('data.txt')
figObj = DynamicPlot(ran_y=[-1,1])
dispObj= GetDisplay(readObj,figObj)

readObj.start()
dispObj.start()
readObj.read=True


#######################################################################
#este codigo corre en consola o tambien en IPython

#definir una funcion para actualizar la grafica
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
    
#definir variables
readObj= reader('data.txt')
readObj.read=True

#para usar arduino comentar las lineas anteriores y quitar el comentario de las siguientes
#readObj     = comObj(portname,portrate)
#readObj.read=True  #iniciar la lectura 
  
fig = plt.figure()
ax  = fig.add_subplot(1,1,1)
ax.set_autoscaley_on(True)
ax.set_ylim(-1, 1)

readObj.start() #iniciar hilo para lectura de datos
ani = FuncAnimation(fig, update, interval=500)#, blit=True)
plt.show()

readObj.stop=True

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
