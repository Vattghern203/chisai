import pygame
import cv2
from scripts.scenes.Scene import Scene
from scripts.elements.Object import Object
from scripts.utils.Music import MusicPlayer
from scripts.StartGame import *

import sys

class Cutscene(Scene):
    def __init__(self):
        super().__init__()

        self.music_player = MusicPlayer()
        self.music_path = "src/assets/music/startcutscene.mp3"
        self.music_player.play_music(self.music_path)

        cap = cv2.VideoCapture('src/assets/imgs/cutscene/startcut.mp4')
        success, img = cap.read()
        shape = img.shape[1::-1]
        wn = pygame.display.set_mode(shape)
        clock = pygame.time.Clock()

        while(cap.isOpened()):
            clock.tick(15000)
            success, img = cap.read()

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        success = False
                        pygame.quit()

            if success:

                wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
                pygame.display.update()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

            
            self.active = False
            

        
