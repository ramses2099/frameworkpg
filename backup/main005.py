import pygame, sys, random
from pygame.locals import *

WINDOW_SIZE = (600, 600)
TITLE = "Breakout"
FPS = 60
BLACK = (0, 0, 0)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (50, 230, 40)

BLOCK_RED = (242, 85, 96)
BLOCK_BLUE = (86, 174, 87)
BLOCK_GREEN = (69, 177, 233)

PADDLE_COLOR = (142, 135, 123)
PADDLE_OUTLINE = (100, 100, 100)


BG =(234,218,184)

pygame.init()
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()      

COLS = 6
ROWS = 6

class Wall:
    def __init__(self) -> None:
        self.width = WINDOW_SIZE[0] // COLS
        self.height = 50
        self.blocks = []
        
    def create_wall(self):
        block_individual = []
        for row in range(ROWS):
            block_row = []            
            for col in range(COLS):
                b_x = col * self.width
                b_y = row * self.height
                rect = pygame.Rect(b_x,b_y,self.width, self.height)
                strenght = random.randint(1,3)
                block_individual = [rect,strenght]
                block_row.append(block_individual)
            self.blocks.append(block_row)
        
    def draw(self):
        for row in self.blocks:
            for block in row:
                if block[1] == 3:
                    block_col = BLOCK_BLUE
                elif block[1] == 2:
                    block_col = BLOCK_GREEN
                elif block[1] == 1:
                    block_col = BLOCK_RED
                #Draw
                pygame.draw.rect(screen,block_col, block[0])
                pygame.draw.rect(screen,BG, block[0],3)
            
        
class Paddle:
    def __init__(self) -> None:
        self.width = int(WINDOW_SIZE[0]/COLS)
        self.height = 20
        self.x = int((WINDOW_SIZE[0]/2)- (self.width/2))
        self.y = WINDOW_SIZE[1] - (self.height * 2)
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = 0
        
    def move(self, dt):
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed * dt
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < WINDOW_SIZE[0]:
            self.rect.x += self.speed * dt
            self.direction = 1
            

    def draw(self):
        #Draw
        pygame.draw.rect(screen, PADDLE_COLOR, self.rect)
        pygame.draw.rect(screen, PADDLE_OUTLINE, self.rect,3)

class Ball:
    def __init__(self, x, y) -> None:
        self.rad = 10
        self.x = x - self.rad
        self.y = y 
        self.rect = pygame.Rect(x, y, (self.rad * 2), (self.rad * 2))
        self.vx = 4
        self.vy = -4
        self.v_max = 5 # max velocity
        self.game_over = 0
        self.collision_thresh = 5
        
    def update(self, paddle, dt):
        #check collition
        if self.rect.left < 0 or self.rect.right > WINDOW_SIZE[0]:
            self.vx *= -1
        if self.rect.top < 0:
            self.vy *= -1
            
        #game over
        if self.rect.bottom > WINDOW_SIZE[1]:
            self.game_over =-2
        
        #look for collision with paddle
        if self.rect.colliderect(paddle):
            if abs(self.rect.bottom - paddle.rect.top) < self.collision_thresh and self.vy > 0:
                self.vy *= -1
                self.vx += paddle.direction
                if self.vx > self.v_max:
                    self.vx = self.v_max
                elif self.vx < 0 and self.vx < -self.v_max:
                    self.vx = -self.v_max
            else:
                self.vx *= -1
        
        
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt
        
        return self.game_over

    def draw(self):
        #Draw
        x = self.rect.x + self.rad
        y = self.rect.y + self.rad
        pygame.draw.circle(screen, PADDLE_COLOR, (x,y),self.rad)
        pygame.draw.circle(screen, PADDLE_OUTLINE, (x,y),self.rad,3)

class App:
    def __init__(self) -> None:
       self.wall = Wall()
       self.wall.create_wall()
       self.paddle = Paddle()
       self.ball = Ball(self.paddle.x +(self.paddle.width // 2), self.paddle.y - self.paddle.height)
       
    def draw(self):
        self.wall.draw()
        self.paddle.draw()
        self.ball.draw()
    
    def update(self, dt):
        self.paddle.move(dt)
        self.ball.update(self.paddle,dt)
    
    def run(self):
        while True:
            #DELTA TIME
            dt = clock.tick(FPS) * .001 * FPS
            #INPUT EVENT
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                                    
                    
            screen.fill(BG)
            
            # Update
            self.update(dt)

            # Draw
            self.draw()
            
            pygame.display.flip()
        



if __name__ == "__main__":
    App().run()
