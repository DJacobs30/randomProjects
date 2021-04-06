import pygame

class Draw():
    ''' Class to hold information for drawing '''

    def __init__(self, settings, screen):
        ''' Initialize the draw class '''
        self.settings = settings
        self.screen = screen

        self.color = (0, 0, 0)
        self.size = 5
        self.mouse_pos = (-50, -50)

    def draw_shape(self):
        ''' Draw the shape to the screen where the mouse cursor is '''
        pygame.draw.circle(self.screen, self.color, self.mouse_pos, self.size)