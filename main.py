import  time
import pygame
from timeit import default_timer as timer
from klikato import eventuser
from printplansza import printplanszeszybko, printborder, printcyferki, smileconverter
from gameclass import Gamesettings
from textureclass import Textureclass

nx = 8
ny = 8
n = 32

game = Gamesettings(nx, ny, n, 83, 12, 16, 16)
pygame.init()
screen = pygame.display.set_mode((game.windowsizex, game.windowsizey))
texture = Textureclass(game.theme)

screen.fill((189,189,189))

while game.running:
    if(game.starttime): game_time = int(timer() - game.starttime)
    else: game_time = 0

    game.scanforwin()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            eventuser(event, game)
        if event.type == pygame.QUIT:
            game.running = False

    printplanszeszybko(screen, game, texture)

    printborder(screen, game, texture)
    printcyferki(0, game.clicks, screen, game, texture)
    printcyferki(1, game_time, screen, game, texture)
    smileconverter(screen, game, texture)
    pygame.display.flip()

smileconverter(screen, game, texture)
pygame.display.flip()

time.sleep(2)
