# This is a test file to test the game and its functionalities.
from BattleSystem import BattleSystem
from Character import *

player = Character("Bob", 120, Jobs.WARRIOR, [], {}, {}, is_player=True)
# BattleSystem.load_battle_from_file(player, 1)

print(Character.load_character_from_file("Goblin"))
