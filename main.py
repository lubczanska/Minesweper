import  time
import pygame
from timeit import default_timer as timer
from klikato import eventuser
from printplansza import printplanszeszybko, printborder, printcyferki, smileconverter, printmenu
from gameclass import Gamesettings
from textureclass import Textureclass
from textfieldclass import InputBox

nx = 10
ny = 10
n = 10

game = Gamesettings(nx, ny, n, 91, 12, 16, 16)                          #stworzenie obiektu z parametrami gry
pygame.init()                                                           #inicjalizacja gry
screen = pygame.display.set_mode((game.windowsizex, game.windowsizey))  #stworzenie ekranu
clock = pygame.time.Clock()                                             #stworzenie Zegara
texture = Textureclass(game.theme)                                      #stworzenie obiektu z texturami
sizex = InputBox(98, 47, 22, 17, 'gray', 'white')                       #wejscie w menu wysokosc planszy
sizey = InputBox(98, 68, 22, 17, 'gray', 'white')                       #wejscie w menu szerokosc planszy
bombs = InputBox(98, 89, 22, 17, 'gray', 'white')                       #wejscie w menu ilsco bomby
boxes = [sizex, sizey, bombs]
sizextext = InputBox(31, 47, 60, 17, 'gray', 'white', False, "Height")  #napis w menu wysoksc nx
sizeytext = InputBox(31, 68, 60, 17, 'gray', 'white', False, "Width")   #napis w menu szerokosc ny
bombstext = InputBox(31, 89, 60, 17, 'gray', 'white', False, "Bombs")   #napis w menu ilsoc bomb n
themetext = InputBox(31, 110, 60, 17, 'gray', 'white', False, "Theme")  #napis w menu motyw game.theme
texts = [sizextext, sizeytext, bombstext, themetext]
gamebutton = InputBox(20, 15, 41, 16, "gray", 'white', False, "Game", True, 12)   #napis w menu ilsoc bomb n
multibutton = InputBox(game.nx * 16 - 35, 15, 35, 16, 'gray', 'white', False, "Multi", True, 12)  #napis w menu motyw game.theme
buttons = [gamebutton, multibutton]

while game.running:
    #zablokowanie odswiezania gry do 30 FPS
    clock.tick(30)
    #Czas gry
    if(game.starttime): game_time = int(timer() - game.starttime)
    else: game_time = 0
    #Sprawdzanie wygranej
    game.scanforwin()

    for event in pygame.event.get():
        #Klikniecie przycisku myszy
        if event.type == pygame.MOUSEBUTTONDOWN:
            eventuser(event, game)
        #Zamkniecie gry
        if event.type == pygame.QUIT:
            game.running = False
        #Eventy w wejsciach
        for box in boxes:
            box.handle_event(event)

    #rysowanie gry
    printborder(screen, game, texture)
    printplanszeszybko(screen, game, texture)
    printcyferki(0, game.clicks, screen, game, texture)
    printcyferki(1, game_time, screen, game, texture)
    smileconverter(screen, game, texture)
    for button in buttons:
        button.draw(screen)
    if game.menuvisible:
        printmenu(screen, game, texture)
        for box in boxes: box.draw(screen)
        for text in texts: text.draw(screen)
    pygame.display.flip()

time.sleep(2)
