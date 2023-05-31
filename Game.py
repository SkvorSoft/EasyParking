import pygame
import PakingPlace
import Cars
import random
from datetime import datetime, timedelta, date

# aktuelles Datum/Zeit
today = date.today()
jetzt = datetime.now()
time = jetzt.strftime("%H:%M:%S")

"""Eine Klasse enthält sowhol eine Anzahl von Instruktionen , als auch die konktrete Bedienungen
    Hier wird ein Kostrukt der Klasse Game erstellt.
"""

# Load the image
Pfeil_Links = pygame.image.load("Images/PfeilLinks.png")
Pfeil_Rechts = pygame.image.load("Images/PfeilRechts.png")
Firmen_Logo = pygame.image.load("Images/Firmenlogo.png")
Megges = pygame.image.load("Images/Fressbude.png")

# Get the original size of the image
original_width, original_height = Firmen_Logo.get_size()
original_width2, original_height2 = Megges.get_size()

# Scale the image to half of its original size
Firmen_Logo = pygame.transform.scale(Firmen_Logo, (original_width // 8, original_height // 8))
Megges = pygame.transform.scale(Megges, (original_width // 5, original_height // 3))


class Game:
    def __init__(self, breite, hohe, titel, spalten, fps, win_logo, speed, price):
        pygame.init()
        self.black_color = (145, 175, 0)
        self.fps = fps
        self.cars = []
        self.window = pygame.display.set_mode((breite, hohe))
        self.clock = pygame.time.Clock()
        self.fahre_zu_PP = []
        self.ausfahrt = PakingPlace.PP_Ort(-100, 675, self.window)
        self.speed = speed
        self.mache_parkplatze(4, spalten)
        self.price = price
        self.zeige_preis = True

        pygame.display.set_caption(titel)
        logo = pygame.image.load(win_logo)
        pygame.display.set_icon(logo)

    # Parkplätze und Autos generieren
    def mache_parkplatze(self, zeilen, spalten):
        x = 55
        y = 150
        for i in range(zeilen):
            for j in range(spalten):
                place = PakingPlace.PP_Ort(x, y, self.window)
                self.fahre_zu_PP.append(place)
                car = self.get_random_car(y)
                self.add_car(car)
                car.add_target(self.ausfahrt)
                car.add_target(place)
                car.wartezeit = datetime.now() + timedelta(seconds=random.randint(1, 10))
                x = x + 35
            y = y + 150
            x = 55

    # Random Auto generieren
    def get_random_car(self, y):
        rand = random.randint(0, 2)
        randY = [215, 365, 565]
        if rand == 0:
            return Cars.RedCar(-100, random.choice(randY))
        elif rand == 1:
            return Cars.BlueCar(-100, random.choice(randY))
        elif rand == 2:
            return Cars.YellowCar(-100, random.choice(randY))

    # Ein Auto in die "car-Liste" hinzufügen
    def add_car(self, car):
        car.window = self.window
        self.cars.append(car)
        car.speed = self.speed

    # Bedientaste erstellen
    def tasten_leiste(self):
        schrift = pygame.font.SysFont('gloucesterextracondensed', 28)

        BLACK = (0, 0, 0)
        # HELLGRUEN = (130, 214, 28)
        # GOLD = (233, 171, 47)
        pygame.draw.rect(self.window, (223, 226, 222), (155, 10, 875, 50))
        pygame.draw.rect(self.window, (BLACK), (155, 10, 875, 50), 3)

        text = schrift.render("F1:Geschwindigkeit Hoch", True, BLACK)
        self.window.blit(text, (180, 20))

        text2 = schrift.render("F2:Geschwindigkeit Runter", True, BLACK)
        self.window.blit(text2, (480, 20))

        text3 = schrift.render("F3:Umsatz", True, BLACK)
        self.window.blit(text3, (780, 20))

        text4 = schrift.render("F4:Exit", True, BLACK)
        self.window.blit(text4, (950, 20))

        # Menü rechts oben Fläche
        pygame.draw.rect(self.window, (223, 226, 222), (1040, 10, 250, 300))
        pygame.draw.rect(self.window, (BLACK), (1040, 10, 250, 300), 3)

        # Asphalt fläche
        pygame.draw.rect(self.window, (80, 80, 80), (25, 110, 930, 620))
        pygame.draw.rect(self.window, (BLACK), (25, 110, 930, 620), 3)

        # Flächen für die einfahrt
        pygame.draw.rect(self.window, (80, 80, 80), (0, 210, 28, 90))
        pygame.draw.rect(self.window, (80, 80, 80), (0, 361, 28, 90))
        pygame.draw.rect(self.window, (80, 80, 80), (0, 511, 28, 90))
        pygame.draw.rect(self.window, (80, 80, 80), (0, 662, 28, 65))

        # aktuelles Datum und Uhrzeit anzeigen
        text5 = schrift.render(f"Datum: {today}", True, BLACK)
        self.window.blit(text5, (1060, 20))
        text6 = schrift.render(f"Uhrzeit: {time} Uhr", True, BLACK)
        self.window.blit(text6, (1060, 60))

        # Fahrtrichtungspfeile
        self.window.blit(Pfeil_Links, (80, 675))
        self.window.blit(Pfeil_Rechts, (80, 235))
        self.window.blit(Pfeil_Rechts, (80, 385))
        self.window.blit(Pfeil_Rechts, (80, 535))

        # Logo sowie Image unten Rechts
        self.window.blit(Firmen_Logo, (0.5, 0.5))
        self.window.blit(Megges, (1000, 400))

        if self.zeige_preis:
            price_text = schrift.render("Umsatz in EUR: " + str(self.calculate_price()), True, BLACK)
            self.window.blit(price_text, (1060, 100))

    # Hauptfunktion pro Bild
    def run(self):
        pygame.display.update()
        self.clock.tick(self.fps)
        self.window.fill(self.black_color)
        self.tasten_leiste()

        for place in self.fahre_zu_PP:
            place.draw()

        for car in self.cars:
            car.move_to_target()
            car.draw()
        self.calculate_price()

        # Preisberechung

    def calculate_price(self):
        price = 0
        for car in self.cars:
            price += car.parkzeit * self.price

        print("price: ", price)
        return price

    # def calculate_price(self):
    #    Summe = 0
    #    for car in self.cars:
    #        if car.parkzeit != 0:
    #            Summe += self.price

    #    print("Summe: ", Summe)
    #    return Summe

    # Ein/Ausblenden vom Umsatz
    def verstecke_preis(self):
        self.zeige_preis = not self.zeige_preis

    # Geschwindigkeiten von Autos

    def SpeedUp(self):
        for car in self.cars:
            car.speed += 1

    def SpeedDown(self):
        for car in self.cars:
            car.speed -= 1
