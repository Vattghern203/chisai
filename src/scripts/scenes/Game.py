import pygame
from scripts.scenes.Scene import Scene
from scripts.elements.Object import Object
from scripts.utils.Music import MusicPlayer
from scripts.Entity import GenericEntity

from scripts.settings import HEIGHT, WIDTH, TILE_SIZE

from scripts.Player import Player


class Game(Scene):

    def __init__(self):
        super().__init__()

        self.bg = Object("src/assets/imgs/bg/muzamba.jpg", [0, 0], [self.all_sprites])

        self.collision_group = pygame.sprite.Group()

        self.music_player = MusicPlayer()
        self.music_path = "src/assets/music/Debussy - Clair de Lune.mp3"
        self.music_player.play_music(self.music_path) 

        self.player = Player(position=[WIDTH / 10, HEIGHT / 2], sprite_path="src/assets/sprites/hero/hero.png", groups=self.all_sprites, collision_group=self.collision_group)

    def events(self, event):

        pass


    def generate_terrain(self):

        for i in range(10):

            GenericEntity(self.terrain_sprites, position=(i * 64, HEIGHT))

    def draw(self):

        super().draw()

        self.all_sprites.draw(self.display)
        self.terrain_sprites.draw(self.display)
        self.generate_terrain()

    def update(self):

        self.all_sprites.update()
        self.terrain_sprites.update()