import pygame
import animationen as am
import configparser as cp
import config_einstellungen as bib
import os
import sound as snd 
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
        self.surface = surface
        self.bewegung = Bewegung(x_pos, tempo_x, scale_tempo_x, sprite_charakter, fps)
        self.springen = Springen(y_pos, sprite_charakter, surface)
        
        # Mehrere Waffen instanziieren mit unterschiedlichen y_offset
        self.waffen =  [
            Waffe(self.bewegung, self.springen, sprite_charakter, surface, x_offset=20, y_offset=5),  # Oben
            Waffe(self.bewegung, self.springen, sprite_charakter, surface, x_offset=60, y_offset=50),
            Waffe(self.bewegung, self.springen, sprite_charakter, surface, x_offset=30, y_offset=30),
            Waffe(self.bewegung, self.springen, sprite_charakter, surface, x_offset=100, y_offset=30),
            Waffe(self.bewegung, self.springen, sprite_charakter, surface, x_offset=70, y_offset=-10)]
        self.health_points = health_points
        self.bar = Health_points(self, self.health_points, surface=surface)
        self.score_points = score_points

    def update(self):
        """Aktualisiert den Charakter: Bewegung, Animation, Schüsse und Springen"""
        for waffe in self.waffen:
            waffe.update(self.springen.y_pos)
        self.bewegung.update()
        jumping_sprite, self.springen.y_pos = self.springen.update(self.bewegung.x_pos)
        if jumping_sprite:
            self.bewegung.image = jumping_sprite  # Aktualisiert die Position der Waffe
        self.bar.update()

    def zeichnen(self):
        """Zeichnet den Charakter auf dem Bildschirm"""
        self.bewegung.zeichnen(self.surface, self.springen.y_pos)
        for waffe in self.waffen:  # Jede Waffe wird gezeichnet
            waffe.zeichnen(self.surface)

    def shoot(self):
        """Schießt eine Kugel ab"""
        for waffe in self.waffen:
            waffe.shoot()  # Jede Waffe kann schießen
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
        return self.x_pos

    def zeichnen(self, surface, y_pos):
        """Zeichnet den Charakter an der aktuellen Position"""
        surface.blit(self.image, (self.x_pos, y_pos))

class Springen:
    def __init__(self, y_pos, sprite_charakter, surface):
        self.y_pos = y_pos
        self.sprite_charakter = sprite_charakter
        self.surface = surface
        self.y_velocity = 0
        self.gravity = 1
        self.jumping_height = 28
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
    def __init__(self, charakter, health_points, surface):
        self.charakter = charakter
        self.health_points = health_points
        self.surface = surface

    def red_rect(self):
        pygame.draw.rect(self.surface, RED, (100, 30, 200, 30))
        pygame.draw.rect(self.surface, GREEN, (100, 30, self.charakter.health_points, 30))
        pygame.draw.rect(self.surface, BLACK, (100, 30, 202, 30), 2)
        return

    def update(self):
        self.red_rect()

class Waffe:
    def __init__(self, bewegung, springen, sprite_charakter, surface, x_offset=0, y_offset=0, new_image="kunai.png"):
        self.surface = surface
        self.bewegung = bewegung
        self.springen = springen
        self.sprite_charakter = sprite_charakter
        self.x_offset = x_offset
        self.initial_y_offset = y_offset
        self.y_offset = y_offset
        self.time = 0
        self.slow_time = 0
        self.new_image = new_image

        game_folder = os.path.dirname(__file__)
        # Lade das Bild einmal basierend auf new_image
        self.image = pygame.image.load(os.path.join(game_folder, '_image', new_image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 20))  # Größe anpassen
        self.rect = self.image.get_rect()

        # Übergabe der Bewegung und Springen Instanzen an die Schießen Klasse
        self.schiessen = Schießen(sprite_charakter, surface=surface, bewegung=self.bewegung, springen=self.springen)

    def change_image(self, new_image):
            """Ändert das Bild der Waffe, wenn der Score hoch genug ist"""
            # Verhindern, dass das Bild bei jedem Frame gewechselt wird
            if new_image != self.new_image:  # Nur ändern, wenn das Bild nicht schon gesetzt wurde
                print(f"Bild für Waffe ändern: {new_image}")  # Debugging-Ausgabe
                game_folder = os.path.dirname(__file__)
                # Lade nur dann ein neues Bild, wenn es sich wirklich ändert
                self.image = pygame.image.load(os.path.join(game_folder, '_image', new_image)).convert_alpha()
                self.image = pygame.transform.scale(self.image, (50, 20))  # Größe anpassen
                self.rect = self.image.get_rect()
                self.new_image = new_image  # Bildname aktualisieren

    def update(self, y_pos):
        """Aktualisiert die Position der Waffe basierend auf der Bewegung des Charakters"""
        # Langsame Veränderung der Y-Position der Waffe (nach oben und unten)
        if self.slow_time % 5 == 0:  # Alle 5 Frames eine kleine Veränderung
            if self.time <= 3:
                self.y_offset = self.initial_y_offset + self.time  # nach unten
            else:
                self.y_offset = self.initial_y_offset - (self.time - 3)  # nach oben

        # Zeit langsam erhöhen, um Bewegung zu verlangsamen
        self.slow_time += 0.5  # Zeit bei jedem Update langsam erhöhen
        self.time += 0.5  # Langsame Veränderung der vertikalen Position (Maximal 3 Pixel)
        if self.time > 6:  # Nach 6 Einheiten zurücksetzen
            self.time = 0

        # Aktualisiere die Position der Waffe
        self.rect.center = (
            self.bewegung.x_pos + self.x_offset,  # Unterschiedliche Position durch Offset
            y_pos + self.y_offset  # Unterschiedliche Position durch y_offset
        )

    def zeichnen(self, surface):
        """Zeichnet die Waffe auf dem Bildschirm"""
        surface.blit(self.image, self.rect.topleft)

