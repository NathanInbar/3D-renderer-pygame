

class Coordinate():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Ray():

    def __init__(self, start:Coordinate, end:Coordinate):

        self.start = start
        self.end = end

class Line():

    def __init__(self, eqn):
        pass

class Graph():

    def __init__(self):