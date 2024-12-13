import pygame
import os
import math
import configparser as cp
import config_einstellungen as bib
from charakter import Charakter, Waffe,Bullet
import animationen as am
from enmy import Enmy  # Importiere die Enmy-Klasse
import pygame.font
from sequenz import wrap_text
import random


# Konfiguration laden oder erstellen
config = cp.ConfigParser()
if not config.read("config_game.ini"):
    print("Erstelle Konfigurationsdatei...")
    bib.erstelle_config_datei()

config.read("config_game.ini")

try:
    HEIGHT = int(config.get("Fenster", "height"))
    WIDTH = int(config.get("Fenster", "width"))
    FPS = int(config.get("FPS", "fps"))
except Exception as e:
    print("Fehler beim Laden der Konfigurationswerte:", e)
    pygame.quit()
    exit()

pygame.init()
pygame.mixer.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (240, 0, 0)
GREEN = (0, 240, 0)
GOLD = (255, 215, 0)


screen1 = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("exam.ension() Run")
clock = pygame.time.Clock()

# Hintergrund laden
game_folder = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(game_folder, '_image', "zombie_map.png")).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_width = background.get_width()

#Bilder für level changer
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


original_charakter = {}

'''
am.sprite_image_loader(
    game_folder=game_folder,
    folder_name = '_image',
    image_max_num =10,
    image_name='zombie_walk',
    original_name=original_charakter,
    sprite_dict_name=enemy_sprites_level_1
)

am.sprite_image_loader(
    game_folder=game_folder,
    folder_name='_image',
    image_max_num = 6,
    image_name='cowboy_run',
    original_name=original_charakter,
    sprite_dict_name=enemy_sprites_level_2

)
'''


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

platform_image_level_0 = pygame.image.load(os.path.join(game_folder, "_image", "grave_tile.png")).convert_alpha()
platform_image_level0 = pygame.transform.scale(platform_image_level_0, (1400, 150))

platform_image_level_1 = pygame.image.load(os.path.join(game_folder, "_image", "sand_tile.png")).convert_alpha()
platform_image_level_1 = pygame.transform.scale(platform_image_level_1, (1400, 150))

platform_image_level_2 = pygame.image.load(os.path.join(game_folder, "_image", "robot_tile.png")).convert_alpha()
platform_image_level_2 = pygame.transform.scale(platform_image_level_2, (1400, 150))

platform_image_level_3 = pygame.image.load(os.path.join(game_folder, "_image", "stone_tile.png")).convert_alpha()
platform_image_level_3 = pygame.transform.scale(platform_image_level_3, (1400, 150))

platform_image_level_4 = pygame.image.load(os.path.join(game_folder, "_image", "santa_tile.png")).convert_alpha()
platform_image_level_4 = pygame.transform.scale(platform_image_level_4, (1400, 150))



scroll = 0
tiles = math.ceil(WIDTH / background_width) + 1

# Score initialisieren
score = 0

# Schriftart für den Score
font = pygame.font.Font(None, 56)  # Standard-Schriftart, Größe 56

# Sprites laden
original_charakter = {}
sprite_charakter = {}
am.sprite_image_loader(game_folder=game_folder, folder_name="_image", image_max_num=8, image_name="ninja_run",
                        original_name=original_charakter, sprite_dict_name=sprite_charakter)
print(sprite_charakter)

main_charakter = Charakter(
    x_pos=0, y_pos=HEIGHT - 200, sprite_charakter=sprite_charakter, fps=FPS,
    tempo_x=2, scale_tempo_x=1.01, health_points=100, score_points=0, surface=screen1
)

sequence = [
    "Es war ein langer Tag, und der Code scheint endlos zu sein.",
    "Die ganze Zeit bist du am coden aber es läuft einfach nicht."
]

