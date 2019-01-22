from klikato import eventuser
import time
from planszator import generujtablice, generujpusta
from printplansza import printplanszeszybko
from gameclass import Gamesettings
import pygame
from clientudp import getboard, getloss
IS_MULTI = 1

nx = 16
ny = 16
n = 30

game = Gamesettings(nx, ny, n, 30, 30, 16, 16)





pygame.init()

screen = pygame.display.set_mode((game.windowsizex, game.windowsizey))

running = 1

fclick = 1

if IS_MULTI == 1:
    fclick = 0
    zwrac = getboard()
    tab = zwrac.get("tablica")
    adress = zwrac.get("adress")

else:
    tab = generujpusta(game.nx, game.ny)


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
    if(IS_MULTI == 1):
        running = getloss()-2

if running == -2 or running == -1:
    print("won")
if running == 0 :
    print("lost")
pygame.display.flip()
time.sleep(5)

