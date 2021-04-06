import pygame
import sys

def check_events(settings, tank):
    ''' Check for keypresses and releases '''

    for event in pygame.event.get():

        # Key Presses
        if event.type == pygame.KEYDOWN:

            # Tank 1 Controls
            if event.key == pygame.K_UP:
                settings.tank1rl = True
            if event.key == pygame.K_DOWN:
                settings.tank1rr = True
            if event.key == pygame.K_LEFT:
                settings.tank1ml = True
            if event.key == pygame.K_RIGHT:
                settings.tank1mr = True
            if event.key == pygame.K_SPACE:
                settings.start_timer = True
                settings.tank_fire = True
                settings.tank_num = 0

            # Tank 2 Controls
            if event.key == pygame.K_s:
                settings.tank2rl = True
            if event.key == pygame.K_w:
                settings.tank2rr = True
            if event.key == pygame.K_a:
                settings.tank2ml = True
            if event.key == pygame.K_d:
                settings.tank2mr = True
            if event.key == pygame.K_x:
                settings.start_timer = True
                settings.tank_fire = True
                settings.tank_num = 1

        # Key Releases
        if event.type == pygame.KEYUP:

            # Tank 1 Controls
            if event.key == pygame.K_UP:
                settings.tank1rl = False
            if event.key == pygame.K_DOWN:
                settings.tank1rr = False
            if event.key == pygame.K_LEFT:
                settings.tank1ml = False
            if event.key == pygame.K_RIGHT:
                settings.tank1mr = False

            # Tank 2 Controls
            if event.key == pygame.K_s:
                settings.tank2rl = False
            if event.key == pygame.K_w:
                settings.tank2rr = False
            if event.key == pygame.K_a:
                settings.tank2ml = False
            if event.key == pygame.K_d:
                settings.tank2mr = False
        
        # Other
        if event.type == pygame.QUIT:
            settings.run_game = False

    # Move the tanks accordingly
    if settings.tank1mr:
        tank.move_tank(0, 'translate', 1)
    if settings.tank1ml:
        tank.move_tank(0, 'translate', -1)
    if settings.tank1rr:
        tank.move_tank(0, 'rotate', 1)
    if settings.tank1rl:
        tank.move_tank(0, 'rotate', -1)

    if settings.tank2mr:
        tank.move_tank(1, 'translate', 1)
    if settings.tank2ml:
        tank.move_tank(1, 'translate', -1)
    if settings.tank2rr:
        tank.move_tank(1, 'rotate', 1)
    if settings.tank2rl:
        tank.move_tank(1, 'rotate', -1)