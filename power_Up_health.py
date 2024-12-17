import pygame
import math 
import os 

HEIGHT= 700
WIDTH = 1400
POSITION = 250
FPS=60

import pygame
import os
import math

class Health_reg(pygame.sprite.Sprite):
    def __init__(self, surface, gamefolder, charakter):
        super().__init__()
        self.x = WIDTH + 10
        self.y = HEIGHT - 270
        self.gamefolder = gamefolder
        self.charakter = charakter
        # Das Herzbild wird geladen
        self.image = pygame.image.load(os.path.join(gamefolder, '_image', "pixel_heart.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Bildgröße ändern
        self.surface = surface
        self.rect = self.image.get_rect()  # Setze das Rechteck basierend auf dem Bild
        self.rect.center = (self.x, self.y)  # Initiale Position festlegen
        self.original_y = self.y  # Ursprüngliche Y-Position speichern für schwebende Bewegung
        self.amplitude = 5  # Maximale Höhe der schwebenden Bewegung
        self.frequency = 0.1  # Geschwindigkeit der Schwebebewegung
        self.angle = 0  # Winkel für die Berechnung der Sinusbewegung
        self.speed = 2  # Geschwindigkeit des Power-ups

    def update(self):
        """Update der Position für schwebende Bewegung"""
        self.angle += self.frequency
        self.y = self.original_y + self.amplitude * math.sin(self.angle)  # Berechnung der schwebenden Bewegung
        self.x -= self.speed  # Power-up bewegt sich nach links
        self.rect.center = (self.x, self.y)  # Update der Rect-Position

    def draw(self):
        """Zeichnet das Bild auf der Oberfläche"""
        self.update()
        self.surface.blit(self.image, self.rect.center)  # Power-up auf der Oberfläche zeichnen

# Die generische Powerups-Klasse
class Powerups(pygame.sprite.Sprite):
    def __init__(self, surface, gamefolder, power_up_image, power_up_type,charakter, speed=2):
        super().__init__()
        self.surface = surface
        self.gamefolder = gamefolder
        self.charakter=charakter
        self.power_up_type = power_up_type  # Typ des Power-ups (z.B. 'jump', 'speed')
        self.image = pygame.image.load(os.path.join(gamefolder, '_image', power_up_image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Größe des Power-ups
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH + 10, HEIGHT - 200)  # Startposition


        # Schwebende Bewegung initialisieren
        self.original_y = self.rect.centery
        self.amplitude = 5
        self.frequency = 0.1
        self.angle = 0
        self.speed = speed

    def update(self):
        """Update der Power-up-Position und Kollision mit dem Charakter"""
        # Schwebende Bewegung
        self.angle += self.frequency
        self.rect.centery = self.original_y + self.amplitude * math.sin(self.angle)  # Schwebebewegung
        self.rect.x -= self.speed  # Power-up bewegt sich nach links

        # Überprüfe, ob das Power-up den Charakter berührt
        if self.rect.colliderect(self.charakter.bewegung.rect):
            self.apply_power_up()

    def apply_power_up(self):
        """Anwenden des spezifischen Power-ups"""
        if self.power_up_type == 'jump':
            self.charakter.springen.jumping_height = 40  # Sprunghöhe erhöhen
        self.kill()  # Entferne das Power-up nach Anwendung

    def draw(self):
        """Zeichnet das Power-up auf der Oberfläche"""
        self.surface.blit(self.image, self.rect)
class Jump_power_up(Powerups):
    def __init__(self, surface, gamefolder, power_up_image, charakter):
        super().__init__(surface, gamefolder, power_up_image, 'jump')
        self.charakter = charakter  # Der Charakter, dem das Power-up gegeben wird