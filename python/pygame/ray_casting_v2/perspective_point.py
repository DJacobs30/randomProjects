import pygame
import math

class PerspectivePoint():
    ''' A class to control the point of perspective in the ray caster '''

    def __init__(self, settings, screen):
        ''' Initialize the point class '''
        self.settings = settings
        self.screen = screen

        self.circlex = 50
        self.circley = 50

        self.update_point()

    def update_point(self):
        ''' Update the point on the screen '''
        self.degree = self.settings.deg_rotation * (math.pi/180)

        if self.settings.moving_forward == True:
            self.circlex += round(self.settings.pp_disp*math.cos(self.degree))
            self.circley += round(self.settings.pp_disp*math.sin(self.degree))

        if self.settings.moving_back == True:
            self.circlex += round(-1*(self.settings.pp_disp*math.cos(self.degree)))
            self.circley += round(-1*(self.settings.pp_disp*math.sin(self.degree)))

        self.dir_pointy = round(self.circley + (2*math.sin(self.degree)))
        self.dir_pointx = round(self.circlex + (2*math.cos(self.degree)))

    def draw_point(self):
        ''' Draw the point to the screen '''
        pygame.draw.circle(self.screen, self.settings.point_color, (self.circlex, self.circley), 5)
        pygame.draw.circle(self.screen, self.settings.dir_color, (self.dir_pointx, self.dir_pointy), 2)