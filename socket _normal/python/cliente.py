import socket

# Coloca aquí la IP local de la computadora que tiene el Servidor (ej. '192.168.1.20')
HOST = 'PON_AQUI_LA_IP_DEL_SERVIDOR' 
PORT = 11000

# Se crea el socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT)) # Se conecta a la IP y puerto
        
        # El mensaje debe incluir <EOF> para que el servidor sepa que terminó
        mensaje = "Mensaje de texto del cliente Python<EOF>"
        
        # Se codifica a bytes en formato ASCII antes de enviarlo
        s.sendall(mensaje.encode('ascii'))
        
        print(f"Mensaje enviado con éxito a {HOST}")
        
    except Exception as e:
        print("Error al conectar. Verifica que el servidor esté corriendo y la IP sea correcta.")
        print(e)

#socket.SOCK_STREAM        <<< siginifca que es un socket basado en flujo
