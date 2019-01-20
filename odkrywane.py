
from planszator import generujtablice


def pokazbomby(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == 9:
                tab[i][j] = 19
    return tab

def pokazpuste(tab, x, y):
    if tab[x][y] == 0:
        tab[x][y] += 10
    elif tab[x][y] < 9:
        tab[x][y] += 10
        return tab
    else:
        return tab
    
    if x > 0:
        pokazpuste(tab, x - 1, y)
    if y > 0:
        pokazpuste(tab, x, y - 1)
    if x < len(tab) - 1:
        pokazpuste(tab, x + 1, y)
    if y < len(tab[0]) - 1:
        pokazpuste(tab, x, y + 1)
    if y < len(tab[0]) - 1 and x < len(tab) - 1:
        pokazpuste(tab, x + 1, y + 1)
    if y < len(tab[0]) - 1 and x > 0:
        pokazpuste(tab, x - 1, y + 1)
    if y > 0 and x < len(tab) - 1:
        pokazpuste(tab, x + 1, y - 1)
    if y > 0 and x > 0:
        pokazpuste(tab, x - 1, y - 1)

    return tab


def odkrywajtablice(tab, x, y):
    print(tab[x][y])
    if tab[x][y] == 9:
        pokazbomby(tab)
    else:
        pokazpuste(tab, x, y)





