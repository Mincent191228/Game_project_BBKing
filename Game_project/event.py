import sys
import pygame
import character
import globalvar

def check_event():
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #if keys[pygame.K_LSHIFT] and keys[pygame.K_n]:
            if event.key == pygame.K_n:
                character.add_character()
            elif event.key == pygame.K_RIGHT:
                globalvar.player_right(0,1)
            elif event.key == pygame.K_LEFT:
                globalvar.player_left(0,1)
            elif event.key == pygame.K_DOWN:
                globalvar.player_down(0,1)
            elif event.key == pygame.K_UP:
                globalvar.player_up(0,1)
            elif event.key == pygame.K_l:
                globalvar.add_ball(0)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                globalvar.player_right(0,0)
            elif event.key == pygame.K_LEFT:
                globalvar.player_left(0,0)
            elif event.key == pygame.K_DOWN:
                globalvar.player_down(0,0)
            elif event.key == pygame.K_UP:
                globalvar.player_up(0,0)

            

def update_screen(setitng):
    #char,ball,water
    globalvar.screen.fill(setitng.bgc)
    l = len(globalvar.player)
    player = globalvar.player
    balls = globalvar.balls
    waters = globalvar.waters
    floors = globalvar.floors
    for i in range(0,15):
        for j in range(0,10):
            floors[i][j].show()
            
    for ball in balls:
        ball.count()
        ball.show()
        if ball.time == 0:
            balls.remove(ball)
    for i in player:
        i.update()
        i.show()
    for water in waters:
        water.count()
        water.show()
        if water.time==0:
            waters.remove(water)
    pygame.display.flip()