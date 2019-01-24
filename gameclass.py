class Gamesettings:
    def __init__(self, nx, ny, n, bordertop, borderleft, blocksizex, blocksizey):
        self.nx = nx + 1
        self.ny = ny + 1
        self.n = n
        self.borderleft = borderleft
        self.bordertop = bordertop
        self.windowsizex = self.nx*blocksizex + 24
        self.windowsizey = self.nx*blocksizey + 55+12
        self.blocksizex = blocksizex
        self.blocksizey = blocksizey
        self.wall = self.windowsizey - self.ny * self.blocksizey

    def scanforwin(self, tab):
        flaggedbombs = 0
        opencells = 0
        for a in tab:
            for b in a:
                if b > 9:
                    opencells += 1

        #if flaggedbombs == self.n and opencells == len(tab) * len(tab[0]):
        if opencells + self.n == len(tab) * len(tab[0]):
            return 0


        for a in tab:
            for b in a:
                if b == 19:
                    return -1
        else:
            return 1
