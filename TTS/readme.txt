hay tres opciones
1) usar pyttsx
para usar esta solucion se tiene que instalar el paquete pyttsx de la siguiente forma

activar su entorno usando source activate mypython
y luego
pip install pyttsx

2) usar la solucion de google que gtts
para usar la api de google se debe instalar el paquete gtts y un codec de audio, tambien con el entorno activo

sudo apt-get install mpg321
pip install gtts

3) usar espeak 
es posible instalarlo directamente como una aplicacion mas del sistema, y no es necesario usar el espeak-python ya que se puede llamar directamente desde la aplicacion instalada en el sistema

para instalar espeak:

sudo apt-get install espeak


