from scripts.elements.Object import Object
from scripts.scenes.Scene import Scene
from scripts.utils.fade import Fade

from scripts.utils.Text import Text
from scripts.utils.Music import MusicPlayer

import random

from scripts.settings import DEATH_MESSAGE

class GameOver(Scene):
    def __init__(self):
        super().__init__()

        Fade(5)

        self.bg = Object("src/assets/imgs/bg/vasco.jpg", [0, 0], [self.all_sprites])

        self.text = Text(self.handle_death_text(), font_size=64, text_color=(255, 50, 50))

        # Additional initialization for the game over screen
        self.music_player = MusicPlayer()
        self.music_player.play_music("src/assets/music/sad_trumpet.mp3", loops=0)

        print(self.handle_death_text())


    def handle_death_text(self) -> str:

        idx = random.randint(0, len(DEATH_MESSAGE))

        return f"Você {DEATH_MESSAGE[idx].title()}!"


    def events(self, event):
        # Handle game over screen-specific events
        pass

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