class Schießen:
    def __init__(self, sprite_charakter, surface, bewegung, springen):
        self.surface = surface
        self.sprite_charakter = sprite_charakter
        self.shoot_cooldown = 0
        self.bullets = pygame.sprite.Group()
        self.bewegung = bewegung
        self.springen = springen
        self.shots_fired = 0
        self.max_shots = 10  # Maximale Anzahl der Schüsse vor dem Cooldown
        self.cooldown_active = False
        self.cooldown_timer = 0
        self.cooldown_duration = 4000  # 4 Sekunden Cooldown

    def shoot(self, waffen_rect, new_image="kunai.png"):
        """Feuert eine Kugel ab, wenn der Cooldown abgelaufen ist"""
        if not self.cooldown_active and self.shoot_cooldown == 0:
            print(f"Schießen von Position: {waffen_rect.centerx}, {waffen_rect.centery}")  # Debugging-Ausgabe
            # Kugel erzeugen und zur Gruppe hinzufügen
            bullet = Bullet(self.bewegung.x_pos + 80, self.springen.y_pos + 40, new_image)
            snd.kunai_sound.play()
            self.bullets.add(bullet)

            self.shoot_cooldown = 40  # Zeitverzögerung zwischen Schüssen aktivieren
            self.shots_fired += 1  # Anzahl der abgefeuerten Schüsse erhöhen

            # Cooldown nach 15 Schüssen aktivieren
            if self.shots_fired >= self.max_shots:
                self.cooldown_active = True
                self.cooldown_timer = pygame.time.get_ticks()  # Startzeitpunkt des Cooldowns speichern

    def update(self):
        """Aktualisiert die Kugeln und den Cooldown"""
        self.bullets.update()  # Kugeln aktualisieren (Bewegung)

        # Cooldown zwischen Schüssen verringern
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 5

        # Verwalte den Cooldown nach maximalen Schüssen
        if self.cooldown_active:
            current_time = pygame.time.get_ticks()
            if current_time - self.cooldown_timer >= self.cooldown_duration:
                self.cooldown_active = False  # Cooldown deaktivieren
                self.shots_fired = 0  # Schusszähler zurücksetzen

    def draw(self, surface):
        """Zeichnet alle Kugeln auf dem Bildschirm"""
        self.bullets.draw(surface)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, new_image):
        super().__init__()

        game_folder = os.path.dirname(__file__)
        self.image = pygame.image.load(os.path.join(game_folder, '_image', new_image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 40))  # Größe der Kugel anpassen
        self.image.set_colorkey((255, 255, 255))  # Weiß als transparent festlegen
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Position von der Waffe nehmen
        self.speed = 13  # Geschwindigkeit der Kugel
        self.new_image = new_image

    def update(self):
        """Bewegt die Kugel nach rechts und entfernt sie, wenn sie den Bildschirm verlässt"""
        self.rect.x += self.speed

        if self.rect.x > pygame.display.get_surface().get_width():  # Wenn die Kugel den Bildschirm verlässt
            self.kill()  # Entfernt die Kugel

    def draw(self, surface):
        """Zeichnet die Kugel auf dem Bildschirm"""
        surface.blit(self.image, self.rect.center)
