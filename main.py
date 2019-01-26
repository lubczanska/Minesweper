import  time
import pygame
from timeit import default_timer as timer
from klikato import eventuser
from planszator import generujpusta
from printplansza import printplanszeszybko, printborder, printcyferki, smileconverter
from gameclass import Gamesettings
from textureclass import Textureclass

nx = 8
ny = 8
n = 10

game = Gamesettings(nx, ny, n, 83, 12, 16, 16)

pygame.init()

screen = pygame.display.set_mode((game.windowsizex, game.windowsizey))

texture = Textureclass(game.theme)

tab = generujpusta(game.nx, game.ny)

pygame.display.flip()
screen.fill((189,189,189))

clock = pygame.time.Clock()

while game.running == 1:

    if(game.starttime != 0): game_time = int(timer() - game.starttime)
    else: game_time = 0
    clock.tick(30)

    game.running = game.scanforwin(tab)

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            tab = eventuser(event, tab, game)
        if event.type == pygame.QUIT:
            game.running = 0

    printplanszeszybko(tab, screen, game, texture)

    printborder(screen, game, texture)
    printcyferki(0, game.clicks, screen, game, texture)
    printcyferki(1, game_time, screen, game, texture)
    smileconverter(screen, game.running, game, texture)
    pygame.display.flip()

smileconverter(screen, game.running, game, texture)
pygame.display.flip()

pygame.display.flip()
time.sleep(2)
