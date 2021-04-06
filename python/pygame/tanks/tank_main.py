import pygame
import sys

# Import the classes from the files
from settings import Settings
from tanks import Tank
import functions as f

def run_game():
    ''' Main function to run the game '''

    # Initialize the settings and screen classes
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    # Initialize the other classes
    tank = Tank(settings, screen)

    # Start the main loop for the game
    while settings.run_game:

        # If the ball is shot, start a timer for t
        if settings.start_timer:
            settings.t += .02
        else:
            settings.t = 1

        # Full the screen with the color of the background
        screen.fill(settings.bg_color)

        # Check for keypresses
        f.check_events(settings, tank)

        # Draw the cannon ball if the tank was fired
        if settings.tank_fire:
            tank.shoot_tank(settings.tank_num)

        # Draw the Tanks
        tank.draw_tank()
        
        # Show the screen
        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    run_game()
