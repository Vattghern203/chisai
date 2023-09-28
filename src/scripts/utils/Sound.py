import pygame

class SoundPlayer:
    def __init__(self):
        pygame.mixer.init()

    def play_sound(self, sound_path):
        sound = pygame.mixer.Sound(sound_path)
        sound.play()
