import pygame, sys
from pygame.locals import *
import constants
import ecs
import factory

# ECS
entities = []

# player_rect = player_image.get_rect()
# player = factory.makePlayer()
# player.addcomponent(engine.Debug())
# entities.append(player)

# element = factory.makeElement(50, 50)
# entities.append(element)

element1 = factory.makeElement(350, 50)
# element1.addcomponent(engine.Direction())
# element1.addcomponent(engine.Debug())
entities.append(element1)

# ballblue = factory.makeBall()
# ballblue.removecomponent("Motion")
# ballblue.addcomponent(engine.Direction())
# ballblue.addcomponent(engine.Debug())
# entities.append(ballblue)

# ballgrey = factory.makeBall(30, 250)
# ballgrey.addcomponent(engine.Direction())
# ballgrey.addcomponent(engine.Debug())
# entities.append(ballgrey)

# # Object Test
# item = factory.makeItem(45, 54)
# item.addcomponent(engine.Debug())
# item.removecomponent("Motion")
# entities.append(item)
# # item.printcomponents()

# System
drawsystem = ecs.DrawSystem()
# movementsystem = engine.MovementSystem()
# inputsystem = engine.InputSystem(window_size=WINDOW_SIZE)
# collisionsystem = engine.CollisionSystem(player)
# debugsystem = engine.DebugSystem()

def main():
    pygame.init()
    pygame.display.set_caption(constants.TITLE)
    screen = pygame.display.set_mode(constants.WINDOW_SIZE)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # input system
            # inputsystem.updates(entities, screen=None, event=event)

        screen.fill(constants.BLACK)
        
        # update system
        # movementsystem.updates(entities, screen=None, event=None)
        
        # update collision system
        # collisionsystem.updates(entities, screen=None, event=None)
        
        # update debugs system
        # debugsystem.updates(entities, screen, event=None)

        # draw system
        drawsystem.updates(entities, screen, event=None)

        pygame.display.flip()
        clock.tick(constants.FPS)


if __name__ == "__main__":
    main()
