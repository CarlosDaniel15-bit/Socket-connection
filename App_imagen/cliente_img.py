import socket
import os

# Usamos la IP de tu máquina Linux Mint que venías manejando
HOST = '192.168.1.161' 
PORT = 65432
NOMBRE_ARCHIVO = 'imagen_a_enviar.jpg'

# Verificamos que la imagen realmente exista antes de intentar enviarla
if not os.path.exists(NOMBRE_ARCHIVO):
    print(f"Error: No se encontró el archivo '{NOMBRE_ARCHIVO}' en esta carpeta.")
else:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Conectando al servidor {HOST}:{PORT}...")
        s.connect((HOST, PORT))
        print("Conexión establecida. Enviando imagen...")

        # Abrimos la imagen en modo 'rb' (Read Binary)
        with open(NOMBRE_ARCHIVO, "rb") as file:
            while True:
                # Leemos la imagen en bloques de 4096 bytes
                bytes_leidos = file.read(4096)
                if not bytes_leidos:
                    break # Terminamos de leer el archivo
                
                # Enviamos el bloque por el socket
                s.sendall(bytes_leidos)

        print("¡Imagen enviada completamente!")
