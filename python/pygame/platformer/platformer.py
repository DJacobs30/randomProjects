import pygame
import sys

# Call the classes for the game from the various .py files
from settings import Settings
from duck import Duck
import functions as func

def run_game():
    ''' Main function to run the platformer '''

    # Initialize the settings and screen classes
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    # Initialize other game classes
    duck = Duck(settings, screen)

    while True:
        ''' Start the main loop of the game '''

        # Fill the background with the color defined in settings.py
        screen.fill(settings.bg_color)

        # Check for keypresses/releases
        func.check_updates(settings)

        # Update the background
        func.draw_background(settings, screen)

        # Draw the character to the screen
        duck.update()

        # Show the latest version of the screen
        pygame.display.flip()

run_game()