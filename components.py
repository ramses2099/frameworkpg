import pygame
from dataclasses import dataclass

#Componenets

@dataclass
class Direction:
    dir:float = 1.0
    name:str ="Direction"

# Has a Position in the world
@dataclass
class Transform:
    x:int=0
    y:int=0
    w:int=0
    h:int=0
    name:str ="Transform"
    
    def rect(self):
       rect = pygame.Rect(self.x, self.y, self.w, self.h)
       return rect

# Can move(velocity, acceleration)
@dataclass
class Motion:
    vx:float = 0.0
    vy:float = 0.0
    ax:float = 0.0 
    ay:float = 0.0 
    name:str ="Motion"

@dataclass
class Type:
    typename:str
    name:str ="Type"

@dataclass# Should display on screen
class Sprite:
    draw = True
    name:str ="Sprite"

@dataclass# Collides with other entity
class Collision:
    name:str ="Collision"

@dataclass# Life 
class Life:
    name:str = "Life"
    currentlife:int = 3
    maxlife:int = 5

@dataclass# Debug component
class Debug:
    name:str = "Debug"

@dataclass
class Collectable:
    name:str = "Collectable"
    collect:bool = True
    
@dataclass
class Input:
    name:str = "Input"
       