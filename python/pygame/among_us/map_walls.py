import pygame

class mapWalls(pygame.sprite.Sprite):
    ''' Make a class to render all of the rects for the map to the screen '''

    def __init__(self, settings, screen, coords, length_width, walls):
        ''' Initialize the map walls class '''
        super().__init__(walls)
        self.settings = settings
        self.screen = screen

        self.image = pygame.Surface(length_width)
        self.image.fill(self.settings.map_color)
        self.rect = self.image.get_rect(topleft=coords)