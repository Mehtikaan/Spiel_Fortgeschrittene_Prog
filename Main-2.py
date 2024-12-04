import pygame
import os
import math
import configparser as cp
import config_einstellungen as bib
from charakter import Charakter
import animationen as am
from enmy import Enmy  # Importiere die Enmy-Klasse

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

screen1 = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("exam.ension() Run")
clock = pygame.time.Clock()

# Hintergrund laden
game_folder = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(game_folder, '_image', "City3_pale.png")).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_width = background.get_width()
scroll = 0
tiles = math.ceil(WIDTH / background_width) + 1

# Sprites laden
original_charakter = {}
sprite_charakter = {}
am.sprite_image_loader(game_folder=game_folder, folder_name="_image", image_max_num=8, image_name="ninja_run",
                        original_name=original_charakter, sprite_dict_name=sprite_charakter)
am.sprite_image_loader(game_folder=game_folder, folder_name="_image", image_max_num=10, image_name="zombie_walk",
                        original_name=original_charakter, sprite_dict_name=sprite_charakter)
print(sprite_charakter)
main_charakter = Charakter(
    x_pos=0, y_pos=HEIGHT - 200, sprite_charakter=sprite_charakter, fps=FPS,
    tempo_x=2, scale_tempo_x=1.01, health_points=4, score_points=0, surface=screen1
)

# Startbildschirm anzeigen, bevor das Spiel beginnt
start_background = pygame.image.load(os.path.join(game_folder, '_image', "classroom.png")).convert()
start_background = pygame.transform.scale(start_background, (WIDTH, HEIGHT))

# Startbildschirm anzeigen
am.show_start_screen(screen1=screen1, clock=clock, start_background=start_background,name="play_button",game_folder=game_folder)

# Zombie-Gruppe erstellen
# Zombie-Gruppe erstellen
all_zombies = pygame.sprite.Group()

# Funktion zum Erstellen von Zombies
def create_zombie():
    zombie = Enmy(x=WIDTH + 100, y=HEIGHT - 200, surface=screen1, sprite_charakter=sprite_charakter)
    all_zombies.add(zombie)

# Neuen Zombie beim Start des Spiels erstellen
create_zombie()

last_spawn_time = pygame.time.get_ticks()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                main_charakter.springen.start_sprung()
            if event.key == pygame.K_f:  # Schießen
                main_charakter.schiessen.shoot(main_charakter.bewegung.x_pos, main_charakter.springen.y_pos)

    # Hintergrund scrollen
    scroll -= 6
    if abs(scroll) > background_width:
        scroll = 0

    for i in range(tiles):
        screen1.blit(background, (scroll + i * background_width, 0))

    # Zombies und Charakter aktualisieren
    all_zombies.update()  # Alle Zombies aktualisieren
    main_charakter.update()
    main_charakter.zeichnen()

    # Neuen Zombie mit einer gewissen Wahrscheinlichkeit erzeugen
    elapsed_time = pygame.time.get_ticks() // 1000  # Spielzeit in Sekunden
    spawn_interval = max(1000, 5000 - (elapsed_time * 100))  # Intervall wird alle 10 Sekunden kürzer
    if pygame.time.get_ticks() - last_spawn_time > spawn_interval:
        create_zombie()  # Zombie nur hier erzeugen
        last_spawn_time = pygame.time.get_ticks()

    # Alle Zombies zeichnen
    all_zombies.draw(screen1)

    # Kollisionserkennung mit den Zombies
    for zombie in all_zombies:
        am.hitbox_check_enmy(wer=main_charakter, mitwem=zombie, surface=screen1)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

