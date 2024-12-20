
import pygame
import os
import math
import configparser as cp
from charakter import Charakter, Waffe,Bullet
import animationen as am
from enemy import Enemy
import pygame.font
import random
from endboss import Endboss,Meteoriten,Blitzen
from power_Up_health import Health_reg, Powerups
from traps import Trap
from animationen import show_pause_menu
import image as img
import sound as snd
import sequence as sqn
import game_logic as gl

HEIGHT= 700
WIDTH = 1400
POSITION = 250
FPS=60

pygame.init()
pygame.mixer.init() 
pygame.display.set_caption("exam.ension() Run") 
clock = pygame.time.Clock()
screen1 = pygame.display.set_mode((WIDTH, HEIGHT))
game_folder = os.path.dirname(__file__)
pygame.mixer.music.set_volume(0.3)  # Lautstärke auf 50% einstellen


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (240, 0, 0)
GREEN = (0, 240, 0)
GOLD = (255, 215, 0)
BLUE = (150, 0, 160)
font = pygame.font.Font(None, 56) 

#Versuche
am.versuch_erhöhen()
versuche=am.lese_versuche()
am.speichere_versuche(versuche=versuche)


start_music_channel = snd.start_music.play()
start_music_channel = pygame.mixer.Channel(0) 
start_music_channel.play(snd.start_music)

background = img.background
background_width = img.background_width
backround_scroll = 0.0
backround_tiles = math.ceil(WIDTH / background_width) + 1
start_background  = img.start_background

platform_y = HEIGHT - 127
platform_rect = pygame.Rect(0,platform_y, 1400, 150) 
platform_width = img.platform_width
platform_height = img.platform_height
platform_image = img.platform_image
platform_scroll = 0.0
platform_tiles = math.ceil(WIDTH / platform_width) + 1

trap_image = img.trap_image


# Score initialisieren
score = 0.0

#Sprite Gruppen
herzen_group=pygame.sprite.Group()
blitze_group=pygame.sprite.Group()
power_up_group=pygame.sprite.Group()
all_traps = pygame.sprite.Group()
all_zombies = pygame.sprite.Group()

#Sprites laden
original_charakter = {}
sprite_charakter = {}
am.sprite_image_loader(game_folder=game_folder, folder_name="_image", image_max_num=8, image_name="ninja_run",
                        original_name=original_charakter, sprite_dict_name=sprite_charakter)

#Klassen
main_charakter = Charakter(
    x_pos=0, y_pos=HEIGHT - 195, sprite_charakter=sprite_charakter, fps=FPS,
    tempo_x=2, scale_tempo_x=1.01, health_points=200, score_points=0, surface=screen1)
am.main_charakter = main_charakter

trap = Trap(x=1600, y=HEIGHT - 185, surface=screen1, sprite_image=trap_image, scale=(80, 80), speed=8)
all_traps.add(trap)

endboss = Endboss(x=WIDTH-200, y=HEIGHT-400, surface=screen1, sprite_charakter=img.enemy_sprites_level_endboss, anim_name="endboss", hp=100, gamefolder=game_folder)

blitz = Blitzen(350, 1, game_folder, screen1)

waffe = Waffe(sprite_charakter=sprite_charakter, bewegung=main_charakter.bewegung,surface=screen1,springen=main_charakter.springen)


# Startbildschirm anzeigen
am.show_start_screen(screen1=screen1, clock=clock, start_background=start_background,game_folder=game_folder)
sequence = sqn.sequence
sqn.show_sequence(screen1, clock, sequence, font, WIDTH, HEIGHT, game_folder)



# Neuen Zombie beim Start des Spiels erstellen
if score <1000:
    gl.create_enemy(score, all_zombies, screen1)
else:
    pass
last_spawn_time = pygame.time.get_ticks()

#Level Wechsler
current_level = 0

level_music = {
    1: os.path.join(game_folder, '_sounds',"cowboy_music.wav"),
    2: os.path.join(game_folder, '_sounds',"robot_music.wav"),
    3: os.path.join(game_folder, '_sounds',"knight_music.wav"),
    4: os.path.join(game_folder, '_sounds',"santa_music.wav"),
    5: os.path.join(game_folder, '_sounds',"pumpkin_music.wav"),
    6: os.path.join(game_folder, '_sounds',"courli_music.wav")
}

