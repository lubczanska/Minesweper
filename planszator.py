import random

def generujtablice(bx, by, game):

    game.tab[0][0] = 0
    game.tab[0][1] = 1
    game.tab[0][2] = 2
    game.tab[0][3] = 3
    game.tab[0][4] = 4
    game.tab[0][5] = 5
    game.tab[0][6] = 6
    game.tab[1][0] = 7
    game.tab[1][1] = 8
    game.tab[1][2] = 9
    game.tab[1][3] = 20
    '''
    for i in range(game.n):
        # losowanie koordynatow bomby
        rx = random.randint(0, game.nx - 1)
        ry = random.randint(0, game.ny - 1)

        #sprawdzanie czy wylosowane koordynaty nie sa pod klikiem lub nie zawieraja bomby
        while rx == bx or ry == by or game.tab[rx][ry] > 8:
            rx = random.randint(0, game.nx - 1)
            ry = random.randint(0, game.ny - 1)

        # wstawianie bomby na koordynaty
        game.tab[rx][ry] = 9

        #zwiekszanie znacznikow naookolo bomby
        if rx > 0 and game.tab[rx - 1][ry] < 9:
            game.tab[rx - 1][ry] += 1
        if rx < game.nx - 1 and game.tab[rx + 1][ry] < 9:
            game.tab[rx + 1][ry] += 1
        if ry > 0 and game.tab[rx][ry - 1] < 9:
            game.tab[rx][ry - 1] += 1
        if ry < game.ny - 1 and game.tab[rx][ry + 1] < 9:
            game.tab[rx][ry + 1] += 1
        if rx > 0 and ry > 0 and game.tab[rx - 1][ry - 1] < 9:
            game.tab[rx - 1][ry - 1] += 1
        if rx < game.nx - 1 and ry > 0 and game.tab[rx + 1][ry - 1] < 9:
            game.tab[rx + 1][ry - 1] += 1
        if rx > 0 and ry < game.ny - 1 and game.tab[rx - 1][ry + 1] < 9:
            game.tab[rx - 1][ry + 1] += 1
        if rx < game.nx - 1 and ry < game.ny - 1 and game.tab[rx + 1][ry + 1] < 9:
            game.tab[rx + 1][ry + 1] += 1
'''