import pygame
import animationen as am  
import configparser as cp



class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, surface, sprite_charakter, anim_name, hp, scale=(75, 75)):
        super().__init__()
        self.x = x
        self.y = y
        self.hp = hp 
        self.max_hp = hp  
        self.surface = surface
        self.sprite_charakter = sprite_charakter  
        self.anim_name = anim_name  
        self.anim_frames = len([key for key in self.sprite_charakter.keys() if anim_name in key]) 
        self.act_frame = 1  # Aktueller Frame der Animation
        self.timer = 0  # Timer für die Animation
        self.max_ticks_anim = 5  
        self.speed = 4
        self.scale = scale  # Zielgröße für die Bilder

        self.image = pygame.transform.scale(
            self.sprite_charakter.get(f"{self.anim_name}{self.act_frame}"), self.scale
        )
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)

    def update(self):
        # Timer erhöhen und Frame wechseln, wenn nötig
        self.timer += 1
        if self.timer >= self.max_ticks_anim:
            self.timer = 0
            self.act_frame += 1

            # Animation zurücksetzen, wenn alle Frames abgespielt wurden
            if self.act_frame > self.anim_frames:
                self.act_frame = 1

            self.image = pygame.transform.scale(
                self.sprite_charakter.get(f"{self.anim_name}{self.act_frame}"), self.scale
            )

        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()

    def draw_healthbar(self):
        bar_width = 50  
        bar_height = 5  
        # Berechne die Breite der Gesundheitsanzeige basierend auf der aktuellen Gesundheit
        health_ratio = self.hp / self.max_hp
        health_bar_width = bar_width * health_ratio

        #Rechtecke zeichnen
        pygame.draw.rect(self.surface, (0, 0, 0), (self.rect.x - 5, self.rect.y - 10, bar_width + 10, bar_height + 5))
        pygame.draw.rect(self.surface, (0, 255, 0), (self.rect.x, self.rect.y - 10, health_bar_width, bar_height))

    def draw(self):
        self.draw_healthbar()  
        self.surface.blit(self.image, self.rect)
