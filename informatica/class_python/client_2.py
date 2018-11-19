#ipconfig /all

import socket

HOST = '172.16.193.149'  # El nombre del servidor o direccion IP  127.0.0.1
PORT = 65432        # El puerto usado por el servidor


continuar=True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  while continuar:
    data=input('yo digo: ')
    
    if data=='':
        continuar=False
    else:
        s.sendall(data.encode())
        rec_data = s.recv(1024)
        print(HOST+' dice: ', rec_data.decode('utf-8'))
    if not(continuar):
        s.sendall(b'Conexion cerrada por el cliente')
        
