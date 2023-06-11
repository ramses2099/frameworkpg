import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, color, size=(64,64)) -> None:
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=position)
