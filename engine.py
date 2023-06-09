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
        spcomp = entity.getcomponent("Sprite")
        return spcomp is not None

    def update(self, entity, screen, event):
        typecomp = entity.getcomponent("Type")
        trancomp = entity.getcomponent("Transform")

        if typecomp.typename == factory.ENTITY_TYPE[1]:
            x, y = trancomp.rect.x, trancomp.rect.y
            screen.blit(factory.IMG_ELEMENT_PURPLE, (x, y))

        if typecomp.typename == factory.ENTITY_TYPE[0]:
            p_x, p_y = trancomp.rect.x, trancomp.rect.y
            screen.blit(factory.IMG_PLAYER_BLUE, (p_x, p_y))

        if typecomp.typename == factory.ENTITY_TYPE[2]:
            p_x, p_y = trancomp.rect.x, trancomp.rect.y
            screen.blit(factory.IMG_BALL_BLUE, (p_x, p_y))


class MovementSystem(System):
    def __init__(self) -> None:
        super().__init__()

    def check(self, entity):
        movcomp = entity.getcomponent("Motion")
        return movcomp is not None

    def update(self, entity, screen, event):
        typecomp = entity.getcomponent("Type")
        trancomp = entity.getcomponent("Transform")
        movcomp = entity.getcomponent("Motion")

        if typecomp.typename == factory.ENTITY_TYPE[1]:
            pass
        if typecomp.typename == factory.ENTITY_TYPE[0]:
            pass
        if typecomp.typename == factory.ENTITY_TYPE[2]:
            movcomp.vx += 4
            trancomp.rect.x = movcomp.vx


class InputSystem(System):
    def __init__(self, window_size) -> None:
        super().__init__()
        self.window_size = window_size

    def check(self, entity):
        inputcomp = entity.getcomponent("Input")
        return inputcomp is not None

    def update(self, entity, screen, event):
        typecomp = entity.getcomponent("Type")
        trancomp = entity.getcomponent("Transform")
        movcomp = entity.getcomponent("Motion")
        dircomp = entity.getcomponent("Direction")

        if typecomp.typename == factory.ENTITY_TYPE[0]:
            if event.type == KEYDOWN and event.key == K_RIGHT:
                if trancomp.rect.x <= self.window_size[0] - (trancomp.rect.w * 2):
                    dircomp.direction = 1
                    trancomp.rect.x += movcomp.vx * dircomp.direction
            if event.type == KEYDOWN and event.key == K_LEFT:
                if trancomp.rect.x >= trancomp.rect.w:
                    dircomp.direction = -1
                    trancomp.rect.x += movcomp.vx * dircomp.direction


class Direction:
    def __init__(self, direction=1):
        self.name = "Direction"
        self.direction = direction

# Has a Position in the world
class Transform:
    def __init__(self, x, y, w, h):
        self.name = "Transform"
        self.rect = pygame.Rect(x, y, w, h)

# Can move(velocity, acceleration)
class Motion:
    def __init__(self, vx, vy, ax =0, ay=0):
        self.name = "Motion"
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay


class Type:
    def __init__(self, typename) -> None:
        self.name = "Type"
        self.typename = typename

# Should display on screen
class Sprite:
    def __init__(self) -> None:
        self.name = "Sprite"
        self.draw = True

# Collides with other entity
class Collision:
    def __init__(self) -> None:
        self.name = "Collision"

# Life 
class Life:
    def __init__(self) -> None:
        self.name = "Life"
        self.currentlife = 3
        self.maxlife = 5


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
