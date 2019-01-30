import math
from  odkrywane import odkrywajtablice
from planszator import generujtablice
from timeit import default_timer as timer
from textureclass import Textureclass

def clicked(mousex, mousey, button, game):
    if button == 1:
        #chowa poprzednie pole
        if game.tab[game.clickedx][game.clickedy] >= 30:
            game.tab[game.clickedx][game.clickedy] -= 30
        #sprawdza czy klikane jest w plansze
        if mousex >= game.borderleft and mousex <= game.windowsizex - game.borderleft and mousey >= game.bordertop and mousey <= game.windowsizey - game.borderleft:
            game.clickedx = (mousex - game.borderleft) // 16
            game.clickedy = (mousey - game.bordertop) // 16
            #animacja tu sie dzieje
            if game.tab[game.clickedx][game.clickedy] <= 9:
                game.tab[game.clickedx][game.clickedy] += 30
    if button == 2:
        #chowa poprzednie pole
        for a in range(3):
            for b in range(3):
                if game.clickedx + (a - 1) >= 0 and game.clickedx + (a - 1) < game.nx and game.clickedy + (b - 1) >= 0 and game.clickedy + (b - 1) < game.ny:
                    if game.tab[game.clickedx + (a - 1)][game.clickedy + (b - 1)] >= 30:
                        game.tab[game.clickedx  + (a - 1)][game.clickedy + (b - 1)] -= 30
        #sprawdza czy klikane jest w plansze
        if mousex >= game.borderleft and mousex <= game.windowsizex - game.borderleft and mousey >= game.bordertop and mousey <= game.windowsizey - game.borderleft:
            game.clickedx = (mousex - game.borderleft) // 16
            game.clickedy = (mousey - game.bordertop) // 16
            #animacja tu sie dzieje
            for a in range(3):
                for b in range(3):
                    if game.clickedx + (a - 1) >= 0 and game.clickedx + (a - 1) < game.nx and game.clickedy + (b - 1) >= 0 and game.clickedy + (b - 1) < game.ny:
                        if game.tab[game.clickedx + (a - 1)][game.clickedy + (b - 1)] <= 9:
                            game.tab[game.clickedx + (a - 1)][game.clickedy + (b - 1)] += 30

def leftclick(lclick, game):
    #zwiekszanie liczby klikniec
    if game.tab[lclick[0]][lclick[1]] < 10:
        game.clicks += 1
    #klikniecie w bombe
    if game.tab[lclick[0]][lclick[1]] == 9:
        game.bombsvisible = True
        game.tab[lclick[0]][lclick[1]] = 40
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

def scrollclick(sclick, game):
    is_clear = 1
    if game.tab[sclick[0]][sclick[1]] >= 11 and game.tab[sclick[0]][sclick[1]] <= 18:
        # sprawdza czy wszystkie bomby wokol oznaczone
        for a in range(3):
            for b in range(3):
                if game.clickedx + (a - 1) >= 0 and game.clickedx + (a - 1) < game.nx and game.clickedy + (b - 1) >= 0 and game.clickedy + (b - 1) < game.ny:
                    if game.tab[sclick[0] + (a - 1)][sclick[1] + (b - 1)] == 9:
                        is_clear = 0
        # odkrywanie kafelkow
        if is_clear == 1:
            for a in range(3):
                for b in range(3):
                    if game.clickedx + (a - 1) >= 0 and game.clickedx + (a - 1) < game.nx and game.clickedy + (b - 1) >= 0 and game.clickedy + (b - 1) < game.ny:
                        odkrywajtablice(game, sclick[0] + (a - 1), sclick[1] + (b - 1))


def eventuser(event, game, screen):
    #koordynaty klikniecia
    rclick = [0, 1]
    lclick = [0, 1]
    sclick = [0, 1]

    #lewy klik
    if event.button == 1:
        #pokazywanie i chowanie menu
        if event.pos[0] > 16 and event.pos[0] < 66 and event.pos[1] > 16 and event.pos[1] < 32:
            game.menuvisible = not game.menuvisible
        elif game.menuvisible and event.pos[0] > 100 and event.pos[0] < 118 and event.pos[1] > 110 and event.pos[1] < 128:
            if game.theme == 'dark': game.theme = 'light'
            else: game.theme = 'dark'
            game.themechanged = True
        #klikanie w buzke - reset
        if event.pos[0] > 78 and event.pos[0] < 103 and event.pos[1] > 41 and event.pos[1] < 76:
            screen = game.reset()
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

    # srodkowy klik
    if event.button == 2:
        # klikniecie w plansze
        if (not game.menuvisible and event.pos[0] > game.borderleft) and (
                event.pos[0] < game.windowsizex - game.borderleft) and (event.pos[1] > game.bordertop) and (
                event.pos[1] < game.windowsizey - game.borderleft):
            sclick[0] = int((event.pos[0] - game.borderleft) // game.blocksizex)
            sclick[1] = int((event.pos[1] - game.bordertop) // game.blocksizey)
            if (game.fclick == 1):
                generujtablice(lclick[0], lclick[1], game)
                game.starttime = timer()
                game.fclick = False

            scrollclick(sclick, game)

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