from scripts.Entity import Entity
from typing import List
from scripts.settings import TILE_SIZE, GRAVITY

import pygame
 # Define your gravity constant

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
            pygame.image.load(sprite_path).convert_alpha(), (TILE_SIZE * 4, TILE_SIZE * 4))

        self.speed = 5  # Adjust speed as needed
        self.health = 10  # Adjust health as needed
        self.attack_cooldown = 60  # Adjust as needed

        self.attack_duration = 3

        self.block_group = parameters["block_group"]
        self.player = parameters["player"]
        self.collision_group = parameters["collision_group"]

    def apply_gravity(self):
        self.direction.y += GRAVITY
        self.rect.move_ip(0, self.direction.y)

    def handle_collision(self):
        for block in self.collision_group:
            if block.rect.colliderect(self.rect):
                self.collision_math(block.rect)
    

    def follow_player(self, player):
        if player.rect.x < self.rect.x:
            self.direction.x = -self.speed
        elif player.rect.x > self.rect.x:
            self.direction.x = self.speed

        if player.rect.y < self.rect.y:
            self.direction.y = -self.speed
        elif player.rect.y > self.rect.y:
            self.direction.y = self.speed

    def update(self):
        self.attack_cooldown -= 1
        self.attack_duration -= 1
        if self.attack_duration == 0:
            self.attacking = False

        if self.attack_cooldown == 0:
            player = self.player  # Get the player object
            if player:
                self.follow_player(player)

        # Apply gravity
        self.apply_gravity()

        # Check for collision with ground
        self.handle_collision()

        # Add any additional boss-specific logic here

        super().update()

