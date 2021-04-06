import pygame

class Buttons(pygame.sprite.Sprite):
    ''' A class to make all the buttons into rects to collide to '''
    
    def __init__(self, settings, screen, x, y, l, w, group):
        ''' Initialize the button class '''
        super().__init__(group)
        self.settings = settings
        self.screen = screen

        self.image = pygame.Surface((l, w))
        self.image.fill(self.settings.button_bg_color)
        self.rect = self.image.get_rect(topleft= (x, y))