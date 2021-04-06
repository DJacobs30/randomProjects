import pygame
import threading
import time
import socket

from settings import Settings
from players import localPlayer
import functions as func

def run_game():
    ''' Function to run the game '''
    # Socket Settings
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.1.69'
    port = 42069
    s.connect((host, port))
    
    # Initialize pygame libraries
    pygame.init()

    # Initialize the settings and screen classes
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    # Intialize player settings
    pLocal = localPlayer(settings, screen)

    # Create Sprite Groups
    walls = pygame.sprite.Group()
    func.draw_map(settings, screen, walls)

    # Start the multithreads for the packet sending and recieving
    t = threading.Thread(target=(func.recieve_packets), args=(settings, s,))
    t.start()

    ''' Start the main loop of the game '''
    while True:
        screen.fill(settings.bg_color)

        pLocal.move_player()

        func.check_events(settings, pLocal, walls, s)

        pLocal.draw_player(0)

        walls.draw(screen)

        pygame.display.flip()

run_game()