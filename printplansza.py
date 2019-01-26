def printplanszeszybko (tab, screen, game, textury):

    # 0-9 - nie wciśnięte wgle
    # 10 - wcisnięty pusty
    # 11 - 18 wciśnięte, widać co jest
    # 19 - bomba kliknięta
    # 29 - bomba oflagowana
    # 20-28 - flaga
    for i in range(game.nx):
        for j in range(game.ny):
            if tab[i][j] == 0:
                screen.blit(textury.closed, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif tab[i][j] == 9 and game.bombsvisible:
                screen.blit(textury.bomb, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif tab[i][j] == 11:
                screen.blit(textury.open1, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif tab[i][j] == 12:
                screen.blit(textury.open2, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif tab[i][j] == 13:
                screen.blit(textury.open3, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif tab[i][j] == 14:
                screen.blit(textury.open4, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif tab[i][j] == 15:
                screen.blit(textury.open5, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif tab[i][j] == 16:
                screen.blit(textury.open6, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif tab[i][j] == 17:
                screen.blit(textury.open7, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif tab[i][j] == 18:
                screen.blit(textury.open8, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif tab[i][j] >= 0 and tab[i][j] <=9:
                screen.blit(textury.closed, (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif tab[i][j] == 10:
                screen.blit(textury.open0,  (16 * i + game.borderleft, 16 * j + game.bordertop))
            elif tab[i][j] > 19:
                screen.blit(textury.flaga, (16*i + game.borderleft, 16* j + game.bordertop))

def smileconverter(screen, a, game, texture):

    if(a == 1):
        screen.blit(texture.smile, (game.nx * 8 - 2, game.bordertop - 40))
    elif(a == 0):
        screen.blit(texture.won, (game.nx * 8 - 2, game.bordertop - 40))
    elif(a == -1):
        screen.blit(texture.lost, (game.nx * 8 - 2, game.bordertop - 40))

def printborder (screen, game, texture):
    #przyciski
    screen.blit(texture.bordertl, (0, 0))
    screen.blit(texture.bordertr, (game.nx * 16 + game.borderleft, 0))
    screen.blit(texture.buttongame, (12, 12))
    screen.blit(texture.buttonmulti, (game.nx * 16 + game.borderleft - 50, 12))
    for a in range(game.nx):
        screen.blit(texture.bottom_middle, (16 * a + game.borderleft, 0))
    for a in range(4):
        screen.blit(texture.borderlr, (0, 12 + a * 4))
    for a in range(4):
        screen.blit(texture.borderlr, (game.borderleft + game.nx * 16, 12 + a * 4))

    #wyswietlacz
    screen.blit(texture.top_left, (0, game.bordertop - 55))
    for a in range(game.nx - 6):
        screen.blit(texture.top_middle, (16 * a + game.borderleft + 16 * 3, game.bordertop - 55))
    screen.blit(texture.top_right, (16 * game.nx - 16 * 3 + game.borderleft, game.bordertop - 55))

    #plansza
    for b in range(game.nx):
        screen.blit(texture.side_left, (0, 16 * b + game.bordertop))
        screen.blit(texture.side_right, (16 * game.nx + game.borderleft, 16 * b + game.bordertop))
    screen.blit(texture.bottom_left, (0, 16 * game.nx + game.bordertop))
    for a in range(game.nx):
        screen.blit(texture.bottom_middle, (16 * a + game.borderleft, 16 * game.nx + game.bordertop))
    screen.blit(texture.bottom_right, (16 * game.nx + game.borderleft, 16 * game.nx + game.bordertop))

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
        i = i + 1
