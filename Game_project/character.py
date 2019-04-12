import pygame
import random
import globalvar
from pygame.sprite import Group
from pygame.sprite import Sprite
class char():
    def __init__(self,screen,who,location):
        self.screen = screen
        self.image = pygame.image.load('image/character'+str(who)+'.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = location
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.speed = 50
        self.power = 3
        self.hold = 2

    def show(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right:
            self.rect.move_ip(self.speed,0)
        elif self.moving_left:
            self.rect.move_ip(-self.speed,0)
        elif self.moving_down:
            self.rect.move_ip(0,self.speed)
        elif self.moving_up:
            self.rect.move_ip(0,-self.speed)

class water(Sprite):
    def __init__(self,location):
        super().__init__()
        self.image = pygame.image.load('image/water.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = location
        self.time = 5
        self.screen = globalvar.screen

    def show(self):
        self.screen.blit(self.image,self.rect)
    
    def count(self):
        self.time = self.time-1



class wball(Sprite):
    def __init__(self,location,power):
        super().__init__()
        self.screen = globalvar.screen
        self.image = pygame.image.load('image/waterball.png')
        self.power = power
        self.time = 10
        self.rect = self.image.get_rect()
        self.rect.topleft = location
    def bloosm(self):
        #image = pygame.image.load('image/water.png')
        l  = self.rect.topleft
        x = int(l[0]/80)
        y = int(l[1]/80)
        globalvar.floors[x][y].ball=0
        globalvar.add_water(l,0,0)
        for i in range(1,self.power+1):
            globalvar.add_water(l,i*80,0)
            globalvar.add_water(l,i*-80,0)
            globalvar.add_water(l,0,i*80)
            globalvar.add_water(l,0,i*-80)
        
            
    def count(self):
        self.time = self.time-1
        if self.time==0:
            self.bloosm()
    def show(self):
        self.screen.blit(self.image,self.rect)

class floor():
    def __init__(self,x,y,n):
        self.screen = globalvar.screen
        if n == 0:
            self.image = pygame.image.load('image/floor0.png')
        if n == 1:
            self.image = pygame.image.load('image/floor1.png')
        self.water = 0
        self.ball = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    
    def show(self):
        self.screen.blit(self.image,self.rect)

    

global ch_num
chnum = [0,1,2,3]

def start_game(player_num,screen):
    #Locations = globalvar.location
    playerlist = []
    for i in range(0,player_num):
        r = random.randint(0,player_num-1-i)
        l = globalvar.location_pop(r)
        x = random.randint(0,player_num-1-i)
        y = chnum.pop(x)
        playerlist.append(char(screen,y,l))
    return playerlist

def add_character():
    n = len(globalvar.location)-1
    if n >= 0:
        r = random.randint(0,n)
        l = globalvar.location_pop(r)
        x = random.randint(0,n)
        y = chnum.pop(x)
        globalvar.add_player(char(globalvar.screen,y,l))

