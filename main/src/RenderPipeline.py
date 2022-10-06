from typing import Tuple
import pygame
import pygame.gfxdraw
from src.globals import WIN_WIDTH, WIN_HEIGHT
from src.GraphUtil import Point, Vector3, Transform
import heapq

class RenderPipeline():
    CULL_DISTANCE=100 #how far away an object can be before not being rendered

    def __init__(self, win, scene, camera):
        self.win = win
        self.render_queue = heapq()
        self.scene = scene
        self.cam = camera

    def push(self, renderFunc, pos:Point, size:Tuple[int,int], *args ):
        '''push a render request onto the queue after adjusting for perspective'''
        
        #get vector from camera to object point
        cam_to_obj = Transform(self.cam.transform.position, Vector3(self.cam.transform.position, pos))

        pos = self._wp_to_sp(cam_to_obj)
        width,height = self._scale_with_depth(size,pos[1]) #depth = y
        
        if width == None:
            return

        #NOTE i think i will need to make my own priority queue where priority = max depth
        heapq.heappush(self.render_queue,(renderFunc,(self.win,pos.x,pos.y,width,height,*args)))

    def render(self):
        '''execute all queued render instructions on the heap'''
        while len(self.render_queue) != 0:
            ex = heapq.heappop()
            #execute render instruction
            ex[0](ex[1][0],ex[1][1],ex[1][2],ex[1][3],ex[1][4],ex[1][5])
            

    def _wp_to_sp(self, cam_to_obj:Vector3)->Point:
        '''finds screen point relative to camera perspective'''
        # center the point and then displace it to screen position, where x = x, y = -z
        return Point(WIN_WIDTH//2+cam_to_obj[0], WIN_HEIGHT//2-cam_to_obj[2])

    def _scale_with_depth(self, size:Tuple[int,int], depth)->Tuple[int,int]:

        if depth >= self.CULL_DISTANCE:
            return (None,None)

        return (size[0]/depth,size[1]/depth)