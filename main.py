from klikato import eventuser
from odkrywane import pokazpuste, pokazbomby
from planszator import generujtablice
from printplansza import printplanszeszybko
import pygame
nx = 15
ny = 15
x = nx*16
y = ny*16




tab = generujtablice(30,nx,ny)

pygame.init()

screen = pygame.display.set_mode((x, y))

running = 1


while running:
    for a in range(nx):
        for b in range(ny):
            printplanszeszybko(tab, a, b, screen)




    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            eventuser(event, tab)
        if event.type == pygame.QUIT:
            running = 0

    pygame.display.flip()

