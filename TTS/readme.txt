hay tres opciones
1) usar pyttsx
para este tiene que instalar el paquete pyttsx de la siguiente forma

activar su entorno usando source activate......
y luego
pip install pyttsx

2) usar la solucion de google que gtts
para esto usted debe instalar un paquete y un codec, tambien con su entorno activo

sudo apt-get install mpg321
pip install gtts

3) usar espeak 
que es el que usted estaba usando, en este caso no es necesario usar el espeak-python ya que se puede llamar directamente desde la aplicacion instalada en el sistema
para instalar espeak:

sudo apt-get install espeak


