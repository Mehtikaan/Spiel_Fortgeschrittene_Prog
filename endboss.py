import pygame
import animationen as am
import configparser as cp
import config_einstellungen as bib
import os
import math
HEIGHT= 700
WIDTH = 1400
POSITION = 250
FPS=60

# Meteoriten-Klasse: Verwaltet einzelne Meteoriten
class Meteoriten(pygame.sprite.Sprite):
    def __init__(self, center_x, center_y, game_folder, num_meteorites=6, radius=110, speed=20):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.num_meteorites = num_meteorites
        self.radius = radius
        self.speed = speed
        self.image = pygame.image.load(os.path.join(game_folder, "_image", "meteor.png")).convert_alpha()

        # Liste für die Meteoriten-Objekte
        self.meteorites_group = pygame.sprite.Group()

        # Erstelle Meteoriten und füge sie der Gruppe hinzu
        for i in range(self.num_meteorites):
            meteor = Meteorite(self.center_x, self.center_y, self.image, self.radius, i, self.speed)
            self.meteorites_group.add(meteor)

    def update(self, center_x, center_y):
        # Aktualisiere die Position der Meteoriten basierend auf dem Mittelpunkt des Endbosses
        for meteor in self.meteorites_group:
            meteor.update(center_x, center_y)

    def draw(self, surface):
        # Alle Meteoriten zeichnen
        self.meteorites_group.draw(surface)

class Meteorite(pygame.sprite.Sprite):
    def __init__(self, center_x, center_y, image, radius, index, speed):
        super().__init__()
        self.image = pygame.transform.scale(image, (30, 30))  # Skalieren auf 30x30
        self.rect = self.image.get_rect()
        self.radius = radius
        self.index = index
        self.angle = (360 / 6) * self.index  # Der Winkel für die Position der Meteoriten
        self.speed = speed
        self.update_position(center_x, center_y)

    def update_position(self, center_x, center_y):
        """Berechnet die neue Position des Meteoriten auf dem Kreis um den Endboss"""
        self.x = center_x + self.radius * math.cos(math.radians(self.angle))
        self.y = center_y + self.radius * math.sin(math.radians(self.angle))
        self.rect.center = (self.x, self.y)

    def update(self, center_x, center_y):
        """Ändert den Winkel und bewegt den Meteoriten, während geprüft wird, ob er den Bildschirm verlässt"""
        self.angle += self.speed
        if self.angle >= 360:
            self.angle -= 360  # Der Winkel soll sich wieder von 0 bis 360 wiederholen

        # Update die Position des Meteoriten
        self.update_position(center_x, center_y)

        # Überprüfen, ob der Meteoriten den Bildschirm verlässt
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()  # Meteoriten von der Gruppe entfernen

