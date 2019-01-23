import pygame
from gameclass import Gamesettings
from odkrywane import pokazpuste, pokazbomby
from planszator import generujtablice


def leftclick(lclick,tab):
    if tab[lclick[0]][lclick[1]] >= 20:
        tab[lclick[0]][lclick[1]] -= 20

    elif tab[lclick[0]][lclick[1]] == 9:
        tab = pokazbomby(tab)
        return tab
    elif tab[lclick[0]][lclick[1]] > 0 and tab[lclick[0]][lclick[1]] < 10:
        tab[lclick[0]][lclick[1]] += 10
    else:
        tab = pokazpuste(tab, lclick[0], lclick[1])
    return tab
    
    
def rightclick(rclick,tab):
    if tab[rclick[0]][rclick[1]] < 10:
        tab[rclick[0]][rclick[1]] += 20
    elif tab[lclick[0]][lclick[1]] >= 20:
        tab[lclick[0]][lclick[1]] -= 20
    return tab


def eventuser(event, tab, fclick, game):
    print(event)
    lclick = []
    rclick = []

    for x in range(2):
        lclick.append(x)
        rclick.append(x)

    sizex = game.nx
    sizey = game.ny

    if event.button == 1:
        if(event.pos[0] > game.borderleft) and (event.pos[0] < game.windowsizex-game.borderleft) and (event.pos[1] > game.bordertop) and (event.pos[1] < game.windowsizey-game.bordertop):
            lclick[0] = int((event.pos[0]-game.borderleft)//sizex)
            lclick[1] = int((event.pos[1]-game.bordertop)//sizey)

            if(fclick == 1):
                tab = generujtablice(game.n, sizex, sizey, lclick[0], lclick[1])
            tab = leftclick(lclick, tab)
            print(tab)
        else:
            print("somthing")

    if event.button == 3:
        if (event.pos[0] > game.borderleft) and (event.pos[0] < game.windowsizex - game.borderleft) and (event.pos[1] > game.bordertop) and (event.pos[1] < game.windowsizey - game.bordertop):
            rclick[0] = int((event.pos[0]-game.borderleft)//sizex)
            rclick[1] = int((event.pos[1]-game.bordertop)//sizey)
            tab = rightclick(rclick, tab)
        else:
            print("somethingsomethinghere")

    return tab
