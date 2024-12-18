import pygame
import os

pygame.mixer.init()
game_folder = os.path.dirname(__file__)


kunai_sound = pygame.mixer.Sound(os.path.join(game_folder, '_sounds', "kunai.wav"))
kunai_sound.set_volume(0.15)
jump_sound = pygame.mixer.Sound(os.path.join(game_folder, '_sounds', "grunting.wav"))
jump_sound.set_volume(0.15)
death_sound = pygame.mixer.Sound(os.path.join(game_folder, '_sounds','death_sound.wav'))
death_sound.set_volume(0.15)
krauss_attack = pygame.mixer.Sound(os.path.join(game_folder, '_sounds','you_got_it.wav'))
krauss_attack.set_volume(0.15)
welcome_sound = pygame.mixer.Sound(os.path.join(game_folder, '_sounds','welcome.wav'))
welcome_sound.set_volume(0.15)
start_music = pygame.mixer.Sound(os.path.join(game_folder, '_sounds', 'zombie_music.wav'))
start_music.set_volume(0.15)
portal_sound = pygame.mixer.Sound(os.path.join(game_folder, '_sounds', 'portal.wav'))
portal_sound.set_volume(0.15)