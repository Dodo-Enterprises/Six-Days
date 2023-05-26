# This is a test file to test the game and its functionalities.
from BattleSystem import BattleSystem
from Character import *

#player = Character("Bob", 120, Jobs.WARRIOR, [], {}, {}, arm1=Weapon("Knife (H)", Jobs.WARRIOR, WpnTypes.PIERCE, 80), is_player=True)
#BattleSystem.load_battle_from_file(player, 1).start()

#player = Character("Jajawawa", 200, Jobs.WARRIOR, [], {Potion.load_potion_from_file("Health (L)"):5}, {}, arm1=Weapon.load_weapon_from_file("Knife (L)"), arm2=Weapon.load_weapon_from_file("Bare Hands"), helmet=Armor.load_armor_from_file("Leather Helmet"), breastplate=Armor.load_armor_from_file("Leather Tunic"), grieves=Armor.load_armor_from_file("Leather Trousers"), is_player=True)
#player = Character("Jajawawa", 200, Jobs.MAGE, [Spell.load_spell_from_file("Fireball")], {Potion.load_potion_from_file("Health (L)"):5}, {}, arm1=Weapon.load_weapon_from_file("Wooden Staff (L)"), arm2=Weapon.load_weapon_from_file("Bare Hands"), helmet=Armor.load_armor_from_file("Leather Helmet"), breastplate=Armor.load_armor_from_file("Leather Tunic"), grieves=Armor.load_armor_from_file("Leather Trousers"), is_player=True)

#player = Character("Jajawawa", 200, Jobs.WARRIOR, [], {Potion.load_potion_from_file("Health (L)"):5}, {}, arm1=Weapon.load_weapon_from_file("Knife (L)"), arm2=Weapon.load_weapon_from_file("Sword (L)"), helmet=Armor.load_armor_from_file("Leather Helmet"), breastplate=Armor.load_armor_from_file("Leather Tunic"), grieves=Armor.load_armor_from_file("Leather Trousers"), is_player=True)
#player = Character("Jajawawa", 200, Jobs.MAGE, [Spell.load_spell_from_file("Fireball")], {Potion.load_potion_from_file("Health (L)"):5}, {}, arm1=Weapon.load_weapon_from_file("Wooden Staff (L)"), arm2=Weapon.load_weapon_from_file("Nice Wooden Staff (L)"), helmet=Armor.load_armor_from_file("Leather Helmet"), breastplate=Armor.load_armor_from_file("Leather Tunic"), grieves=Armor.load_armor_from_file("Leather Trousers"), is_player=True)

#player = Character("Jajawawa", 200, Jobs.WARRIOR, [], {Potion.load_potion_from_file("Health (M)"):5}, {}, arm1=Weapon.load_weapon_from_file("Stone Hammer (M)"), arm2=Weapon.load_weapon_from_file("Sword (L)"), helmet=Armor.load_armor_from_file("Stone Head"), breastplate=Armor.load_armor_from_file("Stone Chest"), grieves=Armor.load_armor_from_file("Stone Legs"), is_player=True)
player = Character("Jajawawa", 200, Jobs.MAGE, [Spell.load_spell_from_file("Fireball"),Spell.load_spell_from_file("Icespear")], {Potion.load_potion_from_file("Health (M)"):5}, {}, arm1=Weapon.load_weapon_from_file("Nice Wooden Staff (L)"), arm2=Weapon.load_weapon_from_file("Bare Hands"), helmet=Armor.load_armor_from_file("Stone Head"), breastplate=Armor.load_armor_from_file("Stone Chest"), grieves=Armor.load_armor_from_file("Stone Legs"), is_player=True)

BattleSystem.load_battle_from_file(player, 5).start()