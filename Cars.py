import pygame
import random
from datetime import datetime, timedelta  # Echtzeit


# Klasse für Autos. Hier werden alle Vorschriften und "verhalten" vom Auto gemacht.
class Car:
    def __init__(self):
        self.speed = 1
        self.image = None
        self.window = None
        self.x = None
        self.y = None
        self.left_image = None
        self.right_image = None
        self.up_image = None
        self.down_image = None
        self.parkplatze = []
        self.parkplatz = None
        self.wartezeit = None
        self.parkzeit = 0

        # Einem Auto den Parkplatz zuweisen

    def add_target(self, place):
        self.parkplatze.append(place)

    # Fahre zum Ziel mit Verzögerung
    def move_to_target(self):
        if self.wartezeit is not None and datetime.now() < self.wartezeit:
            return
        # Wenn es kein Ziel gibt, dann wähle aus Liste parkplätze
        if self.parkplatz is None and len(self.parkplatze) > 0:
            self.parkplatz = self.parkplatze.pop()
            # print("here")

        if self.parkplatz is None:
            return
        # Bewegung zum Ziel, hier vergleicht das Auto seine eigene koordinaten mit den Koordinaten des Ziels
        if self.x < self.parkplatz.x:
            speed = min(abs(self.parkplatz.x - self.x), self.speed)
            self.move_right(speed)
            # print("nach rechts")
        elif self.y < self.parkplatz.y:
            speed = min(abs(self.parkplatz.y - self.y), self.speed)
            self.move_down(speed)
            # print("nach unten")
        elif self.x > self.parkplatz.x:
            speed = min(abs(self.parkplatz.x - self.x), self.speed)
            self.move_left(speed)
            # print("nach links")
        elif self.y > self.parkplatz.y:
            speed = min(abs(self.parkplatz.y - self.y), self.speed)
            self.move_up(speed)
            # print("nach oben")
        else:
            self.parkzeit = random.randint(3, 10)
            self.wartezeit = datetime.now() + timedelta(seconds=random.randint(10, 30))
            self.parkplatz = None
            # print("Erreicht")

    # Auto darstellen
    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

    # Funktionen für Bewegungen
    def move_right(self, speed):
        self.x = self.x + speed
        self.image = self.right_image

    def move_left(self, speed):
        self.x = self.x - speed
        self.image = self.left_image

    def move_up(self, speed):
        self.y = self.y - speed
        self.image = self.up_image

    def move_down(self, speed):
        self.y = self.y + speed
        self.image = self.down_image



# Klassen mit Autos und deren Einstellungen
class YellowCar(Car):
    def __init__(self, x, y):
        super(YellowCar, self).__init__()
        self.x = -100
        self.y = y
        self.image = pygame.image.load("Images/YellowCar_64.png")
        self.left_image = self.image
        self.right_image = pygame.transform.flip(self.image, True, False)
        self.down_image = pygame.transform.rotate(self.image, 90)
        self.up_image = pygame.transform.rotate(self.image, -90)


class RedCar(Car):
    def __init__(self, x, y):
        super(RedCar, self).__init__()
        self.x = -100
        self.y = y
        self.image = pygame.image.load("Images/RedCar_64.png")
        self.left_image = self.image
        self.right_image = pygame.transform.flip(self.image, True, False)
        self.down_image = pygame.transform.rotate(self.image, 90)
        self.up_image = pygame.transform.rotate(self.image, -90)


class BlueCar(Car):
    def __init__(self, x, y):
        super(BlueCar, self).__init__()
        self.x = -100
        self.y = y
        self.image = pygame.image.load("Images/BlueCar_64.png")
        self.left_image = self.image
        self.right_image = pygame.transform.flip(self.image, True, False)
        self.down_image = pygame.transform.rotate(self.image, 90)
        self.up_image = pygame.transform.rotate(self.image, -90)
