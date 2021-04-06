class Settings():
    ''' Create the class to hold all of the settings for the program '''

    def __init__(self):
        ''' Initialize the setting variables '''

        # Screen Settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # Menu Settings
        self.menu_size = self.screen_height/12
        self.menu_color = (200, 200, 200)
        self.button_size = self.menu_size - (self.menu_size/5)
        self.button_bg_color = (150, 150, 150)
        self.sizes = [5, 10, 15]
        self.colors = [(0, 0, 0), (255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (128, 0, 255), (255, 255, 255), (90, 50, 10)]

        # Save settings
        self.save_file = False
        self.save_dir = "C:\\Users\\sxj0856\\OneDrive - The Home Depot\\Desktop\\Python\\python_projects\\ms_paint\\saves"