import pygame
from scripts.scenes.Scene import Scene
from scripts.elements.Object import Object
from scripts.utils.Music import MusicPlayer

import sys

class Menu(Scene):
    def __init__(self):
        super().__init__()

        self.bg = Object("src/assets/imgs/bg/menu.jpg", [0, 0], [self.all_sprites])

        self.music_player = MusicPlayer()
        self.music_path = "src/assets/music/when it's dark out.mp3"
        self.music_player.play_music(self.music_path) 

        # Additional initialization for the menu

    def next_scene(self):
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def events(self, event):
        # Handle menu-specific events

        pass

    def draw(self):
        super().draw()

        self.all_sprites.draw(self.display)

    def update(self):
        return super().update()