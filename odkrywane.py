def odkrywajtablice(game, x, y):
    #odkrywanie pola 0 i wszystkich na okolo
    if game.tab[y][x] == 0:
        game.tab[y][x] += 10
    #odkrywanie pol z numerkami
    elif game.tab[y][x] < 9:
        game.tab[y][x] += 10
        return 0
    else:
        return 0

    #odkrywanie wszystkich pol na okolo
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

