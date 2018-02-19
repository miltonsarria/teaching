import serial


portName        = '/dev/ttyACM0' #verficar el nombre de su puerto
portRate        = 9600           #velocidad baudrate

sr=serial.Serial(portName, portRate) 

while True:
  
  data=sr.readline()
  print(data)
  
  
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
}
'''
