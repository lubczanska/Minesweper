import random

def generujpusta(x,y):
    tab = [[0 for i in range(x)] for j in range(y)]
    return tab

def generujtablice(n, x, y, bx, by):
    #generowanie pustej tablicy
    tab = generujpusta(x, y)

    for i in range(n):
        # losowanie koordynatow bomby
        rx = random.randint(0, x - 1)
        ry = random.randint(0, y - 1)

        #sprawdzanie czy wylosowane koordynaty nie sa pod klikiem lub nie zawieraja bomby
        while rx == bx and ry == by and tab[rx][ry] == 9:
            rx = random.randint(0, x - 1)
            ry = random.randint(0, y - 1)

        # wstawianie bomby na kordynaty
        tab[rx][ry] = 9

        #zwiekszanie znacznikow naookolo bomby
        if rx > 0 and tab[rx - 1][ry] < 9:
            tab[rx - 1][ry] += 1
        if rx < x - 1 and tab[rx + 1][ry] < 9:
            tab[rx + 1][ry] += 1
        if ry > 0 and tab[rx][ry - 1]< 9:
            tab[rx][ry - 1] += 1
        if ry < y - 1 and tab[rx][ry + 1] < 9:
            tab[rx][ry + 1] += 1
        if rx > 0 and ry > 0 and tab[rx - 1][ry - 1] < 9:
            tab[rx - 1][ry - 1] += 1
        if rx < x - 1 and ry > 0 and tab[rx + 1][ry - 1] < 9:
            tab[rx + 1][ry - 1] += 1
        if rx > 0 and ry < y - 1 and tab[rx - 1][ry + 1] < 9:
            tab[rx - 1][ry + 1] += 1
        if rx < x - 1 and ry < y - 1 and tab[rx + 1][ry + 1] < 9:
            tab[rx + 1][ry + 1] += 1

    return tab

