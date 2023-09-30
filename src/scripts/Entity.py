from typing import List, Literal

import pygame

from scripts.settings import HEIGHT, TILE_SIZE, WIDTH, GRAVITY

# Entity represents a moving character

class Entity(pygame.sprite.Sprite):

    def __init__(
                self, 
                position:List[float | int], 
                sprite_path:str, 
                groups,
                parameters: dict
            ):

        super().__init__(groups)

        # Position

        self.position: List[float | int] = position

        # Sprite

        self.image = pygame.transform.scale(pygame.image.load(sprite_path).convert_alpha(), (TILE_SIZE, TILE_SIZE))

        self.orientation: Literal["horizontal", "vertical"] = "vertical"

        self.rect = self.image.get_rect(topleft=position)
        self.all_sprites = groups

        # Movimentation

        self.direction = pygame.math.Vector2()
        self.speed: int = 6

        # Physics

        self.mass = 5
        self.jump_force: int = 16
        self.touching_ground: bool = False

        self.health: int | float = 5

    def move(self):

        self.direction.y += GRAVITY * self.mass

        self.rect.x += self.direction.x * self.speed

        self.orientation = "horizontal"

        self.rect.y += self.direction.y * self.speed

        self.orientation = "vertical"

    def gravity_exists(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        print('Newton Sucks!')


class GenericEntity(pygame.sprite.Sprite):

    def __init__(
            self, 
            groups:pygame.sprite.Group(), 
            image = pygame.Surface((TILE_SIZE, TILE_SIZE)), 
            position = (HEIGHT, 0)
        ):

        super().__init__(groups)

        self.image = image
        self.rect = self.image.get_rect(topleft=position)