level_texts = {
    1: "Puh, war das knapp!",
    2: "Das Outfit gefällt mir!",
    3: "Was hat es mit den blauen Flammen auf sich?",
    4: "Ich frage, mich wohin es als nächstes geht...",
    5: "Puh, war das kalt...",
    6: "Das kommt mir alles so bekannt vor..."    
    }

pygame.mixer.music.set_volume(0.15)  # Lautstärke einstellen

def level_changer():
    global platform_image, background, current_level, level_music, start_music_channel, trap_image

    # Musik-Stop nur einmal beim ersten Level
    if score >= 1000.0 and current_level == 0:
        if start_music_channel and start_music_channel.get_busy():
            snd.start_music.stop()
    
    # Level-Wechsel mit elif-Kette
    if score >= 9000 and current_level == 6:
        sqn.ending_sequence(screen1, clock, sequence, font, WIDTH, HEIGHT)
        main_game()
    
    elif score >= 6000 and current_level < 6:
        current_level = 6
        snd.portal_sound.play()
        change_level(6)
    elif score >= 5000 and current_level < 5:
        current_level = 5
        snd.portal_sound.play()
        change_level(5)
    elif score >= 4000 and current_level < 4:
        current_level = 4
        snd.portal_sound.play()
        change_level(4)
    elif score >= 3000 and current_level < 3:
        current_level = 3
        snd.portal_sound.play()
        change_level(3) 
    elif score >= 2000 and current_level < 2:
        current_level = 2
        snd.portal_sound.play()
        change_level(2)
    elif score >= 1000 and current_level < 1:
        current_level = 1
        snd.portal_sound.play()
        change_level(1)

def change_level(level):
    sqn.transition_sequence()
    img.platform_image = getattr(img, f"platform_image_level_{level}")
    img.background = getattr(img, f"background_level_{level}")
    pygame.mixer.music.load(level_music[level])
    pygame.mixer.music.play(-1)
    sqn.fade(screen1, BLACK, 1, fade_out=True, text=level_texts[level], font=font)
    all_zombies.empty()


def main_game():
    """Die Hauptspiel-Schleife."""
    global score, main_charakter, all_zombies, current_level
    # Setze alle Werte zurück
    score = 0
    #main_charakter.reset()  # Methode, die den Charakter zurücksetzt
    all_zombies.empty()  # Alle Zombies entfernen
    current_level = 0
    pygame.mixer.music.play(-1)  # Spielmusik starten

jump_power_up = Powerups(screen1, game_folder, power_up_image="play.png",power_up_type='jump' ,charakter=main_charakter)


def game_manager():
    # Überprüfe, ob das aktuelle Herz im Spiel weniger als oder gleich 40 HP ist
    if main_charakter.health_points <= 50:
        if len(herzen_group) <= 1:  
            herz = Health_reg(screen1, game_folder, charakter=main_charakter)
            herz.rect.x = WIDTH + 10  # Das Herz startet vom rechten Rand des Fensters
            herzen_group.add(herz)
        herzen_group.update()
        herzen_group.draw(screen1)

    # Überprüfe, ob die Bedingungen für den Blitz erfüllt sind
    if score >= 6500 and main_charakter.health_points >= 80:
        if len(blitze_group) < 1:  # Wenn noch kein Blitz existiert
            blitz = Blitzen(350, 1, game_folder, screen1)
            blitze_group.add(blitz)  # Blitz der Gruppe hinzufügen
        blitze_group.update() 
        blitze_group.draw(screen1) 

    if score > 6500 and main_charakter.health_points < 80:
        for blitz in blitze_group:
            blitz.kill() 
        blitze_group.empty()  
        endboss.shoot() 

shot_timer=pygame.time.get_ticks()

if score>6500:
            endboss.update()
            endboss.draw()
            current_time=pygame.time.get_ticks()
            if current_time-shot_timer>1000:
                endboss.enable_shooting()
                endboss.shoot()
                shot_timer=current_time


