import configparser as cp
import config_einstellungen as bib
import pygame
import os

bib.erstelle_config_datei()  # Konfigurationsdatei erstellen

# ConfigParser verwenden, um die Datei zu lesen
config=cp.ConfigParser()
config.read("config_game.ini")

# Werte aus der Konfigurationsdatei lesen
HEIGHT = config.get("Fenster", "height")
WIDTH = config.get("Fenster", "width")
HEIGHT=int(HEIGHT)
WIDTH=int(WIDTH)

pygame.init()  # Pygame-Initialisierung
pygame.mixer.init()  # Sound-Ausgabe-Initialisierung
pygame.display.set_caption("exam.ension() Run")  # Überschrift des Fensters

clock = pygame.time.Clock()     #zeit

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED) 

running = True


game_folder = os.path.dirname('/Users/Hassouna/Desktop/Programmieren 2')    #erhöhung der portabilität, zugriff auf skripte o.Ä
image_folder = os.path.dirname('/Users/Hassouna/Desktop/Programmieren 2/Exam.mension() Run/EM Run Bilder')

