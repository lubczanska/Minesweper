from klikato import eventuser
import time
from planszator import generujtablice, generujpusta
from printplansza import printplanszeszybko
from gameclass import Gamesettings
import pygame
IS_MULTI = 0

nx = 16
ny = 16
n = 30

game = Gamesettings(nx, ny, n, 55, 12, 16, 16)




tab = generujpusta(game.nx, game.ny)
pygame.init()

screen = pygame.display.set_mode((game.windowsizex, game.windowsizey))

running = 1

fclick = 1

if IS_MULTI == 1:
    fclick = 0



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
if game.scanforwin(tab) == 0:
    screen.fill((50, 50, 50))
elif game.scanforwin(tab) == -1:
    screen.fill((100, 100, 100))


pygame.display.flip()
time.sleep(5)

