class Settings():
    ''' Class to hold all of the settings for the game '''

    def __init__(self):
        ''' Initialize the Settings class '''

        # Screen Settings
        self.screen_width, self.screen_height = 800, 500
        self.bg_color = (0,0,0)
        self.font = ("C:\\Users\\sxj0856\\OneDrive - The Home Depot\\Desktop\\Python\\fonts\\minecraft.ttf")

        # Game Settings
        self.game_phase = 0
        self.isTyping = True
        self.isScrolling = True
        self.onTrail = True
        self.msg = ''
        self.i = 0
        self.x_pos = 400

        # Player Settings
        self.players = []
        self.p1 = ''
        self.p2 = ''
        self.p3 = ''
        self.p4 = ''