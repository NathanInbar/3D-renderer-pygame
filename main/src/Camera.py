from src.GraphUtil import Point, Vector3, Transform

class Camera():

    def __init__(self, transform:Transform):
        self.transform = transform

    def __init__(self, pos:Point, direction:Vector3):
        self.transform = Transform(pos, direction)

