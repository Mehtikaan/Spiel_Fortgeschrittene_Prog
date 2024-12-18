import pygame
import os


HEIGHT= 700
WIDTH = 1400
POSITION = 250
FPS=60


pygame.init()
pygame.display.init()
pygame.display.set_mode((WIDTH, HEIGHT))

game_folder = os.path.dirname(__file__)
icon = pygame.image.load(os.path.join(game_folder, "_image","ninja.png"))

background = pygame.image.load(os.path.join(game_folder, '_image', "zombie_map.png")).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_width = background.get_width()

start_background = pygame.image.load(os.path.join(game_folder, '_image', "exam_start.png")).convert()
start_background = pygame.transform.scale(start_background, (WIDTH, HEIGHT))


enemy_sprites_level_0 = {
    
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

    

}
enemy_sprites_level_1 = {
    
    "cowboy_run1": pygame.image.load(os.path.join(game_folder, "_image","cowboy_run1.png")).convert_alpha(),
    "cowboy_run2": pygame.image.load(os.path.join(game_folder, "_image","cowboy_run2.png")).convert_alpha(),
    "cowboy_run3": pygame.image.load(os.path.join(game_folder, "_image","cowboy_run3.png")).convert_alpha(),
    "cowboy_run4": pygame.image.load(os.path.join(game_folder, "_image","cowboy_run4.png")).convert_alpha(),
    "cowboy_run5": pygame.image.load(os.path.join(game_folder, "_image","cowboy_run5.png")).convert_alpha(),
    "cowboy_run6": pygame.image.load(os.path.join(game_folder, "_image","cowboy_run6.png")).convert_alpha(),
    "cowboy_run7": pygame.image.load(os.path.join(game_folder, "_image","cowboy_run7.png")).convert_alpha(),
    


}

enemy_sprites_level_2 = {
    "robot_walk1": pygame.image.load(os.path.join(game_folder, "_image","robot_walk1.png")).convert_alpha(),
    "robot_walk2": pygame.image.load(os.path.join(game_folder, "_image","robot_walk2.png")).convert_alpha(),
    "robot_walk3": pygame.image.load(os.path.join(game_folder, "_image","robot_walk3.png")).convert_alpha(),
    "robot_walk4": pygame.image.load(os.path.join(game_folder, "_image","robot_walk4.png")).convert_alpha(),
    "robot_walk5": pygame.image.load(os.path.join(game_folder, "_image","robot_walk5.png")).convert_alpha(),
    "robot_walk6": pygame.image.load(os.path.join(game_folder, "_image","robot_walk6.png")).convert_alpha(),
    


}
enemy_sprites_level_3 = {
    
    "knight_walk1": pygame.image.load(os.path.join(game_folder, "_image","knight_walk1.png")).convert_alpha(),
    "knight_walk2": pygame.image.load(os.path.join(game_folder, "_image","knight_walk2.png")).convert_alpha(),
    "knight_walk3": pygame.image.load(os.path.join(game_folder, "_image","knight_walk3.png")).convert_alpha(),
    "knight_walk4": pygame.image.load(os.path.join(game_folder, "_image","knight_walk4.png")).convert_alpha(),
    "knight_walk5": pygame.image.load(os.path.join(game_folder, "_image","knight_walk5.png")).convert_alpha(),
    "knight_walk6": pygame.image.load(os.path.join(game_folder, "_image","knight_walk6.png")).convert_alpha(),
    "knight_walk7": pygame.image.load(os.path.join(game_folder, "_image","knight_walk7.png")).convert_alpha(),
}


enemy_sprites_level_4 = {
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
}


enemy_sprites_level_5 = {
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
}


enemy_sprites_level_6 = {
    "courli1": pygame.image.load(os.path.join(game_folder, "_image","courli1.png")).convert_alpha(),
    "courli2": pygame.image.load(os.path.join(game_folder, "_image","courli2.png")).convert_alpha(),
    "courli3": pygame.image.load(os.path.join(game_folder, "_image","courli3.png")).convert_alpha(),
    "courli4": pygame.image.load(os.path.join(game_folder, "_image","courli4.png")).convert_alpha(),

}


