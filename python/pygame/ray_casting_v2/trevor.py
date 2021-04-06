import pygame

class Trevor(pygame.sprite.Sprite):
    ''' A class to represent the man (Trevor) wandering around the map '''
    
    def __init__(self, settings, screen, group):
        ''' Initialize the trevor class '''
        super().__init__(group)
        self.settings = settings
        self.screen = screen
        self.move_num = 1
        self.rect = pygame.Rect((self.settings.trevorx, self.settings.trevory), (self.settings.trevor_size*2, self.settings.trevor_size*2))

    def move_trevor(self, walls):
        ''' Function to make trevor move diagonally '''

        if pygame.sprite.spritecollideany(self, walls):
            self.move_num += 1
            if self.move_num % 2 == 0:
                self.settings.trevor_direction_y = self.settings.trevor_direction_y*-1
            elif self.move_num % 2 == 1:
                self.settings.trevor_direction_x = self.settings.trevor_direction_x*-1

        self.settings.trevorx += self.settings.trevor_direction_x
        self.settings.trevory += self.settings.trevor_direction_y
        self.rect = pygame.Rect((self.settings.trevorx, self.settings.trevory), (self.settings.trevor_size*2, self.settings.trevor_size*2))

        self.blit_trevor()

    def blit_trevor(self):
        ''' Function to blit trevor to the screen '''
        pygame.draw.rect(self.screen, self.settings.trevor_color, self.rect)
