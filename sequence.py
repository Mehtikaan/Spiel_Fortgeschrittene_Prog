import pygame 
import os
import pygame.font
import sound as snd

HEIGHT= 700
WIDTH = 1400
POSITION = 250
FPS=60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
screen1 = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 56)  # Standard-Schriftart, Größe 56

score = 0.0


def wrap_text(text, font, max_width):
    """
    Teilt einen Text in mehrere Zeilen, sodass er in eine maximale Breite passt.
    """
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    return lines


sequence = [
    "Was passiert hier?",
    "Und was ist das für eine Musik?",
    "Morgen früh muss ich das Spiel vorstellen...",
    "Sonst lässt Krauss mich durchfallen...",
    "Wo bin ich??",
    "---",
    "Steuerung:",
    "Space = Jump,  F = Shoot,  Esc = Pause",
]


def show_sequence(screen, clock, sequence, font, width, height, game_folder):
    image_path = os.path.join(game_folder, '_image', "comic.png")
    comic = pygame.image.load(image_path).convert()
    comic = pygame.transform.scale(comic, (width, height))  # An Bildschirmgröße anpassen

    # Bild anzeigen
    screen.blit(comic, (0, 0))
    pygame.display.update()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # ENTER gedrückt
                running = False
                
    for text in sequence:
        # Text umbrechen, damit er nicht über den Bildschirm hinausgeht
        lines = wrap_text(text, font, width - 40)  # Padding von 40 für den Rand

        # Text rendern und positionieren
        screen.fill((0, 0, 0))  # Bildschirm schwarz füllen
        y_offset = height // 2 - (len(lines) * 20) // 2  # Vertikale Position, damit der Text mittig ist

        # Jede Zeile des Texts rendern und anzeigen
        for line in lines:
            text_surface = font.render(line, True, (255, 255, 255))  # Weißer Text
            text_rect = text_surface.get_rect(center=(width // 2, y_offset))
            screen.blit(text_surface, text_rect)  # Text anzeigen
            y_offset += 30  # Nächste Zeile nach unten verschieben

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # Mit ENTER zur nächsten Szene
                    running = False


            pygame.display.update()

            clock.tick(30)  # 30 FPS


sequence1 = [
    "Hab ich Ihn besiegt?",
    "Ne, warte mal?",
    "jetzt verstehe ich...",
    "Krauss unbesiegbar im Coden",
    "Ähmm, wieso ist mein Bett jetzt nass?!",
]


def ending_sequence(screen, clock, sequence1, font, width, height):
    for text in sequence1:
        # Text umbrechen, damit er nicht über den Bildschirm hinausgeht
        lines = wrap_text(text, font, width - 40)  # Padding von 40 für den Rand
        snd.end_music.play

        # Text rendern und positionieren
        screen.fill((0, 0, 0))  # Bildschirm schwarz füllen
        y_offset = height // 2 - (len(lines) * 20) // 2  # Vertikale Position, damit der Text mittig ist

        # Jede Zeile des Texts rendern und anzeigen
        for line in lines:
            text_surface = font.render(line, True, (255, 255, 255))  # Weißer Text
            text_rect = text_surface.get_rect(center=(width // 2, y_offset))
            screen.blit(text_surface, text_rect)  # Text anzeigen
            y_offset += 30  # Nächste Zeile nach unten verschieben

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # Mit ENTER zur nächsten Szene
                    running = False


            pygame.display.update()

            clock.tick(30)  # 30 FPS

def fade(screen, color, duration=float, fade_out=True, text=None, font=None, text_color=WHITE):
  
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.fill(color)

    # Schrittweite basierend auf der Dauer und der FPS
    step = int(255 / (FPS * duration))
    
    # Wenn wir ausblenden (fade_out=True), dann müssen wir die Alpha-Werte steigern,
    # beim Einblenden müssen wir sie verringern.
    for alpha in range(0, 255, step):
        fade_surface.set_alpha(alpha if fade_out else 255 - alpha)

        # Text wird direkt während des Fade-Effekts angezeigt und allmählich sichtbar
        if text and font:
            rendered_text = font.render(text, True, text_color)
            text_rect = rendered_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            
            # Text wird mit jedem Schritt immer sichtbarer, je mehr der Hintergrund eingeblendet wird
            screen.blit(fade_surface, (0, 0))
            screen.blit(rendered_text, text_rect) ###############hier vllt

        else:
            screen.blit(fade_surface, (0, 0))

        pygame.display.update()
        clock.tick(FPS)

def transition_sequence():
    global score
    # Score pausieren
    current_score = score  # Aktuellen Score speichern
    fade(screen1, BLACK, 0.1, fade_out=True)  # Bildschirm ausblenden (1 Sekunde)
    
    pygame.time.delay(2000)  # 2 Sekunden pausieren
    
    fade(screen1, BLACK, 0.2, fade_out=False)  # Bildschirm einblenden
    score = current_score  # Score zurücksetzen (während der Pause bleibt er gleich)


