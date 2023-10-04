from scripts.elements.Object import Object
from scripts.scenes.Scene import Scene
from scripts.utils.fade import Fade
from scripts.elements.button import Button

from scripts.settings import HEIGHT, WIDTH, BUTTON_HEIGHT, BUTTON_WIDTH

from scripts.utils.Text import Text
from scripts.utils.Music import MusicPlayer

import random
import pygame
import sys

from scripts.settings import DEATH_MESSAGE

class GameOver(Scene):
    def __init__(self):
        super().__init__()

        Fade(5)

        self.bg = Object("src/assets/imgs/bg/gameover.png", [0, 0], [self.all_sprites])

        self.text = Text(self.handle_death_text(), font_size=64, text_color=(255, 50, 50))

        
        self.play_button = Button("src/assets/imgs/ui/play_again_btn.png", ((WIDTH - BUTTON_WIDTH) // 2), ((HEIGHT - BUTTON_HEIGHT) // 1.5), self.next_scene)


        self.quit_button = Button("src/assets/imgs/ui/quit_btn.png", ((WIDTH - BUTTON_WIDTH) // 2), ((HEIGHT - BUTTON_HEIGHT) // 1.15), self.quit_game)

        # Additional initialization for the game over screen
        self.music_player = MusicPlayer()
        self.music_player.play_music("src/assets/music/sad_trumpet.mp3", loops=0)

        self.all_sprites.add(self.play_button, self.quit_button)

        print(self.handle_death_text())

    def next_scene(self):
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()   


    def handle_death_text(self) -> str:

        idx = random.randint(0, len(DEATH_MESSAGE) - 1)

        return f"Você {DEATH_MESSAGE[idx].title()}!"


    def events(self, event):
        
        self.play_button.events(event)
        self.quit_button.events(event)
        return super().events(event)

    def draw(self):

        super().draw()
        self.all_sprites.draw(self.display)
        self.text.draw_center()
        # self.display.fill(0, 0, 0)
        # Additional drawing for the game over screen

    def update(self):
        super().update()

        self.all_sprites.update()
        # Additional update logic for the game over screen