sequence = sqn.sequence1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                main_charakter.springen.start_sprung()
            if event.key == pygame.K_f:  # Schießen
                waffe.schiessen.shoot(waffe.rect)
            if event.key == pygame.K_ESCAPE:
                show_pause_menu(screen1= screen1, font= font)
        
    for zombie in all_zombies:
        zombie.update()
        zombie.draw()

    # Hintergrund scrollen
    backround_scroll -= 0.6
    if abs(backround_scroll) > background_width:
        backround_scroll = 0
    for i in range(backround_tiles):
        screen1.blit(img.background, (backround_scroll + i * background_width, 0))

        # Platform scrollen
    platform_scroll -= 7.5
    if abs(platform_scroll) > platform_width:
        platform_scroll = 0
    # Plattformen zeichnen
    for i in range(platform_tiles):
        screen1.blit(img.platform_image, (platform_scroll + i * platform_width, platform_y))

    score += 0.6 # Score um 1 pro Frame erhöhen

    score_text = font.render(f"{int(score):05d} m", True, WHITE)
    text_rect = score_text.get_rect(topright=(WIDTH - 60, 50))
    screen1.blit(score_text, text_rect)

    # Zombies und Charakter aktualisieren
    all_zombies.update()

    all_traps.update()
    for obstacle in all_traps:
        obstacle.draw()

    main_charakter.update()
    main_charakter.draw()

    # Neuen Zombie mit einer gewissen Wahrscheinlichkeit erzeugen
    elapsed_time = pygame.time.get_ticks() // 1000  # Spielzeit in Sekunden

    if score>6500:
            endboss.update()
            endboss.draw()
            current_time=pygame.time.get_ticks()
            if current_time-shot_timer>1000:
                endboss.enable_shooting()
                endboss.shoot()
                shot_timer=current_time
    if score == 6500:
        snd.welcome_sound.play()

    if blitze_group:
        for blitz in blitze_group:
            am.hitbox_check_blitz(main_charakter, blitz, screen1)
    if herzen_group:
        herzen_group.draw(screen1)
        for herz in herzen_group:
            if am.hitbox_check_enemy(main_charakter,herz,screen1,eventtyp="heilen"):
                am.hitbox_check_enemy(main_charakter,herz,screen1,eventtyp="heilen")
                herzen_group.empty()
                herz.kill()

    if endboss.meteoriten_target_group:
        for meteor in endboss.meteoriten_target_group:
            if am.hitbox_check_enemy(main_charakter,meteor,screen1,eventtyp="schaden"):
                am.hitbox_check_enemy(main_charakter,meteor,screen1,eventtyp="schaden")
                snd.krauss_attack.play()

    
    spawn_interval = random.randint(500,50000)  # Zufälliger Wert zwischen 500 und 50000 Sekunden in Millisekunden

    if pygame.time.get_ticks() - last_spawn_time > spawn_interval:
        gl.create_enemy(score=score, all_zombies = all_zombies, surface = screen1)  # Zombie nur hier erzeugen
        last_spawn_time = pygame.time.get_ticks()


    all_zombies.draw(screen1)

    waffe.schiessen.update()
    waffe.schiessen.draw(screen1) 
    for zombie in all_zombies:
        if  am.hitbox_check_enemy(wer=main_charakter, mitwem=zombie, surface=screen1,eventtyp="schaden"):
            am.hitbox_check_enemy(wer=main_charakter, mitwem=zombie, surface=screen1,eventtyp="schaden")
            main_charakter.bar.red_rect()
            zombie_stirb=all_zombies.sprites()[0]
            zombie_stirb.kill()
            
    
    # Kollision zwischen Kugeln und Zombies überprüfen
    for bullet in waffe.schiessen.bullets:
        for zombie in all_zombies:
            if am.hitbox_check_enemy_bullet(wer=bullet, mitwem=zombie, surface=screen1):
                zombie.hp-=1
                bullet.kill()
                zombie.draw()
                if zombie.hp==0:
                    zombie.kill()

    level_changer()
    game_manager()

    if main_charakter.health_points <= 0:
        snd.death_sound.play()
        sqn.fade(screen1, WHITE, 3.5, fade_out=True, text=f"Game Over - {versuche} Versuch", font=font, text_color=BLACK)
        am.restart_game()

    if score >= 8000.0:
        sqn.fade(screen1, BLACK, 1, fade_out=True, text='', font=font) 
        sqn.ending_sequence(screen1, clock, sequence, font, WIDTH, HEIGHT )
        am.restart_game()
    
        
    pygame.display.update()

    clock.tick(FPS)

am.show_start_screen(screen1=screen1, clock=clock, start_background=start_background,game_folder=game_folder)
main_game()  # Hauptspiel starten

pygame.quit()
