import pygame, sys, os.path
from pygame.locals import *
import engine
import factory

WINDOW_SIZE = (600, 450)
TITLE = "My pygame Window"
FPS = 60
BLACK = (0, 0, 0)


# ECS
entities = []


# player_rect = player_image.get_rect()
player = factory.makePlayer()
entities.append(player)

element = factory.makeElement(50, 50)
entities.append(element)

element1 = factory.makeElement(350, 350)
entities.append(element1)

ballblue = factory.makeBall()
ballblue.removecomponent("Movible")
entities.append(ballblue)

ballgrey = factory.makeBall(30, 250)
entities.append(ballgrey)

item = factory.makeItem(45, 54)
# item.printcomponents()


drawsystem = engine.DrawSystem()
movementsystem = engine.MovementSystem()
inputsystem = engine.InputSystem(window_size=WINDOW_SIZE)


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
            # input system
            inputsystem.updates(entities, screen=None, event=event)

        screen.fill(BLACK)

        # update system
        movementsystem.updates(entities, screen=None, event=None)

        # draw system
        drawsystem.updates(entities, screen, event=None)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