class MeteorToTarget(pygame.sprite.Sprite):
    def __init__(self, center_x, center_y, image, target_position):
        super().__init__()
        self.image = pygame.transform.scale(image, (30, 30))  # Meteoritenbild skalieren
        self.rect = self.image.get_rect()
        self.rect.center = (center_x, center_y)

        # Berechnung der Richtung zum Ziel (x, y)
        self.target_x, self.target_y = target_position
        self.speed = 10  # Geschwindigkeit der Meteoriten

        # Berechnung des Winkels zum Ziel
        dx = self.target_x - center_x
        dy = self.target_y - center_y
        self.angle = math.atan2(dy, dx)  # Winkelberechnung in Bogenmaß

    def update(self):
        """Bewege den Meteoriten in Richtung des Ziels und prüfe, ob er den Bildschirm verlässt"""
        # Berechne die Bewegung basierend auf dem Winkel und der Geschwindigkeit
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)

        # Überprüfen, ob der Meteoriten den Bildschirm verlässt
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()  # Meteoriten von der Gruppe entfernen

        # Überprüfen, ob der Meteoriten das Ziel erreicht hat
        if self.rect.collidepoint(self.target_x, self.target_y):
            self.kill()  # Meteoriten von der Gruppe entfernen, wenn das Ziel erreicht wurde

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

        # Bild für die Meteoriten laden
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
        # Update die Animation und andere Endboss-Logik
        self.timer += 1
        if self.timer >= self.max_ticks_anim:
            self.timer = 0
            self.act_frame += 1
            if self.act_frame > self.anim_frames:
                self.act_frame = 1
            self.image = pygame.transform.scale(
                self.sprite_charakter.get(f"{self.anim_name}{self.act_frame}"), self.scale
            )

        # Schwebende Bewegung mit Sinuswelle
        self.angle_offset += self.float_speed
        self.y = self.initial_y + self.float_amplitude * math.sin(self.angle_offset)

        self.rect.center = (self.x, self.y)

        # Update der Meteoriten, die den Endboss umkreisen
        for meteor in self.orbiting_meteorites:
            meteor.update(self.rect.centerx, self.rect.centery)

        # Update der Meteoriten, die das Ziel anvisieren
        for meteor in self.meteoriten_target_group:
            meteor.update()

    def draw(self):
        self.surface.blit(self.image, self.rect)

        # Meteoriten, die den Endboss umkreisen
        self.meteoriten_group.draw(self.surface)

        # Meteoriten, die das Ziel anvisieren
        self.meteoriten_target_group.draw(self.surface)

    def shoot(self):
        """Schießt einen Meteoriten auf das Ziel, aber nur wenn noch kein Meteoriten geschossen wurde."""
        sound_fireball= pygame.mixer.Sound(os.path.join(self.gamefolder, '_sounds','fireball.wav'))
        sound_fireball.set_volume(0.15)

        if self.can_shoot:  # Nur schießen, wenn der Endboss gerade nicht schießt
            # Das Ziel, auf das der Meteoriten geschossen wird
            target_position = (30, HEIGHT -90)
            start_x, start_y = self.rect.center  # Meteoriten starten bei der Position des Endbosses

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
        self.images = []  # Liste für die Bilder
        self.index = 0
        
        # Lade die Explosion-Bilder und füge sie der Liste hinzu
        for i in range(5):  # 5 Bilder für die Animation
            image = pygame.image.load(os.path.join(self.gamefolder, "_image", f"Explosion_{i}.png")).convert_alpha()
            print(f"Image size: {image.get_width()} x {image.get_height()}")  # Debug-Ausgabe
            image = pygame.transform.scale(image, (100, HEIGHT + 250))  # Breite x Höhe
            print(f"Scaled image size: {image.get_width()} x {image.get_height()}")  # Debug-Ausgabe
            self.images.append(image)
        
        # Setze das erste Bild als initiales Bild
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)  # Startposition: Oben im Bildschirmbereich

        self.animation_speed = 5  # Geschwindigkeit der Bildwechsel (Verzögerung)
        self.timer = 0  # Timer, um die Bilder zu wechseln

        # Definiere die Hitbox des Blitzes
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)  # Standardhitbox ist das rect

    def update(self):
        """Update die Animation der Explosion"""
        self.timer += 1

        # Wenn genug Zeit vergangen ist, wechsle das Bild
        if self.timer >= self.animation_speed:
            self.timer = 0
            self.index += 1  # Gehe zum nächsten Bild in der Liste
            if self.index >= len(self.images):  # Wenn alle Bilder durch sind, zurück zum ersten Bild
                self.index = 0

            # Setze das neue Bild und aktualisiere das Rechteck
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()  # Aktualisiere das Rechteck
            self.rect.center = (self.x, self.y)  # Position beibehalten

            # Update die Hitbox
            self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

    def draw(self):
        """Zeichne das aktuelle Bild auf die Surface"""
        self.surface.blit(self.image, self.rect)  # Zeichne das Bild an der Position des Rects

        # Debug-Ausgabe der Position
        print(f"Blitz Position: x={self.rect.centerx}, y={self.rect.centery}")

        # Zeichne ein Viereck um die Hitbox (Rot und eine Linienstärke von 1)
        pygame.draw.rect(self.surface, (255, 0, 0), self.hitbox, 1)  # Das Viereck wird rot und 1 Pixel dick gezeichnet

    def get_hitbox(self):
        """Gibt die Hitbox zurück für Kollisionserkennung"""
        return self.hitbox