
import character
import globalvar
import Setting

setting = Setting.Setting()
globalvar.init(setting)
character.start_game(1,globalvar.screen)
player  = globalvar.player()
print(len(player))
character.add_character()
player  = globalvar.player()
print(len(player))
