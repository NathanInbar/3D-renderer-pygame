from src.GraphUtil import Coordinate, Vector

class Camera():

    def __init__(self, pos:Coordinate, direction:Vector):

        self.pos = pos
        self.direction = direction