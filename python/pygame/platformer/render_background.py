import pygame

class RenderBG():
    ''' A class to render in the scrolling background '''

    def __init__(self, settings, screen, x1, y1, x2, y2, x3, y3):
        ''' Initialize the RenderBG class '''

        # Take the triangle locations given and blit them to the screen
        pygame.draw.polygon(screen, settings.tree_color, [(x1, y1), (x2, y2), (x3, y3)])
