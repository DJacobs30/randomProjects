import numpy as np
class Settings():
    ''' A class to hold all of the settings for the game '''
    def __init__(self):
        ''' Initialize all of the game settings '''
        
        # Screen Settings
        self.screen_width = 520
        self.screen_height = 640
        self.bg_color = (0, 0, 0)
        self.update_needed = True

        # Map Settings
        self.map_color = (255, 255, 255)
        self.map_arr = np.array([[10, 10, 500, 10], [10, 20, 10, 290], [500, 20, 10, 290], [20, 300, 480, 10],
                                [10, 100, 150, 10], [200, 200, 10, 100], [85, 190, 75, 10], [300, 250, 10, 50],
                                [350, 20, 10, 100], [360, 110, 140, 10], [300, 150, 10, 50], [400, 120, 10, 100]])

        # Point Settings
        self.point_color = (255, 0, 0)
        self.dir_color = (100, 0, 0)
        self.deg_rotation = 0
        self.pp_disp = 5
        self.degree = 0

        # Control Settings
        self.rotating_left = False
        self.rotating_right = False
        self.moving_forward = False
        self.moving_back = False

        # Ray Settings
        self.ray_color = (100, 100, 100)
        self.ray_degree_range = 60
        self.base_ray_degree_range = 60
        self.distances = []
        self.collision_origin_distance = []
        self.angle_distance = 1
        self.resolution = 8

        # Line Settings
        self.line_base_length = 300
        self.line_width = 8
        self.line_lengths = []
        self.linex = 20

        # Trevor Settings
        self.trevorx, self.trevory = 450, 150
        self.trevor_direction_x = -2
        self.trevor_direction_y = -2
        self.trevor_color = (165, 42, 42)
        self.trevor_size = 5

        #Rhandel Settings
        self.rhandelx, self.rhandely = 150, 250
        self.rhandel_direction_x = 2
        self.rhandel_direction_y = -2
        self.rhandel_color = (165, 42, 42)
        self.rhandel_size = 7.5

        # Roamer Settings
        self.roamer_hit = False
        self.roamer_color = False

