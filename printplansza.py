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
    for y in range(game.ny):
        for x in range(game.nx):
            if game.tab[y][x] == 0:
                screen.blit(textury.closed, (16 * x + game.borderleft, 16 * y + game.bordertop))
            elif game.tab[y][x] == 9 and game.bombsvisible:
                screen.blit(textury.bomb, (16 * x + game.borderleft, 16 * y + game.bordertop))
            elif game.tab[y][x] == 40:
                screen.blit(textury.bombdeath, (16 * x + game.borderleft, 16 * y + game.bordertop))
            elif game.tab[y][x] == 11:
                screen.blit(textury.open1, (16 * x + game.borderleft, 16 * y + game.bordertop))
            elif game.tab[y][x] == 12:
                screen.blit(textury.open2, (16 * x + game.borderleft, 16 * y + game.bordertop))
            elif game.tab[y][x] == 13:
                screen.blit(textury.open3, (16 * x + game.borderleft, 16 * y + game.bordertop))
            elif game.tab[y][x] == 14:
                screen.blit(textury.open4, (16 * x + game.borderleft, 16 * y + game.bordertop))
            elif game.tab[y][x] == 15:
                screen.blit(textury.open5, (16 * x + game.borderleft, 16 * y + game.bordertop))
            elif game.tab[y][x] == 16:
                screen.blit(textury.open6, (16 * x + game.borderleft, 16 * y + game.bordertop))
            elif game.tab[y][x] == 17:
                screen.blit(textury.open7, (16 * x + game.borderleft, 16 * y + game.bordertop))
            elif game.tab[y][x] == 18:
                screen.blit(textury.open8, (16 * x + game.borderleft, 16 * y + game.bordertop))
            elif game.tab[y][x] >= 0 and game.tab[y][x] <=9:
                screen.blit(textury.closed, (16 * x + game.borderleft, 16 * y + game.bordertop))
            elif game.tab[y][x] == 10 or game.tab[y][x] >= 30:
                screen.blit(textury.open0, (16 * x + game.borderleft, 16 * y + game.bordertop))
            elif game.tab[y][x] >= 20 and game.tab[y][x] <= 28 and game.bombsvisible:
                screen.blit(textury.bombmisflagged, (16 * x + game.borderleft, 16 * y + game.bordertop))
            elif game.tab[y][x] > 19:
                screen.blit(textury.flaga, (16 * x + game.borderleft, 16 * y + game.bordertop))




def smileconverter(screen, game, texture, button):

    if button == 1 and pygame.mouse.get_pos()[0] > game.borderleft + game.nx / 2 * game.blocksizex - 13 and pygame.mouse.get_pos()[0] < game.borderleft + game.nx / 2 * game.blocksizex + 13 and pygame.mouse.get_pos()[1] > 41 and pygame.mouse.get_pos()[1] < 76:
        screen.blit(texture.smileclicked, (game.nx * 8 - 2, game.bordertop - 40))
    elif game.running and button > 0:
        screen.blit(texture.ooh, (game.nx * 8 - 2, game.bordertop - 40))
    elif game.running:
        screen.blit(texture.smile, (game.nx * 8 - 2, game.bordertop - 40))
    elif game.bombsvisible:
        screen.blit(texture.lost, (game.nx * 8 - 2, game.bordertop - 40))
    else:
        screen.blit(texture.won, (game.nx * 8 - 2, game.bordertop - 40))

def printborder (screen, game, texture, button):
    #wypelnienie
    screen.fill(game.color)

    #PRZYCISKI
    #narozniki
    screen.blit(texture.bordertl, (0, 0))
    screen.blit(texture.bordertr, (game.nx * 16 + game.borderleft, 0))
    #przyciski
    if game.running and button == 1 and pygame.mouse.get_pos()[0] > 16 and pygame.mouse.get_pos()[0] < 66 and pygame.mouse.get_pos()[1] > 16 and pygame.mouse.get_pos()[1] < 32:
        screen.blit(texture.buttonclicked, (16, 16))
    else:
        screen.blit(texture.button, (16, 16))
    if game.running and button == 1 and pygame.mouse.get_pos()[0] > game.nx * 16 + game.borderleft - 54 and pygame.mouse.get_pos()[0] < game.nx * 16 + game.borderleft - 4 and pygame.mouse.get_pos()[1] > 16 and pygame.mouse.get_pos()[1] < 32:
        screen.blit(texture.buttonclicked, (game.nx * 16 + game.borderleft - 54, 16))
    else:
        screen.blit(texture.button, (game.nx * 16 + game.borderleft - 54, 16))
    #gorna belka
    for x in range(game.nx*4):
        screen.blit(texture.bordertb, (4 * x + game.borderleft, 0))
    #prawy i lewy bok
    for y in range(6):
        screen.blit(texture.borderlr, (0, 12 + y * 4))
        screen.blit(texture.borderlr, (game.borderleft + game.nx * 16, 12 + y * 4))

    #WYSWIETALCZ
    #narozniki
    screen.blit(texture.borderjl, (0, game.bordertop - 55))
    screen.blit(texture.borderjr, (16 * game.nx + game.borderleft, game.bordertop - 55))
    screen.blit(texture.borderjl, (0, game.bordertop - 12))
    screen.blit(texture.borderjr, (16 * game.nx + game.borderleft, game.bordertop - 12))
    #gorna i dolna belka
    for x in range(game.nx*4):
        screen.blit(texture.bordertb, (4 * x + 12, game.bordertop - 55))
        screen.blit(texture.bordertb, (4 * x + 12, game.bordertop - 12))
    #prawy i lewy bok
    for y in range(8):
        screen.blit(texture.borderlr, (0, game.bordertop - 44 + y * 4))
        screen.blit(texture.borderlr, (16 * game.nx + game.borderleft, game.bordertop - 44 + y * 4))

    #PLANSZA
    #narozniki
    screen.blit(texture.borderbl, (0, 16 * game.ny + game.bordertop))
    screen.blit(texture.borderbr, (16 * game.nx + game.borderleft, 16 * game.ny + game.bordertop))
    #dolna belka
    for x in range(game.nx*4):
        screen.blit(texture.bordertb, (4 * x + game.borderleft, 16 * game.ny + game.bordertop))
    #prawy i lewy bok
    for y in range(game.ny):
        screen.blit(texture.borderl, (0, 16 * y + game.bordertop))
        screen.blit(texture.borderl, (16 * game.nx + game.borderleft, 16 * y + game.bordertop))

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
    for x in range(24):
        screen.blit(texture.bordertb, (4 * x + 28, 32))
    for x in range(24):
        screen.blit(texture.bordertb, (4 * x + 28, 130))
    #prawy i lewy bok
    for y in range(23):
        screen.blit(texture.borderlr, (16, 4 * y + 44))
        screen.blit(texture.borderlr, (124, 4 * y + 44))
    #wypelnienie
    pygame.draw.rect(screen, game.color, (28, 44, 96, 86))
    #przycisk do zmiany motywu
    screen.blit(texture.theme, (100, 110))