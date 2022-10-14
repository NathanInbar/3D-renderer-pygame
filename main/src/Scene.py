
from src.GraphUtil import Point
from src.RenderPipeline import RenderPipeline
from src.Camera import Camera
import src.shapes as shapes

class Scene():

    def __init__(self, win):
        self.cam = Camera()
        self.renderer = RenderPipeline(win,self.cam)
        #scene objects
        self.objects = \
        [shapes.Sphere(self.renderer,Point(5,5,5),5)
        ]
        #---
    def update(self):
        for o in self.objects:
            o.update()

    def render(self):
        self.renderer.render()