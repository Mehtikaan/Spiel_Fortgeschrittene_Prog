import configparser as cp
import config_einstellungen as bib  # Sicherstellen, dass config_einstellungen existiert und die Funktion erstelle_config_datei hat
import pygame
import os
import random

# Konfiguration laden oder erstellen
config = cp.ConfigParser()
if not config.read("config_game.ini"):
    print("Erstelle Konfigurationsdatei...")
    bib.erstelle_config_datei()  # Erstellt Konfigurationsdatei, falls sie nicht vorhanden ist

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
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("exam.ension() Run")
clock = pygame.time.Clock()

# Sprites laden
game_folder = os.path.dirname(__file__)
sprite_charakter = {}
try:
    for i in range(1, 9):
        # Jedes Bild des Laufcharakters laden und in einem Dictionary speichern
        sprite_path = os.path.join(game_folder, '_image', f'charakter_run{i}.png')
        if not os.path.exists(sprite_path):
            raise FileNotFoundError(f"Bilddatei nicht gefunden: {sprite_path}")
        sprite_charakter[f"charakter_run{i}"] = pygame.image.load(sprite_path).convert_alpha()
except Exception as e:
    print("Fehler beim Laden der Sprite-Bilder:", e)
    pygame.quit()
    exit()

class Ball:
    def __init__(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.image = sprite_charakter["charakter_run1"]
        self.imageRect = self.image.get_rect()
        self.timer = 0
        self.anim_frames = 8
        self.act_frame = 1
        self.max_ticks_anim = 0.6 * FPS / self.anim_frames

    def update(self):
        # Animationsframe aktualisieren
        self.timer += 1
        if self.timer >= self.max_ticks_anim:
            self.timer = 0
            self.act_frame = (self.act_frame % self.anim_frames) + 1
            self.image = sprite_charakter[f"charakter_run{self.act_frame}"]

        # Position aktualisieren
        self.x += self.sx
        self.y += self.sy
        self.imageRect.topleft = (self.x, self.y)

        # Randkollision behandeln
        if self.imageRect.right >= WIDTH or self.imageRect.left <= 0:
            self.sx *= -1
        if self.imageRect.bottom >= HEIGHT or self.imageRect.top <= 0:
            self.sy *= -1

    def draw(self, surface):
        # Sprite auf dem Bildschirm zeichnen
        surface.blit(self.image, self.imageRect)

# Liste der Ball-Sprites erstellen
sprites = [
    Ball(
        random.randint(64, WIDTH - 64),
        random.randint(64, HEIGHT - 64),
        random.choice([-3, -2, -1, 1, 2, 3]),
        random.choice([-3, -2, -1, 1, 2, 3])
    )
]

# Hauptschleife
running = True
while running:
    # Ereignisverarbeitung
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Alle Sprites aktualisieren
    for sprite in sprites:
        sprite.update()

    # Alles zeichnen
    screen.fill((255, 255, 255))  # Bildschirm mit weißem Hintergrund leeren
    for sprite in sprites:
        sprite.draw(screen)

    pygame.display.flip()  # Display aktualisieren
    clock.tick(FPS)  # Bildrate steuern

# Pygame beenden
pygame.quit()
