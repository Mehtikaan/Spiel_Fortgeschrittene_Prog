import pygame
import os

HEIGHT= 700
WIDTH = 1400
POSITION = 250
FPS=60

clock = pygame.time.Clock()
screen1 = pygame.display.set_mode((WIDTH, HEIGHT))


# sequence = [
#     "Was passiert hier?",
#     "Und was ist das für eine Musik?",
#     "Morgen früh muss ich das Spiel vorstellen...",
#     "Sonst lässt Krauss mich durchfallen...",
#     "Wo bin ich??",

# ]


# def show_sequence(screen, clock, sequence, font, width, height, game_folder):
#     image_path = os.path.join(game_folder, '_image', "comic.png")
#     comic = pygame.image.load(image_path).convert()
#     comic = pygame.transform.scale(comic, (width, height))  # An Bildschirmgröße anpassen

#     # Bild anzeigen
#     screen.blit(comic, (0, 0))
#     pygame.display.update()
    
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()

#             if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # ENTER gedrückt
#                 running = False
                
#     for text in sequence:
#         # Text umbrechen, damit er nicht über den Bildschirm hinausgeht
#         lines = wrap_text(text, font, width - 40)  # Padding von 40 für den Rand

#         # Text rendern und positionieren
#         screen.fill((0, 0, 0))  # Bildschirm schwarz füllen
#         y_offset = height // 2 - (len(lines) * 20) // 2  # Vertikale Position, damit der Text mittig ist

#         # Jede Zeile des Texts rendern und anzeigen
#         for line in lines:
#             text_surface = font.render(line, True, (255, 255, 255))  # Weißer Text
#             text_rect = text_surface.get_rect(center=(width // 2, y_offset))
#             screen.blit(text_surface, text_rect)  # Text anzeigen
#             y_offset += 30  # Nächste Zeile nach unten verschieben

#         running = True
#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     exit()

#                 if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # Mit ENTER zur nächsten Szene
#                     running = False


#             pygame.display.update()

#             clock.tick(30)  # 30 FPS


# # Hindernis-Gruppe erstellen
# all_traps = pygame.sprite.Group()
# trap = Trap(
#     x=1600, y=HEIGHT - 142, surface=screen1, sprite_image=trap_image, scale=(60, 30), speed=7
# )
# all_traps.add(trap)




# # Startbildschirm anzeigen
# am.show_start_screen(screen1=screen1, clock=clock, start_background=start_background,name="play",game_folder=game_folder)

# show_sequence(screen1, clock, sequence, font, WIDTH, HEIGHT, game_folder)


# # Zombie-Gruppe erstellen
# all_zombies = pygame.sprite.Group()

# # Funktion zum Erstellen von Gegnern
# def create_enemy():
#     if score < 1000:
#         sprite_set = img.enemy_sprites_level_0  # Zombies bis Score 1000
#         anim_name = "zombie_walk"

#     elif score <2000:
#         sprite_set = img.enemy_sprites_level_1  # Cowboys ab Score 1000
#         anim_name = "cowboy_run"

#     elif score < 3000:
#         sprite_set = img.enemy_sprites_level_2
#         anim_name = "robot_walk"

#     elif score < 4000:
#         sprite_set = img.enemy_sprites_level_3
#         anim_name = "knight_walk"

#     elif score < 5000:
#         sprite_set = img.enemy_sprites_level_4
#         anim_name = "santa_walk"

#     elif score < 6000:
#         sprite_set = img.enemy_sprites_level_5
#         anim_name = "pumpkin_walk"

#     elif score < 7000:
#         sprite_set = img.enemy_sprites_level_6
#         anim_name = "courli"

    
#     enemy = Enemy(
#         x=WIDTH + 100,
#         y=HEIGHT - 192,
#         surface=screen1,
#         sprite_charakter=sprite_set,
#         anim_name=anim_name,
#         hp=5,
#     )
#     all_zombies.add(enemy)




# endboss = Endboss(x=WIDTH-200, y=HEIGHT-400, surface=screen1, sprite_charakter=img.enemy_sprites_level_endboss, anim_name="endboss", hp=100, gamefolder=game_folder)
# blitz = Blitzen(350, 1, game_folder, screen1)
# blitze=pygame.sprite.Group()


# # Neuen Zombie beim Start des Spiels erstellen
# if score <1000:
#     create_enemy()
# else:
#     pass

# score = 0.0

# herzen_group=pygame.sprite.Group()

# waffe = Waffe(sprite_charakter=sprite_charakter, bewegung=main_charakter.bewegung,surface=screen1,springen=main_charakter.springen)
# last_spawn_time = pygame.time.get_ticks()

# #Levelwechsel Übergang

# def fade(screen, color, duration=float, fade_out=True, text=None, font=None, text_color=WHITE):
  
#     fade_surface = pygame.Surface((WIDTH, HEIGHT))
#     fade_surface.fill(color)

#     # Schrittweite basierend auf der Dauer und der FPS
#     step = int(255 / (FPS * duration))
    
#     # Wenn wir ausblenden (fade_out=True), dann müssen wir die Alpha-Werte steigern,
#     # beim Einblenden müssen wir sie verringern.
#     for alpha in range(0, 255, step):
#         fade_surface.set_alpha(alpha if fade_out else 255 - alpha)

#         # Text wird direkt während des Fade-Effekts angezeigt und allmählich sichtbar
#         if text and font:
#             rendered_text = font.render(text, True, text_color)
#             text_rect = rendered_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            
#             # Text wird mit jedem Schritt immer sichtbarer, je mehr der Hintergrund eingeblendet wird
#             screen.blit(fade_surface, (0, 0))
#             screen.blit(rendered_text, text_rect) ###############hier vllt

#         else:
#             screen.blit(fade_surface, (0, 0))

#         pygame.display.update()
#         clock.tick(FPS)

# def transition_sequence():
#     global score
#     # Score pausieren
#     current_score = score  # Aktuellen Score speichern
#     fade(screen1, BLACK, 0.1, fade_out=True)  # Bildschirm ausblenden (1 Sekunde)
    
#     pygame.time.delay(2000)  # 2 Sekunden pausieren
    
#     fade(screen1, BLACK, 0.2, fade_out=False)  # Bildschirm einblenden
#     score = current_score  # Score zurücksetzen (während der Pause bleibt er gleich)