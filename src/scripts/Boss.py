from scripts.Entity import Entity
from typing import List
from scripts.settings import TILE_SIZE, GRAVITY, WIDTH

import pygame

class Boss(Entity):

    def __init__(
            self,
            position: List[int],
            sprite_path: str,
            groups:pygame.sprite.Group,
            parameters: dict
        ):

        super().__init__(position, sprite_path, groups, parameters)

        self.image = pygame.transform.scale(
            pygame.image.load(sprite_path).convert_alpha(), (256, 256))
    
        self.rect = self.image.get_rect(topleft=position)

        self.speed = 5  
        self.health = 10  
        self.attack_cooldown = 60

        self.attack_duration = 3

        self.block_group = parameters["block_group"]
        self.player = parameters["player"]
        self.collision_group = parameters["collision_group"]

        self.direction = pygame.math.Vector2(1, 0)

    def apply_gravity(self):
        self.rect.move_ip(0, self.direction.y)

    def handle_collision(self):
        for block in self.collision_group:
            if block.rect.colliderect(self.rect):
                self.collision_math(block.rect)

    def move(self):
        self.rect.x += self.direction.x * self.speed

        
        if self.rect.right >= WIDTH - self.rect.width:
            self.direction.x = -1

        if self.rect.left <= 0:
            self.direction.x = 1
    
    def follow_player(self):
        move_x = 0
        move_y = 0

        if self.player.rect.x < self.rect.x:
            move_x = 1
        elif self.player.rect.x > self.rect.x:
            move_x = -1

        if self.player.rect.y < self.rect.y:
            move_y = -1
        elif self.player.rect.y > self.rect.y:
            move_y = 1

        self.direction.x = move_x
        self.direction.y = move_y

    def update(self):
        self.apply_gravity()
        self.handle_collision()
        self.move()
        self.follow_player()

        #super().update()
