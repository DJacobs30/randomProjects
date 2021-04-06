import pygame

class writeText():
    ''' A class to take a string input and output a rect w/ said msg '''

    def __init__(self, settings, msg, size, x, y):
        ''' Initialize the writeText class '''

        font = pygame.font.Font(settings.font, size)

        text = font.render(msg, True, (255, 255, 255))

        textRect = text.get_rect()

        textRect.center = x, y

        return(text, textRect)