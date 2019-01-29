import  time
import pygame
from timeit import default_timer as timer
from klikato import eventuser
from printplansza import printplanszeszybko, printborder, printcyferki, smileconverter, printmenu
from gameclass import Gamesettings
from textureclass import Textureclass
from textfieldclass import InputBox

nx = 12
ny = 8
n = 1

game = Gamesettings(nx, ny, n, 91, 12, 16, 16)
pygame.init()
screen = pygame.display.set_mode((game.windowsizex, game.windowsizey))
clock = pygame.time.Clock()
texture = Textureclass(game.theme)
sizex = InputBox(98, 47, 22, 17, 'gray', 'white')
sizey = InputBox(98, 68, 22, 17, 'gray', 'white')
bombs = InputBox(98, 89, 22, 17, 'gray', 'white')
boxes = [sizex, sizey, bombs]
sizextext = InputBox(31, 47, 60, 17, 'gray', 'white', False, "Height")  #nx
sizeytext = InputBox(31, 68, 60, 17, 'gray', 'white', False, "Width")   #ny
bombstext = InputBox(31, 89, 60, 17, 'gray', 'white', False, "Bombs")   #n
themetext = InputBox(31, 110, 60, 17, 'gray', 'white', False, "Theme")  #game.theme
texts = [sizextext, sizeytext, bombstext, themetext]

while game.running:
    clock.tick(30)

    if(game.starttime): game_time = int(timer() - game.starttime)
    else: game_time = 0

    game.scanforwin()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            eventuser(event, game)
        if event.type == pygame.QUIT:
            game.running = False
        for box in boxes:
            box.handle_event(event)

    printborder(screen, game, texture)
    printplanszeszybko(screen, game, texture)
    printcyferki(0, game.clicks, screen, game, texture)
    printcyferki(1, game_time, screen, game, texture)
    smileconverter(screen, game, texture)
    #printmenu(screen, game, texture)
    for box in boxes: box.draw(screen)
    for text in texts: text.draw(screen)
    pygame.display.flip()

time.sleep(2)
