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
        self.theme = "dark" #dark light
        self.starttime = False
        self.fclick = True
        self.running = True
        self.tab = [[0 for i in range(self.nx)] for j in range(self.ny)]
        if(self.theme == "dark"): self.color = (51, 51, 51)
        else: self.color = (189, 189, 189)

    def scanforwin(self):

        opencells = 0
        for a in self.tab:
            for b in a:
                if b > 9 and b < 20:
                    opencells += 1

        if opencells + self.n == self.nx * self.ny:
            self.running = False
        elif self.bombsvisible:
            self.running = False
        else:
            self.running = True
