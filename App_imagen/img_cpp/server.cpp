#include <iostream>
#include <fstream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <cstring>

#define PORT 65432

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);

    // 1. Crear configuración del socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) return -1;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt));
    
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    bind(server_fd, (struct sockaddr *)&address, sizeof(address));
    listen(server_fd, 3);

    std::cout << "Servidor listo. Esperando imagen en el puerto " << PORT << "...\n";
    new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen);
    
    std::cout << "Cliente conectado. Recibiendo datos...\n";

    // 2. Abrir archivo en modo binario para escribir (wb)
    std::ofstream outfile("imagen_recibida.jpg", std::ios::binary);
    if (!outfile) {
        std::cerr << "Error al crear el archivo de salida.\n";
        return -1;
    }

    char buffer[4096];
    int bytesRead = 0;
    
    // 3. Recibir fragmentos y escribirlos en el archivo hasta que el cliente cierre la conexión
    while ((bytesRead = read(new_socket, buffer, sizeof(buffer))) > 0) {
        outfile.write(buffer, bytesRead);
    }

    std::cout << "¡Imagen recibida y guardada exitosamente!\n";
    
    // 4. Cerrar todo
    outfile.close();
    close(new_socket);
    close(server_fd);

    return 0;
}
