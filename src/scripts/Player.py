from typing import List
import pygame
from scripts.Entity import Entity

from scripts.utils.EventHandler import EventHandler

class Player(Entity):

    def __init__(
            self, 
            position:List[int], 
            sprite_path:str, 
            groups:pygame.sprite.Group(), 
            parameters: dict = {}
        ):

        super().__init__(position, sprite_path, groups, parameters)

        self.speed: int = 6
        
        self.mass: float | int = 10

        # Group Related

        self.block_group = parameters['block_group']
        self.collision_group = parameters["collision_group"]


    def input(self):
        keys = pygame.key.get_pressed()

        move_x = 0
        move_y = 0

        if keys[pygame.K_a]:
            move_x = -1

        elif keys[pygame.K_d]:
            move_x = 1

        if keys[pygame.K_s]:
            move_y = 1

        if self.touching_ground == True and EventHandler.keydown(pygame.K_SPACE):
            
            self.touching_ground = False

            move_y -= self.jump_force


        self.direction.x = move_x
        self.direction.y = move_y


    def collision_math(self, rect):
        overlap_x = min(self.rect.right, rect.right) - max(self.rect.left, rect.left)

        overlap_y = min(self.rect.bottom, rect.bottom) - max(self.rect.top, rect.top)

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


    def handle_collision(self):

        for block in self.collision_group:

            if block.rect.colliderect(self.rect):

                self.collision_math(block.rect)


    def handle_physics(self):

        self.handle_orientation()
        #self.handle_sprite_flip()
        self.handle_collision()


    def update(self):

        self.input()
        self.move()
        self.handle_physics()
        super().update()
