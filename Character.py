from Commands import Commands
from Items import *
from Constants import *
import random
import os


class Character:
    """"""
    _path_to_character_preset_file = os.getcwd() + "\\Character_Presets.txt"
    type_advantage = 2
    def_arm = Weapon("Bare Hands", Jobs.WARRIOR, WpnTypes.BLUNT, 10, effect=Effects.STUN, effect_chance=0.2,
                     effect_amt=0)
    def_helmet = Armor("Bare Head", Jobs.NONE, 100, 100, ArmorTypes.NONE, ArmorPieces.HELMET)
    def_breastplate = Armor("Bare Chest", Jobs.NONE, 100, 100, ArmorTypes.NONE, ArmorPieces.BREASTPLATE)
    def_grieves = Armor("Bare Legs", Jobs.NONE, 100, 100, ArmorTypes.NONE, ArmorPieces.GRIEVES)
    effect_duration = 3

    def __init__(self, name: str, health: int, job: Jobs, spells: list[Spell], potions: dict[Potion, int],
                 items: dict[Item, int], arm1: Weapon = def_arm, arm2: Weapon = def_arm, helmet: Armor = def_helmet,
                 breastplate: Armor = def_breastplate, grieves: Armor = def_grieves, is_player: bool = False):
        """Creates an instance of the Character class.

        :param name: the character's name
        :param job: the character's class
        :param arm1: the 1st armament of the character
        :param arm2: the 2nd armament of the character
        :param helmet: the headgear of the character
        :param breastplate: the chestwear of the character
        :param grieves: the legwear of the character
        :param spells: the list of spells the character can cast
        :param potions: the list of potions the character has
        :param items: the list of items the character has
        """
        assert isinstance(name, str), f"Name expected to be string type, got: {type(name)}"
        assert isinstance(health, int), f"Health expected to be float type, got: {type(health)}"
        assert isinstance(job, Jobs), f"Job expected to be Jobs type, got: {type(job)}"
        assert isinstance(arm1, Weapon), f"Armament1 expected to be Weapon type, got: {type(arm1)}"
        assert isinstance(arm2, Weapon), f"Armament2 expected to be Weapon type, got: {type(arm2)}"
        assert isinstance(helmet, Armor), f"Helmet expected to be Armor type, got: {type(helmet)}"
        assert isinstance(breastplate, Armor), f"Breastplate expected to be Armor type, got: {type(breastplate)}"
        assert isinstance(grieves, Armor), f"Grieves expected to be Armor type, got: {type(grieves)}"
        assert isinstance(spells, list), f"Spells list expected to be list type, got: {type(spells)}"
        if len(spells) != 0:
            if spells[0] is None:
                self.spells = []
            else:
                for spell in spells:
                    assert isinstance(spell, Spell), f"Spell element expected to be spell type, got: {type(spell)}"
                self.spells = spells
        assert isinstance(potions, dict), f"Potions list expected to be dictionary type, got: {type(potions)}"
        if len(potions.items()) != 0:
            for potion in potions.keys():
                if potion is not None:
                    assert isinstance(potion, Potion), f"Potion element expected to be potion type, got: {type(potion)}"
        assert isinstance(items, dict), f"Items list expected to be dict type, got: {type(items)}"
        if len(items.items()) != 0:
            for item in items.keys():
                assert isinstance(item, Weapon) or isinstance(item, Armor), \
                    f"Item element expected to be Weapon or Armor type, got: {type(item)}"

        self.name = name
        self.health = health
        self.job = job
        self.arm1 = arm1
        self.arm2 = arm2
        self.helmet = helmet
        self.breastplate = breastplate
        self.grieves = grieves
        self.spells = spells
        self.potions = potions
        self.items = items
        self.status = {}
        self.is_player = is_player

    def equip(self, item):
        """Equips a specified item to the desired equipment slot

        :param item: the item to be equipped
        :return: Nothing
        """
        try:
            assert isinstance(item, Weapon) or isinstance(item, Armor) or isinstance(item, str), \
                f"Item expected to be Weapon, Armor, or string type, got: {type(item)}"
        except AssertionError:
            print("please")
        if isinstance(item, Weapon):
            # Equipping a weapon to the armament slot
            while True:
                while True:
                    try:
                        i = int(input("Which armament slot do you want to equip your weapon into? (1 or 2)"))
                        assert i == 1 or i == 2
                        break
                    except ValueError or AssertionError:
                        print("The input was not recognized as a valid input. Please input a valid response. "
                              "Try again...")
                if i == 1:
                    if self.arm1 != Character.def_arm:
                        while True:
                            try:
                                ans = input(f"You already have an armament equipped in this slot. "
                                            f"Are you sure you want to replace {self.arm1.name} with {item.name}? y/n")
                                assert ans == "y" or ans == "n"
                                break
                            except AssertionError:
                                print("The input was not recognized as a valid input. Please input a valid response. "
                                      "Try again...")
                        if ans == "y":
                            self.add_to_inventory(self.arm1)
                            self.arm1 = item
                            self.remove_from_inventory(item)
                        else:
                            break
                    else:
                        self.arm1 = item
                        self.remove_from_inventory(item)
                        break
                else:
                    if self.arm2 != Character.def_arm:
                        while True:
                            try:
                                ans = input(f"You already have an armament equipped in this slot. "
                                            f"Are you sure you want to replace {self.arm2.name} with {item.name}? y/n")
                                assert ans == "y" or "n"
                                break
                            except AssertionError:
                                print("The input was not recognized as a valid input. Please input a valid response. "
                                      "Try again...")
                        if ans == "y":
                            self.add_to_inventory(self.arm2)
                            self.arm2 = item
                            self.remove_from_inventory(item)
                        else:
                            break
                    else:
                        self.arm2 = item
                        self.remove_from_inventory(item)
                        break
        elif isinstance(item, str):
            assert item in [i.name for i in self.items.keys()], \
                f"That item does not exist in your inventory."
            name_instance_dict = {i.name: i for i in self.items.keys()}
            for key, value in name_instance_dict.items():
                if item == key:
                    self.equip(value)
        else:
            # Equipping an armor piece to an armor slot
            while True:
                if item.armor_piece == ArmorPieces.HELMET:
                    if self.helmet != Character.def_helmet:
                        while True:
                            try:
                                ans = input(f"You already have a helmet equipped. Are you sure you want to replace "
                                            f"{self.helmet.name} with {item.name}? y/n")
                                assert ans == "y" or ans == "n"
                                break
                            except AssertionError:
                                print("The input was not recognized as a valid input. Please input a valid response. "
                                      "Try again...")
                        if ans == "y":
                            self.add_to_inventory(self.helmet)
                            self.helmet = item
                            self.remove_from_inventory(item)
                            break
                    else:
                        self.helmet = item
                        self.remove_from_inventory(item)
                        break
                elif item.armor_piece == ArmorPieces.BREASTPLATE:
                    if self.breastplate != Character.def_breastplate:
                        while True:
                            try:
                                ans = input(
                                    f"You already have a breastplate equipped. Are you sure you want to replace "
                                    f"{self.breastplate.name} with {item.name}? y/n")
                                assert ans == "y" or ans == "n"
                                break
                            except AssertionError:
                                print("The input was not recognized as a valid input. Please input a valid response. "
                                      "Try again...")
                        if ans == "y":
                            self.add_to_inventory(self.breastplate)
                            self.breastplate = item
                            self.remove_from_inventory(item)
                            break
                    else:
                        self.breastplate = item
                        self.remove_from_inventory(item)
                        break
                else:
                    if self.grieves != Character.def_grieves:
                        while True:
                            try:
                                ans = input(f"You already have grieves equipped. Are you sure you want to replace "
                                            f"{self.grieves.name} with {item.name}? y/n")
                                assert ans == "y" or ans == "n"
                                break
                            except AssertionError:
                                print("The input was not recognized as a valid input. Please input a valid response. "
                                      "Try again...")
                        if ans == "y":
                            self.add_to_inventory(self.grieves)
                            self.grieves = item
                            self.remove_from_inventory(item)
                            break
                    else:
                        self.grieves = item
                        self.remove_from_inventory(item)
                        break

    def unequip(self, slot):
        assert slot == "arm1" or slot == "arm2" or slot == "helmet" or slot == "breastplate" or slot == "grieves", \
            f"slot expected to be a valid equipment slot, got: {slot}"
        match slot:
            case "arm1":
                if self.arm1 != Character.def_arm:
                    self.add_to_inventory(self.arm1)
                self.arm1 = Character.def_arm
            case "arm2":
                if self.arm2 != Character.def_arm:
                    self.add_to_inventory(self.arm2)
                self.arm2 = Character.def_arm
            case "helmet":
                if self.helmet != Character.def_helmet:
                    self.add_to_inventory(self.helmet)
                self.helmet = Character.def_helmet
            case "breastplate":
                if self.breastplate != Character.def_breastplate:
                    self.add_to_inventory(self.breastplate)
                self.breastplate = Character.def_breastplate
            case "grieves":
                if self.grieves != Character.def_grieves:
                    self.add_to_inventory(self.grieves)
                self.grieves = Character.def_grieves

    def add_to_inventory(self, item):
        """Adds the specified item or list/tuple of items into the inventory

        :param item: the specified item to be added into inventory
        :return:
        """
        if isinstance(item, list) or isinstance(item, tuple):
            for i in item:
                assert isinstance(i, Weapon) or isinstance(i, Armor) or isinstance(i, Spell) or isinstance(i, Potion)\
                       or isinstance(i, Item), f"The item expected to be Weapon, Armor, Spell, Potion, or Item type, " \
                                               f"got: {type(item)}"
                if isinstance(i, Weapon) or isinstance(i, Armor) or isinstance(i, Item):
                    self.items[i] = self.items[i] + 1 if i in self.items.items() else 1
                elif isinstance(i, Spell):
                    self.spells.append(i)
                else:
                    self.potions[i] = self.potions[i] + 1 if i in self.potions.items() else 1
            return
        assert isinstance(item, Weapon) or isinstance(item, Armor) or isinstance(item, Spell) \
               or isinstance(item, Potion), f"The item expected to be Weapon, Armor, " \
                                            f"Spell, or Potion type, got: {type(item)}"
        if isinstance(item, Weapon) or isinstance(item, Armor) or isinstance(item, Item):
            self.items[item] = self.items[item] + 1 if item in self.items.items() else 1
        elif isinstance(item, Spell):
            self.spells.append(item)
        else:
            self.potions[item] = self.potions[item] + 1 if item in self.potions.items() else 1

    def remove_from_inventory(self, item):
        """Removes the specified item from the player's inventory"""
        assert isinstance(item, Item) or isinstance(item, Weapon) or isinstance(item, Armor) or \
               isinstance(item, Potion) or isinstance(item, Spell), f"Item expected to be of Item, Weapon, Armor, " \
                                                                     f"Potion, or Spell type, got: {type(item)}"
        for key, value in self.items.items():
            if item != key:
                continue
            if value > 1:
                self.items[key] = value - 1
                return True
            del self.items[key]
            return True
        return False

    def phy_attack(self, weapon, defender):
        """Enacts a physical attack on the specified defender with the specified weapon.

        :param weapon: the specific weapon that the character uses to attack
        :param defender: the character that is being attacked
        :return: the damage done to the character and how much health they have left in a tuple
        """
        assert isinstance(weapon, Weapon), f"Weapon expected to be Weapon type, got: {type(weapon)}"
        assert isinstance(defender, Character), f"Defender expected to be Character type, got: {type(defender)}"
        # Calculating the advantage the attacker gets
        helmet_adv = False
        breastplate_adv = False
        grieves_adv = False
        if self.job == Jobs.WARRIOR or Jobs.ANY:
            match weapon.wpn_type:
                case WpnTypes.BLUNT:
                    if defender.helmet.armor_type == ArmorTypes.PLATE:
                        helmet_adv = True
                    if defender.breastplate.armor_type == ArmorTypes.PLATE:
                        breastplate_adv = True
                    if defender.grieves.armor_type == ArmorTypes.PLATE:
                        grieves_adv = True
                case WpnTypes.SLASH:
                    if defender.helmet.armor_type == ArmorTypes.LEATHER:
                        helmet_adv = True
                    if defender.breastplate.armor_type == ArmorTypes.LEATHER:
                        breastplate_adv = True
                    if defender.grieves.armor_type == ArmorTypes.LEATHER:
                        grieves_adv = True
                case WpnTypes.PIERCE:
                    if defender.helmet.armor_type == ArmorTypes.CHAIN:
                        helmet_adv = True
                    if defender.breastplate.armor_type == ArmorTypes.CHAIN:
                        breastplate_adv = True
                    if defender.grieves.armor_type == ArmorTypes.CHAIN:
                        grieves_adv = True
                case WpnTypes.STAFF:
                    if defender.helmet.armor_type == ArmorTypes.PLATE:
                        helmet_adv = True
                    if defender.breastplate.armor_type == ArmorTypes.PLATE:
                        breastplate_adv = True
                    if defender.grieves.armor_type == ArmorTypes.PLATE:
                        grieves_adv = True
        # Calculating the attack done on defender
        if self.job == Jobs.WARRIOR or Jobs.ANY:
            if weapon.effect != Effects.NONE:
                if helmet_adv:
                    helmet_dmg = float((Character.type_advantage * weapon.phy_damage * defender.helmet.phy_neg)
                                       + (weapon.mag_damage * defender.helmet.magic_neg))
                else:
                    helmet_dmg = float((weapon.phy_damage * defender.helmet.phy_neg)
                                       + (weapon.mag_damage * defender.helmet.magic_neg))
                if breastplate_adv:
                    breastplate_dmg = float(
                        (Character.type_advantage * weapon.phy_damage * defender.breastplate.phy_neg)
                        + (weapon.mag_damage * defender.helmet.magic_neg))
                else:
                    breastplate_dmg = float((weapon.phy_damage * defender.breastplate.phy_neg)
                                            + (weapon.mag_damage * defender.helmet.magic_neg))
                if grieves_adv:
                    grieves_dmg = float((Character.type_advantage * weapon.phy_damage * defender.grieves.phy_neg)
                                        + (weapon.mag_damage * defender.helmet.magic_neg))
                else:
                    grieves_dmg = float((weapon.phy_damage * defender.grieves.phy_neg)
                                        + (weapon.mag_damage * defender.helmet.magic_neg))
                total_dmg = round((helmet_dmg + breastplate_dmg + grieves_dmg), 2)
                defender.hurt(total_dmg)
                if weapon.effect != Effects.LIFESTEAL:
                    defender.afflict(weapon.effect, weapon.effect_chance, weapon.effect_amt)
                    return total_dmg, defender.health
                else:
                    self.hurt(-float(total_dmg * weapon.effect_amt))
                    return total_dmg, defender.health
            else:
                if helmet_adv:
                    helmet_dmg = float((Character.type_advantage * weapon.phy_damage * defender.helmet.phy_neg)
                                       + (weapon.mag_damage * defender.helmet.magic_neg))
                else:
                    helmet_dmg = float((weapon.phy_damage * defender.helmet.phy_neg)
                                       + (weapon.mag_damage * defender.helmet.magic_neg))
                if breastplate_adv:
                    breastplate_dmg = float(
                        (Character.type_advantage * weapon.phy_damage * defender.breastplate.phy_neg)
                        + (weapon.mag_damage * defender.helmet.magic_neg))
                else:
                    breastplate_dmg = float((weapon.phy_damage * defender.breastplate.phy_neg)
                                            + (weapon.mag_damage * defender.helmet.magic_neg))
                if grieves_adv:
                    grieves_dmg = float((Character.type_advantage * weapon.phy_damage * defender.grieves.phy_neg)
                                        + (weapon.mag_damage * defender.helmet.magic_neg))
                else:
                    grieves_dmg = float((weapon.phy_damage * defender.grieves.phy_neg)
                                        + (weapon.mag_damage * defender.helmet.magic_neg))
                total_dmg = round((helmet_dmg + breastplate_dmg + grieves_dmg), 2)
                defender.hurt(total_dmg)
                return total_dmg, defender.health
        else:
            helmet_dmg = float((weapon.phy_damage * defender.helmet.phy_neg) +
                               (weapon.mag_damage * defender.helmet.magic_neg))
            breastplate_dmg = float((weapon.phy_damage * defender.breastplate.phy_neg)
                                    + (weapon.mag_damage * defender.helmet.magic_neg))
            grieves_dmg = float((weapon.phy_damage * defender.grieves.phy_neg)
                                + (weapon.mag_damage * defender.helmet.magic_neg))
            total_dmg = round((helmet_dmg + breastplate_dmg + grieves_dmg) / Character.type_advantage, 2)
            defender.hurt(total_dmg)
            return total_dmg, defender.health

    def mag_attack(self, staff, spell, defender):
        """Enacts a magical attack with the specified spell and staff against the defender

        :param staff: The staff the attacker is using
        :param spell: The spell the Attacker is using
        :param defender: The specified defender
        :return: the damage done to the character and how much health they have left in a tuple
        """
        assert isinstance(staff, Weapon), f"Staff expected to be Weapon type, got {type(staff)}"
        assert staff.wpn_type == WpnTypes.STAFF, f"Staff expected to be a staff, got {staff.wpn_type}"
        assert isinstance(spell, Spell), f"Spell expected to be Spell type, got {type(spell)}"
        assert isinstance(defender, Character), f"Defender expected to be Character type, got {type(defender)}"
        assert staff is self.arm1 or staff is self.arm2, "staff expected to be an equipped armament"
        if self.job == Jobs.MAGE or Jobs.ANY:
            helmet_dmg = float((staff.mag_damage + spell.mag_damage) * defender.helmet.magic_neg)
            breastplate_dmg = float((staff.mag_damage + spell.mag_damage) * defender.breastplate.magic_neg)
            grieves_dmg = float((staff.mag_damage + spell.mag_damage) * defender.grieves.magic_neg)
            total_dmg = round((helmet_dmg + breastplate_dmg + grieves_dmg), 2)
            defender.hurt(total_dmg)
            defender.afflict(spell.effect, spell.effect_chance, spell.effect_amt)
            if staff.effect != Effects.NONE:
                defender.afflict(staff.effect, staff.effect_chance, staff.effect_amt)
            return total_dmg, defender.health
        else:
            helmet_dmg = float((staff.mag_damage + spell.mag_damage) * defender.helmet.magic_neg)
            breastplate_dmg = float((staff.mag_damage + spell.mag_damage) * defender.breastplate.magic_neg)
            grieves_dmg = float((staff.mag_damage + spell.mag_damage) * defender.grieves.magic_neg)
            total_dmg = round((helmet_dmg + breastplate_dmg + grieves_dmg) / Character.type_advantage, 2)
            defender.hurt(total_dmg)
            return total_dmg, defender.health

    def hurt(self, dmg):
        assert isinstance(dmg, float), f"Expected Damage to be float type, got: {type(dmg)}"
        self.health = int(round(float(self.health) - dmg))
        return self.health

    def afflict(self, effect: Effects, effect_chance: float, effect_amt: int):
        assert isinstance(effect, Effects), f"Expected an effect type, got: {type(effect)}"
        assert isinstance(effect_amt, int), f"effect_amt is expected to be int type, got {type(effect_amt)}"
        assert isinstance(effect_chance, float), f"Effect_chance expected to be float type, got {type(effect_chance)}"
        if effect == Effects.NONE:
            return False
        if random.random() > effect_chance:
            return False
        print(f"{effect.value} was successful afflicted on {self.name}")
        for key in self.status:
            if effect == key:
                del self.status[key]
                self.status.update({effect: (effect_amt,
                                             Character.effect_duration)})
                return True
        self.status.update({effect: (effect_amt, Character.effect_duration)})
        return True

    def remove_effects(self, effect: Effects = None):
        """Removes the symptoms of the effect does not change the character's status"""
        if effect is not None:
            for effect_2, (amt, duration) in self.status.items():
                if effect_2 == effect:
                    match effect_2:
                        case Effects.STRENGTH:
                            self.arm1.phy_damage -= amt
                            self.arm2.phy_damage -= amt
                        case Effects.DEFENSE:
                            self.helmet.phy_neg -= amt
                            self.helmet.magic_neg -= amt
                            self.breastplate.phy_neg -= amt
                            self.breastplate.magic_neg -= amt
                            self.grieves.phy_neg -= amt
                            self.grieves.magic_neg -= amt
                        case Effects.MAGIC:
                            self.arm1.mag_damage -= amt
                            self.arm2.mag_damage -= amt
            self.status.clear()
            return True
        for effect_2, (amt, duration) in self.status.items():
            match effect_2:
                case Effects.STRENGTH:
                    self.arm1.phy_damage -= amt
                    self.arm2.phy_damage -= amt
                case Effects.DEFENSE:
                    self.helmet.phy_neg -= amt
                    self.helmet.magic_neg -= amt
                    self.breastplate.phy_neg -= amt
                    self.breastplate.magic_neg -= amt
                    self.grieves.phy_neg -= amt
                    self.grieves.magic_neg -= amt
                case Effects.MAGIC:
                    self.arm1.mag_damage -= amt
                    self.arm2.mag_damage -= amt
        self.status.clear()
        return True

    def open_inventory(self):
        """Displays the inventory information.

        return True if player used a potion. False if they did not.
        """
        print(f"Current Health: {self.health}")
        print(f"Armament_1: {self.arm1.name}, Armament_2: {self.arm2.name}")
        print(f"Helmet: {self.helmet.name}, Breastplate: {self.breastplate.name}, Grieves: {self.grieves.name}")
        print([spell.name for spell in self.spells])
        display_items_dict = {key.name: value for key, value in self.items.items()}
        display_potions_dict = sorted({key.name: value for key, value in self.potions.items()})
        print(f"Potions: {display_potions_dict}")
        print(f"Items: {display_items_dict}")
        while True:
            cmd = input().split(" ")
            if len(cmd) > 2:
                command = cmd.pop(0)
                temp = ""
                i = 0
                for arg in cmd:
                    i += 1
                    if i == 1:
                        temp += arg
                        continue
                    temp += " " + arg
                cmd = [command, temp]
            try:
                assert cmd[0] in Commands._value2member_map_, f"Command expected to be of approved type, got: {cmd[0]}"
            except AssertionError:
                print("Invalid command, Please try again.")
                print(f"list of helpful commands:\n{Commands.HELP.value}\n{Commands.EQUIP.value}"
                      f"\n{Commands.UNEQUIP.value}\n{Commands.USE.value}\n{Commands.TRASH.value}\n{Commands.INFO.value}"
                      f"\n{Commands.EXIT.value}")
                continue
            match cmd[0]:
                case Commands.HELP.value:
                    print(f"list of commands:\n{Commands.HELP.value}\n{Commands.EQUIP.value}\n{Commands.UNEQUIP.value}"
                          f"\n{Commands.USE.value}\n{Commands.TRASH.value}\n{Commands.EXIT.value}")
                    continue
                case Commands.EQUIP.value:
                    try:
                        print(cmd[1])
                        self.equip(cmd[1])
                        continue
                    except AssertionError:
                        print("Invalid command. Please specify a valid item in your inventory to equip.")
                        continue
                case Commands.UNEQUIP.value:
                    try:
                        self.unequip(cmd[1])
                    except AssertionError:
                        print("Invalid command. Please specify which slot you would like to unequip. "
                              "Valid inputs are arm1, arm2, helmet, breastplate, and grieves.")
                        continue
                case Commands.USE.value:
                    name_potion_dict = {i.name: i for i in self.potions.keys()}
                    if cmd[1] in name_potion_dict:
                        for key in self.potions.keys():
                            if name_potion_dict[cmd[1]] == key:
                                self.afflict(key.effect, key.effect_chance, key.effect_amt)
                                return True
                        continue
                    print(f"{cmd[1]} does not exist in you potion inventory.")
                case Commands.TRASH.value:
                    name_item_dict = {i.name: i for i in self.items.keys()}
                    name_potion_dict = {i.name: i for i in self.potions.keys()}
                    try:
                        assert cmd[1] in name_item_dict or cmd[1] in name_potion_dict, \
                            f"{cmd[1]} not in items or potions. Try again."
                    except AssertionError:
                        print("Invalid command. Try again.")
                        continue
                    if cmd[1] in name_item_dict:
                        for key in self.items.keys():
                            if name_item_dict[cmd[1]] != key:
                                continue
                            del self.items[key]
                            break
                    else:
                        for key in self.potions.keys():
                            if name_potion_dict[cmd[1]] != key:
                                continue
                            del self.potions[key]
                            break
                case Commands.INFO.value:
                    print(f"Current Health: {self.health}")
                    print(f"Current Status: {self.status}")
                    print(f"Armament_1: {self.arm1.name}, Armament_2: {self.arm2.name}")
                    print(f"Helmet: {self.helmet.name}, Breastplate: {self.breastplate.name}, Grieves: {self.grieves.name}")
                    print(f"Spells: {[spell.name for spell in self.spells]}")
                    display_items_dict = {key.name: value for key, value in self.items.items()}
                    display_potions_dict = {key.name: value for key, value in self.potions.items()}
                    print(f"Potions: {display_potions_dict}")
                    print(f"Items: {display_items_dict}")
                case Commands.EXIT.value:
                    break
        return False

    @classmethod
    def load_character_from_file(cls, character_name: str):
        """Loads the preset character from file to create a specific Character instance.

        :param character_name:
        :return: A Character instance that is specified by the character_name argument.
        """
        with open(cls._path_to_character_preset_file, 'r') as f:
            lines = f.read().splitlines()
            character_arguments = []
            for line in lines:
                character_arguments.append(line.split(", "))
            first_item = [i[0] for i in character_arguments]
            assert character_name in first_item, \
                f"{character_name} does not exist in Character_Presets.txt"
            character_arguments = character_arguments[first_item.index(character_name)]
            return Character(character_arguments[0], int(character_arguments[1]), Jobs[character_arguments[2]],
                             [Spell.load_spell_from_file(i) if i != "NONE" else None for i in character_arguments[3][1:-1].split(",")],
                             Potion.stack_potions(
                                 [Potion.load_potion_from_file(i) if i != "NONE" else None for i in character_arguments[4].split(",")]),
                             {}, arm1=Weapon.load_weapon_from_file(character_arguments[5]),
                             arm2=Weapon.load_weapon_from_file(character_arguments[6]),
                             helmet=Armor.load_armor_from_file(character_arguments[7]),
                             breastplate=Armor.load_armor_from_file(character_arguments[8]),
                             grieves=Armor.load_armor_from_file(character_arguments[9]))
