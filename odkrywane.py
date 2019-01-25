def odkrywajtablice(tab, x, y):

    if tab[x][y] == 0:
        tab[x][y] += 10
    elif tab[x][y] < 9:
        tab[x][y] += 10
        return tab
    else:
        return tab
    
    if x > 0:
        odkrywajtablice(tab, x - 1, y)
    if y > 0:
        odkrywajtablice(tab, x, y - 1)
    if x < len(tab) - 1:
        odkrywajtablice(tab, x + 1, y)
    if y < len(tab[0]) - 1:
        odkrywajtablice(tab, x, y + 1)
    if y < len(tab[0]) - 1 and x < len(tab) - 1:
        odkrywajtablice(tab, x + 1, y + 1)
    if y < len(tab[0]) - 1 and x > 0:
        odkrywajtablice(tab, x - 1, y + 1)
    if y > 0 and x < len(tab) - 1:
        odkrywajtablice(tab, x + 1, y - 1)
    if y > 0 and x > 0:
        odkrywajtablice(tab, x - 1, y - 1)

    return tab
