import pygame
from typing import List

class Object(pygame.sprite.Sprite):

    def __init__(self, img_path:str, position:List[int], *groups: pygame.sprite.Group()) -> None:
        super().__init__(*groups)

        self.image = pygame.image.load(img_path).convert()
        self.rect = self.image.get_rect(topleft=position)
        self.groups = groups