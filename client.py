import socket
import pickle
import gameclass

def waitforboard():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 1111

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(10240) # buffer size is 1024 bytes
        return pickle.dump(data)
def getlos():


    UDP_IP = "127.0.0.1"
    UDP_PORT = 1111

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        sock.setblocking(0)
        data, addr = sock.recvfrom(1024)
        if data.decode() == "lost":
            return 2
        if data.decode() == "won":
            return 1
        else:
            return 0

def sendwin(game, string):
    UDP_IP = game.serverip
    UDP_PORT = 1111
    MESSAGE = string.encode()
    sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)  # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))