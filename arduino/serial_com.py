#Milton Orlando Sarria
#USC - Cali

from tools import reader, DynamicPlot, GetDisplay, comObj


#######################################################################      
portname        = '/dev/ttyACM1' #remember to check the name of your port
portrate        = 9600
arduinoData     = comObj(portname,portrate)

################

figObj = DynamicPlot(ran_y=[-2,2]) #create figure to plot data
dispObj= GetDisplay(arduinoData,figObj,update=0.2)#create object to update plot with arduino data
arduinoData.start()    #start the thread for reading data from arduino
dispObj.start()        #start the thread to update plot with data
arduinoData.read=True  #set flag to read data from usb port as True

#to finish you have to execute the command
#dispObj.kill()

#######################################################################
#arduino code
'''
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
#### test code with serial reader
'''
readObj= reader('data.txt')
figObj = DynamicPlot(ran_y=[-1,1])
dispObj= GetDisplay(readObj,figObj)

readObj.start()
dispObj.start()
readObj.read=True
''' 




