# This is a test file to test the game and its functionalities.
from BattleSystem import BattleSystem
from Character import *

player = Character("Bob", 120, Jobs.WARRIOR, [], {}, {},
                   arm1=Weapon("Knife (H)", Jobs.WARRIOR, WpnTypes.PIERCE, 80), is_player=True)
#BattleSystem.load_battle_from_file(player, 1).start()
BattleSystem.load_battle_from_file(player, 1).start()
str
