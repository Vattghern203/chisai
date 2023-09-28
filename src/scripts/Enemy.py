import pygame

from typing import List
from scripts.Entity import Entity

from scripts.settings import WIDTH

class Enemy(Entity):

    def __init__(self, position: List[float], sprite_path: str, groups: pygame.sprite.Group, collision_group: pygame.sprite.Group):
        super().__init__(position, sprite_path, groups, collision_group)

        self.speed: float = 3  # Adjust speed as needed
        self.direction: pygame.math.Vector2 = pygame.math.Vector2(1, 0)  # Start by moving to the right

    def move(self):
        self.rect.x += self.direction.x * self.speed

        # If the enemy reaches the right edge of the screen, reverse direction
        if self.rect.right >= WIDTH:
            self.direction.x = -1

        # If the enemy reaches the left edge of the screen, reverse direction
        if self.rect.left <= 0:
            self.direction.x = 1

    def update(self):
        self.move()
        # Implement any additional logic for the enemy's behavior

