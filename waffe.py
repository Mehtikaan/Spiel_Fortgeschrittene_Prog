import pygame

#load bullet image

bullet_img = pygame.image.load(" ").convert_alpha()


class Bullet(pygame.sprite.Sprite):

  def __init__(self, x , y, direction):
    
    pygame.sprite.Sprite__init__(self)
    self.speed = 10
    self.image = bullet_img
    self.rect = self.image.get_rect()
    self.rect.center = (x , y)
    self.direction = direction 

  
