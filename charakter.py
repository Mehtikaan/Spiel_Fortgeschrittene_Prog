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
    def __init__(self,x_pos,y_pos,shoot,health_points, score_points,sprite_charakter):
        self.x_pos=1/4*WIDTH
        self.y_pos= 1/4*HEIGHT
        self.health_points=4
        self.score_points = None
        self.image=sprite_charakter["charakter_run1"]
        self.imageRect= self.image.get_rect()
        self.timer = 0
        self.anim_frames = 8
        self.act_frame = 1
        self.max_ticks_anim = 0.6 * FPS / self.anim_frames
    
    def animation_update(self):
        am.animation_gehen(timer=self.timer,
                           max_timer=self.max_ticks_anim,
                           act_frame=self.act_frame,
                           anim_frames=self.anim_frames,
                           sprite_images=None,
                           name="charakter"
                           )