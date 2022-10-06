import pygame

from src.globals import WIN_WIDTH, WIN_HEIGHT
from src.GraphUtil import Graph


class Window():
    pygame.init()
    clock = pygame.time.Clock()

    WIDTH=WIN_WIDTH
    HEIGHT=WIN_HEIGHT
    FPS = 30
    BKG_COLOR= (255,255,235)

    win = pygame.display.set_mode((WIDTH,HEIGHT))

    def __init__(self):
        
        self.graph = Graph()

        pygame.display.set_caption("3D Renderer")


    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

    def render(self):
        self.win.fill(self.BKG_COLOR)
        self.graph.render(self.win)
        pygame.display.flip()

    def start(self):
        while True:
            self.update()
            self.render()

if __name__ == "__main__":

    window = Window()
    window.start()