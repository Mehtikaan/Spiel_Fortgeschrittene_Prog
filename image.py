import pygame
import os

# Pygame initialisieren
pygame.init()
pygame.display.init()
# Ein Display erstellen (kann minimal sein)
pygame.display.set_mode((800, 600))

game_folder = os.path.dirname(__file__)

#Bilder fÃ¼r level changer
enemy_sprites_level_0 = {
    #Gegner
    "zombie_walk1": pygame.image.load(os.path.join(game_folder, "_image","zombie_walk1.png")).convert_alpha(),
    "zombie_walk2": pygame.image.load(os.path.join(game_folder, "_image","zombie_walk2.png")).convert_alpha(),
    "zombie_walk3": pygame.image.load(os.path.join(game_folder, "_image","zombie_walk3.png")).convert_alpha(),
    "zombie_walk4": pygame.image.load(os.path.join(game_folder, "_image","zombie_walk4.png")).convert_alpha(),
    "zombie_walk5": pygame.image.load(os.path.join(game_folder, "_image","zombie_walk5.png")).convert_alpha(),
    "zombie_walk6": pygame.image.load(os.path.join(game_folder, "_image","zombie_walk6.png")).convert_alpha(),
    "zombie_walk7": pygame.image.load(os.path.join(game_folder, "_image","zombie_walk7.png")).convert_alpha(),
    "zombie_walk8": pygame.image.load(os.path.join(game_folder, "_image","zombie_walk8.png")).convert_alpha(),
    "zombie_walk9": pygame.image.load(os.path.join(game_folder, "_image","zombie_walk9.png")).convert_alpha(),
    "zombie_walk10": pygame.image.load(os.path.join(game_folder, "_image","zombie_walk10.png")).convert_alpha(),

    #Waffe

}
enemy_sprites_level_1 = {
    #Gegner
    "cowboy_run1": pygame.image.load(os.path.join(game_folder, "_image","cowboy_run1.png")).convert_alpha(),
    "cowboy_run2": pygame.image.load(os.path.join(game_folder, "_image","cowboy_run2.png")).convert_alpha(),
    "cowboy_run3": pygame.image.load(os.path.join(game_folder, "_image","cowboy_run3.png")).convert_alpha(),
    "cowboy_run4": pygame.image.load(os.path.join(game_folder, "_image","cowboy_run4.png")).convert_alpha(),
    "cowboy_run5": pygame.image.load(os.path.join(game_folder, "_image","cowboy_run5.png")).convert_alpha(),
    "cowboy_run6": pygame.image.load(os.path.join(game_folder, "_image","cowboy_run6.png")).convert_alpha(),
    "cowboy_run7": pygame.image.load(os.path.join(game_folder, "_image","cowboy_run7.png")).convert_alpha(),
    #Map Hintergrund


}

enemy_sprites_level_2 = {
    #Gegner
    "robot_walk1": pygame.image.load(os.path.join(game_folder, "_image","robot_walk1.png")).convert_alpha(),
    "robot_walk2": pygame.image.load(os.path.join(game_folder, "_image","robot_walk2.png")).convert_alpha(),
    "robot_walk3": pygame.image.load(os.path.join(game_folder, "_image","robot_walk3.png")).convert_alpha(),
    "robot_walk4": pygame.image.load(os.path.join(game_folder, "_image","robot_walk4.png")).convert_alpha(),
    "robot_walk5": pygame.image.load(os.path.join(game_folder, "_image","robot_walk5.png")).convert_alpha(),
    "robot_walk6": pygame.image.load(os.path.join(game_folder, "_image","robot_walk6.png")).convert_alpha(),
    #Map Hintergrund


}
enemy_sprites_level_3 = {
    #Gegner
    "knight_walk1": pygame.image.load(os.path.join(game_folder, "_image","knight_walk1.png")).convert_alpha(),
    "knight_walk2": pygame.image.load(os.path.join(game_folder, "_image","knight_walk2.png")).convert_alpha(),
    "knight_walk3": pygame.image.load(os.path.join(game_folder, "_image","knight_walk3.png")).convert_alpha(),
    "knight_walk4": pygame.image.load(os.path.join(game_folder, "_image","knight_walk4.png")).convert_alpha(),
    "knight_walk5": pygame.image.load(os.path.join(game_folder, "_image","knight_walk5.png")).convert_alpha(),
    "knight_walk6": pygame.image.load(os.path.join(game_folder, "_image","knight_walk6.png")).convert_alpha(),
    "knight_walk7": pygame.image.load(os.path.join(game_folder, "_image","knight_walk7.png")).convert_alpha(),
    #Map Hintergrund
}

