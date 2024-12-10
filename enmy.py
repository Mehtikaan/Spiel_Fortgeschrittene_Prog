import pygame
import animationen as am
import configparser as cp
import config_einstellungen as bib
#from waffe import Bullet


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
import pygame
import animationen as am

class Enmy(pygame.sprite.Sprite):
    def __init__(self, x, y, surface, sprite_charakter,hp):
        super().__init__()
        self.x = x
        self.y = y
        self.hp=hp
        self.surface = surface
        self.fps = 60  # Standard FPS, kann aus der Konfiguration übernommen werden
        self.sprite_charakter = sprite_charakter  # Hier das sprite_charakter übergeben
        self.anim_frames = 10  # Anzahl der Animationsbilder
        self.act_frame = 1
        self.timer = 0
        self.max_ticks_anim = 0.6 * self.fps / self.anim_frames
        self.image = self.sprite_charakter["zombie_walk1"]  # Startbild
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)
        self.speed = 4  # Die Geschwindigkeit des Zombies nach links

    def update(self):
        # Animation des Zombies
        self.image, self.timer, self.act_frame = am.animation_update(
            timer=self.timer,
            max_ticks=self.max_ticks_anim,
            act_frame=self.act_frame,
            anim_frames=self.anim_frames,
            sprite_images=self.sprite_charakter,
            name="zombie_walk"
        )

        # Zombie nach links bewegen
        self.rect.x -= self.speed
        
        # Entfernen, wenn der Zombie den linken Bildschirmrand verlässt
        if self.rect.right < 0:
            self.kill()
