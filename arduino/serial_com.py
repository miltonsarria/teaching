#Milton Orlando Sarria
#USC - Cali
#how to comunicate python with Arduino via serial port 
#first install pySerial 

#pip install pyserial

#source code can be found in https://github.com/pyserial/pyserial

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
#### test code with serial reader
'''
readObj= reader('data.txt')
figObj = DynamicPlot(ran_y=[-1,1])
dispObj= GetDisplay(readObj,figObj)

readObj.start()
dispObj.start()
readObj.read=True
 
'''



