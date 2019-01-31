import pygame


class InputBox:
    def __init__(self, x, y, w, h, text='', editable=True, transparent=False, fontsize = 13, colornotfocused =  (123, 123, 123), colorfocused = (255, 255, 255)):
        self.rect = pygame.Rect(x, y, w, h)             #prostokat w ktorym bedzie wejscie
        self.colornotfocused = colornotfocused          #kolor kiedy pole nie aktywne
        self.colorfocused = colorfocused                #kolor kiedy pole aktywne
        self.editable = editable                        #czy mozna zmienaic text
        self.color = self.colornotfocused               #color fonta
        self.text = text                                #tekst na poczatku
        self.fontsize = fontsize
        self.txt_surface = pygame.font.SysFont('Arial', self.fontsize, True).render(text, True, self.color)    #wyrenderowanie tekstu poczatkowego
        self.transparent = transparent                  #czy wyswietlac ramke
        self.active = False                             #czy aktywne

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.editable:
            #klikniecie w pole zmienia aktywnosc
            if self.rect.collidepoint(event.pos): self.active = not self.active
            #klikniecie poza pole dezaktywuje pole
            else: self.active = False
        #zczytywanie przycisniec
        if event.type == pygame.KEYDOWN and self.editable:
            if self.active:
                #usuwanie ostatniego znaku
                if event.key == pygame.K_BACKSPACE: self.text = self.text[:-1]
                #dodawanie nowego znaku na koncu maksymalnie 2
                elif len(self.text) < 2: self.text += event.unicode

    def draw(self, screen, theme):
        #
        if theme == "dark":
            self.colornotfocused = (123, 123, 123)
            self.colorfocused = (255, 255, 255)
        else:
            self.colornotfocused = (102, 102, 102)
            self.colorfocused = (000, 000, 000)
        # zmiana kolory pola w zaleznosci od aktywnosci
        self.color = self.colorfocused if self.active else self.colornotfocused

        # wyrenderowanie tekstu
        self.txt_surface = pygame.font.SysFont('Arial', self.fontsize, True).render(self.text, True, self.color)
        #rysowanie tekstu
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+2))
        #rysowanie ramki
        if not self.transparent:
            pygame.draw.rect(screen, self.color, self.rect, 2)
