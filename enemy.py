import pygame
import animationen as am  

import pygame
import animationen as am  # Ich nehme an, dass 'am.animation_update' korrekt definiert ist
import configparser as cp
import config_einstellungen as bib

HEIGHT = 700
WIDTH = 1400
POSITION = 250
FPS = 60

class HealthBar:
    def __init__(self, x, y, max_hp):
        self.x = x
        self.y = y
        self.max_hp = max_hp
        self.current_hp = max_hp

    def update(self, current_hp):
        """Aktualisiert die Lebensanzeige mit dem aktuellen HP-Wert"""
        self.current_hp = current_hp

    def draw(self, surface):
        """Zeichnet die Lebensanzeige"""
        bar_width = 50  # Breite der Gesundheitsanzeige
        bar_height = 5  # Höhe der Gesundheitsanzeige

        # Berechne die Breite der Gesundheitsanzeige basierend auf der aktuellen Gesundheit
        health_ratio = self.current_hp / self.max_hp
        health_bar_width = bar_width * health_ratio

        # Rechteck für den Hintergrund der Gesundheitsanzeige (schwarz)
        pygame.draw.rect(surface, (0, 0, 0), (self.x - 5, self.y - 10, bar_width + 10, bar_height + 5))

        # Rechteck für den aktuellen Gesundheitsbalken (grün)
        pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y - 10, health_bar_width, bar_height))


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

        # Lebensanzeige erstellen
        self.health_bar = HealthBar(self.rect.centerx - 25, self.rect.top - 10, self.hp)

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

        # Lebensanzeige aktualisieren
        self.health_bar.update(self.hp)

        # Position der Lebensanzeige anpassen (immer oben und in der Mitte des Gegners)
        self.health_bar.x = self.rect.centerx - 25  # Zentrale Position des Balkens
        self.health_bar.y = self.rect.top - 10     # Direkt über dem Gegner

    def draw(self):
        """Zeichnet den Gegner und seine Gesundheitsanzeige"""
        # Zeichne den Gegner
        self.surface.blit(self.image, self.rect)

        # Zeichne die Lebensanzeige
        self.health_bar.draw(self.surface)
