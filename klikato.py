import pygame

from odkrywane import pokazpuste, pokazbomby
from planszator import generujtablice
def leftclick(lclick,tab):
    if(tab[lclick[0]][lclick[1]] >= 20):
        tab[lclick[0]][lclick[1]] -= 20

    elif (tab[lclick[0]][lclick[1]] == 9):
        tab = pokazbomby(tab)
        return tab
    elif tab[lclick[0]][lclick[1]] > 0 and tab[lclick[0]][lclick[1]] < 10:
        tab[lclick[0]][lclick[1]] += 10
    else:
        tab = pokazpuste(tab, lclick[0], lclick[1])
    return tab
    






def rightclick(rclick,tab):
    if tab[rclick[0]][rclick[1]] < 10:
        tab[rclick[0]][rclick[1]]+=20
    return tab



def eventuser(event, tab, fclick):
    print(event)
    lclick = []
    rclick = []

    for x in range(2):
        lclick.append(x)
        rclick.append(x)



    


    sizex = 16
    sizey = 16

    if event.button == 1:
        lclick[0] = int(event.pos[0]//sizex)
        lclick[1] = int(event.pos[1]//sizey)

        if(fclick == 1):
            tab = generujtablice(30, sizex, sizey, lclick[0], lclick[1])
        tab = leftclick(lclick, tab)
        print(tab)
    if event.button == 3:
        rclick[0] = int(event.pos[0]//sizex)
        rclick[1] = int(event.pos[1]//sizey)
        tab = rightclick(rclick, tab)



    return tab





