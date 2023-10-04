import pygame

from typing import List, Literal
from scripts.Entity import Entity

from scripts.settings import WIDTH, HEIGHT, TILE_SIZE

class Enemy(Entity):
    def __init__(self, 
                position: List[float], 
                sprite_path: str, 
                groups: pygame.sprite.Group,
                behavior: Literal[
                    "walk_lr",
                    "walk_td",
                    "shoot",
                    "follow",
                    "jump",
                    "explode"
                ],
                parameters: dict = {},
                ):
        
        super().__init__(position, sprite_path, groups, parameters)

        self.speed: float = 3  # Adjust speed as needed
        self.direction: pygame.math.Vector2 = pygame.math.Vector2(1, 0)  # Start by moving to the right

        self.behavior = behavior
        self.health = 1

        print(self.behavior)

    def handle_behavior(self):
        if self.behavior == "walk_lr":
            self.move()
        elif self.behavior == "walk_td":
            self.move_up_down()
        

    def move(self):
        self.rect.x += self.direction.x * self.speed

        # If the enemy reaches the right edge of the screen, reverse direction
        if self.rect.right >= WIDTH:
            self.direction.x = -1

        # If the enemy reaches the left edge of the screen, reverse direction
        if self.rect.left <= 0:
            self.direction.x = 1

    def move_up_down(self):
        self.rect.y += self.direction.y * self.speed

        # If the enemy reaches the bottom edge of the screen, reverse direction
        if self.rect.top > 0 + self.rect.height:
            self.direction.y = -1

        # If the enemy reaches the top edge of the screen, reverse direction
        if self.rect.bottom >= HEIGHT + self.rect.height:
            self.direction.y = 1

    def handle_altitude(self):
        # Check if the enemy is in the air (above the ground)
        if self.rect.y < HEIGHT - self.rect.height - TILE_SIZE:
            # Move the enemy downward until it hits the ground
            self.rect.y += self.speed  # You can adjust the speed as needed

    def update(self):
        self.handle_orientation()
        self.handle_behavior()
        self.handle_altitude()  # Call the altitude handling method
        # Implement any additional logic for the enemy's behavior


