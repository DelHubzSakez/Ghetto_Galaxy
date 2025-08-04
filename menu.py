import pygame
from constants import *

class Menu():
    def __init__(self, screen, option_list, init_selection_index):

        self.screen   = screen
        self.options  = option_list
        self.selected = init_selection_index
        
        self.font            = pygame.font.Font(None, 74) 
        self.text_color      = (255, 255, 255) 
        self.highlight_color = (102,255,0) 
        self.line_spacing    = 80

    def draw(self, screen):
        
        selected_index = 0
        
        start_y = (SCREEN_HEIGHT / 2) - (len(self.options) * self.line_spacing / 2)

        for i in self.options:
            color_to_use = self.text_color
            
            if selected_index == self.selected:
                
                color_to_use  = self.highlight_color
            
            text_surface      = self.font.render(f"{i}", True, color_to_use)
            
            text_rect         = text_surface.get_rect()
            
            text_rect.centerx = (SCREEN_WIDTH / 2)

            text_rect.top     = start_y + (selected_index * self.line_spacing)

            screen.blit(text_surface, text_rect)

            selected_index   += 1

    def move_up(self):    
        if self.selected == 0:
            self.selected = len(self.options) - 1
        else:
            self.selected -= 1    

    def move_down(self):    
        if self.selected == len(self.options) - 1:
            self.selected = 0
        else:
            self.selected += 1    
                   