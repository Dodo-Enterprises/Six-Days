# This is a test file to test the game and its functionalities.
from BattleSystem import BattleSystem
from Character import *

#player = Character("Bob", 120, Jobs.WARRIOR, [], {}, {},
                   #arm1=Weapon("Knife (H)", Jobs.WARRIOR, WpnTypes.PIERCE, 80, effect=Effects.BURN, effect_amt=30, effect_chance=50.0), is_player=True)
#BattleSystem.load_battle_from_file(player, 1).start()
player = Character("Sam", 120, Jobs.MAGE, [Spell.load_spell_from_file("Fireball")],
                   {Potion.load_potion_from_file("Health (L)"):3}, {Armor.load_armor_from_file("Leather Helmet"):2},
                   arm1=Weapon.load_weapon_from_file("Nice Wooden Staff (M)"), is_player=True)
BattleSystem.load_battle_from_file(player, 1).start()
