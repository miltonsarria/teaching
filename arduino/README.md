###Arduino and python###
This is an example to communicate arduino and python to display data adquired from sensors

To comunicate python with Arduino via serial port first install pySerial 

```python
pip install pyserial
```

source code can be found in https://github.com/pyserial/pyserial


Currently you need to execute the example using IPython
```python
[1]:run serial_com.py
```

to finish reading

```python
[2]: dispObj.kill()
```

by default you will get data stored in the file 'newfile.txt', if you want to change the name
before killing the process, you need to do this
        
```python
[3]:dispObj.fileName= 'myfile.txt'
```
