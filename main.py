import pygame
from Game import Game


# Haupt Window erstellen
def main_run(PP_Anzahl, Geschwindigkeit, price):
    BREITE, HOHE = 1300, 780
    WIN_LOGO = "Images/Logo128.png"
    TITEL = "EasyParking"
    FPS = 60
    PP_in_Reihe = PP_Anzahl
    AutoZahl = PP_in_Reihe * 4
    running = True

    # Hauptklasse, mit allen Einstellungen
    game = Game(BREITE, HOHE, TITEL, PP_in_Reihe, FPS, WIN_LOGO, Geschwindigkeit, price)

    while running:
        game.run()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    game.SpeedUp()
                if event.key == pygame.K_F2:
                    game.SpeedDown()
                if event.key == pygame.K_F3:
                    game.verstecke_preis()
                if event.key == pygame.K_F4:
                    running = False
