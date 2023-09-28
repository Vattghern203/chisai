import pygame
from scripts.Entity import Entity

class Player(Entity):

    def __init__(self, position, sprite_path, groups, collision_group):
        super().__init__(position, sprite_path, groups, collision_group)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.direction.x = -1
            print("going left")
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

    def update(self):
        self.move()
        self.input()
        self.handle_colision()
        # Uncomment when there's ground
        # self.gravity_exists()
