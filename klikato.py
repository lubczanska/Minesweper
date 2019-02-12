import math
from  odkrywane import odkrywajtablice
from planszator import generujtablice
from timeit import default_timer as timer
from textfieldclass import InputBox

def clicked(mousex, mousey, button, game):
    if button == 1 and game.running and not game.menuvisible:
        #chowa poprzednie pole
        if game.tab[game.clickedy][game.clickedx] >= 30:
            game.tab[game.clickedy][game.clickedx] -= 30
        #sprawdza czy klikane jest w plansze
        if mousex >= game.borderleft and mousex < game.windowsizex - game.borderleft and mousey >= game.bordertop and mousey < game.windowsizey - game.borderleft:
            game.clickedx = (mousex - game.borderleft) // 16
            game.clickedy = (mousey - game.bordertop) // 16
            #animacja tu sie dzieje
            if game.tab[game.clickedy][game.clickedx] <= 9:
                game.tab[game.clickedy][game.clickedx] += 30
    if button == 2:
        #chowa poprzednie pole
        for x in range(3):
            for y in range(3):
                if game.clickedx + (x - 1) >= 0 and game.clickedx + (x - 1) < game.nx and game.clickedy + (y - 1) >= 0 and game.clickedy + (y - 1) < game.ny:
                    if game.tab[game.clickedy + (y - 1)][game.clickedx + (x - 1)] >= 30:
                        game.tab[game.clickedy + (y - 1)][game.clickedx  + (x - 1)] -= 30
        #sprawdza czy klikane jest w plansze
        if mousex >= game.borderleft and mousex < game.windowsizex - game.borderleft and mousey >= game.bordertop and mousey < game.windowsizey - game.borderleft:
            game.clickedx = (mousex - game.borderleft) // 16
            game.clickedy = (mousey - game.bordertop) // 16
            #animacja tu sie dzieje
            for x in range(3):
                for y in range(3):
                    if game.clickedx + (x - 1) >= 0 and game.clickedx + (x - 1) < game.nx and game.clickedy + (y - 1) >= 0 and game.clickedy + (y - 1) < game.ny:
                        if game.tab[game.clickedy + (y - 1)][game.clickedx + (x - 1)] <= 9:
                            game.tab[game.clickedy + (y - 1)][game.clickedx + (x - 1)] += 30

def leftclick(lclick, game):
    #zwiekszanie liczby klikniec
    if game.tab[lclick[1]][lclick[0]] < 10:
        game.clicks += 1
    #klikniecie w bombe
    if game.tab[lclick[1]][lclick[0]] == 9:
        game.bombsvisible = True
        game.tab[lclick[1]][lclick[0]] = 40
    #odkrycie pojedynczego kafelka
    elif game.tab[lclick[1]][lclick[0]] > 0 and game.tab[lclick[1]][lclick[0]] < 10:
        game.tab[lclick[1]][lclick[0]] += 10
    #odkrycie wielu kafelkow
    else:
        odkrywajtablice(game, lclick[0], lclick[1])

def rightclick(rclick, game):
    if(game.tab == None):
        generujtablice(rclick[1], rclick[1], game)
    #dodanie flagi
    if game.tab[rclick[1]][rclick[0]] < 10:
        game.tab[rclick[1]][rclick[0]] += 20
    #zabranie flagi
    elif game.tab[rclick[1]][rclick[0]] >= 20 and game.tab[rclick[1]][rclick[0]] < 30:
        game.tab[rclick[1]][rclick[0]] -= 20

def scrollclick(sclick, game):
    is_clear = 1
    if game.tab[sclick[1]][sclick[0]] >= 11 and game.tab[sclick[1]][sclick[0]] <= 18:
        # sprawdza czy wszystkie bomby wokol oznaczone
        for x in range(3):
            for y in range(3):
                if game.clickedx + (x - 1) >= 0 and game.clickedx + (x - 1) < game.nx and game.clickedy + (y - 1) >= 0 and game.clickedy + (y - 1) < game.ny:
                    if game.tab[sclick[1] + (y - 1)][sclick[0] + (x - 1)] == 9:
                        is_clear = 0
        # odkrywanie kafelkow
        if is_clear == 1:
            for x in range(3):
                for y in range(3):
                    if game.clickedx + (x - 1) >= 0 and game.clickedx + (x - 1) < game.nx and game.clickedy + (y - 1) >= 0 and game.clickedy + (y - 1) < game.ny:
                        odkrywajtablice(game, sclick[0] + (x - 1), sclick[1] + (y - 1))


def eventuser(event, game, boxes, buttons):
    #koordynaty klikniecia
    rclick = [0, 1]     #[x, y]
    lclick = [0, 1]     #[x, y]
    sclick = [0, 1]     #[x, y]

    #lewy klik
    if event.button == 1:
        #obsluga multiplayera
        if event.pos[0] > game.nx * 16 + game.borderleft - 54 and event.pos[0] < game.nx * 16 + game.borderleft - 54 + 50  and event.pos[1] > 16 and event.pos[1] < 32:
            screen = game.reset()
            game.ismulti = 1

        #pokazywanie i chowanie menu
        if event.pos[0] > 16 and event.pos[0] < 66 and event.pos[1] > 16 and event.pos[1] < 32:
            game.menuvisible = not game.menuvisible
            if game.ny != int(boxes[0].text) or game.nx != int(boxes[1].text) or game.n != int(boxes[2].text):
                game.ny = int(boxes[0].text)
                game.nx = int(boxes[1].text)
                game.n  = int(boxes[2].text)
                buttons[1] = InputBox(game.nx * 16 - 35, 15, 35, 16, "Multi", False, True, 12)
                screen = game.reset()
        elif game.menuvisible and event.pos[0] > 100 and event.pos[0] < 118 and event.pos[1] > 110 and event.pos[1] < 128:
            if game.theme == 'dark': game.theme = 'light'
            else: game.theme = 'dark'
            game.themechanged = True
        #klikanie w buzke - reset
        if event.pos[0] > game.borderleft + game.nx / 2 * game.blocksizex - 13 and event.pos[0] < game.borderleft + game.nx / 2 * game.blocksizex + 13 and event.pos[1] > 41 and event.pos[1] < 76:
            screen = game.reset()
        #klkianie w plansze
        elif game.running and not game.menuvisible and event.pos[0] > game.borderleft and (event.pos[0] < game.windowsizex-game.borderleft) and (event.pos[1] > game.bordertop) and (event.pos[1] < game.windowsizey-game.borderleft):
            lclick[0] = math.floor((event.pos[0]-game.borderleft)//game.blocksizex)
            lclick[1] = math.floor((event.pos[1]-game.bordertop )//game.blocksizey)
            #generowanie planszy po pierwszym kliknieciu
            if(game.fclick == 1):
                generujtablice(lclick[0], lclick[1], game)
                game.starttime = timer()
                game.fclick = False

            leftclick(lclick, game)

    # srodkowy klik
    if event.button == 2 and game.running:
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
    if event.button == 3 and game.running:
        #klikniecie w plansze
        if (not game.menuvisible and event.pos[0] > game.borderleft) and (event.pos[0] < game.windowsizex - game.borderleft) and (event.pos[1] > game.bordertop) and (event.pos[1] < game.windowsizey - game.borderleft):
            rclick[0] = int((event.pos[0]-game.borderleft)//game.blocksizex)
            rclick[1] = int((event.pos[1]-game.bordertop)//game.blocksizey)
            if(game.fclick == 1):
                generujtablice(lclick[0], lclick[1], game)
                game.starttime = timer()
                game.fclick = False

            rightclick(rclick, game)
