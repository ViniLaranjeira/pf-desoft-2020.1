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
          
#Classe monstro
class Beast(pygame.sprite.Sprite):
    
    def __init__(self, blocks, player):
        
        pygame.sprite.Sprite.__init__(self)
        
        beastsheet =    [pygame.image.load(path.join(img_dir, "beast_idle0.png")).convert(),
                          pygame.image.load(path.join(img_dir, "beast_idle1.png")).convert(),
                          pygame.image.load(path.join(img_dir, "beast_idle2.png")).convert(),
                          pygame.image.load(path.join(img_dir, "beast_idle3.png")).convert(),
                          pygame.image.load(path.join(img_dir, "beast_idle4.png")).convert(),
                          pygame.image.load(path.join(img_dir, "beast_idle5.png")).convert(),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_idle0.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_idle1.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_idle2.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_idle3.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_idle4.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_idle5.png")).convert(), True, False),
                          pygame.image.load(path.join(img_dir, "beast_teleport0.png")).convert(),
                          pygame.image.load(path.join(img_dir, "beast_teleport1.png")).convert(),
                          pygame.image.load(path.join(img_dir, "beast_teleport2.png")).convert(),
                          pygame.image.load(path.join(img_dir, "beast_teleport3.png")).convert(),
                          pygame.image.load(path.join(img_dir, "beast_teleport4.png")).convert(),
                          pygame.image.load(path.join(img_dir, "beast_teleport5.png")).convert(),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_teleport0.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_teleport1.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_teleport2.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_teleport3.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_teleport4.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_teleport5.png")).convert(), True, False),
                          pygame.image.load(path.join(img_dir, "beast_fire0.png")).convert(),
                          pygame.image.load(path.join(img_dir, "beast_fire1.png")).convert(),
                          pygame.image.load(path.join(img_dir, "beast_fire2.png")).convert(),
                          pygame.image.load(path.join(img_dir, "beast_fire3.png")).convert(),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_fire0.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_fire1.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_fire2.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "beast_fire3.png")).convert(), True, False)] 
                          
        i = 0
        while i < len(beastsheet):
            if i < 12:
                beastsheet[i] = pygame.transform.scale(beastsheet[i],(330,330))
                self.image = beastsheet[i]
                self.image.set_colorkey(WHITE)
            elif i < 24:
                beastsheet[i] = pygame.transform.scale(beastsheet[i],(330,700))
                self.image = beastsheet[i]
                self.image.set_colorkey(WHITE)
            else:
                beastsheet[i] = pygame.transform.scale(beastsheet[i],(400,330))
                self.image = beastsheet[i]
                self.image.set_colorkey(WHITE)
            i += 1
            
        self.animations = {BREATH_LEFT:beastsheet[0:6],BREATH:beastsheet[6:12],
                           TELEPORT_LEFT:beastsheet[12:18],TELEPORT:beastsheet[18:24],
                           FIRE_LEFT:beastsheet[24:28],FIRE:beastsheet[28:32]} 
        self.rect = self.image.get_rect()
        
        # Define estado 
        self.state = BREATH_LEFT
        self.animation = self.animations[self.state]
        self.frame = 0
        self.vida = 100
        self.move = False
        self.attacked = False
        self.teleported = False
        self.fire = False
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.blocks = blocks
        self.rect.bottom = HEIGHT - 100
        self.rect.centerx = WIDTH/2 + 300
        self.speedy = 0
        self.speedx = 0
        self.last_fire = pygame.time.get_ticks()
        self.last_teleport = pygame.time.get_ticks()
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 100
        
    def update(self):
        
        now_teleport = pygame.time.get_ticks()
        elapsed_teleport = now_teleport - self.last_teleport
        if elapsed_teleport > random.randint(12000,18000):
            self.last_fire = now_teleport
            self.last_teleport = now_teleport
            self.teleported = True
            self.state = TELEPORT_LEFT
            fire_sound.play()
            
        now_fire = pygame.time.get_ticks()
        elapsed_fire = now_fire - self.last_fire
        if elapsed_fire > random.randint(4000,8000):
            self.last_fire = now_fire
            self.fire = True
            self.state = FIRE_LEFT
            fireball_sound.play()
        
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
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.mask = pygame.mask.from_surface(self.image)
            
        if self.state == TELEPORT_LEFT and self.frame == 5 and self.teleported == True:
            self.rect.x = random.randint(0, WIDTH - 165)
            self.state = IDLE_LEFT
            self.teleported = False
            
        if self.state == FIRE_LEFT and self.frame == 3 and self.fire == True:
            self.state = IDLE_LEFT
            self.fire = False
            
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for collision in collisions:
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                self.speedy = 0
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                self.speedy = 0   
                
        if self.move == False:
            self.speedx = 0
        if self.move == True:
            if self.attacked == False:
                knife_miss.stop()
                self.vida -= 10
                knife_hit.play()
                self.attacked = True
                self.rect.x += 10
                self.move = False
                
        self.speedy += GRAVITY
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.vida <= 0:
            self.kill()

