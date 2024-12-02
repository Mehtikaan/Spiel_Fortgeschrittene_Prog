import pygame
import os

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        game_folder = os.path.dirname(__file__)
        # Kunai-Bild laden und skalieren
        self.image = pygame.image.load(os.path.join(game_folder, '_image', "6.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 10))  # Größe anpassen

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10  # Bullet speed

    def update(self):
        # Kugeln bewegen sich nach rechts
        self.rect.x += self.speed
        if self.rect.x > pygame.display.get_surface().get_width():  # Entfernen, wenn außerhalb des Bildschirms
            self.kill()