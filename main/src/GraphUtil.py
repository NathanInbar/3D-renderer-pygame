from cmath import sqrt
from typing import TypeVar
import pygame
import pygame.gfxdraw
from src.globals import WIN_WIDTH, WIN_HEIGHT

#UNIT_SCALAR = int(WIN_HEIGHT/10)

class Point():

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    #TODO - implement contstructors to turn vector/transform into point easily
    # def __init__(self, vector):
    #     '''end point of vector from origin'''
    #     self.x = vector.x
    #     self.y = vector.y
    #     self.z = vector.z

    # def __init__(self, transform):
    #     '''end point of a vector starting from a point'''
    #     self.x = transform.direction.x - transform.position.x
    #     self.y = transform.direction.y - transform.position.y
    #     self.z = transform.direction.z - transform.position.z


    def toScreenSpace(self):
        return (int(self.x+(WIN_WIDTH/2)),int(self.y+(WIN_HEIGHT/2)))

    def get(self):
        return (self.x,self.y,self.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

TVector3 = TypeVar("TVector3",bound="Vector3")
class Vector3():

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def getVec(self, start:Point, end:Point):
        self.x = end.x - start.x
        self.y = end.y - start.y
        self.z = end.z - start.z

    def Negate(self)->TVector3:
        return Vector3(-self.x,-self.y,-self.z)
    def Add(self, v2:TVector3)->TVector3:
        return Vector3(self.x+v2.x,self.y+v2.y,self.z+v2.z)
    def Subtract(self, v2:TVector3)->TVector3:
        return self.Add(v2.Negate())
    def Multiply(self, v2:TVector3)->TVector3:
        return Vector3(self.x*v2.x,self.y*v2.y,self.z*v2.z)
    def Divide(self, v2:TVector3)->TVector3:
        '''!RETURNS VECTOR WITH FLOATS!'''
        return Vector3(self.x/v2.x,self.y/v2.y,self.z/v2.z)

    def Dot(self,v2:TVector3)->TVector3:
        return (self.x*v2.x)+(self.y*v2.y)+(self.z*v2.z)
    def Cross(self,v2:TVector3)->TVector3:
        return Vector3(self.y*v2.z-self.z*v2.y,self.z*v2.x-self.x*v2.z,self.x*v2.y-self.y*v2.x)
    def Magnitude(self)->float:
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    def Project(self, v2:TVector3)->TVector3:
        '''!RETURNS VECTOR WITH FLOATS!'''
        '''projection of self onto v2'''
        return self.Multiply(self.Divide(self.Dot(v2),self.Dot(self)),self)

    def floor(self):
        self.x = int(self.x)
        self.y = int(self.y)
        self.z = int(self.z)
        return self

    def get(self):
        return (self.x,self.y,self.z)

    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

class Transform():

    def __init__(self, position:Point, direction:Vector3):
        self.position = position
        self.direction = direction

class Graph():
    MIN,MAX = -WIN_HEIGHT,WIN_HEIGHT
    ORIGIN = Point(0,0,0)
    X_AXIS = Vector3().getVec(Point(MIN,0,0),Point(MAX,0,0))
    Y_AXIS = Vector3().getVec(Point(0,MIN,0),Point(0,MAX,0))
    Z_AXIS = Vector3().getVec(Point(0,0,MIN),Point(0,0,MAX))

    AXIS_COL = (0,0,0)
    def __init__(self):
        pass

    def render(self):
        pass
        # origin =self.ORIGIN.toScreenSpace()
        # pygame.gfxdraw.filled_ellipse(win, origin[0], origin[1], 4, 4, self.AXIS_COL)

        # x_axis = self.X_AXIS.toScreenSpace()
        # pygame.gfxdraw.line(win, x_axis[0][0], x_axis[0][1], x_axis[1][0], x_axis[1][1], self.AXIS_COL)
        
        # y_axis = self.Y_AXIS.toScreenSpace()
        # pygame.gfxdraw.line(win, y_axis[0][0], y_axis[0][1], y_axis[1][0], y_axis[1][1], self.AXIS_COL)





