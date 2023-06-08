import pygame
from pygame.locals import *
import uuid
import factory


class System:
    def __init__(self) -> None:
        pass

    def check(self, entity):
        return True

    def updates(self, entities, screen, event):
        for entity in entities:
            if self.check(entity):
                self.update(entity, screen, event)

    def update(self, entity, screen, event):
        pass


class DrawSystem(System):
    def __init__(self) -> None:
        super().__init__()

    def check(self, entity):
        drawcomp = entity.getcomponent("Drawable")
        return drawcomp is not None

    def update(self, entity, screen, event):
        typecomp = entity.getcomponent("Type")
        poscomp = entity.getcomponent("Position")

        if typecomp.typename == factory.ENTITY_TYPE[1]:
            x, y = poscomp.rect.x, poscomp.rect.y
            screen.blit(factory.IMG_ELEMENT_PURPLE, (x, y))

        if typecomp.typename == factory.ENTITY_TYPE[0]:
            p_x, p_y = poscomp.rect.x, poscomp.rect.y
            screen.blit(factory.IMG_PLAYER_BLUE, (p_x, p_y))

        if typecomp.typename == factory.ENTITY_TYPE[2]:
            p_x, p_y = poscomp.rect.x, poscomp.rect.y
            screen.blit(factory.IMG_BALL_BLUE, (p_x, p_y))


class MovementSystem(System):
    def __init__(self) -> None:
        super().__init__()

    def check(self, entity):
        movcomp = entity.getcomponent("Movible")
        return movcomp is not None

    def update(self, entity, screen, event):
        typecomp = entity.getcomponent("Type")
        poscomp = entity.getcomponent("Position")
        velcomp = entity.getcomponent("Velocity")

        if typecomp.typename == factory.ENTITY_TYPE[1]:
            pass
        if typecomp.typename == factory.ENTITY_TYPE[0]:
            pass
        if typecomp.typename == factory.ENTITY_TYPE[2]:
            velcomp.vx += 4
            poscomp.rect.x = velcomp.vx


class InputSystem(System):
    def __init__(self, window_size) -> None:
        super().__init__()
        self.window_size = window_size

    def check(self, entity):
        inputcomp = entity.getcomponent("Input")
        return inputcomp is not None

    def update(self, entity, screen, event):
        typecomp = entity.getcomponent("Type")
        poscomp = entity.getcomponent("Position")
        velcomp = entity.getcomponent("Velocity")
        dircomp = entity.getcomponent("Direction")

        if typecomp.typename == factory.ENTITY_TYPE[0]:
            if event.type == KEYDOWN and event.key == K_RIGHT:
                if poscomp.rect.x <= self.window_size[0] - (poscomp.rect.w * 2):
                    dircomp.direction = 1
                    poscomp.rect.x += velcomp.vx * dircomp.direction
            if event.type == KEYDOWN and event.key == K_LEFT:
                if poscomp.rect.x >= poscomp.rect.w:
                    dircomp.direction = -1
                    poscomp.rect.x += velcomp.vx * dircomp.direction


class Direction:
    def __init__(self, direction=1):
        self.name = "Direction"
        self.direction = direction


class Position:
    def __init__(self, x, y, w, h):
        self.name = "Position"
        self.rect = pygame.Rect(x, y, w, h)


class Velocity:
    def __init__(self, vx, vy):
        self.name = "Velocity"
        self.vx = vx
        self.vy = vy


class Type:
    def __init__(self, typename) -> None:
        self.name = "Type"
        self.typename = typename


class Drawable:
    def __init__(self) -> None:
        self.name = "Drawable"
        self.draw = True


class Movible:
    def __init__(self) -> None:
        self.name = "Movible"
        self.move = True


class Collectable:
    def __init__(self) -> None:
        self.name = "Collectable"
        self.collect = True


class Input:
    def __init__(self) -> None:
        self.name = "Input"
        self.collect = True


class Entity:
    def __init__(self) -> None:
        self.id = str(uuid.uuid4().fields[-1])[:5]
        self.components = {}

    def addcomponent(self, value):
        name = value.name
        self.components[name] = value

    def getcomponents(self):
        return self.components

    def getcomponent(self, name):
        return self.components.get(name)

    def removecomponent(self, name):
        self.components.pop(name)

    def getallkeys(self):
        return self.components.keys()

    def existscomponent(self, name):
        return self.components.setdefault(name)

    def printcomponents(self):
        comptype = self.getcomponent("Type")
        print(f"entity id {self.id}")
        if comptype is not None:
            print(f"entity type {comptype.typename}")
        for name in self.getallkeys():
            print(f"component name {name}")
