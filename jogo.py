import pygame, math, random
from os import path

# Estabelece imports
img_dir = path.join(path.dirname(__file__), 'imagens')
snd_dir = path.join(path.dirname(__file__), 'sons')

# Define tela
WIDTH = 1300
HEIGHT = 700
FPS = 60 
GRAVITY = 0.2
JUMP_SIZE = 10
TILE_SIZE = 40

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MANA = (49,70,176)

# Ações
IDLE = 0
IDLE_LEFT = 1
WALK = 2
WALK_LEFT = 3
ATTACK = 4
ATTACK_LEFT = 5
JUMP = 6
JUMP_LEFT = 7
FALL = 8
FALL_LEFT = 9
SLASH = 10
SLASH_LEFT = 11
POS = [IDLE, WALK, ATTACK, JUMP]
NEG = [IDLE_LEFT, WALK_LEFT, ATTACK_LEFT, JUMP_LEFT]
AIR = [JUMP, JUMP_LEFT, FALL, FALL_LEFT]
AIR_R = [JUMP,FALL]
AIR_L = [JUMP_LEFT,FALL_LEFT]
BREATH = 0
BREATH_LEFT = 1
FIRE = 2
FIRE_LEFT = 3
TELEPORT = 4
TELEPORT_LEFT = 5
RUN = 0
RUN_LEFT = 1

ARMED = 0
EXPLODE = 1

null = 0
block = 1

map1 = [
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
# define a classe dos blocos
class Tile(pygame.sprite.Sprite):
    def __init__(self, row, column):
        pygame.sprite.Sprite.__init__(self)
        tile_img = pygame.image.load(path.join(img_dir, "tile.png")).convert()
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))
        self.image = tile_img
        self.rect = self.image.get_rect()

        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row
