from typing import List, Literal

import pygame

from scripts.settings import HEIGHT, TILE_SIZE, GRAVITY, TERMINAL_VELOCITY

# Entity represents a moving character

class Entity(pygame.sprite.Sprite):

    def __init__(
                self, 
                position:List[float | int], 
                sprite_path:str, 
                groups,
                parameters: dict = {}
            ):

        super().__init__(groups)

        # Position ----------------------------------------

        self.position: List[float | int] = position

        # Sprite ----------------------------------------
        self.orientation: Literal["horizontal", "vertical"] = "vertical"

        self.sprite_orientation: dict = {
            "left": False,
            "right": True,
            "top": False,
            "bottom": False
        }

        self.image = pygame.transform.scale(pygame.image.load(sprite_path).convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.all_sprites = groups

        self.rect = self.image.get_rect(topleft=position)

        # Movimentation ----------------------------------------

        self.direction = pygame.math.Vector2()
        self.speed: int = 1

        # Physics ----------------------------------------

        self.mass = 2

        self.jump_force: int = 20

        self.touching_ground: bool = False

        self.terminal_velocity: float | int = self.mass * TERMINAL_VELOCITY

        self.gravitacional_force: float | int = GRAVITY * self.mass

        self.health: int = 5

    def move(self):

        self.direction.y += self.gravitacional_force
        
        # Determines a terminal velocity to avoid physics problem, and the risk of creating portals to another worlds and this kind of stuff

        if self.direction.y > self.terminal_velocity:

            self.direction.y = self.terminal_velocity

        self.rect.x += self.direction.x * self.speed

        self.rect.y += self.direction.y * self.speed

    def handle_orientation(self):

        if self.direction.x != 0:

            self.orientation = "horizontal"

        elif self.direction.y != 0:

            self.orientation = "vertical"


class GenericEntity(pygame.sprite.Sprite):

    def __init__(
            self, 
            groups:pygame.sprite.Group, 
            image = pygame.Surface((TILE_SIZE, TILE_SIZE)),
            sprite_path = None,
            position = (HEIGHT, 0)
        ):
        
        super().__init__(groups)

        if sprite_path:

            self.image = pygame.transform.scale(
                pygame.image.load(sprite_path).convert_alpha(), (TILE_SIZE, TILE_SIZE)
            )

        else:

            self.image = image

        self.rect = self.image.get_rect(topleft=position)