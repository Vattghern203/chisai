import pygame

from typing import List, Literal

from scripts.Entity import Entity

class Player(Entity):

    def __init__(
            self, 
            position:List[int], 
            sprite_path:str, 
            groups:pygame.sprite.Group(), 
            collision_group:pygame.sprite.Group()
        ):

        super().__init__(position, sprite_path, groups, collision_group)

        self.speed: int = 12
        
        self.mass: float | int = 5

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:

            self.direction.x = -1
    
        elif keys[pygame.K_d]:

            self.direction.x = 1

        elif keys[pygame.K_s]:

            self.direction.y = 1

        elif keys[pygame.K_w]:

            self.direction.y = -1

        elif keys[pygame.K_SPACE]:

            self.direction.y -= self.jump_force  # Adjusted this line to apply an upward force
        else:

            self.direction.x = 0
            self.direction.y = 0

        # print(self.rect.x, self.rect.y)

    def update(self):
        self.move()
        self.input()
        self.handle_colision()
        # Uncomment when there's ground
        # self.gravity_exists()
