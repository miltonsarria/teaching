#Milton Orlando Sarria
#USC - Cali
#visualizar datos provenientes de arduino en la consola

import serial

portName        = '/dev/ttyACM0' #verficar el nombre de su puerto en windows sw usa COM1 o COM2....
portRate        = 9600           #velocidad (baudrate)

sr=serial.Serial(portName, portRate)

#iniciar un ciclo infinito que lea los datos que aparecen en el puerto serial
while True:
  data=sr.readline()
  print(data)

#el siguiente codigo se puede copiar y pegar en el IDE de arduino para luego transmitirlo al chip

'''
float t  = 0;  //valor de la variable independiente
double value = 0;  //resultado que se va a transmitir al pc
int t_sample = 500; //tiempo de retardo, en ms. Separacion entre muestras
const float pi=3.141592;

void setup() {
   Serial.begin(9600);
}

void loop() { 
  //Calcular un valor usando una funcion matematica y transmitirlo al pc
  value=sin(2*pi*0.1*t);
  Serial.println(value,4);
  t=t+float(t_sample)/1000;
  delay(t_sample);  
}
'''
