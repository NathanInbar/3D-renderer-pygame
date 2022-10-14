from cmath import tan
from typing import Tuple
import pygame
import pygame.gfxdraw
from src.globals import WIN_WIDTH, WIN_HEIGHT, FOV
from src.GraphUtil import Point
import heapq

class RenderPipeline():

    def __init__(self, win, scene, camera):
        self.win = win
        self.render_queue = []
        self.scene = scene
        self.cam = camera

    def push(self, renderFunc, pos:Point, size:Tuple[int,int], *args ):
        '''push a render request onto the queue after adjusting for perspective'''

        pos, depth = self._wp_to_sp(pos)


        #NOTE i think i will need to make my own priority queue where priority = max depth
        heapq.heappush(self.render_queue,(renderFunc,(self.win,pos.x,pos.y,depth,depth,*args)))

    def render(self):
        '''execute all queued render instructions on the heap'''
        while len(self.render_queue) != 0:
            ex = heapq.heappop()
            #execute render instruction
            ex[0](ex[1][0],ex[1][1],ex[1][2],ex[1][3],ex[1][4],ex[1][5])
            

    def _wp_to_sp(self, wp:Point)->Point:
        '''finds screen point relative to camera perspective'''
        # center the point and then displace it to screen position, where x = x, y = -z
        (x,y,z) = wp.get()
        a = WIN_WIDTH/WIN_HEIGHT #aspect ratio
        f = 1 / tan(FOV/2) # x,y scaling factor
        zNear = self.cam.zNear
        zFar = self.cam.zFar
        q = zFar/(zFar-zNear) # z scaling factor

        #<x,y,z,1> -> projection matrix -> <afx, fy, zq-znearq, z>
        #then x,y coord = <afx/z, afy/z> , size scales by zq-znearq
        return Point(a*f*x/z, f*y/z), z*q-zNear*q #coordinates with applied transformation matrix, z to be used as size scalar

    def _scale_with_depth(self, size:Tuple[int,int], depth)->Tuple[int,int]:

        if depth >= self.CULL_DISTANCE:
            return (None,None)

        return (size[0]/depth,size[1]/depth)