def show_sequence(screen, clock, sequence, font, width, height):
    for text in sequence:
        # Text umbrechen, damit er nicht über den Bildschirm hinausgeht
        lines = wrap_text(text, font, width - 40)  # Padding von 40 für den Rand

        # Text rendern und positionieren
        screen.fill((0, 0, 0))  # Bildschirm schwarz füllen
        y_offset = height // 2 - (len(lines) * 20) // 2  # Vertikale Position, damit der Text mittig ist

        # Jede Zeile des Texts rendern und anzeigen
        for line in lines:
            text_surface = font.render(line, True, (255, 255, 255))  # Weißer Text
            text_rect = text_surface.get_rect(center=(width // 2, y_offset))
            screen.blit(text_surface, text_rect)  # Text anzeigen
            y_offset += 30  # Nächste Zeile nach unten verschieben

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # Mit ENTER zur nächsten Szene
                    running = False


            pygame.display.update()

            clock.tick(30)  # 30 FPS

# Startbildschirm anzeigen, bevor das Spiel beginnt
start_background = pygame.image.load(os.path.join(game_folder, '_image', "classroom.png")).convert()
start_background = pygame.transform.scale(start_background, (WIDTH, HEIGHT))

# Startbildschirm anzeigen
am.show_start_screen(screen1=screen1, clock=clock, start_background=start_background,name="play",game_folder=game_folder)
show_sequence(screen1, clock, sequence, font, WIDTH, HEIGHT)

# Zombie-Gruppe erstellen
all_zombies = pygame.sprite.Group()

# Funktion zum Erstellen von Gegnern
def create_enemy():
    if score < 1000:
        sprite_set = enemy_sprites_level_0  # Zombies bis Score 1000
        anim_name = "zombie_walk"

    elif score <2000:
        sprite_set = enemy_sprites_level_1  # Cowboys ab Score 1000
        anim_name = "cowboy_run"

    elif score < 3000:
        sprite_set = enemy_sprites_level_2
        anim_name = "robot_walk"

    elif score < 4000:
        sprite_set = enemy_sprites_level_3
        anim_name = "knight_walk"

    elif score < 5000:
        sprite_set = enemy_sprites_level_4
        anim_name = "santa_walk"


    
    enemy = Enmy(
        x=WIDTH + 100,
        y=HEIGHT - 200,
        surface=screen1,
        sprite_charakter=sprite_set,
        anim_name=anim_name,
        hp=5,
    )
    all_zombies.add(enemy)

# Neuen Zombie beim Start des Spiels erstellen
if score <1000:
    create_enemy()
else:
    pass

score = 0.0

# Plattform-Rechteck für Kollisionserkennung
platform_rect = pygame.Rect(0, HEIGHT - 127, 1400, 150)

#platform = pygame.Rect( 0, HEIGHT-127 ,1400, 150)           #y, x, width, height
platform_image = pygame.image.load(os.path.join(game_folder, "_image", "stone_tile.png")).convert_alpha()
platform_image = pygame.transform.scale(platform_image, (1400, 150))

waffe = Waffe(sprite_charakter=sprite_charakter, bewegung=main_charakter.bewegung,surface=screen1,springen=main_charakter.springen)
last_spawn_time = pygame.time.get_ticks()



#Level Wechsler
current_level = 0

def level_changer():
   global platform_image, background, current_level
   if score >= 1000 and current_level < 1:
       current_level = 1
       platform_image = platform_image_level_1
       background = background_level_1
       for enemy in all_zombies:
           enemy.kill()


   elif score >= 2000 and current_level < 2 :
      current_level = 2
      platform_image = platform_image_level_2
      background = background_level_2
      for enemy in all_zombies:
           enemy.kill()

   elif score >= 3000 and current_level < 3:
       current_level = 3
       platform_image = platform_image_level_3
       background = background_level_3
       for enemy in all_zombies:
           enemy.kill()
           
   elif score >= 4000 and current_level < 4:
       current_level = 4
       platform_image = platform_image_level_4
       background = background_level_4
       for enemy in all_zombies:
           enemy.kill()  


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                main_charakter.springen.start_sprung()
            if event.key == pygame.K_f:  # Schießen
               waffe.schiessen.shoot(waffe.rect)
               print("F-Taste gedrückt - Schuss ausgelöst!") 

    # Hintergrund scrollen
    scroll -= 6
    if abs(scroll) > background_width:
        scroll = 0
    waffe.schiessen.draw(screen1)
    waffe.schiessen.update()
    for i in range(tiles):
        screen1.blit(background, (scroll + i * background_width, 0))

    # Score aktualisieren
    score += 3  # Score um 1 pro Frame erhöhen

    # Score rendern und anzeigen

    score_text = font.render(f"{int(score):05d} m", True, WHITE)
    text_rect = score_text.get_rect(topright=(WIDTH - 30, 10))
    screen1.blit(score_text, text_rect)

    # Zombies und Charakter aktualisieren
    all_zombies.update()  # Alle Zombies aktualisieren

    main_charakter.update()

    main_charakter.zeichnen()



    #Boden zeichnen 
    screen1.blit(platform_image, (platform_rect.x, platform_rect.y))
    

    # Neuen Zombie mit einer gewissen Wahrscheinlichkeit erzeugen
    elapsed_time = pygame.time.get_ticks() // 1000  # Spielzeit in Sekunden

    # Zufälligen Spawn-Intervall setzen
    spawn_interval = random.randint(500,50000)  # Zufälliger Wert zwischen 500 und 50000 Sekunden in Millisekunden

    if pygame.time.get_ticks() - last_spawn_time > spawn_interval:
        create_enemy()  # Zombie nur hier erzeugen
        last_spawn_time = pygame.time.get_ticks()

   
 # Alle Zombies zeichnen
    all_zombies.draw(screen1)
    # Kugeln aktualisieren und zeichnen
    waffe.schiessen.update()  # Aktualisiere Kugeln
    waffe.schiessen.draw(screen1)  # Zeichne Kugeln
    for zombie in all_zombies:
        # Kollision mit dem Spieler (wer) und Zombie (mitwem)
        if  am.hitbox_check_enmy(wer=main_charakter, mitwem=zombie, surface=screen1):
            main_charakter.health_points=-10
            main_charakter.bar.red_rect()
            zombie_stirb=all_zombies.sprite(zombie)[0]
            zombie_stirb.kill()
            

    


    # Kollision zwischen Kugeln und Zombies überprüfen
    for bullet in waffe.schiessen.bullets:
        for zombie in all_zombies:
            if am.hitbox_check_enmy_bullet(wer=bullet, mitwem=zombie, surface=screen1):
                zombie.hp-=1
                bullet.kill()
                if zombie.hp==0:
                    zombie.kill()
    level_changer()

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()