import os
import pygame

TITLE = "My pygame Window"
FPS = 60

# Windows Size
WINDOW_SIZE = (600, 450)

# Colors
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (50, 230, 40)
BLACK = (0, 0, 0)

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
