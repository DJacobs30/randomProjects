import pygame

def run_game(settings, screen, s, ep):
    ''' Function to Run the Game '''

    # Play Intro
    if settings.game_phase == 0:
        write_text(settings, screen, s.intro1, 48, (400, 250))
        write_text(settings, screen, s.intro2, 24, (400, 300))
        cfe(settings)

    # Start Day Screen
    if settings.game_phase == 1:
        start_day(settings, screen, s, s.amc1)

    # Friend Picking
    if settings.game_phase == 2:
        draw_image(settings, screen, s.amc_img, (150, 250))
        write_text(settings, screen, s.amc2, 32, (500, 100))
        write_text(settings, screen, s.amc3, 12, (500, 150))
        write_text(settings, screen, s.amc4, 12, (500, 175))
        write_text(settings, screen, s.amc5, 12, (390, 225))
        if settings.isTyping:
            typeing(settings, screen)

    # Start Gameplay
    if settings.game_phase == 3:
        draw_image(settings, screen, s.amc_img, (150, 250))
        write_text(settings, screen, s.amc6, 24, (520, 150))
        write_text(settings, screen, s.amc7, 18, (520, 200))
        write_text(settings, screen, s.amc8, 18, (520, 220))
        write_text(settings, screen, s.intro2, 18, (520, 250))
        cfe(settings)

    # Main Trail Loop
    if settings.game_phase == 4:
        if settings.onTrail:
            scroll_screen(settings, screen, s, settings.isScrolling)
            pygame.draw.rect(screen, (0,0,0), (0, 350, 800, 150))
            ep.draw_ep(settings, screen, 1, True)
        
        else:
            settings.game_phase += 1

    # Springer Mountain
    if settings.game_phase == 5:
        draw_image(settings, screen, s.spr_img, (400, 200))
        write_text(settings, screen, s.spr1, 32, (400, 390))
        write_text(settings, screen, s.spr2, 24, (400, 425))
        write_text(settings, screen, s.spr3, 18, (400, 450))
        write_text(settings, screen, s.intro2, 12, (400, 475))
        cfe(settings)

    if settings.game_phase == 6:
        settings.onTrail = True
        ep.x, ep.y, ep.i, ep.eps, ep.leps, ep.second = -5, 480, 0, [], [], True
        start_day(settings, screen, s, s.spr4)

    # Day 2 Hike
    if settings.game_phase == 7:
        if settings.onTrail:
            scroll_screen(settings, screen, s, settings.isScrolling)
            pygame.draw.rect(screen, (0,0,0), (0, 350, 800, 150))
            ep.draw_ep(settings, screen, 2, True)

        else:
            settings.game_phase += 1

    # Hawk Mountain
    if settings.game_phase == 8:
        draw_image(settings, screen, s.hwk_img, (400, 200))
        write_text(settings, screen, s.hwk1, 32, (400, 390))
        write_text(settings, screen, s.hwk2, 24, (400, 425))
        write_text(settings, screen, s.hwk3, 18, (400, 450))
        write_text(settings, screen, s.intro2, 12, (400, 475))
        cfe(settings)
    
    if settings.game_phase == 9:
        settings.onTrail = True
        ep.x, ep.y, ep.i, ep.eps, ep.leps, ep.second = -5, 480, 0, [], [], True
        start_day(settings, screen, s, s.hwk4)

    # Day 3 Hike
    if settings.game_phase == 10:
        if settings.onTrail:
            scroll_screen(settings, screen, s, settings.isScrolling)
            pygame.draw.rect(screen, (0,0,0), (0, 350, 800, 150))
            ep.draw_ep(settings, screen, 3, True)

        else:
            settings.game_phase += 1

    if settings.game_phase == 11:
        settings.onTrail = True
        ep.x, ep.y, ep.i, ep.eps, ep.leps, ep.second = -5, 480, 0, [], [], True
        draw_image(settings, screen, s.sas_img, (400, 200))
        write_text(settings, screen, s.sas1, 32, (400, 390))
        write_text(settings, screen, s.sas2, 24, (400, 425))
        write_text(settings, screen, s.intro2, 12, (400, 475))
        cfe(settings)

    if settings.game_phase == 12:
        if settings.onTrail:
            scroll_screen(settings, screen, s, settings.isScrolling)
            pygame.draw.rect(screen, (0,0,0), (0, 350, 800, 150))
            ep.draw_ep(settings, screen, 4, True)

        else:
            settings.game_phase += 1

    # Gooch Mountain
    if settings.game_phase == 13:
        draw_image(settings, screen, s.goo_img, (400, 200))
        write_text(settings, screen, s.goo1, 32, (400, 390))
        write_text(settings, screen, s.goo2, 24, (400, 425))
        write_text(settings, screen, s.goo3, 18, (400, 450))
        write_text(settings, screen, s.intro2, 12, (400, 475))
        cfe(settings)
    


def write_text(settings, screen, msg, size, pos):
    ''' Blit a message on the screen '''

    font = pygame.font.Font(settings.font, size)

    text = font.render(msg, True, (255, 255, 255))

    textRect = text.get_rect()

    textRect.center = pos

    screen.blit(text, textRect)

def draw_image(settings, screen, img, pos):
    ''' Blit an image on the screen '''

    image = pygame.image.load(img)

    imageRect = image.get_rect()

    imageRect.center = pos

    screen.blit(image, imageRect)

def typeing(settings, screen):
    ''' Type into pygame window '''

    # Get keyboard input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            # If [enter] then save the name and move to the next
            if event.key == pygame.K_RETURN:
                settings.i += 1
                if settings.i == 4:
                    settings.isTyping = False
                    settings.game_phase += 1
                    pass
                settings.players.append(settings.msg)
                settings.msg = ''

            # If [backspace] then pop the most recent character
            elif event.key == pygame.K_BACKSPACE:
                settings.msg = settings.msg[:-1]

            # Else, check the string of the key pressed and add to the name
            else:
                settings.msg += event.unicode

    # Write the name typed to the screen
    write_text(settings, screen, settings.msg, 12, (410, 250 + settings.i*15))

    # Write the previous names to the scren
    if len(settings.players) > 0:
        write_text(settings, screen, settings.players[0], 12, (410, 250))
        if len(settings.players) > 1:
            write_text(settings, screen, settings.players[1], 12, (410, 265))
            if len(settings.players) > 2:
                write_text(settings, screen, settings.players[2], 12, (410, 280))

def cfe(settings):
    ''' Check for Enter '''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                settings.game_phase += 1

def start_day(settings, screen, s, msg):
    ''' Function to use for each day start screen '''

    write_text(settings, screen, msg, 32, (400, 250))
    write_text(settings, screen, s.intro2, 18, (400, 300))
    cfe(settings)

def scroll_screen(settings, screen, s, scroll):
    ''' Function to scroll the background '''

    if scroll:
        if settings.x_pos <= -400:
            settings.x_pos = 400

    settings.x_pos -= 1
    draw_image(settings, screen, s.tr_img, ((settings.x_pos), 250))
    draw_image(settings, screen, s.tr_img, ((settings.x_pos + 800), 250))

def trail_encounters():
    ''' Function to manage random encounters '''
    pass