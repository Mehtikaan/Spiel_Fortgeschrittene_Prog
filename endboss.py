import pygame
import animationen as am
import os
import math
import sound as snd

HEIGHT= 700
WIDTH = 1400
POSITION = 250
FPS=60

#Verwaltet einzelne Meteoriten
class Meteoriten(pygame.sprite.Sprite):
    def __init__(self, center_x, center_y, game_folder, num_meteorites=6, radius=110, speed=20):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.num_meteorites = num_meteorites
        self.radius = radius
        self.speed = speed
        self.image = pygame.image.load(os.path.join(game_folder, "_image", "meteor.png")).convert_alpha()

        self.meteorites_group = pygame.sprite.Group()

        # Erstelle Meteoriten und füge sie der Gruppe hinzu
        for i in range(self.num_meteorites):
            meteor = Meteorite(self.center_x, self.center_y, self.image, self.radius, i, self.speed)
            self.meteorites_group.add(meteor)

    def update(self, center_x, center_y):
        # Aktualisiert die Position der Meteoriten basierend auf den Mittelpunkt des Endbosses
        for meteor in self.meteorites_group:
            meteor.update(center_x, center_y)

    def draw(self, surface):
        self.meteorites_group.draw(surface)

class Meteorite(pygame.sprite.Sprite):
    def __init__(self, center_x, center_y, image, radius, index, speed):
        super().__init__()
        self.image = pygame.transform.scale(image, (30, 30))
        self.rect = self.image.get_rect()
        self.radius = radius
        self.index = index
        self.angle = (360 / 6) * self.index  # Der Winkel für die Position der Meteoriten
        self.speed = speed
        self.update_position(center_x, center_y)

    #ChatGPT
    #Berechnet die neue Position des Meteoriten auf dem Kreis um den Endboss
    def update_position(self, center_x, center_y):
        self.x = center_x + self.radius * math.cos(math.radians(self.angle))
        self.y = center_y + self.radius * math.sin(math.radians(self.angle))
        self.rect.center = (self.x, self.y)

    #Ändert den Winkel und bewegt den Meteoriten, während geprüft wird, ob er den Bildschirm verlässt
    def update(self, center_x, center_y):
        self.angle += self.speed
        if self.angle >= 360:
            self.angle -= 360  # Der Winkel soll sich wieder von 0 bis 360 wiederholen

        self.update_position(center_x, center_y)

        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()  

class MeteorToTarget(pygame.sprite.Sprite):
    def __init__(self, center_x, center_y, image, target_position):
        super().__init__()
        self.image = pygame.transform.scale(image, (30, 30)) 
        self.rect = self.image.get_rect()
        self.rect.center = (center_x, center_y)

        # Berechnung der Richtung zum Ziel (x, y)
        self.target_x, self.target_y = target_position
        self.speed = 10  

        #ChatGPT
        # Berechnung des Winkels zum Ziel
        dx = self.target_x - center_x
        dy = self.target_y - center_y
        self.angle = math.atan2(dy, dx)  # Winkelberechnung in Bogenmaß

    def update(self):
        #ChatGPT
        # Berechne die Bewegung basierend auf dem Winkel und der Geschwindigkeit
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)

        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

        # Überprüfen, ob der Meteoriten das Ziel erreicht hat
        if self.rect.collidepoint(self.target_x, self.target_y):
            self.kill() 

