import pygame

def printplanszeszybko (tab, x_coord, y_coord, screen, game):

    path = "images/" + game.theme + "/"

    closed = pygame.image.load(path + "blank.gif")
    closed.convert()
    open0 = pygame.image.load(path + "open0.gif")
    open0.convert()
    open1 = pygame.image.load(path + "open1.gif")
    open1.convert()
    open2 = pygame.image.load(path + "open2.gif")
    open2.convert()
    open3 = pygame.image.load(path + "open3.gif")
    open3.convert()
    open4 = pygame.image.load(path + "open4.gif")
    open4.convert()
    open5 = pygame.image.load(path + "open5.gif")
    open5.convert()
    open6 = pygame.image.load(path + "open6.gif")
    open6.convert()
    open7 = pygame.image.load(path + "open7.gif")
    open7.convert()
    open8 = pygame.image.load(path + "open8.gif")
    open8.convert()
    bomb = pygame.image.load(path + "bombrevealed.gif")
    bomb.convert()
    bombdeath = pygame.image.load(path + "bombdeath.gif")
    bombdeath.convert()
    flaga = pygame.image.load(path + "bombflagged.gif")
    flaga.convert()

    # 0-9 - nie wciśnięte wgle
    # 10 - wcisnięty pusty
    # 11 - 18 wciśnięte, widać co jest
    # 19 - bomba kliknięta
    # 29 - bomba oflagowana
    # 20-28 - flaga

    if tab[x_coord][y_coord] == 0:
        screen.blit(closed, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 9 and game.bombsvisible:
        screen.blit(bomb, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 11:
        screen.blit(open1, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 12:
        screen.blit(open2, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 13:
        screen.blit(open3, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 14:
        screen.blit(open4, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 15:
        screen.blit(open5, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 16:
        screen.blit(open6, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 17:
        screen.blit(open7, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 18:
        screen.blit(open8, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] >= 0 and tab[x_coord][y_coord] <=9:
        screen.blit(closed, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 10:
        screen.blit(open0,  (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] > 19:
        screen.blit(flaga, (16*x_coord + game.borderleft, 16* y_coord + game.bordertop))

def smileconverter(screen, a, game):

    path = "images/" + game.theme + "/"

    won = pygame.image.load(path + "facewin.gif")
    won.convert()
    lost = pygame.image.load(path + "facedead.gif")
    lost.convert()
    smile = pygame.image.load(path + "crying_laughing.gif")
    smile.convert()
    if(a == 1):
        screen.blit(smile, (game.nx * 8 - 1, 15))
    elif(a == 0):
        screen.blit(won, (game.nx * 8 - 1, 15))
    elif(a == -1):
        screen.blit(lost, (game.nx * 8 - 1, 15))

def printborder (screen, game):

    path = "images/" + game.theme + "/"

    top_left = pygame.image.load(path + "top_left.gif")
    top_left.convert()
    top_middle = pygame.image.load(path + "top_middle.gif")
    top_middle.convert()
    top_right = pygame.image.load(path + "top_right.gif")
    top_right.convert()
    side_left = pygame.image.load(path + "side_left.gif")
    side_left.convert()
    side_right = pygame.image.load(path + "side_right.gif")
    side_right.convert()
    bottom_left = pygame.image.load(path + "bottom_left.gif")
    bottom_left.convert()
    bottom_middle = pygame.image.load(path + "bottom_middle.gif")
    bottom_middle.convert()
    bottom_right = pygame.image.load(path + "bottom_right.gif")
    bottom_right.convert()
    smile = pygame.image.load(path + "crying_laughing.gif")
    smile.convert()

    screen.blit(top_left, (0, 0))
    for a in range(game.nx - 6):
        screen.blit(top_middle, (16 * a + game.borderleft + 16 * 3, 0))
    screen.blit(top_right, (16 * game.nx - 16 * 3 + game.borderleft, 0))
    for b in range(game.ny):
        screen.blit(side_left, (0, 16 * b + game.bordertop))
        screen.blit(side_right, (16 * game.nx + game.borderleft, 16 * b + game.bordertop))
    screen.blit(bottom_left, (0, 16 * game.nx + game.bordertop))
    for a in range(game.nx):
        screen.blit(bottom_middle, (16 * a + game.borderleft, 16 * game.nx + game.bordertop))
    screen.blit(bottom_right, (16 * game.nx + game.borderleft, 16 * game.nx + game.bordertop))
    screen.blit(smile, (game.nx * 8 - 1, 15))

def printcyferki (side, input, screen, game):

    path = "images/" + game.theme + "/"

    time0 = pygame.image.load(path + "time0.gif")
    time0.convert()
    time1 = pygame.image.load(path + "time1.gif")
    time1.convert()
    time2 = pygame.image.load(path + "time2.gif")
    time2.convert()
    time3 = pygame.image.load(path + "time3.gif")
    time3.convert()
    time4 = pygame.image.load(path + "time4.gif")
    time4.convert()
    time5 = pygame.image.load(path + "time5.gif")
    time5.convert()
    time6 = pygame.image.load(path + "time6.gif")
    time6.convert()
    time7 = pygame.image.load(path + "time7.gif")
    time7.convert()
    time8 = pygame.image.load(path + "time8.gif")
    time8.convert()
    time9 = pygame.image.load(path + "time9.gif")
    time9.convert()
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
            screen.blit(time0, (print_side + 13 * i, 16))
        elif a == 1:
            screen.blit(time1, (print_side + 13 * i, 16))
        elif a == 2:
            screen.blit(time2, (print_side + 13 * i, 16))
        elif a == 3:
            screen.blit(time3, (print_side + 13 * i, 16))
        elif a == 4:
            screen.blit(time4, (print_side + 13 * i, 16))
        elif a == 5:
            screen.blit(time5, (print_side + 13 * i, 16))
        elif a == 6:
            screen.blit(time6, (print_side + 13 * i, 16))
        elif a == 7:
            screen.blit(time7, (print_side + 13 * i, 16))
        elif a == 8:
            screen.blit(time8, (print_side + 13 * i, 16))
        elif a == 9:
            screen.blit(time9, (print_side + 13 * i, 16))
        i = i + 1
