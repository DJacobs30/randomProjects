class Settings():
    ''' Settings to hold all of the settings for the hide and seek game '''

    def __init__(self): 
        ''' Initialize the settings class '''

        # Screen Settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (50, 50, 50)

        # General Player Settings
        self.player_speed = .5
        self.latest_packet = []

        # Local Player Settings
        self.pLocal_moving_right = False
        self.pLocal_moving_left = False
        self.pLocal_moving_up = False
        self.pLocal_moving_down = False
        self.pLocal_wall_collide = False

        # Map Settings
        self.walls = [[(50, 50), (400, 20)], [(50, 70), (20, 500)], [(450, 50), (20, 500)], [(50, 550), (420, 20)]]
        self.map_color = (200, 200, 200)