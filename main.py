from klikato import eventuser
from odkrywane import scanforwin
from planszator import generujtablice, generujpusta
from printplansza import printplanszeszybko
from gameclass import Gamesettings
import pygame
nx = 16
ny = 16
n = 30

game = Gamesettings(nx, ny, n, 30, 30, 16, 16)




tab = generujpusta(game.nx, game.ny)
pygame.init()

screen = pygame.display.set_mode((game.windowsizex, game.windowsizey))

running = 1

fclick = 1
while running:
    for a in range(game.nx):
        for b in range(game.ny):

            printplanszeszybko(tab, a, b, screen, game)



    if scanforwin(tab, 30) == 0:
        running = 0
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            tab = eventuser(event, tab, fclick, game)
            fclick = 0
        if event.type == pygame.QUIT:
            running = 0

    pygame.display.flip()

print("wygrales")
