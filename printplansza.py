import pygame
from planszator import generujtablice



def printplanszeszybko (x_coord, y_coord):
    if tab[x_coord][y_coord] == 0:
        screen.blit(open0, (16 * x_coord, 16 * y_coord))
    elif tab[x_coord][y_coord] == 1:
        screen.blit(open1, (16 * x_coord, 16 * y_coord))
    elif tab[x_coord][y_coord] == 2:
        screen.blit(open2, (16 * x_coord, 16 * y_coord))
    elif tab[x_coord][y_coord] == 3:
        screen.blit(open3, (16 * x_coord, 16 * y_coord))
    elif tab[x_coord][y_coord] == 4:
        screen.blit(open4, (16 * x_coord, 16 * y_coord))
    elif tab[x_coord][y_coord] == 5:
        screen.blit(open5, (16 * x_coord, 16 * y_coord))
    elif tab[x_coord][y_coord] == 6:
        screen.blit(open6, (16 * x_coord, 16 * y_coord))
    elif tab[x_coord][y_coord] == 7:
        screen.blit(open7, (16 * x_coord, 16 * y_coord))
    elif tab[x_coord][y_coord] == 8:
        screen.blit(open8, (16 * x_coord, 16 * y_coord))
    elif tab[x_coord][y_coord] == 9:
        screen.blit(bomb, (16 * x_coord, 16 * y_coord))



pygame.init()

screen = pygame.display.set_mode((160, 160))

running = True

open0 = pygame.image.load("images/open0.gif")
open0.convert()
open1 = pygame.image.load("images/open1.gif")
open1.convert()
open2 = pygame.image.load("images/open2.gif")
open2.convert()
open3 = pygame.image.load("images/open3.gif")
open3.convert()
open4 = pygame.image.load("images/open4.gif")
open4.convert()
open5 = pygame.image.load("images/open5.gif")
open5.convert()
open6 = pygame.image.load("images/open6.gif")
open6.convert()
open7 = pygame.image.load("images/open7.gif")
open7.convert()
open8 = pygame.image.load("images/open8.gif")
open8.convert()
bomb = pygame.image.load("images/bombrevealed.gif")
bomb.convert()

size_x = 10
size_y = 10
bombs = 30
tab = generujtablice(bombs, size_x, size_y)



while running:


    for x_coord in range(size_x):
        for y_coord in range(size_y):
            printplanszeszybko(x_coord, y_coord)
    pygame.display.flip()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


