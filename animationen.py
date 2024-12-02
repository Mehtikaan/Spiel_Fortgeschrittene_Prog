
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

def show_start_screen(screen1,start_background,clock):
    button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 - 25, 150, 50)  # Button-Position und Größe
    font = pygame.font.Font(None, 50)
    button_text = font.render("Start", True, (255, 255, 255))  # Weißer Text
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

        # Button zeichnen
        pygame.draw.rect(screen1, (0, 128, 255), button_rect)  # Blau
        screen1.blit(button_text, (button_rect.x + 40, button_rect.y + 5))  # Text auf den Button

        # Hover-Effekt
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen1, (0, 100, 200), button_rect)  # Dunkleres Blau
            screen1.blit(button_text, (button_rect.x + 40, button_rect.y + 5))

        pygame.display.flip()
        clock.tick(FPS)