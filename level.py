import pygame
from tile import Tile

class Level:
    def __init__(self, level_data, surface) -> None:
        self.surface = surface
        self.level_data = level_data
        self.titles = pygame.sprite.Group()
        
    def set_level(self, layout):
        for row_idx, row in enumerate(self.level_data):
            for col_idx, cel in enumerate(row):
                pass
            
        
    def run(self):
        pass