enemy_sprites_level_4 = {
    #Gegner
    "santa_walk1": pygame.image.load(os.path.join(game_folder, "_image","santa_walk1.png")).convert_alpha(),
    "santa_walk2": pygame.image.load(os.path.join(game_folder, "_image","santa_walk2.png")).convert_alpha(),
    "santa_walk3": pygame.image.load(os.path.join(game_folder, "_image","santa_walk3.png")).convert_alpha(),
    "santa_walk4": pygame.image.load(os.path.join(game_folder, "_image","santa_walk4.png")).convert_alpha(),
    "santa_walk5": pygame.image.load(os.path.join(game_folder, "_image","santa_walk5.png")).convert_alpha(),
    "santa_walk6": pygame.image.load(os.path.join(game_folder, "_image","santa_walk6.png")).convert_alpha(),
    "santa_walk7": pygame.image.load(os.path.join(game_folder, "_image","santa_walk7.png")).convert_alpha(),
    "santa_walk8": pygame.image.load(os.path.join(game_folder, "_image","santa_walk8.png")).convert_alpha(),
    "santa_walk9": pygame.image.load(os.path.join(game_folder, "_image","santa_walk9.png")).convert_alpha(),
    "santa_walk10": pygame.image.load(os.path.join(game_folder, "_image","santa_walk10.png")).convert_alpha(),
    "santa_walk11": pygame.image.load(os.path.join(game_folder, "_image","santa_walk11.png")).convert_alpha(),
    #Map Hintergrund
}

enemy_sprites_level_5 = {
    #Gegner
    "pumpkin_walk1": pygame.image.load(os.path.join(game_folder, "_image","pumpkin_walk1.png")).convert_alpha(),
    "pumpkin_walk2": pygame.image.load(os.path.join(game_folder, "_image","pumpkin_walk2.png")).convert_alpha(),
    "pumpkin_walk3": pygame.image.load(os.path.join(game_folder, "_image","pumpkin_walk3.png")).convert_alpha(),
    "pumpkin_walk4": pygame.image.load(os.path.join(game_folder, "_image","pumpkin_walk4.png")).convert_alpha(),
    "pumpkin_walk5": pygame.image.load(os.path.join(game_folder, "_image","pumpkin_walk5.png")).convert_alpha(),
    "pumpkin_walk6": pygame.image.load(os.path.join(game_folder, "_image","pumpkin_walk6.png")).convert_alpha(),
    "pumpkin_walk7": pygame.image.load(os.path.join(game_folder, "_image","pumpkin_walk7.png")).convert_alpha(),
    "pumpkin_walk8": pygame.image.load(os.path.join(game_folder, "_image","pumpkin_walk8.png")).convert_alpha(),
    "pumpkin_walk9": pygame.image.load(os.path.join(game_folder, "_image","pumpkin_walk9.png")).convert_alpha(),
    "pumpkin_walk10": pygame.image.load(os.path.join(game_folder, "_image","pumpkin_walk10.png")).convert_alpha(),
    #Map Hintergrund
}

enemy_sprites_level_6 = {
    #Gegner
    "courli1": pygame.image.load(os.path.join(game_folder, "_image","courli1.png")).convert_alpha(),
    "courli2": pygame.image.load(os.path.join(game_folder, "_image","courli2.png")).convert_alpha(),
    "courli3": pygame.image.load(os.path.join(game_folder, "_image","courli3.png")).convert_alpha(),
    "courli4": pygame.image.load(os.path.join(game_folder, "_image","courli4.png")).convert_alpha(),

    #Map Hintergrund
}

enemy_sprites_level_endboss = {
    #Gegner
    "endboss1": pygame.image.load(os.path.join(game_folder, "_image","endboss1.png")).convert_alpha(),
    "endboss2": pygame.image.load(os.path.join(game_folder, "_image","endboss2.png")).convert_alpha(),
    "endboss3": pygame.image.load(os.path.join(game_folder, "_image","endboss3.png")).convert_alpha(),
    "endboss4": pygame.image.load(os.path.join(game_folder, "_image","endboss4.png")).convert_alpha(),
    "endboss5": pygame.image.load(os.path.join(game_folder, "_image","endboss5.png")).convert_alpha(),
    "endboss6": pygame.image.load(os.path.join(game_folder, "_image","endboss6.png")).convert_alpha(),
 

    #Map Hintergrund
}
