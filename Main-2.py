import configparser as cp
import pygame
import os
import math
import animationen as am  # Importiere die Animationsbibliothek, die die update-Funktion enthält
import config_einstellungen as bib
from charakter import Charakter


# Konfiguration laden oder erstellen
config = cp.ConfigParser()
if not config.read("config_game.ini"):
    print("Erstelle Konfigurationsdatei...")
    bib.erstelle_config_datei()  # Stelle sicher, dass die Funktion existiert

config.read("config_game.ini")  # Konfigurationsdatei lesen

# Werte aus der Konfiguration laden und konvertieren
try:
    HEIGHT = int(config.get("Fenster", "height"))
    WIDTH = int(config.get("Fenster", "width"))
    FPS = int(config.get("FPS", "fps"))
    POSITION= int(config.get("Fenster", "position"))
except Exception as e:
    print("Fehler beim Laden der Konfigurationswerte:", e)
    pygame.quit()
    exit()

# Pygame initialisieren
pygame.init()
pygame.mixer.init()

# Display initialisieren und Titel setzen
screen1 = pygame.display.set_mode((WIDTH, HEIGHT)) #pygame.SCALED
pygame.display.set_caption("exam.ension() Run")
clock = pygame.time.Clock()

# Sprites laden
game_folder = os.path.dirname(__file__)

# Hintergrund
background = pygame.image.load(os.path.join(game_folder, '_image', "City3_pale.png")).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_width = background.get_width()

start_background = pygame.image.load(os.path.join(game_folder, '_image', "6.png")).convert()
start_background = pygame.transform.scale(start_background, (WIDTH, HEIGHT))

#game variablen definieren
tiles = math.ceil(WIDTH / background_width) + 1
scroll = 0


pygame.display.update()
original_charakter = {}
sprite_charakter = {}
am.sprite_image_loader(game_folder=game_folder,folder_name="_image", image_max_num=9,image_name="ninja_run",original_name=original_charakter,sprite_dict_name=sprite_charakter)
# Beispiel für die Verwendung der Klassen
pygame.init()
x_pos=0
main_charakter = Charakter(x_pos=x_pos,tempo_x=4, y_pos=HEIGHT - 200, sprite_charakter=sprite_charakter, fps=FPS,shoot=None,health_points=4,score_points=0,scale_tempo_x=1.01)  # Startet an der unteren linken Ecke, aber etwas höher

y_velocity = 0
gravity = 1
jumping_height = 15
jumping = False


show_start_screen = True



# Spiel Schleife
running = True
while running:

    clock.tick(FPS)

    if main_charakter.x_pos<POSITION:
        screen1.blit(background, (0, 0))
        main_charakter.animation_update_laufen()
        main_charakter.zeichnen(surface=screen1)
        pygame.display.flip()

    else:
        
        pygame.display.flip()
        for i in range(0, tiles):
            screen1.blit(background, (i* background_width + scroll, 0))

        #background scrollen
        scroll -= 5

        #reset scroll
        if abs(scroll) > background_width:
            scroll = 0



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE] and not jumping:
            jumping = True
            y_velocity = jumping_height

        if jumping:
            main_charakter.y_pos -= y_velocity
            y_velocity -= gravity
    
            if main_charakter.y_pos >= HEIGHT - 200: #Bodenpostion
                main_charakter.y_pos = HEIGHT - 200
                jumping = False
        

        #screen1.blit(background, (0, 0))

        if jumping:
            # Setze die Sprung-Animation, wenn der Charakter springt
            JUMPING_SURFACE = sprite_charakter.get("ninja_jump", sprite_charakter["ninja_run1"])
            screen1.blit(JUMPING_SURFACE, (main_charakter.x_pos, main_charakter.y_pos))
        else:
            # Wenn der Charakter nicht springt, führe die Lauf-Animation aus
            main_charakter.animation_update_laufen()
            main_charakter.zeichnen(surface=screen1)

        pygame.display.flip()
    # Bildschirm aktualisieren


    # Framerate (FPS) einstellen
    # clock.tick(FPS)

pygame.quit()