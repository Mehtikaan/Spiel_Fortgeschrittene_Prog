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
background = pygame.image.load(os.path.join(game_folder, '_image', "City3_pale.png")).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_width = background.get_width()


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
am.sprite_image_loader(game_folder=game_folder, folder_name="_image", image_max_num=10, image_name="zombie_walk",
                        original_name=original_charakter, sprite_dict_name=sprite_charakter)
print(sprite_charakter)
main_charakter = Charakter(
    x_pos=0, y_pos=HEIGHT - 200, sprite_charakter=sprite_charakter, fps=FPS,
    tempo_x=2, scale_tempo_x=1.01, health_points=100, score_points=0, surface=screen1
)

sequence = [
    "Es war ein langer Tag, und der Code scheint endlos.",
    "Du sitzt an deinem Schreibtisch, die Müdigkeit übermannt dich...",
    "Plötzlich wachst du auf, aber nicht in deinem Zimmer.",
    "Chaos herrscht: fliegende Compiler-Fehler, endlose Schleifen, blinkende Variablen.",
    "Eine Stimme dröhnt: 'Willkommen in deinem Traum... oder Albtraum.'",
    "Bestehe die Prüfungen oder bleib gefangen!",
    "Nur ein Weg führt dich zurück in die Realität: Kämpfe und überliste den Bug!"
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

        pygame.display.update()
        
        # 3 Sekunden warten, bevor die nächste Szene kommt
        pygame.time.wait(3000)  # Warten für 3000 ms (3 Sekunden)

# Startbildschirm anzeigen, bevor das Spiel beginnt
start_background = pygame.image.load(os.path.join(game_folder, '_image', "classroom.png")).convert()
start_background = pygame.transform.scale(start_background, (WIDTH, HEIGHT))

# Startbildschirm anzeigen
am.show_start_screen(screen1=screen1, clock=clock, start_background=start_background,name="play_button",game_folder=game_folder)
show_sequence(screen1, clock, sequence, font, WIDTH, HEIGHT)

# Zombie-Gruppe erstellen
all_zombies = pygame.sprite.Group()

# Funktion zum Erstellen von Zombies
def create_zombie():
    zombie = Enmy(x=WIDTH + 100, y=HEIGHT - 200, surface=screen1, sprite_charakter=sprite_charakter,hp=5)
    all_zombies.add(zombie)

# Neuen Zombie beim Start des Spiels erstellen
create_zombie()

score = 0.0

# Plattform-Rechteck für Kollisionserkennung
platform_rect = pygame.Rect(0, HEIGHT - 127, 1400, 150)

#platform = pygame.Rect( 0, HEIGHT-127 ,1400, 150)           #y, x, width, height
platform_image = pygame.image.load(os.path.join(game_folder, "_image", "stone_tile.png")).convert_alpha()
platform_image = pygame.transform.scale(platform_image, (1400, 150))

waffe = Waffe(sprite_charakter=sprite_charakter, bewegung=main_charakter.bewegung,surface=screen1,springen=main_charakter.springen)
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
    score += 0.45  # Score um 1 pro Frame erhöhen

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
    spawn_interval = max(1000, 5000 - (elapsed_time * 100))  # Intervall wird alle 10 Sekunden kürzer
    if pygame.time.get_ticks() - last_spawn_time > spawn_interval:
        create_zombie()  # Zombie nur hier erzeugen
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

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
