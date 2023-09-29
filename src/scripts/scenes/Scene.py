import pygame

from scripts.settings import BG_COLOR

from scripts.utils.fade import Fade
from scripts.utils.Music import MusicPlayer

class Scene:

    def __init__(self):
        
        self.display = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.terrain_sprites = pygame.sprite.Group()

        self.active = True

        self.fade = Fade(5)

    def events(self, event):
        pass

    def draw(self):

        self.all_sprites.draw(self.display)
        self.terrain_sprites.draw(self.display)
        self.display.fill(BG_COLOR)

    def update(self):
        
        self.fade.draw()
        self.all_sprites.update()
        self.terrain_sprites.update()
        