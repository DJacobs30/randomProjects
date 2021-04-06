import pygame
import numpy as np

class RenderMap(pygame.sprite.Sprite):
    ''' A class to draw the map to the screen '''

    def __init__(self, settings, screen, x, y, l, w, *groups):
        ''' Initialize the render map class '''
        super().__init__(*groups)
        self.settings = settings
        self.screen = screen

        self.image = pygame.Surface((l, w))
        self.image.fill(self.settings.map_color)
        self.rect = self.image.get_rect(topleft= (x, y))

        #self.draw_map(settings, screen)

    def draw_map(self, x, y, l, w, *groups):
        ''' Function to draw the map to the screen '''
