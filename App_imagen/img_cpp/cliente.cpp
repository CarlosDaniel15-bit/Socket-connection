#include <iostream>
#include <fstream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <cstring>

#define PORT 65432

int main() {
    int sock = 0;
    struct sockaddr_in serv_addr;
    const char* ip_servidor = "192.168.1.161"; // IP de la máquina receptora
    const char* nombre_archivo = "imagen_a_enviar.jpg";

    // 1. Verificar y abrir el archivo local en modo binario (rb)
    std::ifstream infile(nombre_archivo, std::ios::binary);
    if (!infile) {
        std::cerr << "Error: No se encontro la imagen '" << nombre_archivo << "'\n";
        return -1;
    }

    // 2. Crear y conectar el socket
    sock = socket(AF_INET, SOCK_STREAM, 0);
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);
    inet_pton(AF_INET, ip_servidor, &serv_addr.sin_addr);

    std::cout << "Conectando al servidor...\n";
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        std::cerr << "Fallo de conexion.\n";
        return -1;
    }

    std::cout << "Conexion establecida. Enviando imagen...\n";

    // 3. Leer la imagen y enviarla en bloques de 4096 bytes
    char buffer[4096];
    while (!infile.eof()) {
        infile.read(buffer, sizeof(buffer));
        std::streamsize bytes_leidos = infile.gcount(); // Cuenta los bytes reales leídos
        
        if (bytes_leidos > 0) {
            send(sock, buffer, bytes_leidos, 0);
        }
    }

    std::cout << "¡Imagen enviada completamente!\n";

    // 4. Cerrar recursos
    infile.close();
    close(sock);

    return 0;
}
