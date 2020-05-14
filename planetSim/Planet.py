

class Body:

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass


class Planet(Body):

    def __init__(self, radius, mass, distance_to_star):
        super().__init__(radius, mass)
        self.distance_to_star = distance_to_star
