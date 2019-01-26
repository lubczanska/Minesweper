def printplanszeszybko (tab, x_coord, y_coord, screen, game, textury):

    # 0-9 - nie wciśnięte wgle
    # 10 - wcisnięty pusty
    # 11 - 18 wciśnięte, widać co jest
    # 19 - bomba kliknięta
    # 29 - bomba oflagowana
    # 20-28 - flaga

    if tab[x_coord][y_coord] == 0:
        screen.blit(textury.closed, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 9 and game.bombsvisible:
        screen.blit(textury.bomb, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 11:
        screen.blit(textury.open1, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 12:
        screen.blit(textury.open2, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 13:
        screen.blit(textury.open3, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 14:
        screen.blit(textury.open4, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 15:
        screen.blit(textury.open5, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 16:
        screen.blit(textury.open6, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 17:
        screen.blit(textury.open7, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 18:
        screen.blit(textury.open8, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] >= 0 and tab[x_coord][y_coord] <=9:
        screen.blit(textury.closed, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 10:
        screen.blit(textury.open0,  (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] > 19:
        screen.blit(textury.flaga, (16*x_coord + game.borderleft, 16* y_coord + game.bordertop))

def smileconverter(screen, a, game, texture):

    if(a == 1):
        screen.blit(texture.smile, (game.nx * 8 - 1, 15))
    elif(a == 0):
        screen.blit(texture.won, (game.nx * 8 - 1, 15))
    elif(a == -1):
        screen.blit(texture.lost, (game.nx * 8 - 1, 15))

def printborder (screen, game, texture):

    screen.blit(texture.top_left, (0, 0))
    for a in range(game.nx - 6):
        screen.blit(texture.top_middle, (16 * a + game.borderleft + 16 * 3, 0))
    screen.blit(texture.top_right, (16 * game.nx - 16 * 3 + game.borderleft, 0))
    for b in range(game.ny):
        screen.blit(texture.side_left, (0, 16 * b + game.bordertop))
        screen.blit(texture.side_right, (16 * game.nx + game.borderleft, 16 * b + game.bordertop))
    screen.blit(texture.bottom_left, (0, 16 * game.nx + game.bordertop))
    for a in range(game.nx):
        screen.blit(texture.bottom_middle, (16 * a + game.borderleft, 16 * game.nx + game.bordertop))
    screen.blit(texture.bottom_right, (16 * game.nx + game.borderleft, 16 * game.nx + game.bordertop))
    screen.blit(texture.smile, (game.nx * 8 - 1, 15))

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
            screen.blit(texture.time0, (print_side + 13 * i, 16))
        elif a == 1:
            screen.blit(texture.time1, (print_side + 13 * i, 16))
        elif a == 2:
            screen.blit(texture.time2, (print_side + 13 * i, 16))
        elif a == 3:
            screen.blit(texture.time3, (print_side + 13 * i, 16))
        elif a == 4:
            screen.blit(texture.time4, (print_side + 13 * i, 16))
        elif a == 5:
            screen.blit(texture.time5, (print_side + 13 * i, 16))
        elif a == 6:
            screen.blit(texture.time6, (print_side + 13 * i, 16))
        elif a == 7:
            screen.blit(texture.time7, (print_side + 13 * i, 16))
        elif a == 8:
            screen.blit(texture.time8, (print_side + 13 * i, 16))
        elif a == 9:
            screen.blit(texture.time9, (print_side + 13 * i, 16))
        i = i + 1
