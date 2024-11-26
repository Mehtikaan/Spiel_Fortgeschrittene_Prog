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

  def update(self):
    # move bullet 
    self.rect.x += (self.direction * self.speed)
    # check if bullet has gone of screen 
    if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH
    


# add to when player alive 
if player.alive: 
  bullet = Bullet(player.rect.centerx, player.rect.centery, player.direction)

# add to connections

if event.key == pygame.K_ENTER:
  shoot = True


# add to when keyboard button released 
if event.type == pygame.KEYUP:
  if event.key == pygame.K_ENTER:
    shoot = False 

  
