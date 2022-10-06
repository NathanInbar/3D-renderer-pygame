import pygame
import pygame.gfxdraw
from src.globals import WIN_WIDTH, WIN_HEIGHT

#UNIT_SCALAR = int(WIN_HEIGHT/10)

class Coordinate():

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def toScreenSpace(self):
        return (int(self.x+(WIN_WIDTH/2)),int(self.y+(WIN_HEIGHT/2)))

    def get(self):
        return (self.x,self.y,self.z)
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

class Vector():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

class Ray():

    def __init__(self, start:Coordinate, end:Coordinate):

        self.start = start
        self.end = end

    def toScreenSpace(self):
        return (self.start.toScreenSpace(), self.end.toScreenSpace())

class Graph():
    MIN,MAX = -WIN_HEIGHT,WIN_HEIGHT
    ORIGIN = Coordinate(0,0,0)
    X_AXIS = Ray(Coordinate(MIN,0,0),Coordinate(MAX,0,0))
    Y_AXIS = Ray(Coordinate(0,MIN,0),Coordinate(0,MAX,0))
    Z_AXIS = Ray(Coordinate(0,0,MIN),Coordinate(0,0,MAX))

    AXIS_COL = (0,0,0)
    def __init__(self):
        pass

    def render(self, win):
        origin =self.ORIGIN.toScreenSpace()
        pygame.gfxdraw.filled_ellipse(win, origin[0], origin[1], 4, 4, self.AXIS_COL)

        x_axis = self.X_AXIS.toScreenSpace()
        pygame.gfxdraw.line(win, x_axis[0][0], x_axis[0][1], x_axis[1][0], x_axis[1][1], self.AXIS_COL)
        
        y_axis = self.Y_AXIS.toScreenSpace()
        pygame.gfxdraw.line(win, y_axis[0][0], y_axis[0][1], y_axis[1][0], y_axis[1][1], self.AXIS_COL)





