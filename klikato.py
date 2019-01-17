import pygame


pygame.init()

nx = 4
ny = 4
x = 160
y = 160

sizex = 160/4
sizey = 160/4

screen = pygame.display.set_mode((x,y))
lclick = []
rclick = []

for x in range(2):
    lclick.append(x)
    rclick.append(x)


running = 1

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                lclick[0] = event.pos[0]//sizex
                lclick[1] = event.pos[1]//sizey
                print(lclick)
            if event.button == 3:
                rclick[0] = event.pos[0]//sizex
                rclick[1] = event.pos[1]//sizey
                print(rclick)
