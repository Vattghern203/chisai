import pygame
from scripts.scenes.Scene import Scene
from scripts.elements.Object import Object
from scripts.utils.Music import MusicPlayer
from scripts.elements.button import Button


import sys


class Menu(Scene):
    def __init__(self):
        super().__init__()

        self.bg = Object("src/assets/imgs/bg/menu_title.png", [0, 0], [self.all_sprites])

        self.music_player = MusicPlayer()
        self.music_path = "src/assets/music/when it's dark out.mp3"
        self.music_player.play_music(self.music_path) 

        self.play_button = Button("src/assets/imgs/ui/play_btn.png",64, 380, self.next_scene)
        self.quit_button = Button("src/assets/imgs/ui/quit_btn.png", 64, 500, self.quit_game)

        self.all_sprites.add(self.play_button, self.quit_button)

        # Additional initialization for the menu

    def next_scene(self):
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def events(self, event):
        self.quit_button.events(event)
        self.play_button.events(event)
        return super().events(event)

    def draw(self):
        super().draw()

        self.all_sprites.draw(self.display)

    def update(self):
        return super().update()