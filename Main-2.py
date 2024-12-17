import pygame
import os
import math
import configparser as cp
import config_einstellungen as bib
from charakter import Charakter, Waffe,Bullet
import animationen as am
from enemy import Enemy  # Importiere die Enmy-Klasse
import pygame.font
from sequenz import wrap_text
import random
from endboss import Endboss,Meteoriten,Blitzen
from power_Up_health import Health_reg
from traps import Trap
from animationen import show_pause_menu
from endboss import Endboss,Meteoriten,Blitzen


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

pygame.mixer.init() #Sound Nutzung importieren

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (240, 0, 0)
GREEN = (0, 240, 0)
GOLD = (255, 215, 0)
BLUE = (150, 0, 160)


screen1 = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("exam.ension() Run") # Überschrift

clock = pygame.time.Clock()

# Hintergrund laden
game_folder = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(game_folder, '_image', "zombie_map.png")).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_width = background.get_width()

# Sound
kunai_sound = pygame.mixer.Sound(os.path.join(game_folder, '_sounds', "kunai.mp3"))
kunai_sound.set_volume(0.15)
jump_sound = pygame.mixer.Sound(os.path.join(game_folder, '_sounds', "grunting.wav"))
jump_sound.set_volume(0.15)
death_sound = pygame.mixer.Sound(os.path.join(game_folder, '_sounds','death_sound.wav'))
death_sound.set_volume(0.15)


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


original_charakter = {}



# Plattform-Rechteck für Kollisionserkennung
platform_y = HEIGHT - 127
platform_rect = pygame.Rect(0,platform_y, 1400, 150)

#platform = pygame.Rect( 0, HEIGHT-127 ,1400, 150)           #y, x, width, height
platform_width = 1400
platform_height = 150
platform_image = pygame.image.load(os.path.join(game_folder, "_image", "stone_tile.png")).convert_alpha()
platform_image = pygame.transform.scale(platform_image, (platform_width, platform_height))



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

background_level_6 = pygame.image.load(os.path.join(game_folder, '_image', "dino_map.png")).convert()
background_level_6 = pygame.transform.scale(background_level_6, (WIDTH, HEIGHT))

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

platform_image_level_5 = pygame.image.load(os.path.join(game_folder, "_image", "grave_tile.png")).convert_alpha()
platform_image_level_5 = pygame.transform.scale(platform_image_level_5, (1400, 150))

platform_image_level_6 = pygame.image.load(os.path.join(game_folder, "_image", "dino_tile.png")).convert_alpha()
platform_image_level_6 = pygame.transform.scale(platform_image_level_6, (1400, 150))


back_scroll = 0.0
p_scroll = 0.0

back_tiles = math.ceil(WIDTH / background_width) + 1
p_tiles = math.ceil(WIDTH / platform_width) + 1

# Score initialisieren
score = 6000

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
    tempo_x=2, scale_tempo_x=1.01, health_points=200, score_points=0, surface=screen1
)

am.main_charakter = main_charakter

