import sys
import pygame
from Setting import Setting
import character
from event import check_event,update_screen
import globalvar
def run_game():
    #initialize game and create a dispaly object
    pygame.init()
    setting = Setting()
    globalvar.init(setting)
    pygame.display.set_caption("BB king")
    globalvar.set_player(character.start_game(1,globalvar.screen))

    # game loop
    while True:
        # supervise keyboard and mouse item
        # change stat of objects
        check_event() 
        update_screen(setting)

        
if __name__ == '__main__':
    run_game()