import pygame
import sys

# Import the Classes from the following files
from settings import Settings
from scripts import Script
from profile import eProfile
import game_functions as gf

def run_display():
    ''' Function to run the display '''

    # Initialize the pygame and settings classes
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("GA Appalachian Trail")

    # Initialize the other classes
    script = Script()
    ep = eProfile()

    # Main Loop to tun the game
    while True:

        # Fill he screen with the background color
        screen.fill(settings.bg_color)

        # Check for Closing the Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Main Function to run the game
        gf.run_game(settings, screen, script, ep)

        # Display the most recently drawn frame
        pygame.display.flip()

# If this is the main file, run this code
if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    run_display()