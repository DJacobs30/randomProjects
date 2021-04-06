import pygame
import math

class Tank():
    ''' A class to hold all the information for the tank '''

    def __init__(self, settings, screen):
        ''' Initialize the Tank class '''

        # Save settings and screen as class variables
        self.settings = settings
        self.screen = screen
        self.xdisp, self.ydisp = self.settings.cannon_length, 0
        self.xdisp2, self.ydisp2 = -1*self.settings.cannon_length, 0

    def move_tank(self, tank_num, mtype, direction):
        ''' Function to move the tanks '''

        # If it is the first tanks turn, do the following
        if tank_num == 0:

            # Rotate the cannon
            if mtype == 'rotate':
                self.settings.cannon1t += direction/3
                c1rad = self.settings.cannon1t * (math.pi/180)
                self.xdisp = self.settings.cannon_length * (math.cos(c1rad))
                self.ydisp = self.settings.cannon_length * (math.sin(c1rad))

            # Move the tank
            if mtype == 'translate':
                self.settings.tank1x += .05*direction

        # Vice versa for tank two
        if tank_num == 1:

            # Rotate the cannon
            if mtype == 'rotate':
                self.settings.cannon2t += direction/3
                c2rad = self.settings.cannon2t * (math.pi/180)
                self.xdisp2 = self.settings.cannon_length * (math.cos(c2rad))
                self.ydisp2 = self.settings.cannon_length * (math.sin(c2rad))

            # Move the tank
            if mtype == 'translate':
                self.settings.tank2x += .05*direction

    def shoot_tank(self, tank_num):
        ''' Function to fire cannonballs from the cannons '''

        # Componentize the ball init vel vector
        if tank_num == 0:
            c1rad = self.settings.cannon1t * (math.pi/180)
            xvel = self.settings.ballv * (math.cos(c1rad))
            yvel = self.settings.ballv * (math.sin(c1rad))
        
        else:
            c2rad = self.settings.cannon2t * (math.pi/180)
            xvel = self.settings.ballv * (math.cos(c2rad))
            yvel = self.settings.ballv * (math.sin(c2rad))

        # Calculate the position of the ball with kinematics
        g = 1
        t = self.settings.t
        ydis = round((yvel*t)+(.5*g*(t**2)))
        xdis = round((xvel)*t)

        # Remove the ball when it leaves the screen
        if ydis > 10:
            self.settings.start_timer = False
            self.settings.tank_fire = False

        # Draw the Ball to the screen
        if tank_num == 0:
            pygame.draw.circle(self.screen, (0,0,0), (round(self.settings.tank1x) + xdis, round(self.settings.cannon1y) + ydis), 5)
        if tank_num == 1:
            pygame.draw.circle(self.screen, (0,0,0), (round(self.settings.tank2x) + xdis, round(self.settings.cannon2y) + ydis), 5)

    def draw_tank(self):
        ''' Draw the tank to the screen '''

        # Tank One
        pygame.draw.circle(self.screen, self.settings.tank_color, (round(self.settings.tank1x), round(self.settings.tanky)), 20)
        pygame.draw.line(self.screen, self.settings.tank_color, (self.settings.tank1x, self.settings.tanky), 
                (self.settings.tank1x + self.xdisp, self.settings.cannon1y + self.ydisp), 10)

        # Tank Two
        pygame.draw.circle(self.screen, self.settings.tank_color, (round(self.settings.tank2x), round(self.settings.tanky)), 20)
        pygame.draw.line(self.screen, self.settings.tank_color, (self.settings.tank2x, self.settings.tanky), 
                (self.settings.tank2x + self.xdisp2, self.settings.cannon2y + self.ydisp2), 10)

        # Floor
        pygame.draw.rect(self.screen, (30, 30, 30), (0, 410, self.settings.screen_width, 100))