enemy_sprites_level_endboss = {
    
    "endboss1": pygame.image.load(os.path.join(game_folder, "_image","endboss1.png")).convert_alpha(),
    "endboss2": pygame.image.load(os.path.join(game_folder, "_image","endboss2.png")).convert_alpha(),
    "endboss3": pygame.image.load(os.path.join(game_folder, "_image","endboss3.png")).convert_alpha(),
    "endboss4": pygame.image.load(os.path.join(game_folder, "_image","endboss4.png")).convert_alpha(),
    "endboss5": pygame.image.load(os.path.join(game_folder, "_image","endboss5.png")).convert_alpha(),
    "endboss6": pygame.image.load(os.path.join(game_folder, "_image","endboss6.png")).convert_alpha(),
 
}


background_level_0 = pygame.image.load(os.path.join(game_folder, '_image', "zombie_map.png")).convert()
background_level_0 = pygame.transform.scale(background_level_0, (WIDTH, HEIGHT))

background_level_1 = pygame.image.load(os.path.join(game_folder, '_image', "desert.png")).convert()
background_level_1 = pygame.transform.scale(background_level_1, (WIDTH, HEIGHT))

background_level_2 = pygame.image.load(os.path.join(game_folder, '_image', "robot_map.png")).convert()
background_level_2 = pygame.transform.scale(background_level_2, (WIDTH, HEIGHT))

background_level_3 = pygame.image.load(os.path.join(game_folder, '_image', "knight_map.png")).convert()
background_level_3 = pygame.transform.scale(background_level_3, (WIDTH, HEIGHT))

background_level_4 = pygame.image.load(os.path.join(game_folder, '_image', "santa_map.png")).convert()
background_level_4 = pygame.transform.scale(background_level_4, (WIDTH, HEIGHT))

background_level_5 = pygame.image.load(os.path.join(game_folder, '_image', "pumpkin_map.png")).convert()
background_level_5 = pygame.transform.scale(background_level_5, (WIDTH, HEIGHT))

background_level_6 = pygame.image.load(os.path.join(game_folder, '_image', "courli_map.png")).convert()
background_level_6 = pygame.transform.scale(background_level_6, (WIDTH, HEIGHT))


platform_width = 1400
platform_height = 150
platform_image = pygame.image.load(os.path.join(game_folder, "_image", "stone_tile.png")).convert_alpha()
platform_image = pygame.transform.scale(platform_image, (platform_width, platform_height))

platform_image_level_1 = pygame.image.load(os.path.join(game_folder, "_image", "sand_tile.png")).convert_alpha()
platform_image_level_1 = pygame.transform.scale(platform_image_level_1, (1400, 150))

platform_image_level_2 = pygame.image.load(os.path.join(game_folder, "_image", "robot_tile.png")).convert_alpha()
platform_image_level_2 = pygame.transform.scale(platform_image_level_2, (1400, 150))

platform_image_level_3 = pygame.image.load(os.path.join(game_folder, "_image", "stone_tile.png")).convert_alpha()
platform_image_level_3 = pygame.transform.scale(platform_image_level_3, (1400, 150))

platform_image_level_4 = pygame.image.load(os.path.join(game_folder, "_image", "santa_tile.png")).convert_alpha()
platform_image_level_4 = pygame.transform.scale(platform_image_level_4, (1400, 150))

platform_image_level_5 = pygame.image.load(os.path.join(game_folder, "_image", "grave_tile.png")).convert_alpha()
platform_image_level_5 = pygame.transform.scale(platform_image_level_5, (1400, 150))

platform_image_level_6 = pygame.image.load(os.path.join(game_folder, "_image", "dino_tile.png")).convert_alpha()
platform_image_level_6 = pygame.transform.scale(platform_image_level_6, (1400, 150))

trap_image = pygame.image.load(os.path.join(game_folder, '_image', "flame.png")).convert_alpha()
