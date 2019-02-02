import pygame
class Gamesettings:

    def __init__(self, nx, ny, n, bordertop, borderleft, blocksizex, blocksizey):
        #zwiekszanie planszy jesli jest mniejsza niz 8x8
        if(nx < 8): nx = 8
        if(ny < 8): ny = 8
        #zmniejszanie liczby bomb do 1/3 kafelkow jesli ustawi sie ich liczbe wieksza niz ilosc kafelkow
        if(n > nx * ny): n = int(nx * ny / 3)
        self.nx = nx                                                        #wysokosc planszy
        self.ny = ny                                                        #szerokosc planszy
        self.n = n                                                          #ilosc bomb
        self.bordertop = bordertop                                          #y lewego gornego naroznika planszy
        self.borderleft = borderleft                                        #x lewego gornego naroznika planszy
        self.blocksizex = blocksizex                                        #szerokosc kafelka
        self.blocksizey = blocksizey                                        #wysokosc kafelka
        self.windowsizex = self.nx*blocksizex + borderleft * 2              #szerokosc okna
        self.windowsizey = self.nx*blocksizey + bordertop + 12              #wysokosc okna
        self.clicks = 0                                                     #liczba klikniec
        self.clickedx = 0                                                   #x gdzie jest kliknieta mysz
        self.clickedy = 0                                                   #y gdzie jest kliknieta mysz
        self.bombsvisible = False                                           #widocznosc bomb
        self.theme = "dark"                                                 #motyw dark/light
        self.starttime = False                                              #czy wystartowac timer
        self.fclick = True                                                  #czy pierwszy klik w planszy
        self.running = True                                                 #czy gra jest uruchomiona
        self.tab = [[0 for i in range(self.nx)] for j in range(self.ny)]    #tablica z plansza
        self.menuvisible = False                                            #widocznosc menu
        if(self.theme == "dark"): self.color = (51, 51, 51)                 #kolor wypelnienia
        else: self.color = (189, 189, 189)
        self.themechanged = False
        self.serverip = "192.168.0.1"
    def scanforwin(self):

        #sprawdzanie ile jest otwartych kafelkow
        opencells = 0
        for a in self.tab:
            for b in a:
                if b > 9 and b < 20:
                    opencells += 1

        #wygrana
        if opencells + self.n == self.nx * self.ny:
            self.running = False
        #przegrana
        elif self.bombsvisible:
            self.running = False

    def reset(self):
        self.windowsizex = self.nx * self.blocksizex + self.borderleft * 2
        self.windowsizey = self.nx * self.blocksizey + self.bordertop + 12
        self.clicks = 0
        self.clickedx = 0
        self.clickedy = 0
        self.bombsvisible = False
        self.starttime = False
        self.fclick = True
        self.running = True
        self.tab = [[0 for i in range(self.nx)] for j in range(self.ny)]
        return pygame.display.set_mode((self.windowsizex, self.windowsizey))

