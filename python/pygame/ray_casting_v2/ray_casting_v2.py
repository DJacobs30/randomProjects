import pygame
import math
import time
import sys
from pygame.math import Vector2

from settings import Settings
from perspective_point import PerspectivePoint
from trevor import Trevor
import functions as func

def run_game():
    ''' Main function to run the ray casting program '''

    # Initialize the setting and screen classes
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    # Initialize sprite groups
    all_sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    roamers = pygame.sprite.Group()

    # Initialize other game classes
    func.make_sprite_groups(settings, screen, all_sprites, walls)
    pp = PerspectivePoint(settings, screen)
    trev = Trevor(settings, screen, roamers)
    
    while True:
        
        ''' Start the main loop for the game '''
        func.check_updates(settings)
        screen.fill(settings.bg_color)

        func.update_pp(settings)
        trev.move_trevor(walls)

        pp.update_point()

        func.cast_rays(settings, screen, pp, trev, walls, roamers)

        all_sprites.draw(screen)
        pp.draw_point()
        
        pygame.display.flip()


run_game()