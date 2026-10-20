import socket

HOST = '127.0.0.1' #Direccion IP servidor
PORT = 65432 #Puerto de servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # crear socket
    s.connect((HOST, PORT)) #Conectarse a Asociar IP y puerto para enviar la info
    s.sendall(b'Mensaje de texto del cliente') #enviar informacion
print('Mensaje enviado')


#socket.SOCK_STREAM        <<< siginifca que es un socket basado en flujo
