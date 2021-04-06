import pygame
import math
from pygame.math import Vector2
import sys

from settings import Settings
from perspective_point import PerspectivePoint
import functions as func
import time

def run_game():
    ''' Main function to run the ray casting program '''

    # Initialize the setting and screen classes
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    # Initialize sprite groups
    all_sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    # Initialize other game classes
    func.make_sprite_groups(settings, screen, all_sprites, walls)
    pp = PerspectivePoint(settings, screen)
    
    while True:
        
        ''' Start the main loop for the game '''
        func.check_updates(settings)
        screen.fill(settings.bg_color)

        func.update_pp(settings)

        pp.update_point()
        all_sprites.update()

        func.cast_rays(settings, screen, pp, walls)

        all_sprites.draw(screen)
        pp.draw_point()
        
        pygame.display.flip()


run_game()