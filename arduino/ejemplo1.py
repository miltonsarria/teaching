import serial




portName        = '/dev/ttyACM0' #verficar el nombre de su puerto
portRate        = 9600           #velocidad baudrate

sr=serial.Serial(portName, portRate) 

while True:
  sr.write(b'A')
  data=sr.readline()
  print(data)
  
  
'''
int led = 13;

void setup() {
   Serial.begin(9600);
   pinMode(led, OUTPUT);    
}

void loop() { 
  //sumar tres componentes frecuenciales
  int entrada;
  if(Serial.available()>0)
  {  
    entrada=Serial.read();   
       
    if (entrada==69)
    {
     digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
     delay(1000); 
    }
   
   if (entrada==65)
   {
     digitalWrite(led, LOW);   // turn the LED on (HIGH is the voltage level)
     delay(1000); 
   }
   
   Serial.println(entrada);

  }
}
'''
