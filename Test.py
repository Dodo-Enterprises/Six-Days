# This is a test file to test the game and its functionalities.
from BattleSystem import BattleSystem
from Character import *

#player = Character("Bob", 120, Jobs.WARRIOR, [], {}, {}, arm1=Weapon("Knife (H)", Jobs.WARRIOR, WpnTypes.PIERCE, 80), is_player=True)
#BattleSystem.load_battle_from_file(player, 1).start()

player = Character("Jajawawa", 200, Jobs.ANY, [Spell.load_spell_from_file("Fireball"), Spell.load_spell_from_file("Icespear")], {Potion.load_potion_from_file("Health (L)"):3}, {}, arm1=Weapon.load_weapon_from_file("Nice Wooden Staff (L)"), arm2=Weapon.load_weapon_from_file("Electric Spear (M)"), helmet=Armor.load_armor_from_file("Stone Head"), breastplate=Armor.load_armor_from_file("Stone Chest"), grieves=Armor.load_armor_from_file("Stone Legs"), is_player=True)

BattleSystem.load_battle_from_file(player, 7).start()