from klikato import eventuser
from timeit import default_timer as timer
from planszator import generujtablice, generujpusta
from printplansza import printplanszeszybko, printborder, printcyferki, smileconverter
from gameclass import Gamesettings
import pygame

nx = 15
ny = 15
n = 20


game = Gamesettings(nx, ny, n, 55, 12, 16, 16)






pygame.init()

screen = pygame.display.set_mode((game.windowsizex, game.windowsizey))

running = 1

fclick = 1




tab = generujpusta(game.nx, game.ny)

screen = pygame.display.set_mode((game.windowsizex, game.windowsizey))

running = 1
pygame.display.flip()

clock = pygame.time.Clock()

start = 0
r = 1
while running == 1:

    if tab == generujpusta(game.nx, game.ny):
        fclick = 1
    time = timer()
    if r == 1:
        if fclick == 0:
            start = 0
            time = int(time - start)
    print(game.clicks)
    clock.tick(30)


    r = game.scanforwin(tab)


    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN :
            if fclick == 1:
                start = timer()
            tab = eventuser(event, tab, fclick, game)
            fclick = 0
        if event.type == pygame.QUIT:
            running = 0
    for a in range(len(tab)):

        for b in range(len(tab[0])):

            printplanszeszybko(tab, a, b, screen, game)

    printborder(screen, game)
    printcyferki(0, game.clicks, screen, game)
    printcyferki(1, time, screen, game)
    smileconverter(screen, r, game)
    pygame.display.flip()


pygame.display.flip()



pygame.display.flip()
time.sleep(2)

