import pygame

class SoundPlayer:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(16)  # Set the number of sound channels

    def play_sound(self, sound_path, volume=0.5):
        try:
            sound = pygame.mixer.Sound(sound_path)
            sound.set_volume(volume)
            sound.get_raw()
            sound.play()
        except pygame.error as e:
            print(f"Error playing sound: {e}")