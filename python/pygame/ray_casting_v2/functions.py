import pygame
from pygame.math import Vector2
from pygame import *
import math
import sys
import time

from render_map import RenderMap

def check_updates(settings):
    ''' A function to detect keypresses and update the screen accordingly '''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                settings.moving_forward = True
            if event.key == pygame.K_DOWN:
                settings.moving_back = True
            if event.key == pygame.K_LEFT:
                settings.rotating_left = True
            if event.key == pygame.K_RIGHT:
                settings.rotating_right = True
            if event.key == pygame.K_t:
                truck()
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                settings.moving_forward = False
            if event.key == pygame.K_DOWN:
                settings.moving_back = False
            if event.key == pygame.K_LEFT:
                settings.rotating_left = False
            if event.key == pygame.K_RIGHT:
                settings.rotating_right = False
        elif event.type == pygame.QUIT:
            sys.exit()

def update_pp(settings):
    ''' Update the location of the perspective point with the inputs from the previous function '''
    if settings.rotating_left == True:
        settings.deg_rotation -= 5
        settings.degree -= 5
    elif settings.rotating_right == True:
        settings.deg_rotation += 5
        settings.degree += 5




def ray_cast(settings, origin, target, obstacles, roamers):
    ''' A function to send out the rays to get distance '''


    current_pos = Vector2(origin)
    heading = target - origin

    # Make a vector to point to the target
    direction = heading.normalize()
    
    i = 1

    for value in range(int(heading.length())):
        current_pos += direction
        i += 1
        if i % settings.resolution == 0:
            for sprite in obstacles:
                if sprite.rect.collidepoint(current_pos):
                    return current_pos
            for roamer in roamers:
                if roamer.rect.collidepoint(current_pos):
                    settings.roamer_hit = True
                    settings.ray_degree_range += 1
                    return current_pos

    return Vector2(target)


def make_sprite_groups(settings, screen, all_sprites, walls):
    ''' A function to add all of the walls to sprite groups '''
    arr_drawn = 0

    while arr_drawn < len(settings.map_arr):
        RenderMap(settings, screen, settings.map_arr[arr_drawn, 0], settings.map_arr[arr_drawn, 1], settings.map_arr[arr_drawn, 2], settings.map_arr[arr_drawn, 3], all_sprites, walls)
        arr_drawn += 1


def cast_all_rays(settings, screen, pp, walls, roamers):
    ''' A function to cast all of the rays and get their collision values '''
    degrees = []
    ray_to_add = round(settings.degree - (settings.ray_degree_range/2))
    while len(degrees) < settings.ray_degree_range:
        degrees.append(ray_to_add)
        ray_to_add += settings.angle_distance

    settings.distances = []

    position = Vector2(pp.circlex, pp.circley)
    for degree in degrees:
        degree_value = degree * (math.pi/180)
        collision_point = ray_cast(settings, position, (pp.circlex + (500*math.cos(degree_value)), pp.circley + (500*math.sin(degree_value))), walls, roamers)
        pygame.draw.line(screen, settings.ray_color, (pp.circlex, pp.circley), [int(x) for x in collision_point], 2)
        
        collisionx, collisiony = list(collision_point)
        if settings.roamer_hit == True:
            settings.distances.append(3.14159265)
            settings.distances.append(1)
            settings.roamer_hit = False
        settings.distances.append(collisionx)
        settings.distances.append(collisiony)



def collision_distance(settings, pp):
    ''' Calculate the distance between the pp and the cp '''
    point_num = 0
    min_distance = 750

    for point in settings.distances:
        if point_num % 2 == 0:
            if point == 3.14159265:
                distance = point
                settings.collision_origin_distance.append(distance)
            else:
                collisionx, collisiony = point, settings.distances[point_num + 1]
                distance = math.sqrt(((collisionx - pp.circlex)**2) + ((collisiony - pp.circley)**2))
                settings.collision_origin_distance.append(distance)

                if distance < min_distance:
                    distance = min_distance
            

            if point_num == 0:
                initial_distance = distance

        point_num += 1
    
    return min_distance, initial_distance

def draw_screen(settings, screen, pp, trev):
    ''' Draw the distances to the screen with perspective '''
    min_distance = collision_distance(settings, pp)[0]
    initial_distance = collision_distance(settings, pp)[1]
    lines_drawn = 0
    trevor_seen = False
    n = 0
    avg_dist = 0

    for distance in settings.collision_origin_distance:
        if distance == 3.14159265:
            line_length = distance
        else:
            distance_ratio = initial_distance/min_distance
            line_length = 300 - distance
            if line_length > 300:
                line_length = 300
            if distance < 1:
                line_length = 1
        settings.line_lengths.append(line_length)
    
    while lines_drawn < settings.ray_degree_range:
        line_length = settings.line_lengths[lines_drawn]

        key_char = False

        if line_length == 3.14159265:
            settings.roamer_color = True
            key_char = True

        if key_char == False:
            rect = pygame.Rect(0, 0, settings.line_width, line_length)
            rect.y = 480 - (line_length/2)
            rect.x = settings.linex
            settings.linex += settings.line_width

            if line_length/10 > 0:
                line_color = round(((1/2)*line_length))
            else:
                line_color = 1
            line_color_tuple = (line_color, line_color, line_color)

            if settings.roamer_color:
                trevor_seen = True
                #print(line_length)
                trev.rect.centery = 480
                trev.rect.right = settings.linex
                line_color_change = line_length*(1/3)
                if line_color_change > 90 or line_color_change < 0:
                    line_color_change = 0
                line_color_tuple = (165 + line_color_change, 42 + line_color_change, 42 + line_color_change)
                '''
                line_color_tuple = (settings.trevor_color)
                '''
                
            pygame.draw.rect(screen, line_color_tuple, rect)

            settings.roamer_color = False
        lines_drawn += 1

def reset_lists(settings):
    ''' Reset all of the lists in plotting the line lengths '''
    settings.distances = []
    settings.collision_origin_distance = []
    settings.line_lengths = []
    settings.linex = 20
    settings.ray_degree_range = settings.base_ray_degree_range
    settings.trevor_image_dim = settings.line_width

def cast_rays(settings, screen, pp, trev, walls, roamers):
    cast_all_rays(settings, screen, pp, walls, roamers)
    collision_distance(settings, pp)
    draw_screen(settings, screen, pp, trev)
    reset_lists(settings)

def truck():
    WAVFILE = 'C:\\Users\\sxj0856\\OneDrive - The Home Depot\\Desktop\\Python\\python_projects\\ray_casting_v2\\tree.wav'
    mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
    pygame.init()
    
    s = pygame.mixer.Sound(WAVFILE)
    ch = s.play()
    while ch.get_busy():
        pygame.time.delay(100)