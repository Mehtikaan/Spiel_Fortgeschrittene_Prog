import pygame

#load bullet image




# add to define game variables 
shoot = False 

bullet_img = pygame.image.load(" ").convert_alpha()


class Bullet(pygame.sprite.Sprite):

  def __init__(self, x_pos, y_pos, direction):
    
    pygame.sprite.Sprite__init__(self)
    self.speed = 10
    self.image = bullet_img
    self.Imagerect = self.image.get_rect()
    self.rect.center = (x_pos , y_pos)
    self.direction = direction 



# add to connections

if event.key == pygame.K_SPACE:
  shoot = True


# add to when keyboard button released 
if event.type == pygame.KEYUP:
  if event.key == pygame.K_SPACE:
    shoot = False 

  
