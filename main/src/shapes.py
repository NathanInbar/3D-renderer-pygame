import pygame.gfxdraw
from src.RenderPipeline import RenderPipeline
from src.GraphUtil import Point
from src.Generators import RandomColorGen

class Renderable():
    def __init__(self, render_pipeline):
        self.renderer = render_pipeline

class Sphere(Renderable):

    def __init__(self, renderer:RenderPipeline, position:Point, radius):
        super().__init__(renderer)
        self.position = position
        self.r = radius
        self.color = RandomColorGen.getNext()
        self.renderer.push(self)

    def update(self):
        pass

    def render(self, win, pos, depth):
        #pos, depth = self.renderer.wp_to_sp(self.position)
        print(pos)
        print(depth)
        pygame.gfxdraw.filled_ellipse(win,pos.x,pos.y,depth,depth, self.color)
