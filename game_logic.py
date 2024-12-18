import pygame
import os
import image as img
from enemy import Enemy
import sequence as sqn
import sound as snd 
import random

HEIGHT= 700
WIDTH = 1400
POSITION = 250
FPS=60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 56)  # Standard-Schriftart, Größe 56

game_folder = os.path.dirname(__file__)

start_music_channel = snd.start_music.play()
start_music_channel = pygame.mixer.Channel(0)  # Reserviere Kanal 0
start_music_channel.play(snd.start_music)

def create_enemy(score, all_zombies, surface):
    if score < 1000:
        sprite_set = img.enemy_sprites_level_0  # Zombies bis Score 1000
        anim_name = "zombie_walk"

    elif score <2000:
        sprite_set = img.enemy_sprites_level_1  # Cowboys ab Score 1000
        anim_name = "cowboy_run"

    elif score < 3000:
        sprite_set = img.enemy_sprites_level_2
        anim_name = "robot_walk"

    elif score < 4000:
        sprite_set = img.enemy_sprites_level_3
        anim_name = "knight_walk"

    elif score < 5000:
        sprite_set = img.enemy_sprites_level_4
        anim_name = "santa_walk"

    elif score < 6000:
        sprite_set = img.enemy_sprites_level_5
        anim_name = "pumpkin_walk"

    elif score < 7000:
        sprite_set = img.enemy_sprites_level_6
        anim_name = "courli"

    elif score < 8500:
        sprite_set = img.enemy_sprites_level_6
        anim_name = "courli"

    enemy = Enemy(
        x=WIDTH + 100,
        y=HEIGHT - 192,
        surface=surface,
        sprite_charakter=sprite_set,
        anim_name=anim_name,
        hp=5,
    )
    all_zombies.add(enemy)

