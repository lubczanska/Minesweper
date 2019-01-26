import random

def generujtablice(bx, by, game):

    for i in range(game.n):
        # losowanie koordynatow bomby
        rx = random.randint(0, game.nx - 1)
        ry = random.randint(0, game.ny - 1)

        #sprawdzanie czy wylosowane koordynaty nie sa pod klikiem lub nie zawieraja bomby
        while rx == bx and ry == by and game.tab[rx][ry] != 0:
            rx = random.randint(0, game.nx - 1)
            ry = random.randint(0, game.ny - 1)

        # wstawianie bomby na kordynaty
        game.tab[rx][ry] = 9

        #zwiekszanie znacznikow naookolo bomby
        if rx > 0 and game.tab[rx - 1][ry] < 9:
            game.tab[rx - 1][ry] += 1
        if rx < game.nx - 1 and game.tab[rx + 1][ry] < 9:
            game.tab[rx + 1][ry] += 1
        if ry > 0 and game.tab[rx][ry - 1]< 9:
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

