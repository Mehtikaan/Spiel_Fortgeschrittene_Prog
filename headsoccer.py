import configparser as cp
import pygame
import random
import os
import math
import time 


def erstelle_config():
    config = cp.ConfigParser()
    config["Fenster"] = {
     'height' : '600',
     'width':'800'
    }

    with open('config_game.ini', 'w') as configfile:
     config.write(configfile)

erstelle_config()

config=cp.ConfigParser()
config.read("config_game.ini")
HEIGHT=config.get("Fenster","height")
WIDTH=config.get("Fenster","width")

print(HEIGHT,WIDTH)



pygame.init()  # Pygame-Initialisierung
pygame.mixer.init()  # Sound-Ausgabe-Initialisierung
pygame.display.set_caption("exam.ension() Run")  # Überschrift des Fensters

clock = pygame.time.Clock()     #zeit

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED) 

running = True


game_folder = os.path.dirname('/Users/Hassouna/Desktop/Programmieren 2')    #erhöhung der portabilität, zugriff auf skripte o.Ä
image_folder = os.path.dirname('/Users/Hassouna/Desktop/Programmieren 2/Exam.mension() Run/EM Run Bilder')

