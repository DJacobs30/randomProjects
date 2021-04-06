import pygame

class localPlayer():
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

    def move_player(self):
        ''' Function to move the players rect '''

        if not self.settings.pLocal_wall_collide:
            if self.settings.pLocal_moving_left:
                self.centerx -= self.settings.player_speed
            if self.settings.pLocal_moving_right:
                self.centerx += self.settings.player_speed
            if self.settings.pLocal_moving_up:
                self.centery -= self.settings.player_speed
            if self.settings.pLocal_moving_down:
                self.centery += self.settings.player_speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def draw_player(self, n):
        # Function to draw the player rect to the screen
        pygame.draw.rect(self.screen, (100, 50, n), self.rect)
        try:
            pygame.draw.rect(self.screen, (150, 150, 150), (self.settings.latest_packet[0], self.settings.latest_packet[1], 40, 40))
        except IndexError:
            pass