from planszator import generujtablice

TAB = generujtablice(10, 7, 7)
X = 4
Y = 5

for i in TAB:
    print(i)

def pokazbomby(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == 9:
                tab[i][j] = 19


def pokazpuste(tab, x, y):
    if x < 0 or y < 0 or x > len(tab[0]) or y > len(tab):
        return 0

    if tab[x][y] < 9:
        tab[x][y] += 10

    if y > 0 and tab[y - 1][x] < 9:
        tab[y - 1][x] += 10
        pokazpuste(tab, x, y - 1)
    elif y < len(tab) - 1 and tab[y + 1][x] < 9:
        tab[y + 1][x] += 10
        pokazpuste(tab, x, y + 1)
    elif x > 0 and tab[y][x - 1] < 9:
        tab[y][x - 1] += 10
        pokazpuste(tab, x, y + 1)
    elif x < len(tab[0]) - 1 and tab[y][x + 1] < 9:
        tab[y][x + 1] += 10
        pokazpuste(tab, x, y + 1)

    return 0


def odkrywajtablice(tab, x, y):
    if tab[y][x] == 9:
        pokazbomby(tab)
    else:
        pokazpuste(tab, x, y)


#odkrywajtablice(TAB, X, Y)

print(len(TAB))
print(len(TAB[0]))
print("###")

for i in TAB:
    print(i)
