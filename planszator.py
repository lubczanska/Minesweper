import random

def generujtablice(bx, by, game):

    for n in range(game.n):
        # losowanie koordynatow bomby
        rx = random.randint(0, game.nx - 1)
        ry = random.randint(0, game.ny - 1)

        #sprawdzanie czy wylosowane koordynaty nie sa pod klikiem lub nie zawieraja bomby
        while rx == bx or ry == by or game.tab[ry][rx] > 8:
            rx = random.randint(0, game.nx - 1)
            ry = random.randint(0, game.ny - 1)

        # wstawianie bomby na koordynaty
        game.tab[ry][rx] = 9

        #zwiekszanie znacznikow naookolo bomby
        if ry > 0 and game.tab[ry - 1][rx] < 9:
            game.tab[ry - 1][rx] += 1
        if ry < game.ny - 1 and game.tab[ry + 1][rx] < 9:
            game.tab[ry + 1][rx] += 1
        if rx > 0 and game.tab[ry][rx - 1] < 9:
            game.tab[ry][rx - 1] += 1
        if rx < game.nx - 1 and game.tab[ry][rx + 1] < 9:
            game.tab[ry][rx + 1] += 1
        if ry > 0 and rx > 0 and game.tab[ry - 1][rx - 1] < 9:
            game.tab[ry - 1][rx - 1] += 1
        if ry < game.ny - 1 and rx > 0 and game.tab[ry + 1][rx - 1] < 9:
            game.tab[ry + 1][rx - 1] += 1
        if ry > 0 and rx < game.nx - 1 and game.tab[ry - 1][rx + 1] < 9:
            game.tab[ry - 1][rx + 1] += 1
        if ry < game.ny - 1 and rx < game.nx - 1 and game.tab[ry + 1][rx + 1] < 9:
            game.tab[ry + 1][rx + 1] += 1