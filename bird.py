import pygame
import os


class Bird():
    def __init__(self, window_height):
        self.falling_vel = self.vel = 8
        self.window_height = window_height
        self.y=window_height/2
        local_dir = os.path.dirname(__file__)
        self.bird_up_img = pygame.image.load(os.path.join(local_dir, 'bird_up.png'))
        self.bird_down_img = pygame.image.load(os.path.join(local_dir, 'bird_down.png'))
        self.image = self.bird_down_img

    def draw(self, window):
        if(self.vel<0):
            self.image = self.bird_up_img
        else:
            self.image = self.bird_down_img
        window.blit(self.image,(int(20), int(self.y)))

    def jump(self, jumping):
        if jumping:
            self.vel = -25
        else:
            self.vel = self.falling_vel
    
    def update(self):
        self.y+=self.vel
        self.y = min(self.window_height-self.image.get_height(), self.y)
        self.y = max(0, self.y)
