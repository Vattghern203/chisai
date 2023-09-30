import pygame

from typing import List, Literal
from scripts.Entity import Entity

from scripts.settings import WIDTH, HEIGHT

class Enemy(Entity):

    def __init__(self, 
                position: List[float], 
                sprite_path: str, 
                groups: pygame.sprite.Group,
                behavior:Literal[
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

        print(self.behavior)


    def handle_behavior(self):
        if self.behavior == "walk_lr":
            
            self.move()

        elif self.behavior == "walk_td":

            self.move_up_down()

        elif self.behavior == "shoot":
            # Add the code for shooting behavior here
            pass

        elif self.behavior == "follow":
            # Add the code for following behavior here
            pass

        elif self.behavior == "jump":
            # Add the code for jumping behavior here
            pass

        elif self.behavior == "explode":
            # Add the code for exploding behavior here
            pass
        

    def move(self):
        self.rect.x += self.direction.x * self.speed
        #self.rect.y += self.direction.y * self.speed

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

        #print(self.rect.x, self.rect.y)


    def update(self):
        self.handle_behavior()
        # Implement any additional logic for the enemy's behavior

