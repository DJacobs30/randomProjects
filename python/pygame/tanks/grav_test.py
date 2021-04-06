import pygame

def grav_test(settings, screen, rt):
    ''' Function to demo gravity '''
    g = 1
    t = settings.t
    u = settings.u
    # S = (.5*g*(t**2))

    ydisp = (u*t)+(.5*g*(t**2))
    xdisp = rt*3
    if ydisp >= 0:
        settings.u = u / 2
        settings.t = 0
    pygame.draw.circle(screen, (0, 0, 0), (500 - round(xdisp), round(ydisp) + 580), 20)