import  time
import pygame
from timeit import default_timer as timer
from klikato import eventuser, clicked
from printplansza import printplanszeszybko, printborder, printcyferki, smileconverter, printmenu
from gameclass import Gamesettings
from textureclass import Textureclass
from textfieldclass import InputBox

nx = 16
ny = 10
n = 10
is_clicked = 0
last_x = 0
last_y = 0

game = Gamesettings(nx, ny, n, 91, 12, 16, 16)                          #stworzenie obiektu z parametrami gry
pygame.init()                                                           #inicjalizacja gry
screen = pygame.display.set_mode((game.windowsizex, game.windowsizey))  #stworzenie ekranu
clock = pygame.time.Clock()                                             #stworzenie Zegara
texture = Textureclass(game.theme)                                      #stworzenie obiektu z texturami
sizex = InputBox(98, 47, 22, 17, "10")                                        #wejscie w menu wysokosc planszy
sizey = InputBox(98, 68, 22, 17, "10")                                        #wejscie w menu szerokosc planszy
bombs = InputBox(98, 89, 22, 17, "10")                                        #wejscie w menu ilsco bomby
boxes = [sizex, sizey, bombs]
sizextext = InputBox(31, 47, 60, 17, "Height", False)                   #napis w menu wysoksc nx
sizeytext = InputBox(31, 68, 60, 17, "Width", False)                    #napis w menu szerokosc ny
bombstext = InputBox(31, 89, 60, 17, "Bombs", False)                    #napis w menu ilsoc bomb n
themetext = InputBox(31, 110, 60, 17, "Theme", False)                   #napis w menu motyw game.theme
texts = [sizextext, sizeytext, bombstext, themetext]
gamebutton = InputBox(20, 15, 41, 16, "Game", False, True, 12)          #napis w menu ilsoc bomb n
multibutton = InputBox(game.nx * 16 - 35, 15, 35, 16, "Multi", False, True, 12)  #napis w menu motyw game.theme
buttons = [gamebutton, multibutton]

while game.open:
    #zablokowanie odswiezania gry do 30 FPS
    clock.tick(30)
    #Czas gry
    if(game.starttime) and game.running: game_time = int(timer() - game.starttime)
    elif game.running: game_time = 0
    #Sprawdzanie wygranej
    game.scanforwin()
    #Animacja klikania
    if is_clicked > 0:
        clicked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], is_clicked, game)

    for event in pygame.event.get():
        #Klikniecie przycisku myszy
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 or event.button == 2:
                is_clicked = event.button
            elif event.button == 3:
                eventuser(event, game, screen, boxes )
        elif event.type == pygame.MOUSEBUTTONUP and is_clicked > 0:
            is_clicked = 0
            for x in range(3):
                for y in range(3):
                    if game.clickedx + (x - 1) >= 0 and game.clickedx + (x - 1) < game.nx and game.clickedy + (y - 1) >= 0 and game.clickedy + (y - 1) < game.ny:
                        if game.tab[game.clickedy + (y - 1)][game.clickedx + (x - 1)] >= 30:
                            game.tab[game.clickedy + (y - 1)][game.clickedx + (x - 1)] -= 30
            eventuser(event, game, screen, boxes)
        #Zamkniecie gry
        if event.type == pygame.QUIT:
            game.open = False
        #Eventy w wejsciach
        for box in boxes:
            box.handle_event(event)

    if game.themechanged:
        texture = Textureclass(game.theme)
        if (game.theme == "dark"): game.color = (51, 51, 51)
        else: game.color = (189, 189, 189)
        game.themechange = False

    #rysowanie gry
    printborder(screen, game, texture)
    printplanszeszybko(screen, game, texture)
    printcyferki(0, game.clicks, screen, game, texture)
    printcyferki(1, game_time, screen, game, texture)
    smileconverter(screen, game, texture)
    for button in buttons:
        button.draw(screen, game.theme)
    if game.menuvisible:
        printmenu(screen, game, texture)
        for box in boxes: box.draw(screen, game.theme)
        for text in texts: text.draw(screen, game.theme)
    pygame.display.flip()
