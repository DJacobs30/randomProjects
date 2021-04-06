class Settings():
    ''' Class to hold all of the settings for the game '''

    def __init__(self):
        ''' Initialize the Settings class '''
        
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (60, 60, 60)
        self.run_game = True

        # Tank settings
        self.tank_color = (150, 100, 50)
        self.tank1x = 200
        self.tank2x = 800
        self.tank1mr, self.tank1ml, self.tank1rr, self.tank1rl = False, False, False, False
        self.tank2mr, self.tank2ml, self.tank2rr, self.tank2rl = False, False, False, False

        # Cannon Settings
        self.cannon_length = 40
        self.cannon1y, self.cannon2y = 400, 400
        self.cannon1t, self.cannon2t = 0, 180
        self.tanky = 400
        
        # Cannonball Settings
        self.ballv = 25
        self.start_timer = False
        self.tank_fire = False
        self.t = 1
        self.tank_num = 2