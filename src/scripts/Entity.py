import pygame

from typing import Any, List

from scripts.settings import WIDTH, HEIGHT, TILE_SIZE

# Entity represents a moving character

class Entity(pygame.sprite.Sprite):

    def __init__(self, position:List[float | int], sprite_path:str, groups:pygame.sprite.Group(), collision_group:pygame.sprite.Group()):

        super().__init__(groups, collision_group)

        resized_img = pygame.transform.scale(pygame.image.load(sprite_path).convert_alpha(), (TILE_SIZE, TILE_SIZE))

        self.position = position
        self.image = resized_img

        self.rect = self.image.get_rect(topleft=position)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.jump_force = 16
        self.gravity = 0.6
        self.touching_ground = False

        self.all_sprites = groups
        self.colision_group = collision_group


    def move(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def gravity_exists(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        print('Newton Sucks!')


    # Handle the colison of each entity
    def handle_colision(self):

        """ collisions = pygame.sprite.spritecollide(self, self.colision_group, False)

        for collision in collisions:

            print(collision) """
        
        for sprite in self.colision_group:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    print('out of y')

                if self.direction.x < 0 or self.direction.x > WIDTH:

                    self.position = (0, 0)

    def handle_flip(self):
        pass


class GenericEntity(pygame.sprite.Sprite):

    def __init__(self, groups, image = pygame.Surface((TILE_SIZE, TILE_SIZE)), position = (HEIGHT, 0)) -> None:
        super().__init__(groups)

        self.image = image
        self.rect = self.image.get_rect(topleft=position)