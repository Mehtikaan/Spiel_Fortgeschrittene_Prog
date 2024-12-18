import pygame

class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y, surface, sprite_image, scale=(80, 50), speed=8):
        """
        Ein Hindernis, das von rechts nach links schwebt.
        """
        super().__init__()
        self.surface = surface
        self.image = pygame.transform.scale(sprite_image, scale)  # Hindernisbild skalieren
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)  # Startposition festlegen
        self.speed = speed  # Bewegungsgeschwindigkeit
        self.start_x = x  # Speichert die Startposition

    def update(self):
        """Bewegung von rechts nach links."""
        self.rect.x -= self.speed
        if self.rect.right < 0:  # Wenn das Hindernis aus dem Bildschirm geht
            self.rect.left = 4000  # Zurück an den rechten Rand setzen

    def draw(self):
        """Hindernis auf dem Bildschirm rendern."""
        self.surface.blit(self.image, self.rect)