import socket
from planszator import generujtablice
from gameclass import Gamesettings
import pickle
if __name__ == '__main__':
    nx = 10
    ny = 10
    n = 10
    game = Gamesettings(nx, ny, n, 91, 12, 16, 16)                          #stworzenie obiektu z parametrami gry
