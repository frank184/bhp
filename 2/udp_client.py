import socket

class UDPClient:
    def __init__(self, host, port):
        self.target_host = host
        self.target_port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.connected = False
    
    def send(self, data):
        return self.socket.sendto(data, (self.target_host, self.target_port))

    def receive(self):
        return self.socket.recvfrom(4096)
    

# create socket object
client = UDPClient("127.0.0.1", 80)

# send data
client.send("AAABBBCCC")

# receive data

data, addr = client.receive()

print data
