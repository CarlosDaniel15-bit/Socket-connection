using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace SocketTextoServidor
{
    class Program
    {
        public static string data = null;
        public static void Main(String[] args)
        {
            byte[] bytes = new Byte[1024];  
            
            // MODIFICACIÓN: En lugar de buscar el localhost, le decimos que escuche en cualquier IP de esta máquina
            IPAddress ipAddress = IPAddress.Any; 
            IPEndPoint localEndPoint = new IPEndPoint(ipAddress, 11000); 
            
            Socket listener = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            
            try
            {
                listener.Bind(localEndPoint); 
                listener.Listen(10); 
                
                Console.WriteLine("Esperando conexión en el puerto 11000...");

                while (true)
                {   
                    Socket handler = listener.Accept(); 
                    data = null;

                    while (true)
                    {
                        int bytesRec = handler.Receive(bytes); 
                        data += Encoding.ASCII.GetString(bytes, 0, bytesRec);
                        if (data.IndexOf("<EOF>") > -1) 
                        {
                            break;
                        }
                    }
                    Console.WriteLine("Texto recibido: " + data);
                    handler.Shutdown(SocketShutdown.Both);
                    handler.Close();
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }
    }
}
