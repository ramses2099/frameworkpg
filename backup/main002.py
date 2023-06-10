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

# ECS
entities = []

# Entitys
player = pygame.Rect(350,400, 50,50)


for i in range(10):
   entities.append(pygame.Rect(random.randint(0,600), random.randint(0,450), 50,50))

SPEED = 5


def main():
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player.x -= 15
                if event.key == K_RIGHT:
                    player.x += 15
                if event.key == K_UP:
                    player.y -= 15
                if event.key == K_DOWN:
                    player.y += 15
           
        screen.fill(BLACK)
        
        # Calculate the distance between the enemy and the player
        # # follow targe
        # dx = player.x - enemy.x
        # dy = player.y - enemy.y
        # dist =(dx ** 2 + dy ** 2) ** 0.5
          
        # if dist != 0:
        #     enemy.x += SPEED * dx / dist
        #     enemy.y += SPEED * dy / dist
        
        for enemy in entities:
            # Random direction
            dir = random.choice(["LEFT","RIGHT","UP","DOWN"])
            if dir == "LEFT":
                enemy.x -= SPEED
            elif dir == "RIGHT":
                enemy.x += SPEED
            elif dir == "UP":
                enemy.y -= SPEED
            elif dir == "DOWN":
                enemy.y += SPEED
                
            if player.colliderect(enemy):
                print("Die")
        
        # Draw        
        pygame.draw.rect(screen, BLUE, player)
        
        for enemy in entities:
            pygame.draw.rect(screen, RED, enemy)
     
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
