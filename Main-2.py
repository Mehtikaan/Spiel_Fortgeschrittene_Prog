import configparser as cp
import pygame
import os
import animationen as am  # Importiere die Animationsbibliothek, die die update-Funktion enthält
import config_einstellungen as bib


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
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("exam.ension() Run")
clock = pygame.time.Clock()

# Sprites laden
game_folder = os.path.dirname(__file__)

background = pygame.image.load(os.path.join(game_folder, '_image', "hintergrund_winter.png"))
pygame.display.update()
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

# Klasse für den Charakter
class Charakter:
    def __init__(self, x_pos, y_pos, sprite_charakter, fps):
        """
        Initialisiert den Charakter.
        
        :param x_pos: Die x-Position des Charakters.
        :param y_pos: Die y-Position des Charakters.
        :param sprite_charakter: Das Dictionary der Charakterbilder.
        :param fps: Die Frames per Second des Spiels.
        """
        self.x_pos = x_pos  # Positionierung links
        self.y_pos = y_pos  # Etwas höher positioniert
        self.sprite_charakter = sprite_charakter  # Sprite-Bilder für den Charakter
        self.fps = fps
        self.image = self.sprite_charakter["charakter_run1"]  # Initiales Bild
        self.imageRect = self.image.get_rect(center=(self.x_pos, self.y_pos))   # Dies war ein Verbessernugnsvorschlag von ChatGPT
        
        # Animationseinstellungen
        self.timer = 0
        self.anim_frames = 8
        self.act_frame = 1
        self.max_ticks_anim = 0.6 * self.fps / self.anim_frames

    def update(self):
        """
        Aktualisiert die Animation des Charakters. Da der Charakter feststeht, wird nur die Animation aktualisiert.
        """
        # Update der Geh-Animation (die Timer- und Frame-Logik wird durch die externe Funktion gehandhabt)
        self.image, self.timer, self.act_frame = am.animation_update(
            timer=self.timer,
            max_ticks=self.max_ticks_anim,
            act_frame=self.act_frame,
            anim_frames=self.anim_frames, 
            sprite_images=self.sprite_charakter,
            name="charakter_run"
        )
        
        # Der Charakter bewegt sich nicht, daher bleibt die Position konstant.
        self.imageRect.topleft = (self.x_pos, self.y_pos)  # Bildrechteck bleibt an der festgelegten Position

    def draw(self, surface):
        """
        Zeichnet das Charakterbild auf dem Bildschirm.
        
        :param surface: Das Pygame Bildschirmobjekt.
        """
        surface.blit(self.image, self.imageRect)

# Beispiel für die Verwendung der Klassen
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Beispielhafter Charakter
# Startet relativ links und etwas höher als die untere Kante
charakter = Charakter(x_pos=100, y_pos=HEIGHT - 250, sprite_charakter=sprite_charakter, fps=FPS)  # Startet an der unteren linken Ecke, aber etwas höher

# Spiel Schleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bildschirm leeren
    screen.blit(background, (0, 0))

    # Charakter aktualisieren (Animation)
    charakter.update()

    # Charakter zeichnen
    charakter.draw(screen)

    # Bildschirm aktualisieren
    pygame.display.flip()

    # Framerate (FPS) einstellen
    clock.tick(60)

pygame.quit()
