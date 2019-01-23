import pygame
from gameclass import Gamesettings


def printplanszeszybko (tab, x_coord, y_coord,screen, game):

    closed = pygame.image.load("images/blank.gif")
    closed.convert()
    open0 = pygame.image.load("images/open0.gif")
    open0.convert()
    open1 = pygame.image.load("images/open1.gif")
    open1.convert()
    open2 = pygame.image.load("images/open2.gif")
    open2.convert()
    open3 = pygame.image.load("images/open3.gif")
    open3.convert()
    open4 = pygame.image.load("images/open4.gif")
    open4.convert()
    open5 = pygame.image.load("images/open5.gif")
    open5.convert()
    open6 = pygame.image.load("images/open6.gif")
    open6.convert()
    open7 = pygame.image.load("images/open7.gif")
    open7.convert()
    open8 = pygame.image.load("images/open8.gif")
    open8.convert()
    bomb = pygame.image.load("images/bombrevealed.gif")
    bomb.convert()
    bombdeath = pygame.image.load("images/bombdeath.gif")
    bombdeath.convert()
    flaga = pygame.image.load("images/bombflagged.gif")
    flaga.convert()

    # 0-9 - nie wciśnięte wgle
    # 10 - wcisnięty pusty
    # 11 - 18 wciśnięte, widać co jest
    # 19 - bomba kliknięta
    # 29 - bomba oflagowana
    # 20-28 - flaga
    #
    #
    #
    #
    #
    #
    #

    if tab[x_coord][y_coord] == 0:
        screen.blit(closed, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
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
    elif tab[x_coord][y_coord] == 19:
        screen.blit(bomb, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] >= 0 and tab[x_coord][y_coord] <=9:
        screen.blit(closed, (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] == 10:
        screen.blit(open0,  (16 * x_coord + game.borderleft, 16 * y_coord + game.bordertop))
    elif tab[x_coord][y_coord] > 19:
        screen.blit(flaga,(16*x_coord + game.borderleft, 16* y_coord + game.bordertop   ))

def printborder (screen, game):

    top_left = pygame.image.load("images/top_left.gif")
    top_left.convert()
    top_middle = pygame.image.load("images/top_middle.gif")
    top_middle.convert()
    top_right = pygame.image.load("images/top_right.gif")
    top_right.convert()
    side_left = pygame.image.load("images/side_left.gif")
    side_left.convert()
    side_right = pygame.image.load("images/side_right.gif")
    side_right.convert()
    bottom_left = pygame.image.load("images/bottom_left.gif")
    bottom_left.convert()
    bottom_middle = pygame.image.load("images/bottom_middle.gif")
    bottom_middle.convert()
    bottom_right = pygame.image.load("images/bottom_right.gif")
    bottom_right.convert()
    smile = pygame.image.load("images/crying_laughing.gif")
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
    screen.blit(smile, (game.nx * 8 - 1, 16))
