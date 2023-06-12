import pygame, sys
from pygame.locals import *
from body import Body


WINDOW_SIZE = (600, 450)
TITLE = "My pygame Window"
FPS = 60
BLACK = (0, 0, 0)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (50, 230, 40)

# Bodies Array
bodies = []
body = Body(25,25,30,30, 10)
body.addIstant(0,body.mass*9.81)
body.addIstant(5,-5)
bodies.append(body)

def main():
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    
   
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
        for body in bodies:
            body.update(dt) 

        # Draw
        for body in bodies:
            body.draw(screen) 
      
        
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
