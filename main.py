from klikato import eventuser
import time
from planszator import generujtablice, generujpusta
from printplansza import printplanszeszybko
from gameclass import Gamesettings
import pygame
nx = 16
ny = 16
n = 4

game = Gamesettings(nx, ny, n, 30, 30, 16, 16)




tab = generujpusta(game.nx, game.ny)
pygame.init()

screen = pygame.display.set_mode((game.windowsizex, game.windowsizey))

running = 1

fclick = 1
while running == 1:
    for a in range(nx):
        for b in range(ny):

            printplanszeszybko(tab, a, b, screen, game)




    running = game.scanforwin(tab)
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            tab = eventuser(event, tab, fclick, game)
            fclick = 0
        if event.type == pygame.QUIT:
            running = 0

    pygame.display.flip()
screen.fill((50,50,50))
pygame.display.flip()
time.sleep(5)
print("wygrales")
