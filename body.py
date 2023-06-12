import pygame
from pygame.math import Vector2


class Body:
    def __init__(self, x, y, w, h, mass) -> None:
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.mass = mass
        
        self.image = pygame.surface.Surface([w, h])
        self.react = self.image.get_rect()
        self.react.x = x
        self.react.y = y
        
        self.forces = {}
    
    def draw(self, screen):
        pygame.draw.rect(screen, pygame.color.THECOLORS['red'],self.react)
        
    def addContinued(self,fx,fy):
        self.forces['continued'] = Vector2(fx,fy)
    
    def addIstant(self, fx, fy):
        self.forces['istant'] = Vector2(fx,fy)
        
    def update(self, dt):        
        if self.forces['istant'] is not None:
            self.velocity.x += self.forces['istant'].x / self.mass * dt
            self.velocity.y += self.forces['istant'].y  / self.mass * dt
        
        if self.forces['continued'] is not None:
            self.velocity.y += self.forces['continued'].y  / self.mass * dt
        
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        
        self.react.x += self.position.x
        self.react.y += self.position.y
        