class Endboss(pygame.sprite.Sprite):
    def __init__(self, x, y, surface, sprite_charakter, anim_name, hp, gamefolder, scale=(100, 200)):
        super().__init__()
        self.x = x
        self.y = y
        self.hp = hp
        self.surface = surface
        self.sprite_charakter = sprite_charakter
        self.anim_name = anim_name
        self.anim_frames = len([key for key in self.sprite_charakter.keys() if anim_name in key])
        self.act_frame = 1
        self.timer = 0
        self.max_ticks_anim = 7
        self.scale = scale
        self.gamefolder = gamefolder
        self.image = pygame.transform.scale(
            self.sprite_charakter.get(f"{self.anim_name}{self.act_frame}"), self.scale
        )
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)
        self.meteor_image = pygame.image.load(os.path.join(self.gamefolder, "_image", "iceball.png")).convert_alpha()

        # Meteoriten, die den Endboss umkreisen
        self.meteoriten_group = pygame.sprite.Group()
        self.create_orbiting_meteorites()

        # Meteoriten für das Ziel
        self.meteoriten_target_group = pygame.sprite.Group()

        # Steuerung, um sicherzustellen, dass immer nur ein Meteoriten abgefeuert wird
        self.can_shoot = True  # Variable, um zu überprüfen, ob der Endboss schießen darf

        # Schwebende Bewegung
        self.float_amplitude = 10  # Höhe des Schwebens (in Pixeln)
        self.float_speed = 0.05  # Geschwindigkeit der Schwebebewegung
        self.initial_y = y  # Anfangshöhe
        self.angle_offset = 0  # Startwinkel für die Sinusbewegung

    def create_orbiting_meteorites(self):
        # Erstelle 6 Meteoriten, die den Endboss umkreisen
        self.num_meteorites = 6
        self.radius = 110
        self.speed = 2
        self.orbiting_meteorites = []
        
        for i in range(self.num_meteorites):
            meteor = Meteorite(self.rect.centerx, self.rect.centery, self.meteor_image, self.radius, i, self.speed)
            self.meteoriten_group.add(meteor)
            self.orbiting_meteorites.append(meteor)

    def update(self):
        self.timer += 1
        if self.timer >= self.max_ticks_anim:
            self.timer = 0
            self.act_frame += 1
            if self.act_frame > self.anim_frames:
                self.act_frame = 1
            self.image = pygame.transform.scale(
                self.sprite_charakter.get(f"{self.anim_name}{self.act_frame}"), self.scale
            )

        #ChatGPT
        # Schwebende Bewegung mit Sinuswelle
        self.angle_offset += self.float_speed
        self.y = self.initial_y + self.float_amplitude * math.sin(self.angle_offset)

        self.rect.center = (self.x, self.y)

        for meteor in self.orbiting_meteorites:
            meteor.update(self.rect.centerx, self.rect.centery)

        for meteor in self.meteoriten_target_group:
            meteor.update()

    def draw(self):
        self.surface.blit(self.image, self.rect)

        self.meteoriten_group.draw(self.surface)

        self.meteoriten_target_group.draw(self.surface)

    def shoot(self):
        sound_fireball= pygame.mixer.Sound(os.path.join(self.gamefolder, '_sounds','fireball.wav'))
        sound_fireball.set_volume(0.15)

        if self.can_shoot:  # Nur schießen, wenn der Endboss gerade nicht schießt
            # Das Ziel, auf das der Meteoriten geschossen wird
            target_position = (30, HEIGHT -90)
            start_x, start_y = self.rect.center 

            # Meteoriten zur Ziel-Gruppe hinzufügen
            new_meteor = MeteorToTarget(start_x, start_y, self.meteor_image, target_position)
            self.meteoriten_target_group.add(new_meteor)
            sound_fireball.play()
            # Setze can_shoot auf False, um weitere Schüsse zu verhindern
            self.can_shoot = False

    def enable_shooting(self):
        """Methode, um den Schuss wieder zu ermöglichen, z.B. nach einer Verzögerung oder einer Bedingung."""
        self.can_shoot = True


class Blitzen(pygame.sprite.Sprite):
    def __init__(self, x, y, gamefolder, surface):
        super().__init__()
        self.gamefolder = gamefolder
        self.x = x
        self.y = y  # Y-Position wird beim Initialisieren gesetzt
        self.surface = surface
        self.images = [] 
        self.index = 0
        
        # Laden der Explosion-Bilder und füge sie der Liste hinzu
        for i in range(5): 
            image = pygame.image.load(os.path.join(self.gamefolder, "_image", f"Explosion_{i}.png")).convert_alpha()
            image = pygame.transform.scale(image, (100, HEIGHT + 250))  
            self.images.append(image)
        
        # Setze das erste Bild als initiales Bild
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y) 

        self.animation_speed = 5 
        self.timer = 0  # Timer, um die Bilder zu wechseln

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height) 

    def update(self):
        self.timer += 1

        # Wenn genug Zeit vergeht, wechselt das Bild
        if self.timer >= self.animation_speed:
            self.timer = 0
            self.index += 1  # Geht zum nächsten Bild in der Liste
            if self.index >= len(self.images):  # Wenn alle Bilder durch sind, zurück zum ersten Bild
                self.index = 0

            # Setze das neue Bild und aktualisiere das Rechteck
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()  # Aktualisiere das Rechteck
            self.rect.center = (self.x, self.y)  # Position beibehalten

            self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

    def draw(self):
        self.surface.blit(self.image, self.rect)
        pygame.draw.rect(self.surface, (255, 0, 0), self.hitbox, 1)  # Das Viereck wird rot und 1 Pixel dick gezeichnet

    def get_hitbox(self):
        return self.hitbox