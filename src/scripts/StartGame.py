import pygame

from scripts.settings import FPS, WIDTH, HEIGHT

# Script Modules
from scripts.Entity import Entity

player = Entity(100, 100, 100, 100)

class StartGame:

    def __init__(self) -> None:
        
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.running = True
        self.clock = pygame.time.Clock()

        self.target_fps = FPS

        self.display = pygame.display.set_mode([WIDTH, HEIGHT])



    def run(self):

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    self.running = False

            self.display.fill((0, 0, 0))

            player.draw(screen=self.display)

            pygame.display.flip()            