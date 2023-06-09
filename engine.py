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
        
        if typecomp.typename == factory.ENTITY_TYPE[3]:
            p_x, p_y = trancomp.rect.x, trancomp.rect.y
            screen.blit(factory.IMG_BALL_GREY, (p_x, p_y))


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
        dircomp = entity.getcomponent("Direction")

        if typecomp.typename == factory.ENTITY_TYPE[0]:
            pass
        # ELEMENT
        if typecomp.typename == factory.ENTITY_TYPE[1]:
            bounds = pygame.display.get_surface().get_rect()
            # Motion            
            trancomp.rect.y += dircomp.dir * movcomp.vy
           
            if trancomp.rect.y <= bounds.top or trancomp.rect.y + trancomp.rect.h >= bounds.bottom:
                dircomp.dir *= -1
                
        # BALL  
        if typecomp.typename == factory.ENTITY_TYPE[2]:
            bounds = pygame.display.get_surface().get_rect()
            # Motion
            trancomp.rect.x += dircomp.dir * movcomp.vx            
            trancomp.rect.y += dircomp.dir * movcomp.vy
            
            # Bound
            if trancomp.rect.x <= bounds.lef or trancomp.rect.x + trancomp.rect.w >= bounds.right:
                dircomp.dir *= -1 
            if trancomp.rect.y <= bounds.top or trancomp.rect.y + trancomp.rect.h >= bounds.bottom:
                dircomp.dir *= -1
            
        if typecomp.typename == factory.ENTITY_TYPE[3]:
            # Motion
            # trancomp.rect.x += movcomp.vx
            trancomp.rect.bottom += movcomp.vy
            # movcomp.vx += movcomp.ax
            movcomp.vy += movcomp.ay
            
class CollisionSystem(System):
    def __init__(self, pentity) -> None:
        super().__init__()
        self.pentity = pentity

    def check(self, entity):
        collcomp = entity.getcomponent("Collision")
        return collcomp is not None

    def update(self, entity, screen, event):
        typecomp = entity.getcomponent("Type")
    
        if typecomp.typename == factory.ENTITY_TYPE[1]:
            pass
        if typecomp.typename == factory.ENTITY_TYPE[0]:
            pass
        if typecomp.typename == factory.ENTITY_TYPE[2]:
            pass
        if typecomp.typename == factory.ENTITY_TYPE[3]:
            prect = self.pentity.getcomponent("Transform")
            erect = entity.getcomponent("Transform")
            movcomp = entity.getcomponent("Motion")
            # print
            
            collide = pygame.Rect.colliderect(prect.rect, erect.rect)
            if collide:
                movcomp.ay *= -1


class DebugSystem(System):
    def __init__(self) -> None:
        super().__init__()
        
    def check(self, entity):
        debcomp = entity.getcomponent("Debug")
        return debcomp is not None

    def update(self, entity, screen, event):
        typecomp = entity.getcomponent("Type")
        trancomp = entity.getcomponent("Transform")
    
        if typecomp.typename == factory.ENTITY_TYPE[0]:
           pygame.draw.rect(screen,factory.BLUE, trancomp.rect, 3)
        else:
           pygame.draw.rect(screen,factory.RED, trancomp.rect, 3)



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
    def __init__(self, dire=1):
        self.name = "Direction"
        self.dir = dire

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

# Debug component
class Debug:
    def __init__(self) -> None:
        self.name = "Debug"

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
