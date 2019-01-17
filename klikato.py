import pygame

from odkrywane import pokazbomby,pokazpuste
from planszator import generujtablice
def leftclick(lclick,tab):
    if(tab[lclick[0]][lclick[1]] == 9):
        tab =pokazbomby(tab)
        return tab
    else:
        pokazpuste(tab, lclick[0], lclick[1])
        

pygame.init()

nx = 4
ny = 4
x = 160
y = 160

sizex = 160/nx
sizey = 160/ny

screen = pygame.display.set_mode((x,y))
lclick = []
rclick = []

for x in range(2):
    lclick.append(x)
    rclick.append(x)


running = 1
tab = generujtablice(2, nx, ny)
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                lclick[0] = int(event.pos[0]//sizex)
                lclick[1] = int(event.pos[1]//sizey)
                tab = leftclick(lclick, tab)
                print(tab)
            if event.button == 3:
                rclick[0] = int(event.pos[0]//sizex)
                rclick[1] = int(event.pos[1]//sizey)
                                





    
