import pygame
import random
import os

class Pipe:
    """Pipe class: represents pipes in the game
    """

    VEL = 10

    def __init__(self, window_width, window_height):
        """Init module

        :param window_width: Width of the game window
        :type window_width: int
        :param window_height: Height of the game window
        :type window_height: int
        """
        self.x = window_width
        self.height = random.randint(window_height//4,window_height-window_height//4)
        self.window_height = window_height
        self.width = 80
        self.gap = 200

        local_dir = os.path.dirname(__file__)
        self.bottom_pipe_img = pygame.image.load(os.path.join(local_dir, 'imgs', 'pipe.png'))
        self.top_pipe_img = pygame.transform.flip(self.bottom_pipe_img, False, True)

    def draw(self, window):
        """Draw the pipe to our game's window

        :param window: Running game's window
        :type window: Pygame surface object
        """
        print(window)
        # draw top pipe
        # pygame.draw.rect(window, (0, 255, 0), (self.x, 0, self.width, self.height))
        window.blit(self.top_pipe_img,  (self.x, self.height-self.top_pipe_img.get_height()))
        # draw bottom pipe
        # pygame.draw.rect(window, (0, 255, 0), (self.x, self.height+self.gap, self.width, self.window_height-self.height-self.gap))
        window.blit(self.bottom_pipe_img,  (self.x, self.height+self.gap))

    def update(self):
        """Move the pipe towards the bird at the given velocity
        """
        self.x-=self.VEL
