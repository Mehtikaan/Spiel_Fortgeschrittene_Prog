import pygame 


def show_intro_sequence(screen, clock):
    intro_text = [
        "Es war ein langer Tag, und der Code scheint endlos.",
        "Du sitzt an deinem Schreibtisch, die Müdigkeit übermannt dich...",
        "Plötzlich wachst du auf, aber nicht in deinem Zimmer.",
        "Chaos herrscht: fliegende Compiler-Fehler, endlose Schleifen, blinkende Variablen.",
        "Eine Stimme dröhnt: 'Willkommen in deinem Traum... oder Albtraum.'",
        "Bestehe die Prüfungen oder bleib gefangen!",
        "Nur ein Weg führt dich zurück in die Realität: Kämpfe und überliste den Bug!"
    ]
    
    screen.fill((0, 0, 0))  # Schwarzer Hintergrund
    font = pygame.font.Font(None, 50)  # Standard-Schriftart mit Größe 50
    line_spacing = 10  # Abstand zwischen den Zeilen
    max_width = WIDTH - 40  # Platz auf dem Bildschirm mit Rändern

    for paragraph in intro_text:
        screen.fill((0, 0, 0))  # Hintergrund schwarz machen
        lines = wrap_text(paragraph, font, max_width)  # Text umbrechen
        y_offset = (HEIGHT // 2) - (len(lines) * (font.get_height() + line_spacing)) // 2

        for line in lines:
            rendered_text = font.render(line, True, (255, 255, 255))  # Weißer Text
            text_rect = rendered_text.get_rect(center=(WIDTH // 2, y_offset))
            screen.blit(rendered_text, text_rect)
            y_offset += font.get_height() + line_spacing  # Abstand zwischen Zeilen

        pygame.display.flip()
        pygame.time.wait(3000)  # 3 Sekunden warten pro Text



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

