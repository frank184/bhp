import socket
import threading
import datetime

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

        target_file = open('not_found.html', 'r')
        response_body = target_file.read()
        target_file.close()
        
        body_length = len(response_body)
        timestamp = datetime.datetime.now().strftime("%a, %d %b %Y")

        response_headers = "HTTP/1.1 200 OK\n"
        response_headers += "Date: %s\n" % timestamp
        response_headers += "Content-Type: text/html\n"
        response_headers += "Content-Length: %d" % body_length


        response = response_headers + "\r\n\r\n" + response_body

        print "[*] Response:\n%s" % response
        
        client.send(response)
        client.close()
    

server = TCPServer("0.0.0.0", 9999)
