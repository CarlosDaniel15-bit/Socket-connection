import socket

HOST = '127.0.0.1' #Direccion IP servidor
PORT = 65432      #Puerto de servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #se abre/crea el socket
    s.bind((HOST, PORT)) #asociar el socket a un puerto
    s.listen() #poner el socket en escucha
    conn, addr = s.accept() #Aceptar la conexion
    with conn:
        print('Conectado desde', addr)
        while True:
            data = conn.recv(1024) #se reciben mientras haya datos
            if not data:
                break

            print('Recibido', repr(data)) #se muestra lo que se recibio

#SE EJECUTAN  EN CONSOLAS DIFERENTES
