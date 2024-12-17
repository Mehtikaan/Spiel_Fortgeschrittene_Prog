import pygame
import os
import image as img
from enemy import Enemy
import sequence as sqn
import sound as snd 

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

    
    enemy = Enemy(
        x=WIDTH + 100,
        y=HEIGHT - 192,
        surface=surface,
        sprite_charakter=sprite_set,
        anim_name=anim_name,
        hp=5,
    )
    all_zombies.add(enemy)

#Level Wechsler
current_level = 0

level_music = {
   # 0: "zombie_music.wav",
    1: os.path.join(game_folder, '_sounds',"cowboy_music.wav"),
    2: os.path.join(game_folder, '_sounds',"robot_music.wav"),
    3: os.path.join(game_folder, '_sounds',"knight_music.wav"),
    4: os.path.join(game_folder, '_sounds',"wind-blowing-sfx-12809.mp3"),
    5: os.path.join(game_folder, '_sounds',"pumpkin_music.wav"),
    6: os.path.join(game_folder, '_sounds',"courli_music.wav")
}

def level_changer(score, all_zombies, surface):
    global current_level, platform_image, background, level_music, start_music_channel


    level_texts = {
       1: "Wieso sehe ich nichts mehr ?!! Was passiert hier...?",
       2: "Puh war das heiß, ich verstehe nicht wo ich bin.",
       3: "Nicht schon wieder!!",
       4: "Frohe Weihnachten! Jetzt kommen die Santa-Gegner.",
       5: "Das Kürbislevel! Nichts für schwache Nerven.",
       6: "Warte mal..."    
    }


    if score >= 1000.0 and current_level == 0:
       if start_music_channel:  # Prüfen, ob Kanal existiert
        print("Stopping music on channel:", start_music_channel)
        start_music_channel.stop()
        start_music_channel = None
       else:
           print("start_music_channel does not exist or is None!")

    if score >= 1000 and current_level < 1:
       current_level = 1
       sqn.transition_sequence() 
       platform_image = img.platform_image_level_1
       background = img.background_level_1
       pygame.mixer.music.load(level_music[1])  # Lade Level-1-Musik
       pygame.mixer.music.play(-1)  # Endlosschleife
       sqn.fade(surface, BLACK, 1, fade_out=True, text=level_texts[1], font=font)
       for enemy in all_zombies:
           enemy.kill()
       return current_level, img.platform_image, img.background, level_music, start_music_channel

    elif score >= 2000 and current_level < 2 :
      current_level = 2
      sqn.transition_sequence() 
      platform_image = img.platform_image_level_2
      background = img.background_level_2
      pygame.mixer.music.load(level_music[2])  # Lade Level-2-Musik
      pygame.mixer.music.play(-1)
      sqn.fade(surface, BLACK, 1, fade_out=True, text=level_texts[2], font=font)
      for enemy in all_zombies:
           enemy.kill()
      return current_level, img.platform_image, img.background, level_music, start_music_channel
    
    elif score >= 3000 and current_level < 3:
       current_level = 3
       sqn.transition_sequence() 
       platform_image = img.platform_image_level_3
       background = img.background_level_3
       pygame.mixer.music.load(level_music[3])  # Lade Level-3-Musik
       pygame.mixer.music.play(-1)
       sqn.fade(surface, BLACK, 1, fade_out=True, text=level_texts[3], font=font)
       for enemy in all_zombies:
           enemy.kill()
       return current_level, img.platform_image, img.background, level_music, start_music_channel
       
    elif score >= 4000 and current_level < 4:
       current_level = 4
       sqn.transition_sequence() 
       platform_image = img.platform_image_level_4
       background = img.background_level_4
       pygame.mixer.music.load(level_music[4])  # Lade Level-4-Musik
       pygame.mixer.music.play(-1)
       sqn.fade(surface, BLACK, 1, fade_out=True, text=level_texts[4], font=font)  # Zeichne alle Sprites
       for enemy in all_zombies:
           enemy.kill()
       return current_level, img.platform_image, img.background, level_music, start_music_channel
    
    elif score >= 5000 and current_level < 5:
       current_level = 5
       sqn.transition_sequence() 
       platform_image = img.platform_image_level_5
       background = img.background_level_5
       pygame.mixer.music.load(level_music[5])  # Lade Level-5-Musik
       pygame.mixer.music.play(-1)
       sqn.fade(surface, BLACK, 1, fade_out=True, text=level_texts[5], font=font)
       for enemy in all_zombies:
           enemy.kill()
    
       return current_level, img.platform_image, img.background, level_music, start_music_channel

    elif score >= 6000 and current_level < 6:
       current_level = 6
       sqn.transition_sequence() 
       platform_image = img.platform_image_level_6
       background = img.background_level_6
       pygame.mixer.music.load(level_music[6])  # Lade Level-6-Musik
       pygame.mixer.music.play(-1)
       sqn.fade(surface, BLACK, 1, fade_out=True, text=level_texts[6], font=font)
       for enemy in all_zombies:
           enemy.kill()

    return current_level, img.platform_image, img.background, level_music, start_music_channel