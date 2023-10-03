import pygame
import random
from scripts.elements.Object import Object
from scripts.Enemy import Enemy
from scripts.Entity import GenericEntity
from scripts.Player import Player
from scripts.scenes.Scene import Scene
from scripts.settings import HEIGHT, TILE_SIZE, WIDTH
from scripts.utils.Music import MusicPlayer
from scripts.utils.Sound import SoundPlayer

import time

from typing import Literal

class Game(Scene):
    def __init__(self):
        super().__init__()

        self.bg = Object("src/assets/imgs/bg/bg.png", [0, 0], [self.all_sprites])

        self.enemy_sprites = pygame.sprite.Group()
        self.collision_group = pygame.sprite.Group()

        self.sound_player = SoundPlayer()

        self.music_player = MusicPlayer()
        self.music_path = "src/assets/music/Debussy - Clair de Lune.mp3"
        self.music_player.play_music(self.music_path)

        self.enemy_spawn_timer = 0
        self.spawn_interval = random.randint(200, 400)  # Initial spawn interval (adjust as needed)

        self.player = Player(
            position=[WIDTH / 10, HEIGHT / 2],
            sprite_path="src/assets/sprites/hero/hero.png",
            groups=[self.all_sprites],
            parameters={
                'block_group': self.block_group,
                'collision_group': self.collision_group,
                'enemy_sprites': self.enemy_sprites
            },
        )

        self.generate_terrain()


    # DEATH ------------------------------------------------------------


    def handle_death(self, death_condition: Literal["fall", "attack"]):

        if death_condition == "attack":

            self.sound_player.play_sound("src/assets/sounds/faliceu.wav")

        elif death_condition == "fall":

            self.sound_player.play_sound("src/assets/sounds/wilhelmscream.wav")
            #print('dyiiiiiiiiiiiiiiiiiiiiiiiiing')

        self.player.kill()

        time.sleep(1.15)

        self.active = False


    
    def gameover(self):

        death_condition: Literal["fall", "attack"] = None 

        if self.player.health <= 0:

            death_condition = 'attack'

            self.handle_death(death_condition)     
            
        elif self.player.rect.y > HEIGHT + 200:

            death_condition = "fall"

            self.handle_death(death_condition)

    def spawn_enemy(self):
        # Create a new enemy instance and add it to the groups

        Enemy(
            position=(random.randint(100, WIDTH - 666), random.randint(100, HEIGHT - 100)),
            sprite_path="src/assets/sprites/enemy/enemy.png",
            groups=[self.all_sprites, self.enemy_sprites, self.collision_group],
            behavior="walk_lr",
        )

    def generate_terrain(self):
        for i in range(20):
            GenericEntity(
                [
                    self.all_sprites,
                    self.block_group,
                    self.collision_group
                ],
                sprite_path="src/assets/textures/grass.png",
                position=(
                    TILE_SIZE * i, (HEIGHT - TILE_SIZE)
                )
            )

    def update(self):
        super().update()

        self.gameover()

        # Update the timer
        self.enemy_spawn_timer += 1

        # Check if it's time to spawn a new enemy
        if self.enemy_spawn_timer >= self.spawn_interval:
            self.spawn_enemy()
            # Reset the timer and generate a new spawn interval
            self.enemy_spawn_timer = 0
            self.spawn_interval = random.randint(200, 400)  # Adjust the range as needed