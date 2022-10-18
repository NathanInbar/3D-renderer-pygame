from math import sqrt
from typing import TypeVar

#UNIT_SCALAR = int(WIN_HEIGHT/10)
TPoint = TypeVar("TPoint", bound="Point")
class Point():

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def get(self):
        return self.x,self.y,self.z

    def __add__(self, p2:TPoint):
        return Point(self.x+p2.x, self.y+p2.y, self.z+p2.z)

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
    def __add__(self, v2:TVector3)->TVector3:
        return self.Add(v2)
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
