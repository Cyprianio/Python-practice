from random import randint
from math import sqrt


class Rocket:
    """
    Rocket with speed
    """
    nextId = 1

    def __init__(self, speed):
        self.id = Rocket.nextId
        Rocket.nextId += 1
        self.altitude = 0
        self.speed = speed

    def moveUp(self):
        """
        Moving the rocket w the speed
        """
        self.altitude += self.speed
        self.x = randint(1, 10)

    def __str__(self):
        return ("Position of this rocket is: " +
                str(self.altitude) + ", " + str(self.x))


class RocketBoard:
    def __init__(self, rocketsAmount=5):
        self.rockets = [Rocket(randint(1, 5))
                        for _ in range(rocketsAmount)]

        for _ in range(10):
            rocketIndex = randint(0, len(self.rockets)-1)
            self.rockets[rocketIndex].moveUp()

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

    @staticmethod
    def getDistance(rocket1, rocket2):
        vertical_dist = abs(rocket1.altitude - rocket2.altitude)
        horizontal_dist = (rocket1.x - rocket2.x)
        return sqrt((vertical_dist ** 2) +
                    (horizontal_dist ** 2))

    def getAmountOfRackets(self):
        return len(self.rockets)

    def __len__(self):
        return self.getAmountOfRackets()
