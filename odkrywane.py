def odkrywajtablice(game, x, y):

    if game.tab[x][y] == 0:
        game.tab[x][y] += 10
    elif game.tab[x][y] < 9:
        game.tab[x][y] += 10
        return 0
    else:
        return 0

    if x > 0:
        odkrywajtablice(game, x - 1, y)
    if y > 0:
        odkrywajtablice(game, x, y - 1)
    if x < game.nx - 1:
        odkrywajtablice(game, x + 1, y)
    if y < game.ny - 1:
        odkrywajtablice(game, x, y + 1)
    if y < game.ny - 1 and x < game.nx - 1:
        odkrywajtablice(game, x + 1, y + 1)
    if y < game.ny - 1 and x > 0:
        odkrywajtablice(game, x - 1, y + 1)
    if y > 0 and x < game.nx- 1:
        odkrywajtablice(game, x + 1, y - 1)
    if y > 0 and x > 0:
        odkrywajtablice(game, x - 1, y - 1)

