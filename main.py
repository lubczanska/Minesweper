from klikato import eventuser
import time
from planszator import generujtablice, generujpusta
from printplansza import printplanszeszybko
from gameclass import Gamesettings
import pygame

nx = 15
ny = 15
n = 30

game = Gamesettings(nx, ny, n, 30, 30, 15, 15)





pygame.init()

screen = pygame.display.set_mode((game.windowsizex, game.windowsizey))

running = 1

fclick = 1




tab = generujpusta(game.nx, game.ny)


clock = pygame.time.Clock()

while running == 1:
    clock.tick(60)
    for a in range(game.nx):
        for b in range(game.ny):

            printplanszeszybko(tab, a, b, screen, game)




    running = game.scanforwin(tab)


    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            tab = eventuser(event, tab, fclick, game)
            fclick = 0
        if event.type == pygame.QUIT:
            running = 0
    pygame.display.flip()







pygame.display.flip()
time.sleep(2)

