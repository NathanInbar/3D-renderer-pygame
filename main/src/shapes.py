import pygame.gfxdraw
from src.GraphUtil import Point
from src.Generators import RandomColorGen

class Renderable():
    def __init__(self, render_pipeline):
        self.renderer = render_pipeline

class Sphere(Renderable):

    def __init__(self, position:Point, radius):
        super().__init__()
        self.position = position
        self.r = radius

    def render(self):
        self.renderer.push(pygame.gfxdraw.filled_ellipse,self.position,self.r,self.r,RandomColorGen.getNext())
