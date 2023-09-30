import pygame
from scripts.scenes.Scene import Scene
from scripts.elements.Object import Object
from scripts.utils.Music import MusicPlayer
from scripts.Entity import GenericEntity
from scripts.Enemy import Enemy

from scripts.settings import HEIGHT, WIDTH, TILE_SIZE

from scripts.Player import Player


class Game(Scene):

    def __init__(self):
        super().__init__()

        self.bg = Object("src/assets/imgs/bg/muzamba.jpg", [0, 0], [self.all_sprites])

        self.enemy_sprites = pygame.sprite.Group()
        self.collision_group = pygame.sprite.Group()

        self.music_player = MusicPlayer()
        self.music_path = "src/assets/music/Debussy - Clair de Lune.mp3"
        self.music_player.play_music(self.music_path) 

        self.player = Player(
            position=[WIDTH / 10, HEIGHT / 2],
            sprite_path="src/assets/sprites/hero/hero.png", 
            groups=[self.all_sprites], 
            parameters={
                'block_group': self.block_group,
                'collision_group': self.collision_group
            }, 
        )

        self.enemy = Enemy(
            position=(100, 100), 
            sprite_path="src/assets/sprites/enemy/enemy.png", 
            groups=[self.all_sprites],  
            behavior="walk_lr",
        )

        self.enemy_up = Enemy(
            position=(400, 400), 
            sprite_path="src/assets/sprites/enemy/enemy.png", 
            groups=[self.all_sprites],  
            behavior="walk_td",
        )

        self.generate_terrain()

    def events(self, event):

        pass


    def generate_terrain(self):

        for i in range(20):

            GenericEntity(
                [
                    self.all_sprites,
                    self.block_group
                ],

                position = (
                    TILE_SIZE * i, (HEIGHT - TILE_SIZE)
                )
            )

    def draw(self):

        super().draw()

        self.all_sprites.draw(self.display)

    def update(self):

        self.all_sprites.update()