import random

x = 0
y = 0
n = 0

def generujtablice(n, x, y):
    bsum = 0;
    tab = [[0 for i in range(x)] for j in range(y)]
    #tutaj tworzymy naszą tablicę, o rozmiarach takich jakie mają być za pomocą list comprehension
    for i in range(n):
        tab[random.randint(0,x-1)][random.randint(0,y-1)] = 9
    for i in range(x):
        times = 0
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
            if bsum > 0  and tab[i][j] !=9:
                tab[i][j] = bsum

    return tab



