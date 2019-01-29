import pygame


class InputBox:

    def __init__(self, x, y, w, h, colornotfocused, colorfocused, editable=True, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.colornotfocused = colornotfocused
        self.colorfocused = colorfocused
        self.editable = editable
        self.color = pygame.Color(self.colornotfocused)
        self.text = text
        self.txt_surface = pygame.font.SysFont('Arial', 13, True).render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.editable:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = pygame.Color(self.colorfocused) if self.active else pygame.Color(self.colornotfocused)

        if event.type == pygame.KEYDOWN and self.editable:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif len(self.text) < 2:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = pygame.font.SysFont('Arial', 13, True).render(self.text, True, self.color)

    def draw(self, screen):
        #width = max(2, self.txt_surface.get_width() + 6)
        #height = max(2, self.txt_surface.get_height() + 4)
        #print(width)
        #self.rect.w = width

        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+2))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
