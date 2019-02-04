import socket
import gameclass
import pickle
from planszator import generujtablice
def sendboard(clientip, game):
    myip = "127.0.0.0"
    port = 1111
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind((myip, port))
    generujtablice(0,0,game, 1)
    data = pickle.dumps(game)
    serverSock.sendto(data, (port, clientip))
def getboard():
    myip = "127.0.0.0"
    port = 1111
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data, addr = clientSock.recvfrom(10240)
    return pickle.loads(data)
def sendlosclient(game):
    port = 1111
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock.sendto(game.scanforwin(), (game.serverip, port))
def sendlosserver(game, clientip):


    myip = "127.0.0.0"
    port = 1111
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind((myip, port))
    data = game.scanforwin()
    serverSock.sendto(data, (port, clientip))


def getlosclient():

    port = 1111
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data, addr = clientSock.recvfrom(10240)
    return data
def getlosserver():


    myip = "127.0.0.0"
    port = 1111
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind((myip, port))
    serverSock.setblocking(0)
    data, addr = serverSock.recvfrom(1024)
    return data