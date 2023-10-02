import pygame

class Button:
    def __init__(self, image_normal, image_hover, x, y, call_back):
        self.display = pygame.display.get_surface()
        self.image_normal = pygame.image.load(image_normal)
        self.image = self.image_normal
        self.rect = self.image.get_rect(topleft=(x, y))
        self.call_back = call_back

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.image = self.image_hover
            else:
                self.image = self.image_normal

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.call_back()

    def draw(self):
        self.display.blit(self.image, self.rect.topleft)