# Define a classe cavalo
class Horse(pygame.sprite.Sprite):

    def __init__(self, blocks, player):
        pygame.sprite.Sprite.__init__(self)
        
        horsesheet =    [pygame.image.load(path.join(img_dir, "horse0.png")).convert(),
                          pygame.image.load(path.join(img_dir, "horse1.png")).convert(),
                          pygame.image.load(path.join(img_dir, "horse2.png")).convert(),
                          pygame.image.load(path.join(img_dir, "horse3.png")).convert(),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "horse0.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "horse1.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "horse2.png")).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(path.join(img_dir, "horse3.png")).convert(), True, False)] 
                          
        i = 0
        while i < len(horsesheet):
            horsesheet[i] = pygame.transform.scale(horsesheet[i],(288,192))
            self.image = horsesheet[i]
            self.image.set_colorkey(WHITE)
            i += 1
            
        self.animations = {RUN_LEFT:horsesheet[0:4],RUN:horsesheet[4:8]} 
        self.rect = self.image.get_rect()
        
        if player.state in POS:
            self.state = RUN
            self.speedx = 5
        elif player.state in NEG:
            self.state = RUN_LEFT
            self.speedx = -5
        self.animation = self.animations[self.state]
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.blocks = blocks
        self.rect.bottom = player.rect.bottom
        if self.state == RUN:
            self.rect.centerx = 0
        elif self.state == RUN_LEFT:
            self.rect.centerx = WIDTH
        self.speedy = 0
        
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
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.mask = pygame.mask.from_surface(self.image)
            
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for collision in collisions:
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                self.speedy = 0
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                self.speedy = 0   
        
        self.speedy += GRAVITY
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        
        if self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()
            
def menu(life, mana, screen):
    if life > 50:
        life_color = GREEN
    elif life > 25:
        life_color = YELLOW
    else:
        life_color = RED   
    pygame.draw.rect(screen, life_color, (34, 30, life, 10))
    pygame.draw.rect(screen, MANA, (34, 40, mana, 5))
    lifebar = pygame.transform.scale(pygame.image.load(path.join(img_dir, "lifebar_back.png")).convert() ,(170,44))
    lifebar.set_colorkey(WHITE)
    screen.blit(lifebar, (0,10))
    
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
background = pygame.image.load(path.join(img_dir, 'gothic-castle-preview.png')).convert()
background_rect = background.get_rect()
pygame.display.set_caption("BASE")
clock = pygame.time.Clock()

knife_miss = pygame.mixer.Sound(path.join(snd_dir, 'knife_miss.wav'))
knife_hit = pygame.mixer.Sound(path.join(snd_dir, 'knife_hit.wav'))
horse_noise = pygame.mixer.Sound(path.join(snd_dir, 'horse.wav'))
fire_sound = pygame.mixer.Sound(path.join(snd_dir, 'fire_sound.wav'))
fireball_sound = pygame.mixer.Sound(path.join(snd_dir, 'fireball_sound.wav'))
#loop principal
def game_screen(screen):
    
    running = True
    life = 124
    mana = 124
    pygame.mixer.music.load(path.join(snd_dir, 'Full of memories.ogg'))
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play(loops=-1)
    row = len(map1)
    column = len(map1[0])
    blocks = pygame.sprite.Group()
    player = Player(blocks)
    beast = Beast(blocks, player)
    horses = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(beast)
    all_sprites.add(player)
    
    for row in range(len(map1)):
        for column in range(len(map1[row])):
            tile_type = map1[row][column]
            if tile_type == block:
                tile = Tile(row, column)
                all_sprites.add(tile)
                blocks.add(tile)
            
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:       
                if event.key == pygame.K_q:
                    running = False
                    
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d and player.state != ATTACK and player.state != ATTACK_LEFT:
                        player.speedx = 2
                        player.state = WALK
                    elif event.key == pygame.K_a and player.state != ATTACK and player.state != ATTACK_LEFT:
                        player.speedx = -2
                        player.state = WALK_LEFT
                    if event.key == pygame.K_p and player.state in POS:
                        knife_miss.stop()
                        player.fire = True
                        knife_miss.play()
                    elif event.key == pygame.K_p and player.state in NEG:
                        knife_miss.stop()
                        player.fire = True 
                        knife_miss.play()               
                    if event.key == pygame.K_w:               
                        player.jump()
                    if event.key == pygame.K_o and len(horses) < 1:   
                        if mana >= 50:
                            mana -= 50
                            horse_noise.stop()
                            horse = Horse(blocks, player)              
                            all_sprites.add(horse)
                            horses.add(horse)
                            horse_noise.play()
                            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.speedx = 0                    
                    player.state = IDLE_LEFT
                elif event.key == pygame.K_d:
                    player.speedx = 0                    
                    player.state = IDLE

        col = pygame.sprite.collide_mask(player, beast)
        if col != None:
            for c in col:
                if player.state == ATTACK and player.frame == 2 or player.state == SLASH and player.frame == 4:
                    beast.move = True
                elif player.state == ATTACK and player.frame > 2 or player.state == SLASH and player.frame > 4:
                    beast.move = False
                    beast.attacked = False
                print(beast.vida)
            
        hits = pygame.sprite.spritecollide(beast, horses, False, pygame.sprite.collide_mask)
        for horse in hits:
            beast.move = True
                
        all_sprites.update()
        screen.fill(WHITE)
        screen.blit(background, background_rect)
        menu(life, mana, screen)
        all_sprites.draw(screen)
        pygame.display.flip()
try:
    game_screen(screen)        
finally:
    pygame.quit()
