import pygame

def printplanszeszybko (screen, game, textury):

    # 0-9 - nie wciśnięte wgle
    # 10 - wcisnięty pusty
    # 11 - 18 wciśnięte, widać co jest
    # 19 - bomba kliknięta
    # 29 - bomba oflagowana
    # 20-28 - flaga
    # 30-39 - wyświetla pusty w animacji klikania
    # 40 - czerwona bomba
    for i in range(game.ny):
        for j in range(game.nx):
            if game.tab[i][j] == 0:
                screen.blit(textury.closed, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif game.tab[i][j] == 9 and game.bombsvisible:
                screen.blit(textury.bomb, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif game.tab[i][j] == 40:
                screen.blit(textury.bombdeath, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif game.tab[i][j] == 11:
                screen.blit(textury.open1, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif game.tab[i][j] == 12:
                screen.blit(textury.open2, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif game.tab[i][j] == 13:
                screen.blit(textury.open3, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif game.tab[i][j] == 14:
                screen.blit(textury.open4, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif game.tab[i][j] == 15:
                screen.blit(textury.open5, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif game.tab[i][j] == 16:
                screen.blit(textury.open6, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif game.tab[i][j] == 17:
                screen.blit(textury.open7, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif game.tab[i][j] == 18:
                screen.blit(textury.open8, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif game.tab[i][j] >= 0 and game.tab[i][j] <=9:
                screen.blit(textury.closed, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif game.tab[i][j] == 10 or game.tab[i][j] >= 30:
                screen.blit(textury.open0, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif game.tab[i][j] >= 20 and game.tab[i][j] <= 28 and game.bombsvisible:
                screen.blit(textury.bombmisflagged, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif game.tab[i][j] > 19:
                screen.blit(textury.flaga, (16 * i + game.borderleft, 16 * j + game.bordertop))




def smileconverter(screen, game, texture):

    if game.running:
        screen.blit(texture.smile, (game.nx * 8 - 2, game.bordertop - 40))
    elif game.bombsvisible:
        screen.blit(texture.lost, (game.nx * 8 - 2, game.bordertop - 40))
    else:
        screen.blit(texture.won, (game.nx * 8 - 2, game.bordertop - 40))

def printborder (screen, game, texture):
    #wypelnienie
    screen.fill(game.color)


    #PRZYCISKI
    #narozniki
    screen.blit(texture.bordertl, (0, 0))
    screen.blit(texture.bordertr, (game.nx * 16 + game.borderleft, 0))
    #przyciski
    screen.blit(texture.button, (16, 16))
    screen.blit(texture.button, (game.nx * 16 + game.borderleft - 54, 16))
    #gorna belka
    for a in range(game.nx*4):
        screen.blit(texture.bordertb, (4 * a + game.borderleft, 0))
    #prawy i lewy bok
    for a in range(6):
        screen.blit(texture.borderlr, (0, 12 + a * 4))
        screen.blit(texture.borderlr, (game.borderleft + game.nx * 16, 12 + a * 4))

    #WYSWIETALCZ
    #narozniki
    screen.blit(texture.borderjl, (0, game.bordertop - 55))
    screen.blit(texture.borderjr, (16 * game.nx + game.borderleft, game.bordertop - 55))
    screen.blit(texture.borderjl, (0, game.bordertop - 12))
    screen.blit(texture.borderjr, (16 * game.nx + game.borderleft, game.bordertop - 12))
    #gorna i dolna belka
    for a in range(game.nx*4):
        screen.blit(texture.bordertb, (4 * a + 12, game.bordertop - 55))
        screen.blit(texture.bordertb, (4 * a + 12, game.bordertop - 12))
    #prawy i lewy bok
    for a in range(8):
        screen.blit(texture.borderlr, (0, game.bordertop - 44 + a * 4))
        screen.blit(texture.borderlr, (16 * game.nx + game.borderleft, game.bordertop - 44 + a * 4))

    #PLANSZA
    #narozniki
    screen.blit(texture.borderbl, (0, 16 * game.nx + game.bordertop))
    screen.blit(texture.borderbr, (16 * game.nx + game.borderleft, 16 * game.nx + game.bordertop))
    #dolna belka
    for a in range(game.nx*4):
        screen.blit(texture.bordertb, (4 * a + game.borderleft, 16 * game.nx + game.bordertop))
    #prawy i lewy bok
    for b in range(game.nx):
        screen.blit(texture.borderl, (0, 16 * b + game.bordertop))
        screen.blit(texture.borderl, (16 * game.nx + game.borderleft, 16 * b + game.bordertop))

def printcyferki (side, input, screen, game, texture):
    # 13 x 23 px, (16 * game.nx - 16 * 3 + game.borderleft + 2  , 16)

    if side == 1:
        print_side = 16 * game.nx - 16 * 3 + game.borderleft + 2
    else:
        print_side = 17

    number = []
    number.append(input // 100)
    input = input  % 100
    number.append(input // 10)
    input = input % 10
    number.append(input)
    i = 0
    for a in number:
        if a == 0:
            screen.blit(texture.time0, (print_side + 13 * i, game.bordertop - 39))
        elif a == 1:
            screen.blit(texture.time1, (print_side + 13 * i, game.bordertop - 39))
        elif a == 2:
            screen.blit(texture.time2, (print_side + 13 * i, game.bordertop - 39))
        elif a == 3:
            screen.blit(texture.time3, (print_side + 13 * i, game.bordertop - 39))
        elif a == 4:
            screen.blit(texture.time4, (print_side + 13 * i, game.bordertop - 39))
        elif a == 5:
            screen.blit(texture.time5, (print_side + 13 * i, game.bordertop - 39))
        elif a == 6:
            screen.blit(texture.time6, (print_side + 13 * i, game.bordertop - 39))
        elif a == 7:
            screen.blit(texture.time7, (print_side + 13 * i, game.bordertop - 39))
        elif a == 8:
            screen.blit(texture.time8, (print_side + 13 * i, game.bordertop - 39))
        elif a == 9:
            screen.blit(texture.time9, (print_side + 13 * i, game.bordertop - 39))
        i += 1

def printmenu (screen, game, texture):
    #16 32

    #narozniki
    screen.blit(texture.bordertl, (16, 32))
    screen.blit(texture.bordertr, (16 * 6 + 28, 32))
    screen.blit(texture.borderbl, (16, 130))
    screen.blit(texture.borderbr, (16 * 6 + 28, 130))
    #gorna i dolna belka
    for i in range(24):
        screen.blit(texture.bordertb, (4 * i + 28, 32))
    for i in range(24):
        screen.blit(texture.bordertb, (4 * i + 28, 130))
    #prawy i lewy bok
    for i in range(23):
        screen.blit(texture.borderlr, (16, 4 * i + 44))
        screen.blit(texture.borderlr, (124, 4 * i + 44))
    #wypelnienie
    pygame.draw.rect(screen, game.color, (28, 44, 96, 86))
    #przycisk do zmiany motywu
    screen.blit(texture.theme, (100, 110))