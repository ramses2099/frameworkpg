import pygame, sys
from pygame.locals import *
from setting import *
from level import Level


WINDOW_SIZE = (600, 450)
TITLE = "My pygame Window"
FPS = 60
BLACK = (0, 0, 0)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (50, 230, 40)


def main():
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    
    # Level system
    level = Level(level_map, screen)
      
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
      
      
        # Draw 
      
        
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
