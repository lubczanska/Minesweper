import  time
import pygame
from timeit import default_timer as timer
from klikato import eventuser
from planszator import generujpusta
from printplansza import printplanszeszybko, printborder, printcyferki, smileconverter
from gameclass import Gamesettings
from textureclass import Textureclass

nx = 7
ny = 7
n = 10

game = Gamesettings(nx, ny, n, 86, 12, 16, 16)

pygame.init()

screen = pygame.display.set_mode((game.windowsizex, game.windowsizey))

texture = Textureclass(game.theme)

running = 1
fclick = 1

tab = generujpusta(game.nx, game.ny)

pygame.display.flip()

clock = pygame.time.Clock()

start = timer()

while running == 1:

    end = timer()
    end = int(end - start)
    clock.tick(30)

    running = game.scanforwin(tab)

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            tab = eventuser(event, tab, fclick, game)
            fclick = 0
        if event.type == pygame.QUIT:
            running = 0

    printplanszeszybko(tab, screen, game, texture)

    printborder(screen, game, texture)
    printcyferki(0, game.clicks, screen, game, texture)
    printcyferki(1, end, screen, game, texture)
    smileconverter(screen, running, game, texture)
    pygame.display.flip()

smileconverter(screen, running, game, texture)
pygame.display.flip()

pygame.display.flip()
time.sleep(2)
