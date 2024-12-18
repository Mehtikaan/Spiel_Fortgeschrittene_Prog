import pygame

class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y, surface, sprite_image, scale=(80, 50), speed=8):

        super().__init__()
        self.surface = surface
        self.image = pygame.transform.scale(sprite_image, scale)
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)  
        self.speed = speed 
        self.start_x = x 

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:  
            self.rect.left = 4000 

    def draw(self):
        self.surface.blit(self.image, self.rect)