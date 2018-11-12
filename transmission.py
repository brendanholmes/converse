import socket
import threading
import PIL as pillow
import cv2

#resource
#https://stackoverflow.com/questions/46912475/python-webcam-stream-over-udp-socket

class GetSingleVideoFrame:
    def GetFrame(self, videoStream):
        self.videoStream = videoStream
        frame = self.videoStream.read()
        cv2.imwrite(r'C:\Users\Brendan\Desktop\testcameraframe.png',frame)

class VideoServer:
    def __init__(self, destIp, videoStream):
        self.videoStream = videoStream
        self.destIp = destIp
        self.UDP_PORT = 50001
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.stopEvent = threading.Event()
        self.sendThread = threading.Thread(target=self.SendVideoLoop, args=())
        #self.sendThread.start()
    
    def SendVideoLoop(self):
        while not self.stopEvent.is_set():
            frame = self.videoStream.read()
            data = bytes(frame.flatten())
            size = len(data)
            for i in range(200):
                payload = data[i*size:(i+1)*size]
                self.sock.sendto (payload,(self.destIp, self.UDP_PORT))
            
    def Stop(self):
        self.stopEvent.set()
        
class VideoClient:
    def __init__(self, sourceIp):
        self.sourceIp = sourceIp
        self.UDP_PORT = 50001
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((sourceIp, self.UDP_PORT))
        self.dataBuffer = []
        self.frameBuffer = []
        self.stopEvent = threading.Event()
        self.sendThread = threading.Thread(target=self.SendVideoPacket, args=())
        self.listenThread.start()
    
    def ListenForVideoPackets(self):
        while not self.stopEvent.is_set():
            data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
            self.dataBuffer += data
            if len(self.dataBuffer) == 48000:
                self.frameBuffer.append(pillow.Image.open(self.dataBuffer));
            
    def Stop(self):
        self.stopEvent.set()
    
    def read(self): #lower case to match previous implementation
        return self.frameBuffer.pop()
    
class TestUdpServer:
    def __init__(self, destIp):
        self.destIp = destIp
        self.UDP_PORT = 50001
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

class TestUdpClient:
    def __init__(self, sourceIp):
        self.destIp = sourceIp
        self.UDP_PORT = 50001
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)