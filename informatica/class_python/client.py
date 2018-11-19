import socket

HOST = 'localhost'  # El nombre del servidor o direccion IP  127.0.0.1
PORT = 65432        # El puerto usado por el servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hola, mundo')
    data = s.recv(1024)

print('Datos recibidos desde el servidor: \n', data.decode('utf-8'))
