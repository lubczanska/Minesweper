class Gamesettings:

    def __init__(self, nx, ny, n, bordertop, borderleft, blocksizex, blocksizey):
        if(nx < 8): nx = 8
        if(ny < 8): ny = 8
        if(n > nx * ny): n = int(nx * ny / 2)
        self.nx = nx
        self.ny = ny
        self.n = n
        self.bordertop = bordertop
        self.borderleft = borderleft
        self.blocksizex = blocksizex
        self.blocksizey = blocksizey
        self.windowsizex = self.nx*blocksizex + borderleft * 2
        self.windowsizey = self.nx*blocksizey + bordertop + 12
        self.wall = self.windowsizey - self.ny * self.blocksizey
        self.clicks = 0
        self.bombsvisible = False
        self.theme = "light"
        self.starttime = 0

    def scanforwin(self, tab):

        opencells = 0
        for a in tab:
            for b in a:
                if b > 9 and b < 20:
                    opencells += 1

        if opencells + self.n == len(tab) * len(tab[0]):
            return 0

        if self.bombsvisible:
            return -1
        else:
            return 1
