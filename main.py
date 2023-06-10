import pygame, sys, os.path
from pygame.locals import *
import random
from player import Player


WINDOW_SIZE = (600, 450)
TITLE = "My pygame Window"
FPS = 60
BLACK = (0, 0, 0)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (50, 230, 40)



# ECS
entities = []
player = Player(50,10, 25,25)
tiles= []

def main():
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    
    # rect
    rect_bounds = pygame.display.get_surface().get_rect()
    
    # groun
    rect_ground = pygame.rect.Rect(0,440,600,20)
    tiles.append(rect_ground)
    
    while True:
        #DELTA TIME
        dt = clock.tick(FPS) * .001 * FPS
        #INPUT EVENT
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==KEYDOWN:
                if event.key == K_LEFT:
                    player.LEFT_KEY = True
                elif event.key == K_RIGHT:
                    player.RIGHT_KEY = True
                elif event.key == K_SPACE:
                    player.jump()
                    
            if event.type ==KEYUP:
                if event.key == K_LEFT:
                    player.LEFT_KEY = False
                elif event.key == K_RIGHT:
                    player.RIGHT_KEY = False
                elif event.key == K_SPACE:
                    if player.is_jumping:
                        player.velocity.y *= .25
                        player.is_jumping = False
                    
                
        screen.fill(BLACK)
        
        # Update
        player.update(dt,tiles)
        
    


        # Draw 
        pygame.draw.rect(screen,BLUE,rect_bounds,5)
        
        # ground
        pygame.draw.rect(screen,RED,rect_ground)
        
        player.draw(screen)
        
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
