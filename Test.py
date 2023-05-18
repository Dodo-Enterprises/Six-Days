# This is a test file to test the game and its functionalities.
from BattleSystem import BattleSystem
from Character import *

player = Character("Bob", 120, Jobs.WARRIOR, [], {}, {},
                   arm1=Weapon("Knife (H)", 100, Jobs.WARRIOR, WpnTypes.PIERCE, 80), is_player=True)
battle = BattleSystem.load_battle_from_file(player, 1)
battle.start()

