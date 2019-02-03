import socket
from planszator import generujtablice
from gameclass import Gamesettings
import pickle
if __name__ == '__main__':
    nx = 10
    ny = 10
    n = 10
    HOST = '127.0.0.1'
    PORT = 1111
    client1 = '192.168.0.1'
    client2 = '192.168.0.2'

    game = Gamesettings(nx, ny, n, 91, 12, 16, 16)                          #stworzenie obiektu z parametrami gry
    data = pickle.load(game)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))

    s.sendto(data, (client1, PORT))
    s.sendto(data, (client2, PORT))



