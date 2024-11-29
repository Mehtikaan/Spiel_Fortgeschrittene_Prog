import pygame
import animationen as am
import configparser as cp
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
# Klasse des Hauptcharakters
class Charakter:
    def __init__(self, x_pos, y_pos, shoot, health_points, score_points, sprite_charakter, fps, tempo_x, scale_tempo_x):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.tempo_x = tempo_x
        self.scale_tempo_x = scale_tempo_x
        self.health_points = health_points
        self.score_points = score_points
        self.image = sprite_charakter["ninja_run1"]
        self.imageRect = self.image.get_rect()
        self.timer = 0
        self.anim_frames = 8
        self.act_frame = 1
        self.max_ticks_anim = 0.6 * fps / self.anim_frames
        self.sprite_charakter = sprite_charakter

        # Sprungvariablen
        self.y_velocity = 0
        self.gravity = 1
        self.jumping_height = 20
        self.jumping = False

    # Aus der Bibliothek animation importiert zum Updaten
    def animation_update_laufen(self):                               
        self.image, self.timer, self.act_frame = am.animation_update(
            timer=self.timer,  # Unser Code hatte self.image, self.timer, self.act_frame drin, also nur Aufruf der Funktion am.animation_update
            max_ticks=self.max_ticks_anim,                           
            act_frame=self.act_frame,                                
            anim_frames=self.anim_frames,
            sprite_images=self.sprite_charakter,
            name="ninja_run"
        )
        while self.x_pos <= 320:
            self.scale_tempo_x = self.scale_tempo_x 
            self.tempo_x = self.tempo_x * self.scale_tempo_x
            self.x_pos = self.x_pos + self.tempo_x
            break
            
        self.imageRect.topleft = (self.x_pos, self.y_pos)

    def zeichnen(self, surface):
        surface.blit(self.image, self.imageRect)