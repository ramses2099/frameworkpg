import pygame
import constants
import ecs


# Make Element No Motion
def makeElement(x, y):
    entity = ecs.Entity()
    entity.addcomponent(ecs.Type(typename=constants.ENTITY_TYPE[1]))
    entity.addcomponent(ecs.Transform(rect=pygame.rect.Rect(x, y, constants.SIZE_IMG_ELEMENT[0], constants.SIZE_IMG_ELEMENT[1])))
    entity.addcomponent(ecs.Sprite())    
    return entity


# Make Player
def makePlayer():
    entity = ecs.Entity()
    entity.addcomponent(ecs.Type(typename=constants.ENTITY_TYPE[0]))
    entity.addcomponent(
        ecs.Transform(rect=pygame.rect.Rect(
            constants.PADDLE_START_POS[0],
            constants.PADDLE_START_POS[1],
            constants.SIZE_IMG_PADDLE[0],
            constants.SIZE_IMG_PADDLE[1])
        )
    )
    entity.addcomponent(ecs.Motion(90, 0))
    entity.addcomponent(ecs.Sprite())
    entity.addcomponent(ecs.Direction())
    entity.addcomponent(ecs.Input())
    return entity


# Make Ball
def makeBall(x=0, y=0):
    entity = ecs.Entity()
    entity.addcomponent(ecs.Type(typename=constants.ENTITY_TYPE[2]))
    if x == 0 and y == 0:
        entity.addcomponent(
            ecs.Transform(
                rect=pygame.rect.Rect(constants.BALL_START_POS[0], constants.BALL_START_POS[1], constants.SIZE_IMG_BALL[0], constants.SIZE_IMG_BALL[1])
            )
        )
    else:
        entity.addcomponent(ecs.Transform(x, y, constants.SIZE_IMG_BALL[0], constants.SIZE_IMG_BALL[1]))
    entity.addcomponent(ecs.Motion(1, 9))
    entity.addcomponent(ecs.Sprite())
    return entity


# Make Item
def makeItem(x, y):
    entity = ecs.Entity()
    entity.addcomponent(ecs.Type(typename=constants.ENTITY_TYPE[3]))
    entity.addcomponent(ecs.Transform(rect=pygame.rect.Rect(x, y, constants.SIZE_IMG_BALL[0], constants.SIZE_IMG_BALL[1])))
    entity.addcomponent(ecs.Motion(0, 1, 0,0.5))
    entity.addcomponent(ecs.Direction())
    entity.addcomponent(ecs.Sprite())
    return entity
