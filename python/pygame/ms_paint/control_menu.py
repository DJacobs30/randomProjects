import pygame

from buttons import Buttons

class ControlMenu():
    ''' Class to make the control bar for the program '''

    def __init__(self, settings, screen, draw):
        ''' Initialize the control menu class '''
        self.settings = settings
        self.screen = screen
        self.draw = draw

    def draw_menu(self):
        ''' Function to draw the background for the menu '''
        self.i = 0
        self.draw_menu_background()
        self.draw_size_buttons()
        self.draw_color_buttons()
        self.draw_background_button()
        self.draw_save_button()
        self.draw_clear_button()

    def draw_menu_background(self):
        # Function to make the menu background rect
        pygame.draw.rect(self.screen, self.settings.menu_color, (0, 0, self.settings.screen_width, self.settings.menu_size))

    def draw_size_buttons(self):
        # Function to draw buttons of the three different sizes
        for size in self.settings.sizes:
            pygame.draw.circle(self.screen, self.draw.color, (round((self.settings.menu_size/2) + (self.settings.menu_size * self.i)), round(self.settings.menu_size/2)), size)
            self.i += 1

    def draw_color_buttons(self):
        # Function to draw the buttons of the different colors
        for color in self.settings.colors:
            pygame.draw.rect(self.screen, color, ((self.settings.menu_size/10) + (self.settings.menu_size * self.i), self.settings.menu_size/10,
                            self.settings.button_size, self.settings.button_size))
            self.i += 1

    def draw_background_button(self):
        # Function to draw the button to fill the background a specific color
        pygame.draw.polygon(self.screen, (100, 100, 100), ((self.settings.menu_size/5 + self.i*self.settings.menu_size, self.settings.menu_size/5),
                                                        (self.settings.menu_size/5 + round(self.settings.menu_size*.6) + self.i*self.settings.menu_size, 
                                                        self.settings.menu_size/5),
                                                        (self.settings.menu_size*(2/3) + self.i*self.settings.menu_size,
                                                        self.settings.menu_size/5 + round(self.settings.menu_size*.6)),
                                                        (self.settings.menu_size/3 + self.i*self.settings.menu_size,
                                                        self.settings.menu_size/5 + round(self.settings.menu_size*.6))))
        self.i += 1

    def draw_save_button(self):
        # Function to draw the save button
        pygame.draw.polygon(self.screen, (0, 255, 255), ((self.settings.menu_size/5 + self.i*self.settings.menu_size, self.settings.menu_size/5),
                                                        (self.settings.menu_size/5 + round(self.settings.menu_size*.6) + self.i*self.settings.menu_size, 
                                                        self.settings.menu_size/5),
                                                        (self.settings.menu_size/2 + self.i*self.settings.menu_size,
                                                        self.settings.menu_size/5 + round(self.settings.menu_size*.6))))
        self.i += 1
    
    def draw_clear_button(self):
        # Function to draw the clear button
        pygame.draw.circle(self.screen, (255, 0, 0), (round((self.settings.menu_size/2) + (self.settings.menu_size * self.i)), round(self.settings.menu_size/2)), 15, 2)
        pygame.draw.line(self.screen, (255, 0, 0), (self.settings.menu_size/5 + self.settings.menu_size * self.i, self.settings.menu_size/5), 
                                                    (self.settings.menu_size*.8 + self.settings.menu_size * self.i, self.settings.menu_size*.8), 4)

    def init_buttons(self, buttons):
        # Initialize the buttons
        i = 0
        while i < 15:
            Buttons(self.settings, self.screen, (self.settings.menu_size/10) + (self.settings.menu_size * i), self.settings.menu_size/10,
                            self.settings.button_size, self.settings.button_size, buttons)
            i += 1