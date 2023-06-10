import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (50, 230, 40)

class Player:
    def __init__(self, x, y, w, h) -> None:
        self.rect = pygame.rect.Rect(x,y, w, h)
        self.gravity, self.friction = .35, -.12
        self.position = pygame.math.Vector2(x,y)
        self.velocity= pygame.math.Vector2(0,0)
        self.acceleration = pygame.math.Vector2(0,self.gravity)
        self.LEFT_KEY, self.RIGHT_KEY = False, False
        self.is_jumping, self.on_ground = False, False
    
    
    
    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)
    
    # Newton's Equations of Motion
    # New Velocity = Previus Velocity + Acceleration * Time
    # New Position = Previus Position + (Velocity * Time) + (.5 * Acceleration * (Time^2))
    def update(self, dt, tiles):
        self.horizontal_movement(dt)
        self.checkCollisionx(tiles)
        self.vertical_movement(dt)
        self.checkCollisiony(tiles)
    
    def horizontal_movement(self, dt):
        self.acceleration.x = 0
        if self.LEFT_KEY:
            self.acceleration.x -= .3
        elif self.RIGHT_KEY:
            self.acceleration.x += .3
            
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        #LIMIT VELOCITY
        self.limit_velocity(4)
        self.position.x += self.velocity.x * dt + (self.acceleration.x * .5) * (dt * dt)
        # ADD POSITION RECT PYGAME
        self.rect.x = self.position.x
    
    def vertical_movement(self,dt):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 7: self.velocity.y = 7
        self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
        # VALIDATE GROUND
        # if self.position.y > 450:
        #     self.on_ground = True
        #     self.velocity.y = 0
        #     self.position.y = 450
            
        # ADD POSITION RECT PYGAME   
        self.rect.bottom = self.position.y
        
    def limit_velocity(self, max_vel):
        min(-max_vel, max(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01:self.velocity.x =0
        
    def jump(self):
        if self.on_ground:
            self.is_jumping = True
            self.velocity.y -= 8
            self.on_ground = False
            
    def get_hits(self, tiles):
        hits =[]
        for tile in tiles:
            if self.rect.colliderect(tile):
                hits.append(tile)
        return hits
    
    def checkCollisionx(self,tiles):
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if self.velocity.x > 0:
                self.position.x = tile.left - self.rect.w
                self.rect.y = self.position.x
            elif self.velocity.x < 0:
                self.position.x = tile.right
                self.rect.x = self.position.x
                
    def checkCollisiony(self, tiles):
        self.on_ground = False
        self.rect.bottom += 1
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if self.velocity.y > 0:
                self.on_ground = True
                self.is_jumping = False
                self.velocity.y = 0
                self.position.y = tile.top
                self.rect.bottom = self.position.y
            elif self.velocity.y < 0:
                self.velocity.y = 0
                self.position.y = tile.bottom + self.rect.h
                self.rect.bottom = self.position.y