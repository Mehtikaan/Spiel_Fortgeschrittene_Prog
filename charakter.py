import pygame
import animationen as am
import configparser as cp
import config_einstellungen as bib
from waffe import Bullet


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
        self.bullets = pygame.sprite.Group()  
        self.shoot_cooldown = 0  

        # Sprungvariablen
        self.y_velocity = 0
        self.gravity = 1
        self.jumping_height = 15
        self.jumping = False

    def shoot(self):
            """Feuert eine Kugel ab, wenn der Cooldown abgelaufen ist."""
            if self.shoot_cooldown == 0:  # Schießen nur, wenn Cooldown abgelaufen ist
                bullet = Bullet(self.x_pos + self.imageRect.width, self.y_pos + self.imageRect.height // 2)
                self.bullets.add(bullet)
                self.shoot_cooldown = 20  # Setze den Cooldown auf 20 Frames


    # Animation für Laufen
    def animation_update_laufen(self):
        self.image, self.timer, self.act_frame = am.animation_update(
            timer=self.timer,  # Unser Code hatte self.image, self.timer, self.act_frame drin, also nur Aufruf der Funktion am.animation_update
            max_ticks=self.max_ticks_anim,
            act_frame=self.act_frame,
            anim_frames=self.anim_frames,
            sprite_images=self.sprite_charakter,
            name="ninja_run"
        )
# Berechnung der Beschleunigung
        if self.x_pos <= POSITION:
            # Wenn der Charakter sich innerhalb eines bestimmten Bereichs bewegt, beschleunige ihn
            if self.x_pos < POSITION / 8:
                # Anfangs langsam - Steigere die Geschwindigkeit allmählich
                self.tempo_x += 0.05  # Kleine Erhöhung der Geschwindigkeit am Anfang

            elif self.x_pos < POSITION / 6:
                # Mittelbereich, erhöhe die Geschwindigkeit mehr
                self.tempo_x += 0.07

            else:
                # Später beschleunigen
                self.tempo_x += 0.045

            # Bewegung des Charakters unter Berücksichtigung der Beschleunigung
            self.x_pos += self.tempo_x

            # Beschleunigung durch Skalierung
            self.x_pos += self.tempo_x * self.scale_tempo_x

        self.imageRect.topleft = (self.x_pos, self.y_pos)

    def update(self):
        """Aktualisiert den Zustand des Charakters und der Kugeln."""
        # Aktualisiere Kugeln
        self.bullets.update()

        # Reduziere den Cooldown, wenn er größer als 0 ist
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    # Zeichnen auf der Oberfläche
    def zeichnen(self, surface):
        surface.blit(self.image, self.imageRect)
        self.bullets.draw(surface)
        return surface

    # Funktion für das Springen
    def springen(self,surface):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE] and not self.jumping:
            self.jumping = True
            self.y_velocity = self.jumping_height

        if self.jumping:
            self.y_pos -= self.y_velocity
            self.y_velocity -= self.gravity
    
            if self.y_pos >= HEIGHT - 200: #Bodenpostion
                self.y_pos = HEIGHT - 200
                self.jumping = False
        if self.jumping:
            # Setze die Sprung-Animation, wenn der Charakter springt
            JUMPING_SURFACE = self.sprite_charakter.get("ninja_jump", self.sprite_charakter["ninja_run1"])
            surface.blit(JUMPING_SURFACE, (self.x_pos, self.y_pos))
        else:
            # Wenn der Charakter nicht springt, führe die Lauf-Animation aus
            self.animation_update_laufen()
            self.zeichnen(surface=surface)
