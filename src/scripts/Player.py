import pygame
from typing import List
from scripts.Entity import Entity
from scripts.utils.EventHandler import EventHandler
from scripts.settings import TILE_SIZE, GRAVITY

class Player(Entity):
    def __init__(
            self,
            position: List[int],
            sprite_path: str,
            groups: pygame.sprite.Group(),
            parameters: dict = {}
    ):
        super().__init__(position, sprite_path, groups, parameters)
        self.speed: int = 6
        self.alive: bool = True
        self.mass: float | int = 10
        self.health: int = 5

        # Group Related
        self.block_group = parameters['block_group']
        self.collision_group = parameters["collision_group"]
        self.enemy_group = parameters["enemy_sprites"]
        self.minion_counter = parameters["minion_counter"]
        self.boss_group = parameters["boss_group"]

        self.attack_duration = 0
        self.attacking = False
        self.attack_cooldown = 0
        self.attack_cooldown_duration = 30  # Adjust as needed

        self.jump_count = 0
        self.max_jump_count = 2




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

        if keys[pygame.K_e]:
            self.handle_attack()

        if (self.touching_ground == True and EventHandler.keydown(pygame.K_SPACE) and self.jump_count < self.max_jump_count):

            self.touching_ground = False

            move_y = -self.jump_force

            self.jump_count += 1

            print(self.jump_count)

        elif self.jump_count == 1 and EventHandler.keydown(pygame.K_SPACE):

            self.jump_count += 1
            print(self.jump_count)

            move_y -= self.jump_force

            self.jump_count = 0

        if self.jump_count == 2 and self.touching_ground == True:

            self.jump_count = 0

        self.direction.x = move_x
        self.direction.y = move_y

    def handle_collision(self):
        for block in self.collision_group:
            if block.rect.colliderect(self.rect):
                self.collision_math(block.rect)

    def handle_collision_with_enemy(self):
        for sprite in self.enemy_group:
            if sprite.rect.colliderect(self.rect):
                self.collision_math(sprite.rect)
                if self.attacking:
                    print('Hitted', sprite)
                    sprite.health -= 1

                    self.minion_counter -= 1

                    if sprite.health <= 0:

                        sprite.kill()

                    print(self.minion_counter, 'remaining')

                else:
                    self.health -= 1
                    self.rect.x += 50
                    self.rect.y -= 30
                    print("Don't touch me!")
                    print(self.health)

    def handle_attack(self):
        if not self.attacking and self.attack_cooldown <= 0:
            self.attacking = True
            self.attack_duration = 20  # Adjust the duration of the attack animation

            # Play attack animation and sound effects here

            self.attack_cooldown = self.attack_cooldown_duration

    def handle_physics(self):
        self.handle_orientation()
        # self.handle_sprite_flip()
        self.handle_collision()
        self.handle_collision_with_enemy()


    def update(self):
        self.attack_cooldown -= 1
        self.attack_duration -= 1
        if self.attack_duration == 0:
            self.attacking = False

        self.input()
        self.move()
        self.handle_physics()
        super().update()
