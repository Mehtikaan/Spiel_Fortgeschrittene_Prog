import pygame
import sys

#load bullet image
bullet_img = pygame.image.load(" ").convert_alpha()



# add to define game variables 
shoot = False 

# Groups
bullets = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):
  def __init__(self, x_pos, y_pos, direction):
    pygame.sprite.Sprite__init__(self)
    self.speed = 10
    self.image = bullet_img
    self.Imagerect = self.image.get_rect()
    self.rect.center = (x_pos , y_pos)
    self.direction = 'right'

  def update(self):
          # Kugeln bewegen sich nach rechts
          self.rect.x += BULLET_SPEED
          if self.rect.left > SCREEN_WIDTH:
              self.kill()
    


# Schießen mit der ENTER
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ENTER:
                bullet = Bullet(player.rect.right, player.rect.centery)
                all_sprites.add(bullet)
                bullets.add(bullet)



 # Update
    all_sprites.update()



    # move bullet 
    self.rect.x += (self.direction * self.speed)
    # check if bullet has gone of screen 
    if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
    


# add to when player alive 
if player.alive: 
  bullet = Bullet(player.rect.centerx, player.rect.centery, player.direction)

# add to actions

if event.key == pygame.K_ENTER:
  shoot = True


# add to when keyboard button released 
if event.type == pygame.KEYUP:
  if event.key == pygame.K_ENTER:
    shoot = False 

  
