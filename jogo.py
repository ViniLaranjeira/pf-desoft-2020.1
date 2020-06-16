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
# define a classe do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self, blocks):
        pygame.sprite.Sprite.__init__(self)
        playersheet =    [pygame.image.load(path.join(img_dir, "hero_idle0.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_idle1.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_idle2.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_idle3.png")).convert(),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_idle0.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_idle1.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_idle2.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_idle3.png")).convert(), True, False),
                          pygame.image.load(path.join(img_dir, "hero_run0.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_run1.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_run2.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_run3.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_run4.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_run5.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_run6.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_run7.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_run8.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_run9.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_run10.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_run11.png")).convert(),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_run0.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_run1.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_run2.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_run3.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_run4.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_run5.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_run6.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_run7.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_run8.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_run9.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_run10.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_run11.png")).convert(), True, False),
                          pygame.image.load(path.join(img_dir, "hero_attack0.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_attack1.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_attack2.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_attack3.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_attack4.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_attack5.png")).convert(),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_attack0.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_attack1.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_attack2.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_attack3.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_attack4.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_attack5.png")).convert(), True, False),
                          pygame.image.load(path.join(img_dir, "hero_jump0.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_jump1.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_jump2.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_jump3.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_jump4.png")).convert(),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_jump0.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_jump1.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_jump2.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_jump3.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_jump4.png")).convert(), True, False),
                          pygame.image.load(path.join(img_dir, "hero_slash0.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_slash1.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_slash2.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_slash3.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_slash4.png")).convert(),
                          pygame.image.load(path.join(img_dir, "hero_slash5.png")).convert(),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_slash0.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_slash1.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_slash2.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_slash3.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_slash4.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "hero_slash5.png")).convert(), True, False)] 
                          
        i = 0
        while i < len(playersheet):
            if i < 8:
                playersheet[i] = pygame.transform.scale(playersheet[i],(95,120))
                self.image = playersheet[i]
                self.image.set_colorkey(WHITE)
            elif i < 32:
                playersheet[i] = pygame.transform.scale(playersheet[i],(165,120))
                self.image = playersheet[i]
                self.image.set_colorkey(WHITE)
            elif i <44:
                playersheet[i] = pygame.transform.scale(playersheet[i],(240,120))
                self.image = playersheet[i]
                self.image.set_colorkey(WHITE)
            elif i < 54:
                playersheet[i] = pygame.transform.scale(playersheet[i],(152,192))
                self.image = playersheet[i]
                self.image.set_colorkey(WHITE)
            else:
                playersheet[i] = pygame.transform.scale(playersheet[i],(222,210))
                self.image = playersheet[i]
                self.image.set_colorkey(WHITE)
            i += 1
            
        self.animations = {IDLE:playersheet[0:4],
                            IDLE_LEFT:playersheet[4:8],
                            WALK:playersheet[8:20],
                            WALK_LEFT:playersheet[20:32],
                            ATTACK:playersheet[32:38],
                            ATTACK_LEFT:playersheet[38:44],
                            JUMP:playersheet[44:49],
                            JUMP_LEFT:playersheet[49:54],
                            FALL:playersheet[48:49],
                            FALL_LEFT:playersheet[53:54],
                            SLASH:playersheet[54:60],
                            SLASH_LEFT:playersheet[60:66]} 
        
        self.state = IDLE
        self.animation = self.animations[self.state]
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.fire = False
        self.blocks = blocks
        
        self.rect.x = 0
        self.rect.bottom = HEIGHT
        self.speedx = 0
        self.speedy = 1
        
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 100
        
    def update(self):
        
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            self.animation = self.animations[self.state]
            if self.frame >= len(self.animation):
                self.frame = 0
            center = self.rect.center
            self.image = self.animation[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.mask = pygame.mask.from_surface(self.image)
    
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for collision in collisions:
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                if self.state in AIR_R:
                    self.state = IDLE
                elif self.state in AIR_L:
                    self.state = IDLE_LEFT
                self.speedy = 0
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                if self.state in AIR_R:
                    self.state = IDLE
                elif self.state in AIR_L:
                    self.state = IDLE_LEFT
                self.speedy = 0   
            
        if self.speedy != 0:
            self.speedy += GRAVITY
        self.rect.y += self.speedy
        
        keys = pygame.key.get_pressed() 
        if self.state == IDLE or self.state == IDLE_LEFT:  
            if keys[pygame.K_d] == True and keys[pygame.K_a] == False:
                self.state = WALK
            elif keys[pygame.K_a] == True and keys[pygame.K_d] == False:
                self.state = WALK_LEFT
        if keys[pygame.K_p] == False and self.frame == 5:
            if self.state == ATTACK or self.state == SLASH:
                self.state = IDLE
            elif self.state == ATTACK_LEFT or self.state == SLASH_LEFT:
                self.state = IDLE_LEFT
            self.fire = False
        if self.fire == True and self.state == IDLE:
            self.state = ATTACK
        elif self.fire == True and self.state == IDLE_LEFT:
            self.state = ATTACK_LEFT
        elif self.fire == True and self.state == WALK:
            self.state = SLASH
        elif self.fire == True and self.state == WALK_LEFT:
            self.state = SLASH_LEFT
            
        if self.speedy < 0 and self.state in POS:
            self.state = JUMP
        elif self.speedy > 0 and self.state in POS:
            self.state = FALL
        elif self.speedy < 0 and self.state in NEG:
            self.state = JUMP_LEFT 
        elif self.speedy > 0 and self.state in NEG:
            self.state = FALL_LEFT
            
        self.rect.x += self.speedx
        
    def jump(self):
        
        if self.state in POS and self.state not in AIR:
            self.speedy -= JUMP_SIZE
            self.state = JUMP
        elif self.state in POS and self.state not in AIR:
            self.speedy -= JUMP_SIZE
            self.state = JUMP_LEFT
        self.speedy += GRAVITY
        self.rect.y += self.speedy
