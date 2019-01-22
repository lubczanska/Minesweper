import socket
import json
from planszator import generujtablice


def distributetable(tab, addr1, addr2):
    data = json.dumps({"tablica": tab})
    UDP_PORT = 5555
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP
    sock.sendto(data.encode(), (addr1, UDP_PORT))
    sock.sendto(data.encode(), (addr2, UDP_PORT))

def showlooser(addr):
    UDP_PORT = 5555
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP
    sock.sendto("lost".encode(), (addr, UDP_PORT))

def getwinner(addr1, addr2):
    UDP_IP = "0.0.0.0"
    UDP_PORT = 5555

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        if addr == addr1:
            showlooser(addr2)
            break
        if addr == addr2:
            showlooser(addr1)
            break

if __name__ == '__main__':


    adressclienta1 = "192.168.0.1"
    adressclienta2 = "192.168.0.1"
    tab = generujtablice(30, 15, 15, 0, 0)
    distributetable(tab, adressclienta1, adressclienta2)
    getwinner(adressclienta1, adressclienta2)


