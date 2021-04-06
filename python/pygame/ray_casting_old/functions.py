import pygame
from pygame.math import Vector2
import math
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




def ray_cast(origin, target, obstacles):
    ''' A function to send out the rays to get distance '''

    #print(origin, "origin")
    #print(target, "target")

    current_pos = Vector2(origin)
    heading = target - origin

    #print(heading, "heading")

    # Make a vector to point to the target
    direction = heading.normalize()

    #print(direction, "direction")
    
    i = 1

    for value in range(int(heading.length())):
        current_pos += direction
        i += 1
        if i % 4 == 0:
            for sprite in obstacles:
                if sprite.rect.collidepoint(current_pos):
                    return current_pos


    return Vector2(target)




def make_sprite_groups(settings, screen, all_sprites, walls):
    ''' A function to add all of the walls to sprite groups '''
    arr_drawn = 0

    while arr_drawn < len(settings.map_arr):
        RenderMap(settings, screen, settings.map_arr[arr_drawn, 0], settings.map_arr[arr_drawn, 1], settings.map_arr[arr_drawn, 2], settings.map_arr[arr_drawn, 3], all_sprites, walls)
        arr_drawn += 1



def cast_all_rays(settings, screen, pp, walls):
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
        collision_point = ray_cast(position, (pp.circlex + (500*math.cos(degree_value)), pp.circley + (500*math.sin(degree_value))), walls)
        pygame.draw.line(screen, settings.ray_color, (pp.circlex, pp.circley), [int(x) for x in collision_point], 2)
        
        collisionx, collisiony = list(collision_point)
        settings.distances.append(collisionx)
        settings.distances.append(collisiony)\



def collision_distance(settings, pp):
    ''' Calculate the distance between the pp and the cp '''
    point_num = 0
    min_distance = 750

    for point in settings.distances:
        if point_num % 2 == 0:
            collisionx, collisiony = point, settings.distances[point_num + 1]
            distance = math.sqrt(((collisionx - pp.circlex)**2) + ((collisiony - pp.circley)**2))
            settings.collision_origin_distance.append(distance)

            if distance < min_distance:
                distance = min_distance
            
            if point_num == 0:
                initial_distance = distance

        point_num += 1
    
    return min_distance, initial_distance

def draw_screen(settings, screen, pp):
    ''' Draw the distances to the screen with perspective '''
    min_distance = collision_distance(settings, pp)[0]
    initial_distance = collision_distance(settings, pp)[1]
    lines_drawn = 0

    for distance in settings.collision_origin_distance:
        distance_ratio = initial_distance/min_distance
        line_length = 300 - distance
        if line_length > 300:
            line_length = 300
        if distance < 1:
            line_length = 1
        settings.line_lengths.append(line_length)
    
    while lines_drawn < settings.ray_degree_range:
        line_length = settings.line_lengths[lines_drawn]
        rect = pygame.Rect(0, 0, settings.line_width, line_length)
        rect.y = 480 - (line_length/2)
        rect.x = settings.linex
        settings.linex += settings.line_width

        if line_length/10 > 0:
            line_color = round(((2/3)*line_length))
        else:
            line_color = 1
        line_color_tuple = (line_color, line_color, line_color)

        pygame.draw.rect(screen, line_color_tuple, rect)
        lines_drawn += 1

def reset_lists(settings):
    ''' Reset all of the lists in plotting the line lengths '''
    settings.distances = []
    settings.collision_origin_distance = []
    settings.line_lengths = []
    settings.linex = 20

def cast_rays(settings, screen, pp, walls):
    cast_all_rays(settings, screen, pp, walls)
    collision_distance(settings, pp)
    draw_screen(settings, screen, pp)
    reset_lists(settings)
