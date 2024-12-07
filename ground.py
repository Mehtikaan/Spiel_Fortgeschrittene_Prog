# import pygame
# import configparser as cp
# import config_einstellungen as bib
# from charakter import Charakter
# import animationen as am


# # Konfiguration laden oder erstellen
# config = cp.ConfigParser()
# if not config.read("config_game.ini"):
#     print("Erstelle Konfigurationsdatei...")
#     bib.erstelle_config_datei()

# config.read("config_game.ini")

# try:
#     HEIGHT = int(config.get("Fenster", "height"))
#     WIDTH = int(config.get("Fenster", "width"))
#     FPS = int(config.get("FPS", "fps"))
# except Exception as e:
#     print("Fehler beim Laden der Konfigurationswerte:", e)
#     pygame.quit()
#     exit()

# pygame.init()
# pygame.mixer.init()


# class Ground:
#     def __init__(self, x_pos, y_pos, sprite_map, tempo_x, scale_tempo_x, width, height, segment_count):
#         self.x_pos = x_pos
#         self.y_pos = y_pos
#         self.sprite_map = []
#         self.tempo_x = tempo_x
#         self.scale_tempo_x = scale_tempo_x
#         self.width = width
#         self.height = height
#         self.segment_count = segment_count

#     def update_position(self, delta_time):
#         "Bewegt den Boden nach links."
#         self.x_pos -= self.tempo_x * delta_time

#     def draw(self):
#         "Zeichnet das Bodensegment."
#         self.surface.blit(self.sprite_map, (self.x_pos, self.y_pos))

#     def reset_position(self, total_width):
#         "Setzt den Boden ans Ende zurück, wenn er aus dem Bildschirm verschwindet."
#         if self.x_pos + self.width < 0:
#             self.x_pos += total_width  # Verschiebt das Segment ans rechte Ende

#     def generate_ground_from_schema(schema, y_pos, sprite_map, tempo_x, segment_width, surface):
#         # Generiert Boden-Segmente basierend auf einem Schema.
#         # schema: Eine Zeichenkette aus '1' und '0', z.B. '100001'.
#         # y_pos: Die Y-Position des Bodens.
#         # sprite_map: Das Sprite-Bild des Bodens.
#         # tempo_x: Die Geschwindigkeit des Bodens.
#         # segment_width: Die Breite eines einzelnen Segments.
#         # surface: Die Pygame-Oberfläche.
#         # return: Eine Liste von Ground-Objekten.

#         ground_tiles = []
#         x_pos = 0

#         for char in schema:
#             if char == '1':
#                 ground_tiles.append(Ground(x_pos=x_pos, y_pos=y_pos, sprite_map=sprite_map, tempo_x=tempo_x,
#                                             width=segment_width, surface=surface))
#             x_pos += segment_width  # Verschiebe x_pos für jedes Zeichen, unabhängig von '1' oder '0'

#         return ground_tiles

