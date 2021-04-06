import pygame
import math
import sys

def run_sim():
    ''' Function to run the main simulation '''

    screen = pygame.display.set_mode((600, 540))
    pend = Pendulum(screen)

    while True:
        screen.fill((100, 100, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pend.draw_pendulum()

        pygame.display.flip()

class Pendulum():

    def __init__(self, screen):
        self.screen = screen

        self.centerx, self.centery = 300, 100
        self.plength = 200
        
        self.ang1 = 135
        self.ang2 = 45
        
        self.g = .0002
        
        self.v1 = 0
        self.v2 = 0

    def draw_pendulum(self):
        ''' Function to draw the Pendulum '''


        theta1 = (self.ang1 * (math.pi/180))
        x1 = self.plength * math.cos(theta1)
        y1 = self.plength * math.sin(theta1)

        a1 = self.g*math.cos(theta1)
        self.v1 += a1
        self.ang1 += self.v1


        theta2 = (self.ang2 * (math.pi/180))
        x2 = self.plength * math.cos(theta2)
        y2 = self.plength * math.sin(theta2)

        a2 = self.g*math.cos(theta2)
        self.v2 += a2
        self.ang2 += self.v2 + self.v1


        # Draw the Pieces
        pygame.draw.line(self.screen, (0,0,0), (self.centerx, self.centery), (self.centerx + round(x1), self.centery + round(y1)), 3)
        
        pygame.draw.line(self.screen, (0,0,0), (self.centerx + round(x1), self.centery + round(y1)), 
                    (self.centerx + round(x1) + round(x2), self.centery + round(y1) + round(y2)), 3)
        
        pygame.draw.circle(self.screen, (60, 60, 60), (self.centerx, self.centery), 10)
        
        pygame.draw.circle(self.screen, (100, 150, 50), (self.centerx + round(x1), self.centery + round(y1)), 15)

        pygame.draw.circle(self.screen, (50, 100, 150), (self.centerx + round(x1) + round(x2), self.centery + round(y1) + round(y2)), 15)

if __name__ == "__main__":
    pygame.init()
    run_sim()