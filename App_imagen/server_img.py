import socket

HOST = '0.0.0.0'  # Escucha en todas las interfaces de red
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor listo. Esperando la imagen en el puerto {PORT}...")

    conn, addr = s.accept()
    with conn:
        print(f"Conexión entrante desde {addr}")
        
        # Abrimos un archivo nuevo en modo 'wb' (Write Binary)
        with open("imagen_recibida.jpg", "wb") as file:
            print("Recibiendo datos...")
            while True:
                # Recibimos los datos en bloques de 4096 bytes
                datos = conn.recv(4096)
                if not datos:
                    break # Si ya no hay datos, salimos del ciclo
                
                # Escribimos los bytes recibidos en el archivo
                file.write(datos)
                
        print("¡Imagen recibida y guardada exitosamente!")
