import pygame

from scripts.elements.Object import Object

class Button(Object):
    def __init__(self, image_normal, x, y, call_back):

        super().__init__(image_normal, [x, y])

        self.display = pygame.display.get_surface()
        self.image_normal = pygame.transform.scale(pygame.image.load(image_normal).convert_alpha(), (256, 144))
        self.image = self.image_normal
        self.rect = self.image.get_rect(topleft=(x, y))
        self.call_back = call_back

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.image = self.image_normal
            else:
                self.image = self.image_normal

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.call_back()

    def draw(self):
        self.display.blit(self.image, self.rect.topleft)