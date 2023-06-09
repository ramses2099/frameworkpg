import pygame, sys, os.path
import engine

# Windows Size
WINDOW_SIZE = (600, 450)

# images
PATH_DIR = os.getcwd()
PATH_ASSETS = os.path.join(PATH_DIR, "assets")
PATH_IMG_PADDLE_BLUE = os.path.join(PATH_ASSETS, "paddleblu.png")
PATH_IMG_ELEMENT_PURPLE = os.path.join(PATH_ASSETS, "element_purple_diamond.png")
PATH_IMG_BALL_BLUE = os.path.join(PATH_ASSETS, "ballBlue.png")
PATH_IMG_BALL_GREY = os.path.join(PATH_ASSETS, "ballGrey.png")

# Size images
SIZE_IMG_ELEMENT = (48, 48)
SIZE_IMG_PADDLE = (104, 24)
SIZE_IMG_BALL = (22, 22)

# Gap paddle
GAP_PADDLE = 15

# Paddle start position
PADDLE_START_POS = [
    (WINDOW_SIZE[0] / 2 - SIZE_IMG_PADDLE[0]),
    (WINDOW_SIZE[1] - SIZE_IMG_PADDLE[1] - GAP_PADDLE),
]

BALL_START_POS = [
    (WINDOW_SIZE[0] / 2 - SIZE_IMG_PADDLE[0]),
    15,
]

# Load images
IMG_ELEMENT_PURPLE = pygame.image.load(PATH_IMG_ELEMENT_PURPLE)
IMG_PLAYER_BLUE = pygame.image.load(PATH_IMG_PADDLE_BLUE)
IMG_BALL_BLUE = pygame.image.load(PATH_IMG_BALL_BLUE)
IMG_BALL_GREY = pygame.image.load(PATH_IMG_BALL_GREY)


# Type entity
ENTITY_TYPE = ["PLAYER", "ELEMENT", "BALL", "ITEM"]


# Make Element
def makeElement(x, y):
    entity = engine.Entity()
    entity.addcomponent(engine.Type(typename=ENTITY_TYPE[1]))
    entity.addcomponent(engine.Transform(x, y, SIZE_IMG_ELEMENT[0], SIZE_IMG_ELEMENT[1]))
    entity.addcomponent(engine.Sprite())
    entity.addcomponent(engine.Motion(0, 0))
    return entity


# Make Player
def makePlayer():
    entity = engine.Entity()
    entity.addcomponent(engine.Type(typename=ENTITY_TYPE[0]))
    entity.addcomponent(
        engine.Transform(
            PADDLE_START_POS[0],
            PADDLE_START_POS[1],
            SIZE_IMG_PADDLE[0],
            SIZE_IMG_PADDLE[1],
        )
    )
    entity.addcomponent(engine.Motion(90, 0))
    entity.addcomponent(engine.Sprite())
    entity.addcomponent(engine.Direction())
    entity.addcomponent(engine.Input())
    return entity


# Make Ball
def makeBall(x=0, y=0):
    entity = engine.Entity()
    entity.addcomponent(engine.Type(typename=ENTITY_TYPE[2]))
    if x == 0 and y == 0:
        entity.addcomponent(
            engine.Transform(
                BALL_START_POS[0], BALL_START_POS[1], SIZE_IMG_BALL[0], SIZE_IMG_BALL[1]
            )
        )
    else:
        entity.addcomponent(engine.Transform(x, y, SIZE_IMG_BALL[0], SIZE_IMG_BALL[1]))
    entity.addcomponent(engine.Motion(1, 9))
    entity.addcomponent(engine.Sprite())
    return entity


# Make Item
def makeItem(x, y):
    entity = engine.Entity()
    entity.addcomponent(engine.Type(typename=ENTITY_TYPE[3]))
    entity.addcomponent(engine.Transform(x, y, SIZE_IMG_BALL[0], SIZE_IMG_BALL[1]))
    entity.addcomponent(engine.Motion(1, 9))
    entity.addcomponent(engine.Sprite())
    entity.addcomponent(engine.Collectable())
    return entity
