import random

def generujpusta(x,y):
    tab = [[0 for i in range(x)] for j in range(y)]
    return tab

def generujtablice(n, x, y, bx, by):

    tab = [[0 for i in range(x)] for j in range(y)]
    #tutaj tworzymy naszą tablicę, o rozmiarach takich jakie mają być za pomocą list comprehension
    rx = random.randint(0,x-1)
    ry = random.randint(0,y-1)

    for i in range(n):
        rx = random.randint(0, x - 1)
        ry = random.randint(0, y - 1)
        if rx == bx and ry == by:
            rx = random.randint(0, x - 1)
            ry = random.randint(0, y - 1)
        tab[rx][ry] = 9

    for i in range(x):

        for j in range(y):
            times = 0
            bsum = 0
            topborder = 1
            bottomborder = -1
            leftborder = -1
            rightborder = 1
            
            if i == x-1:
                rightborder = 0
            if i == 0:
                leftborder = 0
            if j == y-1:
                topborder = 0
                
            if j == 0:
                bottomborder = 0

            for k in range(leftborder, rightborder+1):
                for l in range(bottomborder, topborder+1):
                    times += 1
                    if tab[i+k][j+l] == 9 and tab[i][j] != 9:
                        bsum += 1
            if bsum > 0 and tab[i][j] !=9:
                tab[i][j] = bsum

    return tab



