import socket

HOST = 'localhost'  # Nombre del servidor, nombre propio (localhost)
PORT = 65432        # Puertos para escuchar (Puertos sin privilegios son > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Se ha conectado la direccion: ', addr)
        while True:
            data = conn.recv(1024) #recibir hasta 1024 bytes
            if not data:
                break            
            print('Datos recibidos desde el cliente: \n', data.decode('utf-8'))
            data=b'Hola luna'
            conn.sendall(data)
