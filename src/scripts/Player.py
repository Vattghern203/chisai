import pygame

from typing import List, Literal

from scripts.Entity import Entity

class Player(Entity):

    def __init__(
            self, 
            position:List[int], 
            sprite_path:str, 
            groups:pygame.sprite.Group(), 
            parameters: dict = {}
        ):

        super().__init__(position, sprite_path, groups, parameters)

        self.speed: int = 12
        
        self.mass: float | int = 5

        # Group Related

        self.block_group = parameters['block_group']
        self.collision_group = parameters['collision_group']

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


    def handle_collision_y(self):

        for block in self.block_group:

            if block.rect.colliderect(self.rect):

                if self.direction.y > 0:

                    self.direction.y = 0
                    self.rect.bottom = block.rect.top

                if self.direction.y < 0:

                    self.direction.y = 0
                    self.rect.top = block.rect.bottom

    
    def handle_collision_x(self):

        for block in self.block_group:

            if block.rect.colliderect(self.rect):

                if self.direction.x > 0:

                    self.rect.right = block.rect.left

                if self.direction.x < 0:

                    self.rect.left = block.rect.right


    def handle_phisycs(self):

        self.handle_collision_x()
        self.handle_collision_y()


    def update(self):
        self.move()
        self.input()
        self.handle_phisycs()
