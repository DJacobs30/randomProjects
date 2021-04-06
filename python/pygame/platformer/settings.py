import numpy as np

class Settings():
    ''' A class to hold all of the settings for the game '''

    def __init__(self):
        ''' Initialize the settings for the platformer '''

        # Screen Settings
        self.screen_width, self.screen_height = 1100, 800
        self.bg_color = (10, 10, 100)

        # Background Scroll Settings
        self.move = 0
        self.scroll_right = False
        self.scroll_left = False

        # Duck Settings
        self.duck_speed = 4

        # Background Settings
        self.tree_lists = []
        self.x1r, self.y1r, self.x2r, self.y2r, self.x3r, self.y3r = -10, 75, 10, 75, 0, 50
        self.tree_color = (30, 60, 30)

    def make_array(self, x1, y1, x2, y2, x3, y3):
        # Function to condense array code
        array = np.array([[x1 + self.x1r * 0, y1 + self.y1r * 0, x2 + self.x2r * 0, y2 + self.y2r * 0, x3, y3 + self.y3r * 0], 
                        [x1 + self.x1r * 1, y1 + self.y1r * 1, x2 + self.x2r * 1, y2 + self.y2r * 1, x3, y3 + self.y3r * 1], 
                        [x1 + self.x1r * 2, y1 + self.y1r * 2, x2 + self.x2r * 2, y2 + self.y2r * 2, x3, y3 + self.y3r * 2], 
                        [x1 + self.x1r * 3, y1 + self.y1r * 3, x2 + self.x2r * 3, y2 + self.y2r * 3, x3, y3 + self.y3r * 3], 
                        [x1 + self.x1r * 4, y1 + self.y1r * 4, x2 + self.x2r * 4, y2 + self.y2r * 4, x3, y3 + self.y3r * 4], 
                        [x1 + self.x1r * 5, y1 + self.y1r * 5, x2 + self.x2r * 5, y2 + self.y2r * 5, x3, y3 + self.y3r * 5]])
        self.tree_lists.append(array)