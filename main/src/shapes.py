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
        self.color = (140,140,140)#RandomColorGen.getNext()
        self.renderer.push(self)

    def update(self):
        pass

    def render(self, win, pos, depth):
        #pos, depth = self.renderer.wp_to_sp(self.position)
        pygame.gfxdraw.filled_ellipse(win,pos.x,pos.y,depth,depth, self.color)

class Triangle(Renderable):

    def __init__(self, renderer:RenderPipeline, a,b,c, color=(33,33,33)):
        super().__init__(renderer)
        '''A,B,C are points of the triangle given clockwise'''

        self.b = renderer.wp_to_sp(b)[0] #ignore z-size information
        self.a = renderer.wp_to_sp(a)[0]
        self.c = renderer.wp_to_sp(c)[0]
        self.color = color

    def update(self):
        pass

    def render(self, win):

        # A
        # C B
        pygame.gfxdraw.trigon(win, self.a.x, self.a.y, self.b.x, self.b.y, self.c.x, self.c.y, self.color)


class Cube_Wireframe(Renderable):

    def __init__(self, renderer:RenderPipeline, position:Point, size):
        super().__init__(renderer)
        self.position = position
        self.size = size
        self.color = (144,144,10)
        self.renderer.push(self)

    def update(self):
        pass

    def render(self, win, _pos, depth):
        size = self.size
        pos = self.position
        verts = \
            [
                Point(pos.x - size, pos.y + size, pos.z - size),
                Point(pos.x - size, pos.y - size, pos.z - size),
                Point(pos.x + size, pos.y - size, pos.z - size),
                Point(pos.x + size, pos.y + size, pos.z - size),
                Point(pos.x - size, pos.y + size, pos.z + size),
                Point(pos.x - size, pos.y - size, pos.z + size),
                Point(pos.x + size, pos.y - size, pos.z + size),
                Point(pos.x + size, pos.y + size, pos.z + size),
            ]
        tris = \
            [ #NOTE : these should be dynamically ordered by depth in the future , and maybe scale color by depth
                Triangle(self.renderer, verts[2], verts[1], verts[5], (200,200,200)),#back
                Triangle(self.renderer, verts[2], verts[5], verts[6], (200,200,200)),

                Triangle(self.renderer, verts[0], verts[1], verts[2], (160,160,160)),#bot
                Triangle(self.renderer, verts[0], verts[2], verts[3], (160,160,160)),

                Triangle(self.renderer, verts[7], verts[4], verts[5], (160,160,160)),#top
                Triangle(self.renderer, verts[7], verts[5], verts[6], (160,160,160)),

                Triangle(self.renderer, verts[0], verts[4], verts[1], (160,160,160)),#left
                Triangle(self.renderer, verts[1], verts[4], verts[5], (160,160,160)),

                Triangle(self.renderer, verts[2], verts[3], verts[7], (160,160,160)),#right
                Triangle(self.renderer, verts[2], verts[7], verts[6], (160,160,160)),

                Triangle(self.renderer, verts[3], verts[0], verts[4], (140,140,140)),#front
                Triangle(self.renderer, verts[3], verts[4], verts[7], (180,140,140)),
            ]
        for tri in tris:
            tri.render(win)