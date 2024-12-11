import pygame 
import os




def show_intro_sequence(screen, clock):
    game_folder = os.path.dirname(_file_)
    sequence = [
    (os.path.join(game_folder, "_image", "scene1.png"), "Es war ein langer Tag, und der Code scheint endlos."),
    (os.path.join(game_folder, "_image", "scene2.png"), "Du sitzt an deinem Schreibtisch, die Müdigkeit übermannt dich..."),
    (os.path.join(game_folder, "_image", "scene3.png"), "Plötzlich wachst du auf, aber nicht in deinem Zimmer."),
    (os.path.join(game_folder, "_image", "scene4.png"), "Chaos herrscht: fliegende Compiler-Fehler, endlose Schleifen, blinkende Variablen."),
    (os.path.join(game_folder, "_image", "scene5.png"), "Eine Stimme dröhnt: 'Willkommen in deinem Traum... oder Albtraum.'"),
    (os.path.join(game_folder, "_image", "scene6.png"), "Bestehe die Prüfungen oder bleib gefangen!"),
    (os.path.join(game_folder, "_image", "scene7.png"), "Nur ein Weg führt dich zurück in die Realität: Kämpfe und überliste den Bug!")
]

    
    for image_path, text in sequence:
        # Bild laden und skalieren
        image = pygame.image.load(image_path).convert()
        image = pygame.transform.scale(image, (width, height))  # Bild auf die Bildschirmgröße anpassen

        # Text rendern
        text_surface = font.render(text, True, (255, 255, 255))  # Weiße Schriftfarbe
        text_rect = text_surface.get_rect(center=(width // 2, height - 50))  # Text knapp über dem unteren Rand

        # Zeit, wann das Bild wechseln soll
        start_time = pygame.time.get_ticks()  # Aktuelle Zeit in Millisekunden

        # Sequenz anzeigen
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Bildschirm leeren und Hintergrundbild anzeigen
            screen.fill((0, 0, 0))  # Hintergrund schwarz
            screen.blit(image, (0, 0))  # Bild auf den Bildschirm legen
            screen.blit(text_surface, text_rect)  # Text anzeigen

            pygame.display.update()

            # Wenn 3 Sekunden vergangen sind, gehe zur nächsten Szene
            if pygame.time.get_ticks() - start_time > 3000:  # 3000 ms = 3 Sekunden
                running = False

            clock.tick(30)  # 30 FPS




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

