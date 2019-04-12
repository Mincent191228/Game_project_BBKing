import pygame
import character
from pygame.sprite import Group

def init(setting):
    global screen 
    global location
    global floors
    floors = [[] for i in range(15)]
    screen = pygame.display.set_mode((setting.wide,setting.height))
    location = setting.Locations
    for i in range(0,15):
        for j in range(0,10):
            floors[i].append(character.floor(i*80,j*80,(i+j)%2))
def screen():
    return screen

def location():
    return location

def location_pop(n):
    r = location.pop(n)
    return r
def set_player(playerlist):
    global player
    player = playerlist

def add_player(char):
    player.append(char)

def player(n=None):
    if n == None:
        return player
    else:
        return player[n]

def player_right(n,temp):
    if temp == 1:
        player[n].moving_right = True
    elif temp == 0:
        player[n].moving_right = False 
    
def player_left(n,temp):
    if temp == 1:
        player[n].moving_left = True
    elif temp == 0:
        player[n].moving_left = False 
def player_down(n,temp):
    if temp == 1:
        player[n].moving_down = True
    elif temp == 0:
        player[n].moving_down = False 

def player_up(n,temp):
    if temp == 1:
        player[n].moving_up = True
    elif temp == 0:
        player[n].moving_up = False 

global balls
balls = Group()

def add_ball(n):
    l = player[n].rect.center
    x = int(l[0]/80)
    y = int(l[1]/80)
    ball_l = floors[x][y].rect.topleft
    if player[n].hold>0 and floors[x][y].ball==0:
        balls.add(character.wball(ball_l,player[n].power))
        floors[x][y].ball = 1

global waters
waters = Group()

def add_water(l,x,y):
    water = character.water(l)
    water.rect.move_ip(x,y)
    waters.add(water)

def water_show():
    for water in waters:
        water.show()