import pygame


from scripts.settings import HEIGHT, WIDTH

class Text:

    def __init__(self, text_to_display:str, text_color, font_size=24, position=[WIDTH / 2, HEIGHT / 2]) -> None:
        
        self.display = pygame.display.get_surface()

        self.font = pygame.font.SysFont(None, font_size)

        self.text = self.font.render(text_to_display, True, text_color).convert_alpha()

        self.rect = self.text.get_rect(center=position)

        self.position = position

    def draw_center(self):
        self.display.blit(self.text, self.rect)

    def draw(self):

        self.display.blit(self.text, self.position)

    def update_text(self, text, color):

        self.text = self.font.render(text, True, color).convert_alpha()