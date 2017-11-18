#Milton Orlando Sarria
#USC - Cali

from tools import reader, DynamicPlot, GetDisplay, comObj


#######################################################################      
portname        = '/dev/ttyACM0' #remember to check the name of your port
portrate        = 9600
arduinoData     = comObj(portname,portrate)

################

figObj = DynamicPlot(ran_y=[-1,1]) #create figure to plot data
dispObj= GetDisplay(arduinoData,figObj,update=0.2)#create object to update plot with arduino data
arduinoData.start()    #start the thread for reading data from arduino
dispObj.start()        #start the thread to update plot with data
arduinoData.read=True  #set flag to read data from usb port as True

#to finish you have to execute the command
#dispObj.kill()
#if you want to display the data you jsut collected
#data=np.loadtxt('newfile.txt')
#plt.plot(data[:,0],data[:,1])
#plt.show()
#######################################################################

#### test code with serial reader
'''
readObj= reader('data.txt')
figObj = DynamicPlot(ran_y=[-1,1])
dispObj= GetDisplay(readObj,figObj)

readObj.start()
dispObj.start()
readObj.read=True

'''
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
