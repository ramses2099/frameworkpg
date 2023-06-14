import pygame
import constants

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
        
        if typecomp.typename == constants.ENTITY_TYPE[1]:
           p_x, p_y = int(trancomp.rect.x), int(trancomp.rect.y)
           screen.blit(constants.IMG_ELEMENT_PURPLE, (p_x, p_y))

        if typecomp.typename == constants.ENTITY_TYPE[0]:
            p_x, p_y = int(trancomp.rect.x), int(trancomp.rect.y)
            screen.blit(constants.IMG_PLAYER_BLUE, (p_x, p_y))

        if typecomp.typename == constants.ENTITY_TYPE[2]:
            p_x, p_y = int(trancomp.rect.x), int(trancomp.rect.y)
            screen.blit(constants.IMG_BALL_BLUE, (p_x, p_y))
        
        if typecomp.typename == constants.ENTITY_TYPE[3]:
            p_x, p_y = int(trancomp.rect.x), int(trancomp.rect.y)
            screen.blit(constants.IMG_BALL_GREY, (p_x, p_y))


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
        bounds = pygame.display.get_surface().get_rect()
        
        if typecomp.typename == constants.ENTITY_TYPE[0]:
            pass
        # ELEMENT
        if typecomp.typename == constants.ENTITY_TYPE[1]:
            # Motion
            movcomp.vx += movcomp.ax * dircomp.dx
            movcomp.vy += movcomp.ay * dircomp.dy

            trancomp.rect.x += movcomp.vx
            trancomp.rect.y += movcomp.vy
            
            # Bounds
            if trancomp.rect.x <= bounds.left or trancomp.rect.x + trancomp.rect.w >= bounds.right:
                dircomp.dx *= -1 
            if trancomp.rect.y <= bounds.top or trancomp.rect.y + trancomp.rect.h >= bounds.bottom:
                dircomp.dy *= -1

                
        # BALL  
        if typecomp.typename == constants.ENTITY_TYPE[2]:
            # Motion
            movcomp.vx += movcomp.ax * dircomp.dx
            movcomp.vy += movcomp.ay * dircomp.dy
            
            trancomp.rect.x += movcomp.vx
            trancomp.rect.y += movcomp.vy
            
            # Bounds
            if trancomp.rect.x <= bounds.left or trancomp.rect.x + trancomp.rect.w >= bounds.right:
                dircomp.dx *= -1 
            if trancomp.rect.y <= bounds.top or trancomp.rect.y + trancomp.rect.h >= bounds.bottom:
                dircomp.dy *= -1
            
        if typecomp.typename == constants.ENTITY_TYPE[3]:
            # Motion
            movcomp.vx += movcomp.ax * dircomp.dx
            movcomp.vy += movcomp.ay * dircomp.dy
           
            trancomp.rect.x += movcomp.vx
            trancomp.rect.y += movcomp.vy
            
            # Bounds
            if trancomp.rect.x <= bounds.left or trancomp.rect.x + trancomp.rect.w >= bounds.right:
                movcomp.vy *= -1 
            if trancomp.rect.y <= bounds.top or trancomp.rect.y + trancomp.rect.h >= bounds.bottom:
                movcomp.vy *= -1
                
            
            
            
class CollisionSystem(System):
    def __init__(self, pentity) -> None:
        super().__init__()
        self.pentity = pentity

    def check(self, entity):
        collcomp = entity.getcomponent("Collision")
        return collcomp is not None

    def update(self, entity, screen, event):
        typecomp = entity.getcomponent("Type")
    
        if typecomp.typename == constants.ENTITY_TYPE[1]:
            pass
        if typecomp.typename == constants.ENTITY_TYPE[0]:
            pass
        if typecomp.typename == constants.ENTITY_TYPE[2]:
            pass
        if typecomp.typename == constants.ENTITY_TYPE[3]:
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
    
        if typecomp.typename == constants.ENTITY_TYPE[0]:
           pygame.draw.rect(screen,constants.BLUE, trancomp.rect, 3)
        else:
           pygame.draw.rect(screen,constants.RED, trancomp.rect, 3)

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

        if typecomp.typename == constants.ENTITY_TYPE[0]:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if trancomp.rect.x <= self.window_size[0] - (trancomp.rect.w * 2):
                    dircomp.direct = 1
                    trancomp.rect.x += movcomp.vx * dircomp.direct
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if trancomp.rect.x >= trancomp.rect.w:
                    dircomp.direct = -1
                    trancomp.rect.x += movcomp.vx * dircomp.direct
