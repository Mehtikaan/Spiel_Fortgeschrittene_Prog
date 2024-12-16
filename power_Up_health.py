import pygame
import math 
import os 

HEIGHT= 700
WIDTH = 1400
POSITION = 250
FPS=60


class Health_reg(pygame.sprite.Sprite):
    def __init__(self, surface, gamefolder):
        super().__init__()
        self.x = WIDTH+10
        self.y = HEIGHT-200
        self.gamefolder = gamefolder
        # Das Herzbild wird geladen
        self.images = pygame.image.load(os.path.join(gamefolder, '_image', "herz.png")).convert_alpha()
        self.images=pygame.transform.scale(self.images,(50,50))
        self.surface = surface
        self.rect = self.images.get_rect()
        self.rect.center = (self.x, self.y)  # Initiale Position festlegen
        self.original_y = self.y  # Ursprüngliche Y-Position speichern für schwebende Bewegung
        self.amplitude = 5  # Maximale Höhe der schwebenden Bewegung
        self.frequency = 0.1  # Geschwindigkeit der Schwebebewegung
        self.angle = 0  # Winkel für die Berechnung der Sinusbewegung
        self.speed=2
    def update(self):
        """Update der Position für schwebende Bewegung"""
        self.angle += self.frequency
        self.y = self.original_y + self.amplitude * math.sin(self.angle)  # Berechnung der schwebenden Bewegung
        self.x-=self.speed
        self.rect.center = (self.x, self.y)  # Update der Rect-Position

    def draw(self):
        self.update()
        """Zeichnet das Bild auf der Oberfläche"""
        self.surface.blit(self.images, self.rect.center)

class Powerups()