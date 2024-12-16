import os
import pygame
import config_einstellungen as bib
import configparser as cp
import charakter as ck
import time
pygame.mixer.init()
config = cp.ConfigParser()
import sys

WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()



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
    

main_charakter = None


# Vereinfachte Animation-Update-Funktion
def animation_update(timer, max_ticks, act_frame, anim_frames, sprite_images, name: str):
    """Aktualisiert die Animation für das Sprite"""
    timer += 1  # Timer hochzählen, um die Zeit zu verfolgen
    if timer >= max_ticks:
        timer = 0  # Timer zurücksetzen
        act_frame += 1  # Nächster Frame

    # Sicherstellen, dass der Frame innerhalb der verfügbaren Animationen bleibt
    if act_frame >= anim_frames:
        act_frame = 1  # Zurück zum ersten Frame, um eine Schleifenanimation zu erstellen

    # Auswahl des richtigen Animationsbildes basierend auf dem aktuellen Frame
    image = sprite_images.get(f"{name}{act_frame}")
    
    return image, timer, act_frame  # Bild, Timer und aktueller Frame zurückgeben

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
    button_image = pygame.transform.scale(button_image, (120, 120))  # Skalieren, um der Größe des Rects zu entsprechen

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


def draw_blurred_background(screen1):
    # Einen Screenshot machen und eine Verkleinerung für den Blur-Effekt erstellen
    surface = pygame.Surface((WIDTH // 5, HEIGHT // 5))
    pygame.transform.scale(screen1 , (WIDTH // 5, HEIGHT // 5), surface)
    pygame.transform.scale(surface, (WIDTH, HEIGHT), screen1 )

def restart_game():
    """Startet das Spiel durch erneuten Aufruf der Python-Datei."""
    python = sys.executable
    os.execl(python, python, *sys.argv)

running = True

def show_pause_menu(screen1, font):
    running = False
    while running == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if continue_button.collidepoint(mouse_pos):  # Klick auf "Continue"
                    running = True
                elif restart_button.collidepoint(mouse_pos):  # Klick auf "Restart"
                    restart_game()
                    

        # Verschwommenen Hintergrund und Menü-Elemente zeichnen
        draw_blurred_background(screen1= screen1)
        #pygame.draw.rect(screen1, GRAY, (200, 150, 400, 300), border_radius=10)

        # Buttons
        button_width, button_height = 200, 50
        button_spacing = 20  # Abstand zwischen Buttons

        continue_button = pygame.Rect(
            (WIDTH - button_width) // 2,  # X-Position: mittig
            (HEIGHT - button_height) // 2 - button_height - button_spacing // 2,  # Oberhalb der Mitte
            button_width, button_height
        )
        restart_button = pygame.Rect(
            (WIDTH - button_width) // 2,  # X-Position: mittig
            (HEIGHT - button_height) // 2 + button_spacing // 2,  # Unterhalb der Mitte
            button_width, button_height
        )

        # Buttons zeichnen
        pygame.draw.rect(screen1, BLACK, continue_button, border_radius=10)
        pygame.draw.rect(screen1, BLACK, restart_button, border_radius=10)

        # Button-Text rendern
        continue_text = font.render("Continue", True, WHITE)
        restart_text = font.render("Restart", True, WHITE)
        screen1.blit(continue_text, (continue_button.x + (button_width - continue_text.get_width()) // 2,
                                     continue_button.y + (button_height - continue_text.get_height()) // 2))
        screen1.blit(restart_text, (restart_button.x + (button_width - restart_text.get_width()) // 2,
                                    restart_button.y + (button_height - restart_text.get_height()) // 2))

        # Bildschirm aktualisieren
        pygame.display.flip()
        clock.tick(FPS)


game_folder = os.path.dirname(__file__)

damage_sound = pygame.mixer.Sound(os.path.join(game_folder, '_sounds','schmerzen.wav'))
damage_sound.set_volume(0.15)

# Variable, um den Zeitpunkt der letzten Soundwiedergabe zu speichern
last_damage_sound_time = 0  # Startwert ist 0
damage_sound_cooldown = 1  # Cooldown in Sekunden


def hitbox_check_enmy(wer, mitwem, surface):
    global last_damage_time, damage_cooldown
    global last_damage_sound_time, damage_sound_cooldown

    # Initialisiere den Cooldown, falls nicht vorhanden
    if 'last_damage_time' not in globals():
        last_damage_time = 0
    if 'damage_cooldown' not in globals():
        damage_cooldown = 1.0  # Cooldown in Sekunden

    # Erstelle die Hitbox des Gegners (Zombie oder Objekt)
    hitbox = pygame.Rect(mitwem.rect.x + 20, mitwem.rect.y + 20, 50, 50)

    # Erstelle die Hitbox für 'wer' (Charakter)
    playerhitbox = pygame.Rect(wer.bewegung.x_pos, wer.springen.y_pos, 75, 75)

    # Überprüfe, ob die Hitboxen kollidieren
    if playerhitbox.colliderect(hitbox):
        # Überprüfe, ob genug Zeit seit dem letzten Schaden vergangen ist
        current_time = time.time()
        if current_time - last_damage_time > damage_cooldown:
            main_charakter.health_points -= 40
            last_damage_time = current_time  # Aktualisiere die Zeit des letzten Schadens

            # Überprüfe, ob genug Zeit seit dem letzten Sound vergangen ist
            if current_time - last_damage_sound_time > damage_sound_cooldown:
                damage_sound.play()
                last_damage_sound_time = current_time  # Aktualisiere die Zeit der letzten Wiedergabe

            print(main_charakter.health_points)
    else:
        # Wenn keine Kollision vorliegt, aktualisiere die Bewegung des Spielers
        pass

    
    # Zeichne die Hitboxen zur Visualisierung
    pygame.draw.rect(surface, (255, 0, 0), playerhitbox, 2)  # Zeichnet die Hitbox des Spielers (rot)
    pygame.draw.rect(surface, (0, 0, 255), hitbox, 2)       # Zeichnet die Hitbox des Gegners (blau)


def hitbox_check_enmy_bullet(wer, mitwem, surface):
    # Prüfe, ob der 'wer' (z.B. Spieler oder Kugel) und der 'mitwem' (z.B. Zombie) kollidieren

    # Erstelle eine Hitbox für 'wer'
    playerhitbox = pygame.Rect(wer.rect.x, wer.rect.y, wer.rect.width, wer.rect.height)

    # Erstelle eine Hitbox für 'mitwem' (z.B. der Zombie)
    enemyhitbox = pygame.Rect(mitwem.rect.x, mitwem.rect.y, mitwem.rect.width, mitwem.rect.height)

    # Überprüfe, ob die Hitboxen kollidieren
    if playerhitbox.colliderect(enemyhitbox):
        
        print("Kollision zwischen", wer, "und", mitwem)
        # Hier kannst du die Kollision behandeln (z.B. Schaden zufügen, Gegner zerstören)
        return True

    # Zeichne die Hitboxen zur Visualisierung
    pygame.draw.rect(surface, (255, 0, 0), playerhitbox, 2)  # Spielerhitbox (rot)
    pygame.draw.rect(surface, (0, 0, 255), enemyhitbox, 2)   # Gegnerhitbox (blau)