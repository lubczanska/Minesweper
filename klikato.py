import math
from  odkrywane import odkrywajtablice
from planszator import generujtablice
from timeit import default_timer as timer

def leftclick(lclick, game):
    if game.tab[lclick[0]][lclick[1]] < 10:
        game.clicks += 1

    if game.tab[lclick[0]][lclick[1]] == 9:
        game.bombsvisible = True
    elif game.tab[lclick[0]][lclick[1]] > 0 and game.tab[lclick[0]][lclick[1]] < 10:
        game.tab[lclick[0]][lclick[1]] += 10
    else:
        odkrywajtablice(game, lclick[0], lclick[1])

def rightclick(rclick, game):

    if game.tab[rclick[0]][rclick[1]] < 10:
        game.tab[rclick[0]][rclick[1]] += 20
    elif game.tab[rclick[0]][rclick[1]] >= 20:
        game.tab[rclick[0]][rclick[1]] -= 20

def eventuser(event, game):
    rclick = lclick = [0, 1]

    if event.button == 1:
        if(event.pos[0] > game.borderleft) and (event.pos[0] < game.windowsizex-game.borderleft) and (event.pos[1] > game.bordertop) and (event.pos[1] < game.windowsizey-game.borderleft):
            lclick[0] = math.floor((event.pos[0]-game.borderleft)//game.blocksizex)
            lclick[1] = math.floor((event.pos[1]-game.bordertop )//game.blocksizey)

            if(game.fclick == 1):
                generujtablice(lclick[0], lclick[1], game)
                game.starttime = timer()
                game.fclick = False

            leftclick(lclick, game)
        else:
            print("somthing")

    if event.button == 3:
        if (event.pos[0] > game.borderleft) and (event.pos[0] < game.windowsizex - game.borderleft) and (event.pos[1] > game.bordertop) and (event.pos[1] < game.windowsizey - game.borderleft):
            rclick[0] = int((event.pos[0]-game.borderleft)//game.blocksizex)
            rclick[1] = int((event.pos[1]-game.bordertop)//game.blocksizey)
            if(game.fclick == 1):
                game.tab = generujtablice(lclick[0], lclick[1], game)
            rightclick(rclick, game)
        else:
            print("somethingsomethinghere")
