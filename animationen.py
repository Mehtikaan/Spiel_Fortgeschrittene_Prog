
import os
import pygame
import config_einstellungen as bib
import configparser as cp
config = cp.ConfigParser()
if not config.read("config_game.ini"):
    print("Erstelle Konfigurationsdatei...")
    bib.erstelle_config_datei()

config.read("config_game.ini")
try:
    HEIGHT = int(config.get("Fenster", "height"))
    WIDTH = int(config.get("Fenster", "width"))
    FPS = int(config.get("FPS", "fps"))
except Exception as e:
    print("Fehler beim Laden der Konfigurationswerte:", e)
    pygame.quit()
    exit()
    
def animation_update(timer,max_ticks, act_frame,anim_frames, sprite_images,name:str):
    timer+=1
    if timer >=max_ticks:
        timer=0
        act_frame +=1
    if act_frame>=anim_frames:
        act_frame=1
    return sprite_images[name+str(act_frame)], timer, act_frame

def animation_gehen():
    
    pass
def sprite_image_loader(game_folder:str, folder_name:str, image_max_num:int, image_name:str, original_name:dict, sprite_dict_name:dict): 
    try:
        for i in range(1, image_max_num):
            # Jedes Bild des Laufcharakters laden und in einem Dictionary speichern
            sprite_path = os.path.join(game_folder, folder_name, f'{image_name}{i}.png')
            
            # Fehler, wenn das Bild nicht gefunden wird
            if not os.path.exists(sprite_path):
                raise FileNotFoundError(f"Bilddatei nicht gefunden: {sprite_path}")
            
            # Lade das Bild und speichere es im original_name Dictionary
            original_name[f"{image_name}{i}"] = pygame.image.load(sprite_path).convert_alpha()
            
            # Skaliere das Bild und speichere es im sprite_dict_name Dictionary
            sprite_dict_name[f"{image_name}{i}"] = pygame.transform.scale(original_name[f"{image_name}{i}"], (75, 75))  # Bildgröße anpassen wurde mit Chatgpt gemacht

    except Exception as e:
        print("Fehler beim Laden der Sprite-Bilder:", e)
        pygame.quit()
        exit()
    
    # Rückgabe des bearbeiteten Dictionaries
    return sprite_dict_name, original_name


import pygame
import os

# Initialisiere Pygame
pygame.init()

# Funktion zum Abspielen eines "Videos" aus Bildern
def play_video(image_folder, width=WIDTH, height=HEIGHT, fps=FPS ):
    """
    Spielt ein Video ab, das aus einer Serie von Bildern besteht.

    :param image_folder: Der Ordner, der die Bilder enthält.
    :param width: Die Breite des Fenster (Standard: 800).
    :param height: Die Höhe des Fensters (Standard: 600).
    :param fps: Die Frames pro Sekunde (Standard: 30).
    """
    # Fenster erstellen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Video in Pygame")

    # Liste der Bilddateien (Frames des "Videos")
    frame_files = sorted(os.listdir(image_folder))  # Alle Dateien im Ordner sortieren

    # Bilder laden
    frames = []
    for frame_file in frame_files:
        if frame_file.endswith(".png") or frame_file.endswith(".jpg"):  # Nur Bilddateien einbeziehen
            image_path = os.path.join(image_folder, frame_file)
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (width, height))  # Bildgröße anpassen
            frames.append(image)

    # Spiel-Schleife
    clock = pygame.time.Clock()
    running = True
    frame_index = 0

    while running:
        # Ereignisse behandeln
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Nächstes Bild anzeigen
        screen.fill((0, 0, 0))  # Bildschirm löschen
        screen.blit(frames[frame_index], (0, 0))  # Aktuelles Bild anzeigen
        pygame.display.update()

        # Warten, um die Bildrate zu kontrollieren (z.B. 30 FPS)
        frame_index += 1
        if frame_index >= len(frames):
            frame_index = 0  # Wenn das Ende erreicht ist, wieder von vorne starten

        clock.tick(fps)  # Die Bildrate steuern

    # Pygame beenden
    pygame.quit()

# Beispielaufruf der Funktion:
# play_video("_video_frames", width=800, height=600, fps=30)
