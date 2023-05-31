import pygame
import button
import main




pygame.init()

# window
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 780

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# hintergrund erstellen
hintergrund = pygame.image.load("images menu/parkingsearch-780.jpg")
hintergrund_rect = hintergrund.get_rect()

# game variablen
game_paused = True
menu_options = "main"

# schriftart
font = pygame.font.SysFont("arialblack", 40)

# farben
TEXT_COL = (254,254,18)
ZAHLEN_COL = (79, 79, 239)

# zahlenkästen
Box_col = (0, 0, 0)

Box_Ges = pygame.Rect(140, 200, 70, 60)
Box_Geld = pygame.Rect(140, 320, 90, 60)
Box_Anz = pygame.Rect(140, 440, 95, 60)

# button bilder laden
resume_img = pygame.image.load("images menu/start.png").convert_alpha()
options_img = pygame.image.load("images menu/einstellungen.png").convert_alpha()
quit_img = pygame.image.load("images menu/beenden.png").convert_alpha()
back_img = pygame.image.load("images menu/zurück.png").convert_alpha()
up_img = pygame.image.load("images menu/hoch.png").convert_alpha()
down_img = pygame.image.load("images menu/runter.png").convert_alpha()

# button erstellen
resume_button = button.Button(200, 225, resume_img, 1)
options_button = button.Button(200, 315, options_img, 1)
quit_button = button.Button(200, 405, quit_img, 1)

back_button = button.Button(130, 530, back_img, 1)

up_button1 = button.Button(250, 200, up_img, 1)
up_button2 = button.Button(250, 320, up_img, 1)
up_button3 = button.Button(250, 440, up_img, 1)

down_button1 = button.Button(60, 200, down_img, 1)
down_button2 = button.Button(60, 320, down_img, 1)
down_button3 = button.Button(60, 440, down_img, 1)

# counter anfangswert
count1_Ges = 1
count2_Preis = 0.5
count3_Anz = 12

# counter schritte
Geschwindigkeit_wert = 1
Geld_wert = 0.5
Anzahl_wert = 4


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


variable_Parkplätze = 3
variable_Geschwindigkeit = 1
variable_Preis = 0.5

# game loop
run = True
while run:
    # pause hintergrund
    screen.blit(hintergrund, hintergrund_rect)
    # pause
    if game_paused == True:

        if menu_options == "main":
            draw_text("Start", font, TEXT_COL, 300, 225)
            draw_text("Einstellungen", font, TEXT_COL, 300, 325)
            draw_text("Beenden", font, TEXT_COL, 300, 425)

            if resume_button.draw(screen):
                main.main_run(variable_Parkplätze, variable_Geschwindigkeit, variable_Preis)
            if options_button.draw(screen):
                menu_options = "options"
            if quit_button.draw(screen):
                run = False

        # optionen menu
        if menu_options == "options":

            draw_text("Geschwindigkeit ", font, TEXT_COL, 35, 140)
            draw_text("Preis", font, TEXT_COL, 35, 260)
            draw_text("Anzahl der Parkplätze", font, TEXT_COL, 35, 380)

            pygame.draw.rect(screen, Box_col, Box_Ges, 100)
            pygame.draw.rect(screen, Box_col, Box_Anz, 100)
            pygame.draw.rect(screen, Box_col, Box_Geld, 100)

            inhalt1 = "{}".format(count1_Ges)
            text = font.render(inhalt1, 1, ZAHLEN_COL)
            screen.blit(text, (150, 200))

            inhalt2 = "{}".format(count2_Preis)
            text = font.render(inhalt2, 1, ZAHLEN_COL)
            screen.blit(text, (150, 320))

            inhalt3 = "{}".format(count3_Anz)
            text = font.render(inhalt3, 1, ZAHLEN_COL)
            screen.blit(text, (146, 440))

            if count1_Ges < 10:
                if up_button1.draw(screen):
                    count1_Ges += Geschwindigkeit_wert
                    variable_Geschwindigkeit = count1_Ges
                    print(variable_Geschwindigkeit)

            if count1_Ges > 1:
                if down_button1.draw(screen):
                    count1_Ges -= Geschwindigkeit_wert
                    variable_Geschwindigkeit = count1_Ges
                    print(variable_Geschwindigkeit)

            if count2_Preis < 5:
                if up_button2.draw(screen):
                    count2_Preis += Geld_wert
                    variable_Preis = count2_Preis
                    print(variable_Preis)

            if count2_Preis > 0.5:
                if down_button2.draw(screen):
                    count2_Preis -= Geld_wert
                    variable_Preis = count2_Preis
                    print(variable_Preis)

            if count3_Anz < 100:
                if up_button3.draw(screen):
                    count3_Anz += Anzahl_wert
                    variable_Parkplätze = count3_Anz // 4
                    print(variable_Parkplätze)

            if count3_Anz > 12:
                if down_button3.draw(screen):
                    count3_Anz -= Anzahl_wert
                    variable_Parkplätze = count3_Anz // 4
                    print(variable_Parkplätze)

            if back_button.draw(screen):
                menu_options = "main"

    else:
        pass

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_paused = True
                menu_options = "main"
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
