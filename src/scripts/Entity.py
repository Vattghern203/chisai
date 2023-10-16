from typing import List, Literal

import pygame

from scripts.settings import HEIGHT, TILE_SIZE, GRAVITY, TERMINAL_VELOCITY

import math


class Entity(pygame.sprite.Sprite):

    def __init__(
        self,
        position: List[float | int],
        sprite_path: str,
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

        self.current_sprite_orientation: Literal["left", "right"] = "right"

        self.image = pygame.transform.scale(pygame.image.load(
            sprite_path).convert_alpha(), (TILE_SIZE, TILE_SIZE))

        self.mask = pygame.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()

        self.all_sprites = groups

        self.rect = self.image.get_rect(topleft=position)

        # Movimentation ----------------------------------------

        self.direction = pygame.math.Vector2()
        self.speed: int = 1

        # Physics ----------------------------------------

        self.mass = 2

        self.jump_force: int = 48

        self.touching_ground: bool = False

        self.terminal_velocity: float | int = self.mass * TERMINAL_VELOCITY

        self.gravitacional_force: float | int = GRAVITY * self.mass

        self.health: 1

    def move(self):

        self.direction.y += self.gravitacional_force

        # Determines a terminal velocity to avoid physics problem, and the risk of creating portals to another worlds and this kind of stuff

        if self.direction.y > self.terminal_velocity:

            self.direction.y = self.terminal_velocity

        self.rect.x += self.direction.x * self.speed

        self.rect.y += self.direction.y * self.speed

    def handle_orientation(self):

        if self.direction.x < 0:

            self.sprite_orientation["left"] = True
            self.sprite_orientation["right"] = False
            self.current_sprite_orientation = "left"

        elif self.direction.x > 0:

            self.sprite_orientation["left"] = False
            self.sprite_orientation["right"] = True
            self.current_sprite_orientation = "right"

        else:

            self.sprite_orientation["left"] = False
            self.sprite_orientation["right"] = True
            self.current_sprite_orientation = "right"

        if self.direction.y != 0:

            self.orientation = "vertical"

        else:
            self.orientation = "horizontal"

        self.handle_sprite_orientation()



    def handle_sprite_orientation(self) -> None:

        print('Current Sprite Orientation', self.sprite_orientation)

        if (self.sprite_orientation["right"] and not (self.current_sprite_orientation == "right")) or (self.sprite_orientation["left"] and not (self.current_sprite_orientation == "left")):

            self.flip_sprite()

        if self.sprite_orientation["left"] and not (self.sprite_orientation["right"]):

            self.flip_sprite()

        else: pass

    def flip_sprite(self) -> None:

        self.image = pygame.transform.flip(self.image, True, False)

    def collision_math(self, rect):
        overlap_x = min(self.rect.right, rect.right) - \
            max(self.rect.left, rect.left)
        overlap_y = min(self.rect.bottom, rect.bottom) - \
            max(self.rect.top, rect.top)

        if overlap_x < overlap_y:

            if self.rect.left < rect.left and self.direction.x > 0:
                self.rect.right = rect.left
            elif self.rect.right > rect.right and self.direction.x < 0:
                self.rect.left = rect.right
            self.direction.x = 0
        else:
            if self.rect.top < rect.top and self.direction.y > 0:
                self.rect.bottom = rect.top
                self.touching_ground = True
            elif self.rect.bottom > rect.bottom and self.direction.y < 0:
                self.rect.top = rect.bottom
            self.direction.y = 0

    def distance_math(self, second_entity: pygame.Surface):

        distance = math.sqrt(
            (second_entity.rect.x - self.rect.x) ** 2 +
            (second_entity.rect.y - self.rect.x) ** 2
        )

        print(distance)


class GenericEntity(pygame.sprite.Sprite):

    def __init__(
        self,
        groups: pygame.sprite.Group,
        image=pygame.Surface((TILE_SIZE, TILE_SIZE)),
        sprite_path=None,
        position=(HEIGHT, 0)
    ):

        super().__init__(groups)

        if sprite_path:

            self.image = pygame.transform.scale(
                pygame.image.load(
                    sprite_path).convert_alpha(), (TILE_SIZE, TILE_SIZE)
            )

        else:

            self.image = image

        self.rect = self.image.get_rect(topleft=position)
