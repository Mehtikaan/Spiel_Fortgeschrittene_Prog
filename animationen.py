
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
        for i in range(1, image_max_num+1):
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
def show_start_screen(screen1, start_background, clock, game_folder, name):
    # Button-Position und Größe
    button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT-500 , 150, 50)  
    # Laden des Button-Bildes
    button_image = pygame.image.load(os.path.join(game_folder, "_image", f"{name}.png")).convert_alpha()
    button_image = pygame.transform.scale(button_image, (150, 50))  # Skalieren, um der Größe des Rects zu entsprechen

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):  # Klick auf den Start-Button
                    running = False  # Beende den Startbildschirm

        # Hintergrund des Startbildschirms zeichnen
        screen1.blit(start_background, (0, 0))

        # Hover-Effekt
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):  # Maus über dem Button
            # Optional: Ändere das Bild oder füge einen Hover-Effekt hinzu
            # Zum Beispiel könnte das Bild eine leichte Transparenz erhalten oder es könnte sich farblich ändern
            button_image.set_alpha(200)  # Mache den Button etwas transparenter beim Hover
        else:
            button_image.set_alpha(255)  # Normaler Zustand (volle Opazität)

        # Button-Bild zeichnen
        screen1.blit(button_image, button_rect.topleft)

        pygame.display.flip()
        clock.tick(FPS)
