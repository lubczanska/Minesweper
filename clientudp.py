import socket
import json
def getboard():
    UDP_IP = "0.0.0.0"
    UDP_PORT = 5555

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    data, addr = sock.recvfrom(1024)
    zwracanie = {"tablica": data, "adress": addr}

    data = json.loads(data.decode())

    tab = data.get("tablica")

    return zwracanie


def sendwin(adrr):
    UDP_PORT = 5555
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP
    sock.sendto("ja".encode(), (adrr, UDP_PORT))

def getloss():
    UDP_IP = "0.0.0.0"
    UDP_PORT = 5555

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    sock.setblocking(0)

    try:
        data, addr = sock.recvfrom(1024)
        return 0
    except socket.error:
        return 1