import pygame
from src.globals import WIN_WIDTH, WIN_HEIGHT
from src.Scene import Scene
from src.GraphUtil import Point

class Window():
    pygame.init()
    clock = pygame.time.Clock()
    BKG_COLOR = (255,255,235)

    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

    def __init__(self):
        self.scene = Scene(self.win)
        pygame.display.set_caption("3D Renderer")


    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == ord('w'):
                    self.scene.objects[0].position += Point(0,0.25,0) #the cube face is not facing camera, wrong orientation whoopsie
                elif event.key == ord('s'):
                    self.scene.objects[0].position += Point(0,-0.25,0)
                elif event.key == ord('a'):
                    self.scene.objects[0].position += Point(0.25,0,0)
                elif event.key == ord('d'):
                    self.scene.objects[0].position += Point(-0.25,0,0)
                elif event.key == ord('q'):
                    self.scene.objects[0].position += Point(0,0,-0.25)
                elif event.key == ord('e'):
                    self.scene.objects[0].position += Point(0,0,0.25)
        self.scene.update()

    def render(self):
        self.win.fill(self.BKG_COLOR)
        self.scene.render()
        pygame.display.flip()

    def start(self):
        while True:
            self.update()
            self.render()

if __name__ == "__main__":

    window = Window()
    window.start()