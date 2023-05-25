# This is a test file to test the game and its functionalities.
from BattleSystem import BattleSystem
from Character import *

#player = Character("Bob", 120, Jobs.WARRIOR, [], {}, {}, arm1=Weapon("Knife (H)", Jobs.WARRIOR, WpnTypes.PIERCE, 80), is_player=True)
#BattleSystem.load_battle_from_file(player, 1).start()

player = Character("Jajawawa", 200, Jobs.ANY, [Spell.load_spell_from_file("Fireball")], {Potion.load_potion_from_file("Health (L)"):3}, {}, arm1=Weapon.load_weapon_from_file("Wooden Staff (L)"), arm2=Weapon.load_weapon_from_file("Sword (L)"), is_player=True)

BattleSystem.load_battle_from_file(player, 2).start()
