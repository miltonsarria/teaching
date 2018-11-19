import socket

HOST = 'localhost'  # Nombre del servidor, nombre propio (localhost) 127.0.0.1
PORT = 65432        # Puertos para escuchar (Puertos sin privilegios de administrador son > 1023)

s=socket.socket()
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

print('Se ha conectado la direccion: ', addr)
continuar=True
while continuar:
        data = conn.recv(1024) #recibir hasta 1024 bytes
        print(str(addr)+'dice: ', data.decode('utf-8'))
        new_data=input('yo digo: ')
        if new_data=='':
            continuar=False
        else:
            conn.sendall(new_data.encode()	)
            
        if not(continuar):
           conn.sendall(b'conexion cerrada por el servidor:')
           
conn.close()
s.close()
