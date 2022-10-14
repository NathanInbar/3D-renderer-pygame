from main.src.GraphUtil import Transform
from src.globals import WIN_WIDTH,WIN_HEIGHT
from src.GraphUtil import Graph, Point, Vector3
from src.Camera import Camera
from src.RenderPipeline import RenderPipeline
from src.shapes import Sphere

class Scene():

    def __init__(self, win):
        self.graph = Graph()
        cam_start = Point(0,0,0) #Point(sqrt(2)/2, sqrt(2)/2, 0)
        self.camera = Camera(Transform(cam_start,Vector3(1,0,0)))
        self.renderer = RenderPipeline(win, self, self.camera)

        self.sphere = Sphere(self.renderer, Point(-3,-4,2), 4)

    def update(self):
        '''scene updates'''
        pass

    def render(self):
        self.sphere.render()

        self.renderer.render()
