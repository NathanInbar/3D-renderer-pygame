from cmath import sqrt
from src.globals import WIN_WIDTH,WIN_HEIGHT
from src.GraphUtil import Graph, Point, Vector3
from src.Camera import Camera
from src.RenderPipeline import RenderPipeline
from src.shapes import Sphere

class Scene():

    def __init__(self, win):
        self.graph = Graph()
        cam_start = Point(sqrt(2)/2, sqrt(2)/2, 0)
        self.camera = Camera(cam_start, Vector3(cam_start,self.graph.ORIGIN))
        self.renderer = RenderPipeline(win, self, self.camera)

        self.sphere = Sphere(self.renderer, Point(-3,-4,2), 4)

    def update(self):
        '''scene updates'''
        pass

    def render(self):
        self.sphere.render()

        self.renderer.render()
