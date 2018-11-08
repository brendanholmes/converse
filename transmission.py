import socket
import threading

class UdpReceive:
    def __init__(self, sourceIp):
        self.sourceIp = sourceIp
        self.UDP_PORT = 50001
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((sourceIp, self.UDP_PORT))
        self.buffer = []
        
        self.stopEvent = threading.Event()
        self.listenThread = threading.Thread(target=self.Listen, args=())
        self.listenThread.start()
    
    def Listen(self):
        while not self.stopEvent.is_set():
            data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
            self.buffer.append(data)
    
    def Read(self):
        self.buffer.pop()
        
    def __del__(self):
        self.stopEvent.set()
    
class UdpSend:
    def __init__(self, destIp):
        self.destIp = destIp
        self.UDP_PORT = 50001
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def Send(self, data):
        self.sock.sendto(data, (self.destIp, self.UDP_PORT))