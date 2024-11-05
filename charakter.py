import configparser as cp
# ConfigParser verwenden, um die Datei zu lesen
config=cp.ConfigParser()
config.read("config_game.ini")

# Werte aus der Konfigurationsdatei lesen
HEIGHT = config.get("Fenster", "height")
WIDTH = config.get("Fenster", "width")

class Charakter:
    def __init__(self,x_pos,y_pos,shoot,health_points, score_points):
        self.x_pos=1/4*WIDTH
        self.y_pos= 1/4*HEIGHT
        self.health_points=4
        self.score_points = None
        