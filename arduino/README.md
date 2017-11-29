###Arduino and python###
Este es un ejemplo que permite comunicar arduino y python
La idea es mostrar datos adquiridos de la lectura de sensores, pero en este caso se muestra solamente datos generados en el microcontrolador

inicialmente se debe instalar el modulo para comunicacion serial pySerial 

```python
pip install pyserial
```
El codigo fuente se puede encontrar en  https://github.com/pyserial/pyserial


se puede ejecutar en IPython
```python
[1]:run serial_com.py
```
al finalizar es necesario matar el objeto que grafica

```python
[2]: dispObj.kill()
```

o desde la consola

>>>python serial_com.py


Es posible guardar los datos en un archivo txt  'newfile.txt'
comObj.save('newfile.txt'):
