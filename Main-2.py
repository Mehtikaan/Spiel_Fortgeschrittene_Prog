import configparser as cp
import pygame
import os
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
except Exception as e:
    print("Fehler beim Laden der Konfigurationswerte:", e)
    pygame.quit()
    exit()

# Pygame initialisieren
pygame.init()
pygame.mixer.init()

# Display initialisieren und Titel setzen
screen1 = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("exam.ension() Run")
clock = pygame.time.Clock()

# Sprites laden
game_folder = os.path.dirname(__file__)

background = pygame.image.load(os.path.join(game_folder, '_image', "City3_pale.png")).convert_alpha()
background= pygame.transform.scale(background,(WIDTH,HEIGHT))
pygame.display.update()
original_charakter = {}
sprite_charakter = {}

am.sprite_image_loader(
    game_folder=game_folder,
    folder_name="_image",
    image_max_num=9,
    image_name="ninja_run", 
    original_name=original_charakter,
    sprite_dict_name=sprite_charakter, 
)

# Beispiel für die Verwendung der Klassen
pygame.init()
x_pos=0
main_charakter = Charakter(x_pos=x_pos,tempo_x=3  , y_pos=HEIGHT - 200, sprite_charakter=sprite_charakter, fps=FPS,shoot=None,health_points=4,score_points=0,scale_tempo_x=1.03)  # Startet an der unteren linken Ecke, aber etwas höher

# Spiel Schleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Bildschirm leeren
    screen1.blit(background,(0,0))

    # Charakter aktualisieren (Animation)
    main_charakter.animation_update_laufen()
    # Charakter zeichnen
    main_charakter.zeichnen(surface=screen1)


    # Bildschirm aktualisieren
    pygame.display.flip()

    # Framerate (FPS) einstellen
    clock.tick(60)

pygame.quit()
