import pygame
import sys

from render_background import RenderBG

def check_updates(settings):
    ''' Function to check for keypresses/screen updates '''

    # Check for a tab close then use sys to close the program
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                settings.scroll_right = True
            elif event.key == pygame.K_LEFT:
                settings.scroll_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                settings.scroll_right = False
            elif event.key == pygame.K_LEFT:
                settings.scroll_left = False
        elif event.type == pygame.QUIT:
            sys.exit()

def draw_background(settings, screen):
    ''' Function to draw the background triangles to the screen '''

    # Use the key presses to scroll the trees
    update_tree_location(settings)
    update_arrays(settings, screen)

    # Draw the triangles to the screen
    for tlist in settings.tree_lists:
        arr_drawn = 0
        while arr_drawn < len(tlist):

            # Check the row the tree is in to decide the color
            if tlist[0][1] == 200:
                settings.tree_color = (30, 60, 30)
            elif tlist[0][1] == 300:
                settings.tree_color = (30, 75, 30)
            elif tlist[0][1] == 400:
                settings.tree_color = (30, 90, 30)

            # Draw the trees to the screen with the data from the settings array list
            RenderBG(settings, screen, tlist[arr_drawn, 0], tlist[arr_drawn, 1], 
                                        tlist[arr_drawn, 2], tlist[arr_drawn, 3], 
                                        tlist[arr_drawn, 4], tlist[arr_drawn, 5],)
            arr_drawn += 1

def update_tree_location(settings):
    ''' Function to update the location of the trees based on keypresses '''
    if settings.scroll_right == True:
        settings.move -= 1
    if settings.scroll_left == True:
        settings.move += 1

def update_arrays(settings, screen):
    ''' A function to update the arrays in settings '''

    # Empty the list of tree arrays
    settings.tree_lists = []

    # Make tree rows args= settings data, rate of movement, y-location, row number
    make_tree_row(settings, 1, 0, 0)
    make_tree_row(settings, 2, 100, 1)
    make_tree_row(settings, 3, 200, 2)

    # Make a brown rect to represent the floor
    make_floor(settings, screen, 1100, 350, 0, 550)

    # Check if any trees pass the bounding boxes of the screen
    check_screen_tree_collisions(settings)

def make_tree_row(settings, movex, movey, tree_row):
    ''' Function to make rows of trees and update them accordingly '''

    trees_drawn = 0
    # Make 7 trees
    while trees_drawn < 6:
        settings.make_array(50 + settings.move * movex + 220 * trees_drawn,   200 + movey,   150 + settings.move * movex + 220 * trees_drawn,   200 + movey,   100 + settings.move * movex + 220 * trees_drawn,   100 + movey)       # FIRST TREE INITIAL DIMENTIONS
        trees_drawn += 1
    settings.make_array(-170 + settings.move * movex, 200 + movey, -70 + settings.move * movex, 200 + movey, -120 + settings.move * movex, 100 + movey)    # SEVENTH TREE INITIAL DIMENTIONS
    
    # Add trees to compensate for the faster scroll speed
    if tree_row > 0:
        settings.make_array(-390 + settings.move * movex, 200 + movey, -290 + settings.move * movex, 200 + movey, -340 + settings.move * movex, 100 + movey) # EIGHTH TREE INITIAL DIMENSIONS
    if tree_row > 1:
        settings.make_array(-610 + settings.move * movex, 200 + movey, -510 + settings.move * movex, 200 + movey, -560 + settings.move * movex, 100 + movey) # NINTH TREE INITIAL DIMENSIONS
        settings.make_array(-830 + settings.move * movex, 200 + movey, -730 + settings.move * movex, 200 + movey, -780 + settings.move * movex, 100 + movey) # TENTH TREE INITIAL DIMENSIONS


def make_floor(settings, screen, l, w, x, y):
    ''' Function to make a brown floor for the forest '''
    image = pygame.Surface((l, w))
    image.fill((165, 42, 42))
    rect = image.get_rect(topleft= (x, y))
    pygame.draw.rect(screen, (44, 28, 4), rect)

def check_screen_tree_collisions(settings):
    ''' Function to hold logic for screen bounds to tree collision check '''

    # list in this loop represents the 6 sets of 3 coords for the triangles in one tree
    for list in settings.tree_lists:
        list_num = 0
        if list[0][0] == settings.tree_lists[4][0][0]:

            # list in this loop represents individual triangles in a given tree
            for list in list:
                if list_num % 6 == 5:
                    if list[0] >= 1100:
                        settings.move = 0
                list_num += 1
        elif list[0][0] == settings.tree_lists[0][0][0]:

            # list in this loop represents individual triangles in a given tree
            for list in list:
                if list_num % 6 == 5:
                    if list[0] <= 0:
                        settings.move = 220
                list_num += 1