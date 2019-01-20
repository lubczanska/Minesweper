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