import socket
import threading

class TCPServer:
    def __init__(self, bind_ip, bind_port):
        self.socket     = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind_ip    = bind_ip
        self.bind_port  = bind_port

        self.bind()
        self.listen()
    
    def bind(self):
        self.socket.bind((self.bind_ip, self.bind_port))

    def listen(self):
        self.socket.listen(5)
        
        print "[*] Listening on %s:%d" % (self.bind_ip, self.bind_port)

        while True:
            client, addr = self.socket.accept()

            print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

            handler_thread = threading.Thread(target=self.handler, args=(client,))
            handler_thread.start()
        self.socket.close()

    def handler(self, client):
        request = client.recv(1024)

        print "[*] Received:\n%s" % request

        response = "Hello World"

        client.send(response)
        client.close()
    

server = TCPServer("0.0.0.0", 9999)
