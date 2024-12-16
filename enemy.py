import pygame
import animationen as am  # Ich nehme an, dass 'am.animation_update' korrekt definiert ist
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
    POSITION = int(config.get("Fenster", "position"))
except Exception as e:
    print("Fehler beim Laden der Konfigurationswerte:", e)
    pygame.quit()
    exit()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, surface, sprite_charakter, anim_name, hp, scale=(75, 75)):
        super().__init__()
        self.x = x
        self.y = y
        self.hp = hp  # Aktuelle Gesundheit des Gegners
        self.max_hp = hp  # Maximale Gesundheit des Gegners
        self.surface = surface
        self.sprite_charakter = sprite_charakter  # Animationsbilder als Dictionary
        self.anim_name = anim_name  # Name der Animation (z. B. "walk")
        self.anim_frames = len([key for key in self.sprite_charakter.keys() if anim_name in key])  # Anzahl der Frames
        self.act_frame = 1  # Aktueller Frame der Animation
        self.timer = 0  # Timer für die Animation
        self.max_ticks_anim = 5  # Anzahl der Ticks zwischen Frame-Updates
        self.speed = 4  # Geschwindigkeit des Gegners nach links
        self.scale = scale  # Zielgröße für die Bilder

        # Initiales Bild und Rechteck setzen
        self.image = pygame.transform.scale(
            self.sprite_charakter.get(f"{self.anim_name}{self.act_frame}"), self.scale
        )
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)

    def update(self):
        """Update der Gegner-Logik, Animation und Bewegung"""
        # Timer erhöhen und Frame wechseln, wenn nötig
        self.timer += 1
        if self.timer >= self.max_ticks_anim:
            self.timer = 0
            self.act_frame += 1

            # Animation zurücksetzen, wenn alle Frames abgespielt wurden
            if self.act_frame > self.anim_frames:
                self.act_frame = 1

            # Aktuelles Bild aktualisieren und skalieren
            self.image = pygame.transform.scale(
                self.sprite_charakter.get(f"{self.anim_name}{self.act_frame}"), self.scale
            )

        # Bewegung nach links
        self.rect.x -= self.speed

        # Gegner entfernen, wenn er den Bildschirm verlässt
        if self.rect.right < 0:
            self.kill()

    def draw_healthbar(self):
        """Zeichnet die Gesundheitsanzeige des Gegners"""
        bar_width = 50  # Breite der Gesundheitsanzeige
        bar_height = 5  # Höhe der Gesundheitsanzeige
        # Berechne die Breite der Gesundheitsanzeige basierend auf der aktuellen Gesundheit
        health_ratio = self.hp / self.max_hp
        health_bar_width = bar_width * health_ratio

        # Rechteck für den Hintergrund der Gesundheitsanzeige (grau)
        pygame.draw.rect(self.surface, (0, 0, 0), (self.rect.x - 5, self.rect.y - 10, bar_width + 10, bar_height + 5))
        # Rechteck für den aktuellen Gesundheitsbalken (grün)
        pygame.draw.rect(self.surface, (0, 255, 0), (self.rect.x, self.rect.y - 10, health_bar_width, bar_height))

    def draw(self):
        """Zeichnet den Gegner und seine Gesundheitsanzeige"""
        self.draw_healthbar()  # Zeichne die Gesundheitsanzeige
        self.surface.blit(self.image, self.rect)
        