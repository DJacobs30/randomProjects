import pygame

class Duck():
    ''' A class to plit the duck.png frames to the screen '''

    def __init__(self, settings, screen):
        ''' Initialize the duck class '''
        self.settings = settings
        self.screen = screen
        self.frames_passed = 0

        # Load the duck image and its rect
        self.image = pygame.image.load("C:\\Users\\sxj0856\\OneDrive - The Home Depot\\Desktop\\Python\\python_projects\\platformer\\duck_anim\\duck_frame_1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Place duck in the middle of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        # Turn duck location to floats
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def update(self):
        ''' Update the duck's location based on keypresses '''

        if self.settings.scroll_right or self.settings.scroll_left:
            self.frames_passed += 1

            self.frame_num = self.frames_passed % 3

            if self.settings.scroll_left:
                self.frame_num += 3
            self.image = pygame.image.load("C:\\Users\\sxj0856\\OneDrive - The Home Depot\\Desktop\\Python\\python_projects\\platformer\\duck_anim\\duck_frame_" + str(self.frame_num) + '.png')

        # Draw duck to the screen
        self.blitme()

    def blitme(self):
        ''' Blit the duck image to the screen '''
        self.screen.blit(self.image, self.rect)