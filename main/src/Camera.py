from src.GraphUtil import Point, Vector3, Transform

class Camera():

    def __init__(self, transform:Transform):
        self.transform = transform
        self.zNear = 0.1 #near distance from viewing frustrum
        self.zFar = 1000 #far distance from viewing frustrum

    # def __init__(self, pos:Point, direction:Vector3):
    #     self.transform = Transform(pos, direction)