sequence = [
    "Es war ein langer Tag, und der Code scheint endlos zu sein.",
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
start_background = pygame.image.load(os.path.join(game_folder, '_image', "exam_bild.png")).convert()
start_background = pygame.transform.scale(start_background, (WIDTH, HEIGHT))

# Bild für die Falle laden
trap_image = pygame.image.load(os.path.join(game_folder, '_image', "skeleton.png")).convert_alpha()

# Hindernis-Gruppe erstellen
all_traps = pygame.sprite.Group()

trap = Trap(
    x=1600, y=HEIGHT - 158, surface=screen1, sprite_image=trap_image, scale=(75, 45), speed=7
)
all_traps.add(trap)

start_music = pygame.mixer.Sound(os.path.join(game_folder, '_sounds', 'zombie_music.wav'))
start_music.set_volume(0.15)

# Sound abspielen und Kanal speichern
start_music_channel = start_music.play()
start_music_channel = pygame.mixer.Channel(0)  # Reserviere Kanal 0
start_music_channel.play(start_music)

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

    elif score < 6000:
        sprite_set = enemy_sprites_level_5
        anim_name = "pumpkin_walk"

    elif score < 7000:
        sprite_set = enemy_sprites_level_6
        anim_name = "courli"

    
    enemy = Enemy(
        x=WIDTH + 100,
        y=HEIGHT - 200,
        surface=screen1,
        sprite_charakter=sprite_set,
        anim_name=anim_name,
        hp=5,
    )
    all_zombies.add(enemy)




endboss = Endboss(x=WIDTH-200, y=HEIGHT-400, surface=screen1, sprite_charakter=enemy_sprites_level_endboss, anim_name="endboss", hp=100, gamefolder=game_folder)
blitz = Blitzen(350, 1, game_folder, screen1)
blitze=pygame.sprite.Group()
blitze.add(blitz)

# Neuen Zombie beim Start des Spiels erstellen
if score <1000:
    create_enemy()
else:
    pass

score = 0.0
herz=Health_reg(screen1,game_folder)

waffe = Waffe(sprite_charakter=sprite_charakter, bewegung=main_charakter.bewegung,surface=screen1,springen=main_charakter.springen)
last_spawn_time = pygame.time.get_ticks()

#Levelwechsel Übergang

def fade(screen, color, duration=float, fade_out=True, text=None, font=None, text_color=WHITE):
  
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.fill(color)

    # Schrittweite basierend auf der Dauer und der FPS
    step = int(255 / (FPS * duration))
    
    # Wenn wir ausblenden (fade_out=True), dann müssen wir die Alpha-Werte steigern,
    # beim Einblenden müssen wir sie verringern.
    for alpha in range(0, 255, step):
        fade_surface.set_alpha(alpha if fade_out else 255 - alpha)

        # Text wird direkt während des Fade-Effekts angezeigt und allmählich sichtbar
        if text and font:
            rendered_text = font.render(text, True, text_color)
            text_rect = rendered_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            
            # Text wird mit jedem Schritt immer sichtbarer, je mehr der Hintergrund eingeblendet wird
            screen.blit(fade_surface, (0, 0))
            screen.blit(rendered_text, text_rect) ###############hier vllt

        else:
            screen.blit(fade_surface, (0, 0))

        pygame.display.update()
        clock.tick(FPS)

def transition_sequence():
    global score
    # Score pausieren
    current_score = score  # Aktuellen Score speichern
    fade(screen1, BLACK, 0.1, fade_out=True)  # Bildschirm ausblenden (1 Sekunde)
    
    pygame.time.delay(2000)  # 2 Sekunden pausieren
    
    fade(screen1, BLACK, 0.2, fade_out=False)  # Bildschirm einblenden
    score = current_score  # Score zurücksetzen (während der Pause bleibt er gleich)



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

pygame.mixer.music.set_volume(0.3)  # Lautstärke auf 50% einstellen

def level_changer():
   global platform_image, background, current_level, level_music, start_music_channel, trap_image
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
       transition_sequence() 
       platform_image = platform_image_level_1
       background = background_level_1
       pygame.mixer.music.load(level_music[1])  # Lade Level-1-Musik
       pygame.mixer.music.play(-1)  # Endlosschleife
       fade(screen1, BLACK, 1, fade_out=True, text=level_texts[1], font=font)
       for enemy in all_zombies:
           enemy.kill()


   elif score >= 2000 and current_level < 2 :
      current_level = 2
      transition_sequence() 
      platform_image = platform_image_level_2
      background = background_level_2
      pygame.mixer.music.load(level_music[2])  # Lade Level-2-Musik
      pygame.mixer.music.play(-1)
      fade(screen1, BLACK, 1, fade_out=True, text=level_texts[2], font=font)
      for enemy in all_zombies:
           enemy.kill()

   elif score >= 3000 and current_level < 3:
       current_level = 3
       transition_sequence() 
       platform_image = platform_image_level_3
       background = background_level_3
       pygame.mixer.music.load(level_music[3])  # Lade Level-3-Musik
       pygame.mixer.music.play(-1)
       fade(screen1, BLACK, 1, fade_out=True, text=level_texts[3], font=font)
       for enemy in all_zombies:
           enemy.kill()
           
   elif score >= 4000 and current_level < 4:
       current_level = 4
       transition_sequence() 
       platform_image = platform_image_level_4
       background = background_level_4
       pygame.mixer.music.load(level_music[4])  # Lade Level-4-Musik
       pygame.mixer.music.play(-1)
       fade(screen1, BLACK, 1, fade_out=True, text=level_texts[4], font=font)  # Zeichne alle Sprites
       for enemy in all_zombies:
           enemy.kill()
             
   elif score >= 5000 and current_level < 5:
       current_level = 5
       transition_sequence() 
       platform_image = platform_image_level_5
       background = background_level_5
       pygame.mixer.music.load(level_music[5])  # Lade Level-5-Musik
       pygame.mixer.music.play(-1)
       fade(screen1, BLACK, 1, fade_out=True, text=level_texts[5], font=font)
       for enemy in all_zombies:
           enemy.kill()
    
   elif score >= 6000 and current_level < 6:
       current_level = 6
       transition_sequence() 
       platform_image = platform_image_level_6
       background = background_level_6
       pygame.mixer.music.load(level_music[6])  # Lade Level-6-Musik
       pygame.mixer.music.play(-1)
       fade(screen1, BLACK, 1, fade_out=True, text=level_texts[6], font=font)
       for enemy in all_zombies:
           enemy.kill()

def main_game():
    """Die Hauptspiel-Schleife."""
    global score, main_charakter, all_zombies, current_level
    # Setze alle Werte zurück
    score = 0
    #main_charakter.reset()  # Methode, die den Charakter zurücksetzt
    all_zombies.empty()  # Alle Zombies entfernen
    current_level = 0
    #pygame.mixer.music.play(-1)  # Spielmusik starten





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                main_charakter.springen.start_sprung()
                jump_sound.play()
            if event.key == pygame.K_f:  # Schießen
                waffe.schiessen.shoot(waffe.rect)
                kunai_sound.play()
            if event.key == pygame.K_ESCAPE:
                show_pause_menu(screen1= screen1, font= font)
               


    for zombie in all_zombies:
        zombie.update()
        zombie.draw()
    # Hintergrund scrollen
    back_scroll -= 0.6
    if abs(back_scroll) > background_width:
        back_scroll = 0
    waffe.schiessen.draw(screen1)
    waffe.schiessen.update()
    for i in range(back_tiles):
        screen1.blit(background, (back_scroll + i * background_width, 0))


        # Platform scrollen
    p_scroll -= 7.5
    if abs(p_scroll) > platform_width:
        p_scroll = 0
    # Plattformen zeichnen
    for i in range(p_tiles):
        screen1.blit(platform_image, (p_scroll + i * platform_width, platform_y))



    # Score aktualisieren
    score += 1  # Score um 1 pro Frame erhöhen

    # Score rendern und anzeigen

    score_text = font.render(f"{int(score):05d} m", True, WHITE)
    text_rect = score_text.get_rect(topright=(WIDTH - 60, 50))
    screen1.blit(score_text, text_rect)

    # Zombies und Charakter aktualisieren
    all_zombies.update()

     # Hindernisse aktualisieren und zeichnen
    all_traps.update()
    for obstacle in all_traps:
        obstacle.draw()

    main_charakter.update()

    main_charakter.zeichnen()

    

    # Neuen Zombie mit einer gewissen Wahrscheinlichkeit erzeugen
    elapsed_time = pygame.time.get_ticks() // 1000  # Spielzeit in Sekunden

    if score>500:
            endboss.update()
            endboss.draw()
            endboss.shoot()
            herz.draw()
            blitze.update()
            blitze.draw(screen1)
            for blitz in blitze:
               am.hitbox_check_blitz(main_charakter, blitz, screen1)

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
                zombie.draw()
                if zombie.hp==0:
                    zombie.kill()

 

    level_changer()
    # Prüfen, ob Lebenspunkte <= 0 sind
    if main_charakter.health_points <= 0:
        death_sound.play()
        #pygame.mixer.music.stop()
        fade(screen1, WHITE, 3.5, fade_out=True, text="Game Over", font=font, text_color=BLACK)
        am.restart_game()



    pygame.display.update()

    clock.tick(FPS)

am.show_start_screen(screen1=screen1, clock=clock, start_background=start_background,name="play",game_folder=game_folder)
main_game()  # Hauptspiel starten
pygame.quit()



