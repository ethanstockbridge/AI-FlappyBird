from distutils.util import check_environ
import pygame
from pipe import Pipe
from bird import Bird
import os

pygame.init()

class Game():
    SCORE_FONT = pygame.font.SysFont("comicsans", 50)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, width, height):
        self.window = pygame.display.set_mode((width, height))
        self.window_width = width
        self.window_height = height
        self.bird = Bird(height)
        local_dir = os.path.dirname(__file__)
        self.background = pygame.image.load(os.path.join(local_dir, 'background.png'))
        self.pipes = []
        self.score = 0
        self.tick = 0

    def update(self):
        self.tick += 1
        if(self.tick%40==0):
            self.pipes.append(Pipe(self.window_width, self.window_height))
        # self.window.fill(self.BLACK)
        self.window.blit(self.background, (0,0))
        self.bird.update()
        self.bird.draw(self.window)
        ctb4=len(self.pipes)
        self.pipes = [pipe for pipe in self.pipes if pipe.x>0]
        self.score += ctb4 - len(self.pipes)
        for pipe in self.pipes:
            pipe.update()
            pipe.draw(self.window)
        score_txt = self.SCORE_FONT.render(f"{self.score}", 1, self.WHITE)
        self.window.blit(score_txt, (self.window_width // 2 - score_txt.get_width()//2, 10))
        if not self.checkValidity() or self.score>200:
            return False

    def getGameInfo(self):
        bird_y = self.bird.y
        if len(self.pipes)==0:
            return [bird_y, 0, self.window_height]
        closestpipe = self.pipes[0]
        closest_pipe_bottom = closestpipe.height
        closest_pipe_top = closestpipe.height+closestpipe.gap
        return [bird_y, closest_pipe_bottom, closest_pipe_top]

    def checkValidity(self):
        if len(self.pipes) == 0:
            return True
        closestpipe = self.pipes[0]
        if closestpipe.x < self.bird.image.get_width():
            # if bird is within the gap between the pipes
            if (self.bird.y > closestpipe.height) and (self.bird.y+self.bird.image.get_height() < closestpipe.height+closestpipe.gap):
                return True
            else:
                return False
        return True