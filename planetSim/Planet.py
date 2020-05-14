import math

class Body:

    def __init__(self, radius, mass, centre_point):
        self.radius = radius
        self.mass = mass
        self.centre_point = centre_point


class Planet(Body):

    def __init__(self, radius, mass, centre_point):
        """
        :param radius: Radius of the planet in metres
        :param mass: Mass of the planet in Kilograms
        :param centre_point: Distance to the nearest star
        """
        super().__init__(radius, mass, centre_point)

    def __getattribute__(self, attribute):
        object.__getattribute__(self, attribute)
