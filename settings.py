class Settings():
    """A class to store all the settings for the game Aliens Ahoy!"""

    def __init__ (self):
        """Initialize the game's static settings"""
        #screen settings
        self.screen_width = 1275
        self.screen_height = 680
        self.bg_colour = (230, 230, 230)
        #ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_colour = 60, 0, 0
        self.bullets_allowed = 5
        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #how quickly the game speeds up
        self.speedup_scale = 1.1
        #how quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings (self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1.3
        #fleet direction of 1 represents right and -1 represents left
        self.fleet_direction = 1
        #scoring
        self.alien_points = 50

    def increase_speed (self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.score_scale)
        print(self.alien_points)