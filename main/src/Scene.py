
from src.GraphUtil import Point
from src.RenderPipeline import RenderPipeline
from src.Camera import Camera
import src.shapes as shapes
import pygame

class Scene():
    pygame.init()
    def __init__(self, win):
        self.cam = Camera()
        self.renderer = RenderPipeline(win,self.cam)
        #scene objects
        self.objects = \
        [#shapes.Sphere(self.renderer,Point(0,0,0),100),
        shapes.Cube_Wireframe(self.renderer, Point(-0.53,0,0), 0.5),

        ]
        #---
    def update(self):

        for o in self.objects:
            o.update()

    def render(self):
        self.renderer.render()