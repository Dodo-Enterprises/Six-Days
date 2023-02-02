from Items import *
from Constants import *


class Character:
    """"""
    type_advantage = 2

    def __init__(self, name, health, job, arm1,
                 arm2, helmet, breastplate, grieves, spells, potions, items):
        """Creates an instance of the Character class.

        :param name: the name of the character
        :param job: the character class of the character
        :param arm1: the 1st armament of the character
        :param arm2: the 2nd armament of the character
        :param helmet: the headwear of the character
        :param breastplate: the chestwear of the character
        :param grieves: the legwear of the character
        :param spells: the list of spells the character can cast
        :param potions: the list of potions the character has
        :param items: the list of items the character has
        """
        # No armament is this Weapon("Bare Hands", 0, Jobs.Any, WpnTypes.BLUNT, 10, Effects.STUN, 20.0, 0)
        assert isinstance(name, str), f"Name expected to be string type, got: {type(name)}"
        assert isinstance(health, float), f"Health expected to be float type, got: {type(health)}"
        assert isinstance(job, Jobs), f"Job expected to be Jobs type, got: {type(job)}"
        assert isinstance(arm1, Weapon), f"Armament1 expected to be Weapon type, got: {type(arm1)}"
        assert isinstance(arm2, Weapon), f"Armament2 expected to be Weapon type, got: {type(arm2)}"
        assert isinstance(helmet, Armor), f"Helmet expected to be Armor type, got: {type(helmet)}"
        assert isinstance(breastplate, Armor), f"Breastplate expected to be Armor type, got: {type(breastplate)}"
        assert isinstance(grieves, Armor), f"Grieves expected to be Armor type, got: {type(grieves)}"
        assert isinstance(spells, list), f"Spells list expected to be list type, got: {type(spells)}"
        for spell in spells:
            assert isinstance(spell, Spell), f"Spell element expected to be spell type, got: {type(spell)}"
        assert isinstance(potions, list), f"Potions list expected to be list type, got: {type(potions)}"
        for potion in potions:
            assert isinstance(potion, Potion), f"Potion element expected to be potion type, got: {type(potion)}"
        assert isinstance(items, list), f"Items list expected to be list type, got: {type(items)}"
        for item in items:
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
        self.equipment = items

    def __equip__(self, item):
        """Equips a specified item to the desired equipment slot

        :param item: the item to be equipped
        :return: Nothing
        """
        assert isinstance(item, Weapon) or isinstance(item, Armor), \
            f"Item expected to be Weapon or Armor type, got: {type(item)}"
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
                    if self.arm1 is not None:
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
                            self.__add_to_inv__(self, self.arm1)
                            self.arm1 = item
                        else:
                            break
                    else:
                        self.__add_to_inv__(self, self.arm1)
                        self.arm1 = item
                        break
                else:
                    if self.arm2 is not None:
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
                            self.__add_to_inv__(self, self.arm2)
                            self.arm2 = item
                        else:
                            break
                    else:
                        self.__add_to_inv__(self, self.arm2)
                        self.arm2 = item
                        break
        else:
            # Equipping an armor piece to an armor slot
            while True:
                if item.armor_type is ArmorPieces.HELMET:
                    if self.helmet is not None:
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
                            self.__add_to_inv__(self, self.helmet)
                            self.helmet = item
                            break
                    else:
                        self.__add_to_inv__(self, self.helmet)
                        self.helmet = item
                        break
                elif item.armor_type is ArmorPieces.BREASTPLATE:
                    if self.breastplate is not None:
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
                            self.__add_to_inv__(self, self.breastplate)
                            self.breastplate = item
                            break
                    else:
                        self.__add_to_inv__(self, self.breastplate)
                        self.breastplate = item
                        break
                else:
                    if self.grieves is not None:
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
                            self.__add_to_inv__(self, self.grieves)
                            self.grieves = item
                            break
                    else:
                        self.__add_to_inv__(self, self.grieves)
                        self.grieves = item
                        break

    def __add_to_inv__(self, item):
        """Adds the specified item or list/tuple of items into the inventory

        :param item: the specified item to be added into inventory
        :return:
        """
        if isinstance(item, list) or isinstance(item, tuple):
            for i in item:
                assert isinstance(i, Weapon) or isinstance(i, Armor) or isinstance(i, Spell) or isinstance(i, Potion), \
                    f"The item expected to be Weapon, Armor, Spell, or Potion type, got: {type(item)}"
                if isinstance(i, Weapon) or isinstance(i, Armor):
                    self.equipment.append(i)
                elif isinstance(i, Spell):
                    self.spells.append(i)
                else:
                    self.potions.append(i)
        assert isinstance(item, Weapon) or isinstance(item, Armor) or isinstance(item, Spell) \
               or isinstance(item, Potion), f"The item expected to be Weapon, Armor, " \
                                            f"Spell, or Potion type, got: {type(item)}"
        if isinstance(item, Weapon) or isinstance(item, Armor):
            self.equipment.append(item)
        elif isinstance(item, Spell):
            self.spells.append(item)
        else:
            self.potions.append(item)

    def __phy_attack__(self, weapon, defender):
        # TODO add effects
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
        if self.job == Jobs.WARRIOR:
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
        # TODO finish the effect section
        if weapon.effect == Effects.NONE and defender.helmet.effect == Effects.NONE and defender.breastplate.effect \
                == Effects.NONE and defender.grieves.effect == Effects.NONE:
            if helmet_adv:
                helmet_dmg = float((Character.type_advantage * weapon.phy_damage * defender.helmet.phy_neg / 100)
                                   + (weapon.mag_damage * defender.helmet.magic_neg / 100))
            else:
                helmet_dmg = float((weapon.phy_damage * defender.helmet.phy_neg / 100)
                                   + (weapon.mag_damage * defender.helmet.magic_neg / 100))
            if breastplate_adv:
                breastplate_dmg = float(
                    (Character.type_advantage * weapon.phy_damage * defender.breastplate.phy_neg / 100)
                    + (weapon.mag_damage * defender.helmet.magic_neg / 100))
            else:
                breastplate_dmg = float((weapon.phy_damage * defender.breastplate.phy_neg / 100)
                                        + (weapon.mag_damage * defender.helmet.magic_neg / 100))
            if grieves_adv:
                grieves_dmg = float((Character.type_advantage * weapon.phy_damage * defender.grieves.phy_neg / 100)
                                    + (weapon.mag_damage * defender.helmet.magic_neg / 100))
            else:
                grieves_dmg = float((weapon.phy_damage * defender.grieves.phy_neg / 100)
                                    + (weapon.mag_damage * defender.helmet.magic_neg / 100))
            total_dmg = round((helmet_dmg + breastplate_dmg + grieves_dmg), 2)
            defender.__hurt__(total_dmg)
            return total_dmg, defender.health

    def __mag_attack__(self, staff, spell, defender):
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
        # TODO finish the effect section
        if staff.effect == Effects.NONE and defender.helmet.effect == Effects.NONE and defender.breastplate.effect \
                == Effects.NONE and defender.grieves.effect == Effects.NONE:
            helmet_dmg = float((staff.mag_damage + spell.mag_damage) * defender.helmet.magic_neg / 100)
            breastplate_dmg = float((staff.mag_damage + spell.mag_damage) * defender.breastplate.magic_neg / 100)
            grieves_dmg = float((staff.mag_damage + spell.mag_damage) * defender.grieves.magic_neg / 100)
            total_dmg = round((helmet_dmg + breastplate_dmg + grieves_dmg), 2)
            defender.__hurt__(total_dmg)
            return total_dmg, defender.health

    def __hurt__(self, dmg):
        assert isinstance(dmg, float), f"Expected Damage to be float type, got: {type(dmg)}"
        self.health -= dmg
        return self.health
