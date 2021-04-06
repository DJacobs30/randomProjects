import pygame
import sys

from map_walls import mapWalls

def check_events(settings, pLocal, walls, s):
    ''' Function to check pygame keypresses and releases '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            s.close()
            sys.exit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                settings.pLocal_moving_left = True
            if event.key == pygame.K_RIGHT:
                settings.pLocal_moving_right = True
            if event.key == pygame.K_UP:
                settings.pLocal_moving_up = True
            if event.key == pygame.K_DOWN:
                settings.pLocal_moving_down = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                settings.pLocal_moving_left = False
            if event.key == pygame.K_RIGHT:
                settings.pLocal_moving_right = False
            if event.key == pygame.K_UP:
                settings.pLocal_moving_up = False
            if event.key == pygame.K_DOWN:
                settings.pLocal_moving_down = False

    check_player_collisions(settings, pLocal, walls)

def draw_map(settings, screen, walls):
    # Function to draw the walls
    for wall_dim in settings.walls:
        mapWalls(settings, screen, wall_dim[0], wall_dim[1], walls)

def check_player_collisions(settings, pLocal, walls):
    ''' Function to check the players collisions with walls '''
    settings.pLocal_wall_collide = False
    for wall in walls:
        if pygame.sprite.collide_rect(pLocal, wall):
            if settings.pLocal_moving_right:
                pLocal.centerx = wall.rect.centerx - 42
            if settings.pLocal_moving_left:
                pLocal.centerx = wall.rect.centerx + 42
            if settings.pLocal_moving_up:
                pLocal.centery = wall.rect.centery + 42
            if settings.pLocal_moving_down:
                pLocal.centery = wall.rect.centery - 42
            settings.pLocal_wall_collide = True

def recieve_packets(settings, s):
    ''' Function to recieve the data from the server '''
    while True:
        data = s.recv(1024)
        print(data)
        if data:
            settings.latest_packet = []
            for str in data.split():
                num = int(str)
                settings.latest_packet.append(num)