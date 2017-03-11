import socket

class TCPClient:
    def __init__(self, host, port):
        self.target_host = host
        self.target_port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def connect(self):
        self.socket.connect((self.target_host, self.target_port))
        self.connected = True
        return self.connected
    
    def send(self, data):
        self.socket.send(data)
        return self.socket.recv(4096)

    def close(self):
        self.socket.close()
    

# create socket object
client = TCPClient("www.google.com", 80)

# connect the client
client.connect()

# send some data
response = client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

print response

client.close()
