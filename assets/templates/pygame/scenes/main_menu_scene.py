import pygame
import sys

from src.consts.colors import Colors

class MainMenuScene:
    
    def __init__(self, display, goto):
        self.display = display
        self.goto = goto
        
    def draw(self):
        self.display.fill(Colors.BACKGROUND)
        
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
