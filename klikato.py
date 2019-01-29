import math
from  odkrywane import odkrywajtablice
from planszator import generujtablice
from timeit import default_timer as timer

def leftclick(lclick, game):
    #zwiekszanie liczby klikniec
    if game.tab[lclick[0]][lclick[1]] < 10:
        game.clicks += 1
    #klikniecie w bombe
    if game.tab[lclick[0]][lclick[1]] == 9:
        game.bombsvisible = True
        game.tab[lclick[0]][lclick[1]] = 30
    #odkrycie pojedynczego kafelka
    elif game.tab[lclick[0]][lclick[1]] > 0 and game.tab[lclick[0]][lclick[1]] < 10:
        game.tab[lclick[0]][lclick[1]] += 10
    #odkrycie wielu kafelkow
    else:
        odkrywajtablice(game, lclick[0], lclick[1])

def rightclick(rclick, game):
    if(game.tab == None):
        generujtablice(rclick[0], rclick[1], game)
    #dodanie flagi
    if game.tab[rclick[0]][rclick[1]] < 10:
        game.tab[rclick[0]][rclick[1]] += 20
    #zabranie flagi
    elif game.tab[rclick[0]][rclick[1]] >= 20:
        game.tab[rclick[0]][rclick[1]] -= 20

def eventuser(event, game):
    #koordynaty klikniecia
    rclick = [0, 1]
    lclick = [0, 1]

    #lewy klik
    if event.button == 1:
        #pokazywanie i chowanie menu
        if event.pos[0] > 16 and event.pos[0] < 66 and event.pos[1] > 16 and event.pos[1] < 32:
            game.menuvisible = not game.menuvisible
        #klkianie w plansze
        elif not game.menuvisible and event.pos[0] > game.borderleft and (event.pos[0] < game.windowsizex-game.borderleft) and (event.pos[1] > game.bordertop) and (event.pos[1] < game.windowsizey-game.borderleft):
            lclick[0] = math.floor((event.pos[0]-game.borderleft)//game.blocksizex)
            lclick[1] = math.floor((event.pos[1]-game.bordertop )//game.blocksizey)
            #generowanie planszy po pierwszym kliknieciu
            if(game.fclick == 1):
                generujtablice(lclick[0], lclick[1], game)
                game.starttime = timer()
                game.fclick = False

            leftclick(lclick, game)

    #prawy klik
    if event.button == 3:
        #klikniecie w plansze
        if (not game.menuvisible and event.pos[0] > game.borderleft) and (event.pos[0] < game.windowsizex - game.borderleft) and (event.pos[1] > game.bordertop) and (event.pos[1] < game.windowsizey - game.borderleft):
            rclick[0] = int((event.pos[0]-game.borderleft)//game.blocksizex)
            rclick[1] = int((event.pos[1]-game.bordertop)//game.blocksizey)
            if(game.fclick == 1):
                generujtablice(lclick[0], lclick[1], game)
                game.starttime = timer()
                game.fclick = False

            rightclick(rclick, game)
