from math import tan
from src.globals import WIN_WIDTH, WIN_HEIGHT, FOV
from src.GraphUtil import Point

class RenderPipeline():

    def __init__(self, win, camera):
        self.win = win
        self.render_queue = []
        self.cam = camera

    def push(self,obj):
        '''push a renderable object onto the queue'''
        self.render_queue.append(obj)

    def render(self):
        '''execute all queued render instructions on the heap'''
        for _r in self.render_queue:
            _r.render(self.win, *self.wp_to_sp(_r.position))           

    def wp_to_sp(self, wp:Point)->Point:
        '''finds screen point relative to camera perspective'''
        # center the point and then project it to screen position
        x,y,z = wp.get()
        z+=3 #z-offset
        z += 0.1 #for division by zero avoidance
        a = WIN_WIDTH/WIN_HEIGHT #aspect ratio
        f = 1 / tan(FOV/2) # x,y scaling factor
        zNear = self.cam.zNear
        zFar = self.cam.zFar
        q = zFar/(zFar-zNear) # z scaling factor

        #<x,y,z,1> -> projection matrix -> <afx, fy, zq-znearq, z>
        #then x,y coord = <afx/z, afy/z> , size scales by zq-znearq
        sx = ((a*f*x/z +1.0)*0.5*WIN_WIDTH)
        sy = ((f*y/z +1.0)*0.5*WIN_HEIGHT)
        depth = z*q-zNear*q
        return Point(round(sx),round(sy)),round(depth)#coordinates with applied transformation matrix, z to be used as size scalar
