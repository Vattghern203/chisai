import pygame
from scripts.scenes.Scene import Scene
from scripts.elements.Object import Object
from scripts.utils.Music import MusicPlayer

from scripts.Player import Player


class Game(Scene):

    def __init__(self):
        super().__init__()

        self.bg = Object("src/assets/imgs/bg/muzamba.jpg", [0, 0], [self.all_sprites])

        self.collision_group = pygame.sprite.Group()

        self.music_player = MusicPlayer()
        self.music_path = "src/assets/music/Debussy - Clair de Lune.mp3"
        self.music_player.play_music(self.music_path) 

        self.player = Player(position=[100, 100], sprite_path="src/assets/sprites/hero/hero.png", groups=self.all_sprites, collision_group=self.collision_group)

    def events(self, event):

        pass

    def draw(self):

        super().draw()

        self.all_sprites.draw(self.display)

    def update(self):

        self.all_sprites.update()