import pygame


class InputBox:

    def __init__(self, x, y, w, h, colornotfocused, colorfocused, editable=True, text=''):
        self.rect = pygame.Rect(x, y, w, h)             #prostokat w ktorym bedzie wejscie
        self.colornotfocused = colornotfocused          #kolor kiedy pole nie aktywne
        self.colorfocused = colorfocused                #kolor kiedy pole aktywne
        self.editable = editable                        #czy mozna zmienaic text
        self.color = pygame.Color(self.colornotfocused) #color fonta
        self.text = text                                #tekst na poczatku
        self.txt_surface = pygame.font.SysFont('Arial', 13, True).render(text, True, self.color)    #wyrenderowanie tekstu poczatkowego
        self.active = False                             #czy aktywne

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.editable:
            #klikniecie w pole zmienia aktywnosc
            if self.rect.collidepoint(event.pos): self.active = not self.active
            #klikniecie poza pole dezaktywuje pole
            else: self.active = False
            #zmiana kolory pola w zaleznosci od aktywnosci
            self.color = pygame.Color(self.colorfocused) if self.active else pygame.Color(self.colornotfocused)
        #zczytywanie przycisniec
        if event.type == pygame.KEYDOWN and self.editable:
            if self.active:
                #usuwanie ostatniego znaku
                if event.key == pygame.K_BACKSPACE: self.text = self.text[:-1]
                #dodawanie nowego znaku na koncu maksymalnie 2
                elif len(self.text) < 2: self.text += event.unicode
                #wyrenderowanie tekstu
                self.txt_surface = pygame.font.SysFont('Arial', 13, True).render(self.text, True, self.color)

    def draw(self, screen):
        #rysowanie tekstu
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+2))
        #rysowanie ramki
        pygame.draw.rect(screen, self.color, self.rect, 2)
