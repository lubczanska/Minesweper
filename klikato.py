import math

from odkrywane import pokazpuste, pokazbomby, odkrywajtablice
from planszator import generujtablice, generujpusta
36

def leftclick(lclick,tab,game):

    if(tab[lclick[0]][lclick[1]] < 10):
        game.clicks = game.clicks + 1
    if tab[lclick[0]][lclick[1]] >= 20:
        tab[lclick[0]][lclick[1]] -= 20
    elif tab[lclick[0]][lclick[1]] == 9:
        game.bombsvisible = True
    elif tab[lclick[0]][lclick[1]] > 0 and tab[lclick[0]][lclick[1]] < 10:
        tab[lclick[0]][lclick[1]] += 10
    else:
        tab = odkrywajtablice(tab, lclick[0], lclick[1])

    return tab

def rightclick(rclick,tab):

    if tab[rclick[0]][rclick[1]] < 10:
        tab[rclick[0]][rclick[1]] += 20
    elif tab[rclick[0]][rclick[1]] >= 20:
        tab[rclick[0]][rclick[1]] -= 20
    return tab

def eventuser(event, tab, fclick, game):

    lclick = []
    rclick = []

    for x in range(2):
        lclick.append(x)
        rclick.append(x)

    sizex = game.blocksizex
    sizey = game.blocksizey

    if event.button == 1:

        if event.pos[0]> game.nx * 8 - 1 and event.pos[0] < game.nx * 8 - 1 +26 and event.pos[1] > 15 and event.pos[1] < 15 +26:
            tab = generujpusta(game.nx, game.ny)
        elif(event.pos[0] > game.borderleft) and (event.pos[0] < game.windowsizex-game.borderleft) and (event.pos[1] > game.bordertop) and (event.pos[1] < game.windowsizey-game.borderleft):
            print((event.pos[0]-game.borderleft)/sizex)

        if(event.pos[0] > game.borderleft) and (event.pos[0] < game.windowsizex-game.borderleft) and (event.pos[1] > game.bordertop) and (event.pos[1] < game.windowsizey-game.borderleft):

            lclick[0] = math.floor((event.pos[0]-game.borderleft)//sizex)
            lclick[1] = math.floor((event.pos[1]-game.bordertop)//sizey)
            game.clicks = game.clicks+1
            if(fclick == 1):
                tab = generujtablice(game.n, game.nx, game.ny, lclick[0], lclick[1])

            tab = leftclick(lclick, tab, game)
        else:
            print("somthing")

    if event.button == 3:
        if (event.pos[0] > game.borderleft) and (event.pos[0] < game.windowsizex - game.borderleft) and (event.pos[1] > game.bordertop) and (event.pos[1] < game.windowsizey - game.borderleft):
            rclick[0] = int((event.pos[0]-game.borderleft)//sizex)
            rclick[1] = int((event.pos[1]-game.bordertop)//sizey)
            if(fclick == 1):
                tab = generujtablice(game.n, sizex, sizey, lclick[0], lclick[1])
            tab = rightclick(rclick, tab)
        else:
            print("somethingsomethinghere")

    return tab
