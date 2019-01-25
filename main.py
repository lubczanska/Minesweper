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


pygame.display.flip()

clock = pygame.time.Clock()

start = timer()

while running == 1:

    time = timer()
    time = int(time - start)
    print(game.clicks)
    clock.tick(30)


    running = game.scanforwin(tab)


    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

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
    smileconverter(screen, running, game)
    pygame.display.flip()

smileconverter(screen, running, game)
pygame.display.flip()



pygame.display.flip()
time.sleep(2)

