import pygame

class Entity:

    def __init__(self, x:int, y:int, width: float, height: float):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite = pygame.Surface((width, height))
        self.sprite.fill((255, 0, 0))

    def draw(self, screen: pygame.Surface):

        screen.blit(self.sprite, (self.x, self.y))

