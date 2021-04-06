import pygame

class otherPlayers():
    ''' A class to hold all of the information for the player represented by the local pc '''
    
    def __init__(self, settings, screen):
        ''' Initialize the localPlayer class '''
        self.settings = settings
        self.screen = screen

        self.dimensions = pygame.Surface((40, 40))
        self.rect = self.dimensions.get_rect()

        self.screen_rect = self.screen.get_rect()
        self.rect.center = self.screen_rect.center

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)