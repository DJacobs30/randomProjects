import pygame

class Rhandel(pygame.sprite.Sprite):
    ''' A class to represent the man (Rhandel) wandering around the map '''
    
    def __init__(self, settings, screen, group):
        ''' Initialize the rhandel class '''
        super().__init__(group)
        self.settings = settings
        self.screen = screen
        self.move_num = 1
        self.rect = pygame.Rect((self.settings.rhandelx, self.settings.rhandely), (self.settings.rhandel_size*2, self.settings.rhandel_size*2))

    def move_rhandel(self, walls):
        ''' Function to make rhandel move diagonally '''

        if pygame.sprite.spritecollideany(self, walls):
            self.move_num += 1
            if self.move_num % 2 == 0:
                self.settings.rhandel_direction_y = self.settings.rhandel_direction_y*-1
            elif self.move_num % 2 == 1:
                self.settings.rhandel_direction_x = self.settings.rhandel_direction_x*-1

        self.settings.rhandelx += self.settings.rhandel_direction_x
        self.settings.rhandely += self.settings.rhandel_direction_y
        self.rect = pygame.Rect((self.settings.rhandelx, self.settings.rhandely), (self.settings.rhandel_size*2, self.settings.rhandel_size*2))

        self.blit_rhandel()

    def blit_rhandel(self):
        ''' Function to blit rhandel to the screen '''
        pygame.draw.rect(self.screen, self.settings.rhandel_color, self.rect)
