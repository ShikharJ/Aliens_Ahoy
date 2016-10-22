import pygame.font

class Button():

    def __init__ (self, ai_settings, screen, msg):
        """Initialize button features"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #set dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_colour = (255, 0, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        #build the button's rect object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        #button message needs to be pushed only once
        self.prep_msg(msg)
    def prep_msg (self, msg):
        """Turn message into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_colour, self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    def draw_button (self):
        #draw blank button ad then draw message.
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)