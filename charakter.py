import pygame 
import animationen as am
import configparser as cp
import config_einstellungen as bib
from waffe import Bullet
import os

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
    POSITION = int(config.get("Fenster", "position"))
except Exception as e:
    print("Fehler beim Laden der Konfigurationswerte:", e)
    pygame.quit()
    exit()

class Charakter:
    def __init__(self, x_pos, y_pos, sprite_charakter, fps, tempo_x, scale_tempo_x, health_points, score_points, surface):
        # Initialisieren der Unterklassen
        self.bewegung = Bewegung(x_pos, tempo_x, scale_tempo_x, sprite_charakter, fps)
        self.schiessen = Schießen(sprite_charakter)
        self.springen = Springen(y_pos, sprite_charakter, surface)
        self.waffe = Waffe(self.bewegung, sprite_charakter)  # Neue Waffenklasse
        self.health_points = Health_points(healthpoints=100, surface=surface)
        self.score_points = score_points
        self.surface = surface

    def update(self):
        """Aktualisiert den Charakter: Bewegung, Animation, Schüsse und Springen"""
        self.bewegung.update()
        self.schiessen.update()
        jumping_sprite, self.springen.y_pos = self.springen.update(self.bewegung.x_pos)
        if jumping_sprite:
            self.bewegung.image = jumping_sprite
        self.waffe.update(self.springen.y_pos)  # Aktualisiert die Position der Waffe
        self.health_points.update()

    def zeichnen(self):
        """Zeichnet den Charakter auf dem Bildschirm"""
        self.bewegung.zeichnen(self.surface, self.springen.y_pos)
        self.waffe.zeichnen(self.surface)  # Zeichnet die Waffe
        self.schiessen.bullets.draw(self.surface)

class Bewegung:
    def __init__(self, x_pos, tempo_x, scale_tempo_x, sprite_charakter, fps):
        self.x_pos = x_pos
        self.tempo_x = tempo_x
        self.scale_tempo_x = scale_tempo_x
        self.sprite_charakter = sprite_charakter
        self.fps = fps
        self.timer = 0
        self.anim_frames = 8
        self.act_frame = 1
        self.max_ticks_anim = 0.6 * self.fps / self.anim_frames
        self.image = self.sprite_charakter["ninja_run1"]
        self.has_reached_position = False  # Status, ob Zielposition erreicht wurde

    def update(self):
        """Aktualisiert die Bewegung und die Animation des Charakters"""
        self.animation_update_laufen()

    def animation_update_laufen(self):
        """Aktualisiert die Lauf-Animation und die Bewegung des Charakters"""
        # Aktualisiere die Lauf-Animation unabhängig von der Bewegung
        self.image, self.timer, self.act_frame = am.animation_update(
            timer=self.timer,
            max_ticks=self.max_ticks_anim,
            act_frame=self.act_frame,
            anim_frames=self.anim_frames,
            sprite_images=self.sprite_charakter,
            name="ninja_run"
        )

        if not self.has_reached_position:  # Bewege den Charakter nur, wenn Ziel nicht erreicht ist
            if self.x_pos < POSITION:
                self.tempo_x += 0.05 if self.x_pos < POSITION / 4 else 0.03
                self.x_pos += self.tempo_x
            else:
                self.x_pos = POSITION  # Zielposition fixieren
                self.tempo_x = 0  # Geschwindigkeit stoppen
                self.has_reached_position = True

    def zeichnen(self, surface, y_pos):
        """Zeichnet den Charakter an der aktuellen Position"""
        surface.blit(self.image, (self.x_pos, y_pos))

class Waffe:
    def __init__(self, bewegung, sprite_charakter):
        self.bewegung = bewegung
        self.sprite_charakter = sprite_charakter
        game_folder = os.path.dirname(__file__)
        #Bild laden und skalieren
        self.image = pygame.image.load(os.path.join(game_folder, '_image', "US_Thompson.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 20))  # Größe anpassen
        self.rect = self.image.get_rect()

    def update(self, y_pos):
        """Aktualisiert die Position der Waffe basierend auf der Bewegung des Charakters"""
        self.rect.center = (
            self.bewegung.x_pos + self.sprite_charakter["ninja_run1"].get_width(),
            y_pos + 20
        )

    def zeichnen(self, surface):
        """Zeichnet die Waffe auf dem Bildschirm"""
        surface.blit(self.image, self.rect.topleft)

class Schießen:
    def __init__(self, sprite_charakter):
        self.sprite_charakter = sprite_charakter
        self.shoot_cooldown = 0
        self.bullets = pygame.sprite.Group()

    def shoot(self, waffen_rect):
        """Feuert eine Kugel ab, wenn der Cooldown abgelaufen ist"""
        if self.shoot_cooldown == 0:
            bullet = Bullet(waffen_rect.centerx, waffen_rect.centery)
            self.bullets.add(bullet)
            self.shoot_cooldown = 20

    def update(self):
        """Aktualisiert die Kugeln und den Cooldown"""
        self.bullets.update()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

class Springen:
    def __init__(self, y_pos, sprite_charakter, surface):
        self.y_pos = y_pos
        self.sprite_charakter = sprite_charakter
        self.surface = surface
        self.y_velocity = 0
        self.gravity = 1
        self.jumping_height = 23
        self.jumping = False

    def start_sprung(self):
        """Startet das Springen"""
        if not self.jumping:
            self.jumping = True
            self.y_velocity = self.jumping_height

    def update(self, x_pos):
        """Verarbeitet das Springen und aktualisiert die Y-Position des Charakters"""
        if self.jumping:
            self.y_pos -= self.y_velocity * 0.5
            self.y_velocity -= self.gravity
            if self.y_pos >= self.surface.get_height() - 200:
                self.y_pos = self.surface.get_height() - 200
                self.jumping = False
        if self.jumping:
            return self.sprite_charakter.get("ninja_jump", self.sprite_charakter["ninja_run1"]), self.y_pos
        return None, self.y_pos

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (240, 0, 0)
GREEN = (0, 240, 0)
GOLD = (255, 215, 0) 

class Health_points:
    def __init__(self, healthpoints, surface):
        self.healthpoints = healthpoints
        self.surface = surface

    def red_rect(self):
        pygame.draw.rect(self.surface, RED, (660, 65, 100, 15))
        pygame.draw.rect(self.surface, GREEN, (660, 65, self.healthpoints, 15))
        pygame.draw.rect(self.surface, BLACK, (660, 65, 101, 15), 2)
        return

    def update(self):
        self.red_rect()
