import pygame, sys, random
from pygame.locals import *

WINDOW_SIZE = (600, 600)
TITLE = "Breakout"
FPS = 60
BLACK = (0, 0, 0)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (50, 230, 40)

pygame.init()
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()      

class Particle:
    def __init__(self, x, y) -> None:
        self.radius = 10
        self.x = x - self.radius
        self.y = y
        self.rect = pygame.Rect(x, y, (self.radius * 2), (self.radius * 2))
        self.weight = random.random() * 1 + 1
        self.dirX = 1
    
    def update(self, dt):
        # if self.rect.bottom > WINDOW_SIZE[1]:
        #     self.rect.y = 0 - self.radius
        #     self.weight = random.random() * 1 + 1
        #     self.radius = 10
        #     self.rect.x = random.random() * WINDOW_SIZE[0] * 1.3
        self.weight += 0.01
        self.rect.y += self.weight * dt
        self.rect.x += self.dirX
        
    def draw(self, screen):
         #Draw
        x = self.rect.x + self.radius
        y = self.rect.y + self.radius
        pygame.draw.circle(screen, RED, (x,y),self.radius)
        pygame.draw.circle(screen, BLUE, (x,y),self.radius,3)

class Ground:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.w = WINDOW_SIZE[0]
        self.h = 25
        self.rect = pygame.rect.Rect(self.x, self.y-self.h, self.w, self.h)
        
    def draw(self, screen):
         #Draw
        pygame.draw.rect(screen, GREEN, self.rect)
        pygame.draw.rect(screen, RED, self.rect, 3)

class Box:
    def __init__(self, x, y) -> None:
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.w, self.h = 25, 25
        self.mass = random.randint(1,10)
        self.rect = pygame.rect.Rect(self.position.x, self.position.y, self.w, self.h)
    
    
    def applyForce(self, vect):
        x = vect.x / self.mass
        y = vect.y / self.mass
        # Apply        
        self.acceleration.x = x
        self.acceleration.y = y
        
    def draw(self, screen):
         #Draw
        pygame.draw.rect(screen, GREEN, self.rect)
        pygame.draw.rect(screen, BLUE, self.rect, 3) 
       
    def update(self, dt):
        self.velocity.x += self.acceleration.x * dt
        self.velocity.y += self.acceleration.y * dt
        # Position
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        # pygame object
        self.rect.x = int(self.position.x)
        self.rect.y = int(self.position.y)
        # Boucing
        if self.rect.left < self.w or self.rect.right > (WINDOW_SIZE[0] - self.w):
            self.velocity.x *= -1
        if self.rect.bottom > (WINDOW_SIZE[0] - self.h) or self.rect.top < self.h:
            self.velocity.y *= -1
        
class App:
    def __init__(self) -> None:
        self.particlesArray = []
        self.numberOfParticle = 20
        self.groud = Ground(0,WINDOW_SIZE[1])
        # 
        self.init()
        
    def init(self):
        for i in range(self.numberOfParticle):
            x = random.randint(10, WINDOW_SIZE[0]-25)            
            y = random.randint(-25,25)
            # self.particlesArray.append(Particle(x,y))
            self.particlesArray.append(Box(x, y))

            # p = Box(x, y)
            # p.applyForce(pygame.math.Vector2(0,0.15))           
            # self.particlesArray.append(p)
        
    def draw(self):
        for p in self.particlesArray:
            p.draw(screen)
        
        #GROUND    
        self.groud.draw(screen)
    
    def update(self, dt):
        for p in self.particlesArray:
            p.update(dt)
            #Collition ball vs ground
            if pygame.rect.Rect.colliderect(p.rect, self.groud.rect):
               p.velocity.x *= -1
               p.velocity.y *= -1
            for other in self.particlesArray:
                if other.rect != p.rect:
                    if pygame.rect.Rect.colliderect(p.rect, other.rect):
                        p.velocity.x *= -1
                        p.velocity.y *= -1
                        p.applyForce(pygame.math.Vector2(0.10, 0.0))
                        p.applyForce(pygame.math.Vector2(0.0, 0.15))  
        
    
    def run(self):
        while True:
            #DELTA TIME
            dt = clock.tick(FPS) * .001 * FPS
            #INPUT EVENT
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                                    
                    
            screen.fill(BLACK)
            
            # Update
            self.update(dt)

            # Draw
            self.draw()
            
            pygame.display.flip()
        



if __name__ == "__main__":
    App().run()
