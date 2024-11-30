import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))  # A simple rectangle bullet
        self.image.fill((255, 0, 0))  # Red color for the bullet
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10  # Bullet speed


    def update(self):
          # Kugeln bewegen sich nach rechts
        self.rect.x += self.speed
        if self.rect.x > pygame.display.get_surface().get_width():
            self.kill()
  
