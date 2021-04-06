import pygame

def draw(draw):
    ''' Function to check the mouse location with '''
    draw.mouse_pos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        draw.draw_shape()

def button_check(draw, buttons):
    ''' Function to check if any of the buttons are clicked '''

    for button in buttons:
        if pygame.mouse.get_pressed()[0]:
            if button.rect.collidepoint(draw.mouse_pos):
                return((button.rect[0] - 5)/50)

def update_screen(settings, screen, draw, buttons):
    ''' Function to update according to what buttons were pressed '''
    if button_check(draw, buttons) == 0:
        draw.size = settings.sizes[0]
    elif button_check(draw, buttons) == 1:
        draw.size = settings.sizes[1]
    elif button_check(draw, buttons) == 2:
        draw.size = settings.sizes[2]
    elif button_check(draw, buttons) == 3:
        draw.color = settings.colors[0]
    elif button_check(draw, buttons) == 4:
        draw.color = settings.colors[1]
    elif button_check(draw, buttons) == 5:
        draw.color = settings.colors[2]
    elif button_check(draw, buttons) == 6:
        draw.color = settings.colors[3]
    elif button_check(draw, buttons) == 7:
        draw.color = settings.colors[4]
    elif button_check(draw, buttons) == 8:
        draw.color = settings.colors[5]
    elif button_check(draw, buttons) == 9:
        draw.color = settings.colors[6]
    elif button_check(draw, buttons) == 10:
        draw.color = settings.colors[7]
    elif button_check(draw, buttons) == 11:
        draw.color = settings.colors[8]
    elif button_check(draw, buttons) == 12:
        screen.fill(draw.color)
    elif button_check(draw, buttons) == 13:
        settings.save_file = True
    elif button_check(draw, buttons) == 14:
        screen.fill(settings.bg_color)

def get_file_name(settings, screen):
    ''' Function to return the name of the file '''
    text = ''
    font = pygame.font.Font(None, 42)
    color = pygame.Color("firebrick")
    typing = True

    while typing:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    typing = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        txt_surface = font.render(text, True, color)
        screen.blit(txt_surface, (10, settings.screen_height - settings.menu_size))
        pygame.display.flip()

    return(text)

def save(settings, screen):
    ''' Function to save the screenshot of the drawing area '''
    
    save_name = get_file_name(settings, screen)

    rect = pygame.Rect(0, settings.menu_size, settings.screen_width, settings.screen_height - settings.menu_size)
    sub = screen.subsurface(rect)
    pygame.image.save(sub, settings.save_dir + "\\" + save_name + '.jpg')
    settings.save_file = False
