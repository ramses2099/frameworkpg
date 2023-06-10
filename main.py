import pygame, sys, os.path
from pygame.locals import *
import random


WINDOW_SIZE = (600, 450)
TITLE = "My pygame Window"
FPS = 60
BLACK = (0, 0, 0)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (50, 230, 40)


class Particle:
    def __init__(self, x, y) -> None:
        self.position = pygame.math.Vector2(x ,y)
        self.velocity = pygame.math.Vector2(0,0)
        self.acceleration = pygame.math.Vector2(15,10)
        self.radius =25
        
    def update(self,bound, dt):
        self.velocity.x += self.acceleration.x * dt
        self.velocity.y += self.acceleration.y * dt
        
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        
        self.handlerBoxCollision(bound)
        
    def handlerBoxCollision(self, bound):
        if self.position.x -self.radius <= bound.left or self.position.x + self.radius >= bound.right:
            self.velocity.x =-self.velocity.x
        if self.position.y -self.radius <= bound.top or self.position.y +self.radius>= bound.bottom:
            self.velocity.y =-self.velocity.y
    
    def draw(self,screen):
        pygame.draw.circle(screen, RED, self.position,self.radius)


# ECS
entities = []

p = Particle(250,220)

def main():
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    
    # rect
    rect_bounds = pygame.display.get_surface().get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill(BLACK)
        
        # Update
        
        #FPS
        dt = 1/FPS
        p.update(rect_bounds,dt)

        # Draw 
        pygame.draw.rect(screen,BLUE,rect_bounds,5)
        p.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
