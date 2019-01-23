class Gamesettings:
    def __init__(self, nx, ny, n, bordertop, borderleft, blocksizex, blocksizey):
        self.nx = nx
        self.ny = ny
        self.n = n
        self.borderleft = borderleft
        self.bordertop = bordertop
        self.windowsizex = borderleft*2 + self.nx*blocksizex
        self.windowsizey = bordertop*2 + self.nx*blocksizey
        self.blocksizex = blocksizex
        self.blocksizey = blocksizey
        self.wall = self.windowsizey - self.ny * self.blocksizey

    def scanforwin(self, tab):
        flaggedbombs = 0
        opencells = 0
        for a in tab:
            for b in a:
                if b == 29:
                    flaggedbombs += 1
                if b > 9 :
                    opencells += 1
        if opencells == (len(tab) * len(tab[0])-self.n):
            return 0


        for a in tab:
            for b in a:
                if b == 19:
                    return -1
        else:
            return 1