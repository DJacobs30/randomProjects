import pygame
import sys

from settings import Settings

class eProfile():
    ''' A class to draw the elevation profiles for each day '''

    def __init__(self):
        # Array to hold the elevation profile data
        self.ep = [
                        ((0, 2559), (.5, 2623), (1, 2913), (1.5, 2787), (2, 2720), (2.5, 2986), (3, 3041), (3.5, 3354), (4, 3205), 
                        (4.5, 3305), (5, 3314), (5.5, 3310), (6, 3230), (6.5, 3334), (7, 3459), (7.5, 3766)), 
                        
                        ((0, 3755), (.5, 3500), (1, 3393), (1.5, 3271), (2, 3141), (2.5, 2987), (3, 2895), (3.5, 2735), (4, 2714),
                        (4.5, 2590), (5, 2829), (5.5, 2991), (6, 3052), (6.5, 3097), (7, 3353), (7.5, 3230)),
                        
                        ((0, 3230), (.5, 3223), (1, 2997), (1.5, 3103), (2, 3008), (2.5, 2956), (3, 2800), (3.5, 3095), (4, 3329)),

                        ((0, 3329), (.5, 2933), (1, 3201), (1.5, 3016), (2, 2771), (2.5, 2635), (3, 2636), (3.5, 2763), (4, 2967))

                        ]
        self.settings = Settings()
        self.eps = []
        self.leps = []
        self.x, self.y, self.i = -5, 480 - 72.8, 0
        self.second = True

    def draw_ep(self, settings, screen, day_num, first):
        self.eps = []
        xi, yi = 0, 0

        for coord in self.ep[day_num - 1]:

            if first:
                miny = coord[1]
                first = False
            if coord[1] < miny:
                miny = coord[1]

        # Select the day
        for coord in self.ep[day_num - 1]:

            # Change the values in reference to the screen
            x = coord[0] * 50
            y = (coord[1] - miny) * .08

            try:
                slope = -1*((y - yi)/(x - xi))
            except ZeroDivisionError:
                slope = 0
            self.eps.append(slope)

            pygame.draw.line(screen, (255, 255, 255), (x + 20, 480 - y), (xi + 20, 480 - yi), 3)

            self.ep_track(settings, screen, y)

            xi, yi = x, y

    def ep_track(self, settings, screen, y):
        ''' Make a Circle to follow the elevation profile '''

        if self.second:
            self.y = 480 - y
            self.second = False

        if len(self.leps) < len(self.eps):
            self.leps = self.eps

        self.x += .1
        try:
            self.y = ((self.leps[self.i] * self.x) - (self.y - (self.leps[self.i] * self.x)))
        except IndexError:
            settings.onTrail = False

        if round(self.x, 3) % 25 == 20:
            self.i += 1

        if self.x >= 20:
            pygame.draw.circle(screen, (255, 150, 150), (round(self.x), round(self.y)), 5)

''' TEST LOOP '''
if __name__ == '__main__':
    screen = pygame.display.set_mode((800, 500))
    ep = eProfile()
    while True:
        screen.fill((0,0,0))
        ep.draw_ep('', screen, 4, True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()