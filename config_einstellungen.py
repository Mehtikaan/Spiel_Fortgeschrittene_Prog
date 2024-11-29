import configparser as cp

def erstelle_config_datei():
    # Erstellen eines ConfigParser-Objekts
   try: 
    config = cp.ConfigParser()

    # Hinzufügen von Sektionen und Werten
    config['Fenster'] = {
        'height': '600',
        'width': '800',
        'position':'250'
    }
    config["FPS"] = {
        "fps":"60",
    }
    config["Hussein"]= {
        "hüsso":"10",
    }

    # Schreiben der Konfigurationsdatei
    with open('config_game.ini', 'w') as configfile:
        config.write(configfile)

    return print("Die Konfigurationsdatei 'config_game.ini' wurde erstellt.")
   except:
       HEIGHT=600
       WIDTH=800
       POSITION=320
