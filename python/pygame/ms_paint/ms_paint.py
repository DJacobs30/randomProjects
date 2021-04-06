import pygame
import sys

from settings import Settings
from draw import Draw
from control_menu import ControlMenu
import functions as func

def run_game():
    ''' Function to run the main program '''

    # Initialize pygame
    pygame.init()

    # Initialize the settings and screen classes
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    # Initialize the sprite group
    buttons = pygame.sprite.Group()
    
    # Initialize the other classes
    draw = Draw(settings, screen)
    menu = ControlMenu(settings, screen, draw)

    # Initialize the button groups
    menu.init_buttons(buttons)

    # Fill the background with white
    screen.fill(settings.bg_color)

    ''' Start the main loop of the game '''
    while True:

        # Draw the lines with the mouse
        func.draw(draw)
        
        # Draw the toolbar
        menu.draw_menu()
        
        # Check for toolbar clicks
        func.update_screen(settings, screen, draw, buttons)

        if settings.save_file:
            # If the save button is pressed stop the screen refresh and put up the name enterer
            func.save(settings, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Display the most recent frame
        pygame.display.flip()

run_game()