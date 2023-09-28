import pygame

from typing import Literal

from scripts.scenes.Menu import Menu
from scripts.scenes.Game import Game
from scripts.scenes.GameOver import GameOver

from scripts.settings import FPS, WIDTH, HEIGHT, TITLE, BG_COLOR

class StartGame:

    def __init__(self) -> None:
        
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        pygame.display.set_caption(TITLE)
        pygame.display.init()

        # It must be called before any Scene
        self.display = pygame.display.set_mode([WIDTH, HEIGHT])

        self.running = True
        self.clock = pygame.time.Clock()

        self.scene: Literal["menu", "game", "gameover"] = "game"
        self.current_scene = Game()

        self.target_fps = FPS

    def run(self):

        print(self.scene)

        while self.running:

            if self.scene == "menu" and self.current_scene.active == False:
                self.scene = "game"

                self.current_scene = Game()

            elif self.scene == "game" and self.current_scene.active == False:

                self.scene = "gameover"

                self.current_scene = GameOver()

            elif self.scene == "gameover" and self.current_scene.active == False:

                self.scene = "menu"
                self.current_scene = Menu()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                if event.type == pygame.K_e:

                    self.scene = "game"

                self.current_scene.events(event)

            self.display.fill(BG_COLOR)
            self.current_scene.draw()
            self.current_scene.update()

            pygame.display.flip()            