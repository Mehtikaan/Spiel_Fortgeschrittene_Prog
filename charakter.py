import configparser as cp
import pygame 
import animationen as am

# ConfigParser verwenden, um die Datei zu lesen
config=cp.ConfigParser()
config.read("config_game.ini")

# Werte aus der Konfigurationsdatei lesen
HEIGHT = int(config.get("Fenster", "height"))
WIDTH = int(config.get("Fenster", "width"))
FPS = int(config.get("FPS", "fps"))

#Klasse des Hauptcharakters
class Charakter:
    def __init__(self,x_pos,y_pos,shoot,health_points, score_points,sprite_charakter,fps):
        self.x_pos=x_pos
        self.y_pos= y_pos
        self.health_points=int
        self.score_points = int
        self.image=sprite_charakter["charakter_run1"]
        self.imageRect= self.image.get_rect()
        self.timer = 0
        self.anim_frames = 8
        self.act_frame = 1
        self.max_ticks_anim = 0.6 * FPS / self.anim_frames
        self.sprite_charakter=sprite_charakter

    #Aus der Bibleothek  animation importiert zum Updaten
    def animation_update_laufen(self):   
        self.x_pos+=3                             
        self.image,self.timer,self.act_frame=am.animation_update(timer=self.timer,  #Unser Code hatte self.image,self.timer,self.act_frame= drinnen,also nur aufruf der Funktion am.animation_update,
                           max_ticks=self.max_ticks_anim,                           #deshalb hat sich das Bild nicht geupdatet, daher debug mit chatgpt
                           act_frame=self.act_frame,                                
                           anim_frames=self.anim_frames,
                           sprite_images=self.sprite_charakter,
                           name="charakter_run"
                           )
        self.imageRect.topleft=(self.x_pos,self.y_pos)

        

    def zeichnen(self,surface):
        surface.blit(self.image,self.imageRect)
    
    