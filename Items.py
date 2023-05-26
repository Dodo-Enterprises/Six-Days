
#import Character
from Constants import *
import os


class Item:
    """Item data type that holds all relevant information for misc. items"""
    def __init__(self, name: str):
        """Creates the Item instances
        """
        assert isinstance(name, str), f"Name expected to be string type, got: {type(name)}"
        self.name = name


class Weapon:
    """Weapon data type that holds all the relevant information for all weapon items."""
    _path_to_weapons_preset_file_windows = os.getcwd() + "\\Weapons.txt"
    _path_to_weapons_preset_file_mac = os.getcwd() + "/Weapons.txt"

    def __init__(self, name: str, job: Jobs, wpn_type: WpnTypes, phy_damage: int, mag_damage: int = 0,
                 effect: Effects = Effects.NONE, effect_chance: float = 1.0, effect_amt: int = 0):
        """Creates the Weapon instance.

        Keyword arguments:
        name -- the name of this item
        job -- the character class that this item is most effective for
        wpn_type -- the type of weapon it is
        damage -- the default damage this weapon does
        effect -- the specific effect this weapon causes (can't be applied to staffs)
        effect_chance -- the percentage of the effect being activated
        effect_amt -- the amount of effect the effect causes
        """
        assert isinstance(name, str), f"Name expected to be string type, got: {type(name)}"
        assert isinstance(job, Jobs), f"Job expected to be Jobs type, got: {type(job)}"
        assert isinstance(wpn_type, WpnTypes), f"Weapon_Type expected to be Wpn_Types type, got: {type(wpn_type)}"
        assert isinstance(phy_damage, int), f"Damage expected to be Integer type, got: {type(phy_damage)}"
        assert isinstance(effect, Effects), f"Effect expected to be Effects type, got: {type(effect)}"
        assert isinstance(effect_chance, float), f"Effect_Chance expected to be Float type, got: {type(effect_chance)}"
        assert isinstance(effect_amt, int), f"Effect_Amount expected to be integer type, got: {type(effect_amt)}"
        assert isinstance(mag_damage, int), f"Magical Damage expected to be integer type, got: {type(mag_damage)}"
        self.name = name
        self.job = job
        self.wpn_type = wpn_type
        self.phy_damage = phy_damage
        self.effect = effect
        self.effect_chance = float(effect_chance) / 100
        self.effect_amt = effect_amt
        self.mag_damage = mag_damage

    @classmethod
    def load_weapon_from_file(cls, weapon_name: str):
        """Returns a weapon instance of the specified weapon."""
        try:
            with open(cls._path_to_weapons_preset_file_windows, 'r') as f:
                lines = f.read().splitlines()
                weapon_arguments = []
                for line in lines:
                    weapon_arguments.append(line.split(", "))
                first_item = [i[0] for i in weapon_arguments]
                assert weapon_name in first_item, f"{weapon_name} does not exist in Weapons.txt"
                weapon_arguments = weapon_arguments[first_item.index(weapon_name)]
                return Weapon(weapon_arguments[0], Jobs[weapon_arguments[1]],
                              WpnTypes[weapon_arguments[2]], int(weapon_arguments[3]), mag_damage=int(weapon_arguments[4]),
                              effect=Effects(weapon_arguments[5]),
                              effect_chance=float(weapon_arguments[6]), effect_amt=int(weapon_arguments[7]))
        except FileNotFoundError:
            with open(cls._path_to_weapons_preset_file_mac, 'r') as f:
                lines = f.read().splitlines()
                weapon_arguments = []
                for line in lines:
                    weapon_arguments.append(line.split(", "))
                first_item = [i[0] for i in weapon_arguments]
                assert weapon_name in first_item, f"{weapon_name} does not exist in Weapons.txt"
                weapon_arguments = weapon_arguments[first_item.index(weapon_name)]
                return Weapon(weapon_arguments[0], Jobs[weapon_arguments[1]],
                              WpnTypes[weapon_arguments[2]], int(weapon_arguments[3]), mag_damage=int(weapon_arguments[4]),
                              effect=Effects(weapon_arguments[5]),
                              effect_chance=float(weapon_arguments[6]), effect_amt=int(weapon_arguments[7]))


class Armor:
    """Weapon data type that holds all the relevant information for all weapon items."""
    _path_to_armor_preset_file_windows = os.getcwd() + "\\Armor_Pieces.txt"
    _path_to_armor_preset_file_mac = os.getcwd() + "/Armor_Pieces.txt"

    def __init__(self, name: str, job: Jobs, phy_neg: int, magic_neg: int, armor_type: ArmorTypes,
                 armor_piece: ArmorPieces):
        """Creates the Armor Instance.

        Keyword arguments:
        name -- the name of this item
        job -- the character class that this item is most effective for
        phy_neg -- the amount of physical damage absorbed by the armor piece
        magic_neg -- the amount of magical damage absorbed by the armor piece
        armor_type -- the type of armor it is (Plated, chain, and leather)
        armor_piece -- the type of armor piece it is (Helmet, breastplate, and grieves)
        """
        assert isinstance(name, str), f"Name expected to be string type, got: {type(name)}"
        assert isinstance(job, Jobs), f"Job expected to be Jobs type, got: {type(job)}"
        assert isinstance(phy_neg, int), f"Physical_Negation expected to be Integer type, got: {type(phy_neg)}"
        assert phy_neg > 0, f"phy_neg expected to be a non-zero and non-negative number, got: {phy_neg}"
        assert isinstance(magic_neg, int), f"magical_Negation expected to be Integer type, got: {type(magic_neg)}"
        assert magic_neg > 0, f"magic_neg expected to be a non-zero and non-negative number, got: {magic_neg}"
        assert isinstance(armor_type, ArmorTypes),\
            f"Armor_Type expected to be Armor_Types type, got: {type(armor_type)}"
        assert isinstance(armor_piece, ArmorPieces),\
            f"Armor_pieces expected to be ArmorPieces type, got: {type(armor_piece)}"
        self.name = name
        self.job = job
        self.phy_neg = float(phy_neg / 100)
        self.magic_neg = float(magic_neg / 100)
        self.armor_type = armor_type
        self.armor_piece = armor_piece

    @classmethod
    def load_armor_from_file(cls, armor_name: str):
        """Returns an armor instance of the specified armor."""
        try:
            with open(cls._path_to_armor_preset_file_windows, 'r') as f:
                lines = f.read().splitlines()
                armor_arguments = []
                for line in lines:
                    armor_arguments.append(line.split(", "))
                first_item = [i[0] for i in armor_arguments]
                assert armor_name in first_item, \
                    f"{armor_name} does not exist in Character_Presets.txt"
                armor_arguments = armor_arguments[first_item.index(armor_name)]
                return Armor(armor_arguments[0], Jobs[armor_arguments[1]], int(armor_arguments[2]),
                             int(armor_arguments[3]), ArmorTypes[armor_arguments[4]], ArmorPieces[armor_arguments[5]])
        except FileNotFoundError:
            with open(cls._path_to_armor_preset_file_mac, 'r') as f:
                lines = f.read().splitlines()
                armor_arguments = []
                for line in lines:
                    armor_arguments.append(line.split(", "))
                first_item = [i[0] for i in armor_arguments]
                assert armor_name in first_item, \
                    f"{armor_name} does not exist in Character_Presets.txt"
                armor_arguments = armor_arguments[first_item.index(armor_name)]
                return Armor(armor_arguments[0], Jobs[armor_arguments[1]], int(armor_arguments[2]),
                             int(armor_arguments[3]), ArmorTypes[armor_arguments[4]], ArmorPieces[armor_arguments[5]])



class Spell:
    """Spell data type that holds all the relevant information for all spells."""
    _path_to_spell_preset_file_windows = os.getcwd() + "\\Spells.txt"
    _path_to_spell_preset_file_mac = os.getcwd() + "/Spells.txt"

    def __init__(self, name: str, mag_damage: int, is_area_of_effect_damage: bool,
                 effect: Effects = Effects.NONE, effect_chance: float = 1.0, effect_amt: int = 0):
        """Creates the Spell instance.

        Keyword arguments:
        name -- the name of this item
        damage -- the default damage this spell does
        is_AOE -- does the spell afflict damage over all enemies
        effect -- the specific effect this spell causes.
        effect_chance -- the percentage of the effect being activated
        effect_amt -- the amount of effect the effect causes
        """
        assert isinstance(name, str), f"Name expected to be string type, got: {type(name)}"
        assert isinstance(mag_damage, int), f"Damage expected to be Integer type, got: {type(mag_damage)}"
        assert isinstance(is_area_of_effect_damage, bool), f"Is_AOE expected to be Boolean type, " \
                                                           f"got: {type(is_area_of_effect_damage)}"
        assert isinstance(effect, Effects), f"Effect expected to be Effects type, got: {type(effect)}"
        assert isinstance(effect_chance, float), f"Effect_Chance expected to be Float type, got: {type(effect_chance)}"
        assert isinstance(effect_amt, int), f"Effect_Amount expected to be integer type, got: {type(effect_amt)}"
        self.name = name
        self.mag_damage = mag_damage
        self.is_AOE = is_area_of_effect_damage
        self.effect = effect
        self.effect_chance = effect_chance
        self.effect_amt = effect_amt

    @classmethod
    def load_spell_from_file(cls, spell_name: str):
        """Loads a spell from the spells.txt file and returns it as a spell instance."""
        try:
            with open(cls._path_to_spell_preset_file_windows, 'r') as f:
                lines = f.read().splitlines()
                spell_arguments = []
                for line in lines:
                    spell_arguments.append(line.split(", "))
                first_item = [i[0] for i in spell_arguments]
                assert spell_name in first_item, \
                    f"{spell_name} does not exist in Character_Presets.txt"
                spell_arguments = spell_arguments[first_item.index(spell_name)]
                return Spell(spell_arguments[0], int(spell_arguments[1]),
                True if spell_arguments[2] == "TRUE" else False, effect=Effects[spell_arguments[3]],
                                effect_chance=float(spell_arguments[4]), effect_amt=int(spell_arguments[5]))
        except FileNotFoundError:
            with open(cls._path_to_spell_preset_file_mac, 'r') as f:
                lines = f.read().splitlines()
                spell_arguments = []
                for line in lines:
                    spell_arguments.append(line.split(", "))
                first_item = [i[0] for i in spell_arguments]
                assert spell_name in first_item, \
                    f"{spell_name} does not exist in Character_Presets.txt"
                spell_arguments = spell_arguments[first_item.index(spell_name)]
                return Spell(spell_arguments[0], int(spell_arguments[1]),
                             True if spell_arguments[2] == "True" else False, effect=Effects[spell_arguments[3]],
                             effect_chance=float(spell_arguments[4]), effect_amt=int(spell_arguments[5]))

class Potion:
    """Potion data type that holds all the relevant information for all potions."""
    _path_to_potion_preset_file_windows = os.getcwd() + "\\Potions.txt"
    _path_to_potion_preset_file_mac = os.getcwd() + "/Potions.txt"
    def __init__(self, name: str, effect: Effects, effect_amt: int, effect_chance: float = 1):
        """Creates the Potion instance.

        Keyword arguments:
        name -- the name of this item
        effect -- the specific effect this potion causes
        effect_chance -- the percentage of teh effect being activated
        effect_amt -- the amount of effect the effect causes
        """
        assert isinstance(name, str), f"Name expected to be string type, got: {type(name)}"
        assert isinstance(effect, Effects), f"Effect expected to be Effects type, got: {type(effect)}"
        assert isinstance(effect_chance, float), f"Effect_Chance expected to be Float type, got: {type(effect_chance)}"
        assert isinstance(effect_amt, int), f"Effect_Amount expected to be integer type, got: {type(effect_amt)}"
        self.name = name
        self.effect = effect
        self.effect_chance = effect_chance
        self.effect_amt = effect_amt

    def use(self, character):
        """Applies the potions effect to the player"""
        character.afflict(self.effect, self.effect_amt, self.effect_chance)

    @classmethod
    def load_potion_from_file(cls, potion_name: str):
        """Loads a potion from the potions.txt file and returns it as a potion instance."""
        try:
            with open(cls._path_to_potion_preset_file_windows, 'r') as f:
                lines = f.read().splitlines()
                potion_arguments = []
                for line in lines:
                    potion_arguments.append(line.split(", "))
                first_item = [i[0] for i in potion_arguments]
                assert potion_name in first_item, \
                    f"{potion_name} does not exist in Character_Presets.txt"
                potion_arguments = potion_arguments[first_item.index(potion_name)]
                return Potion(potion_arguments[0], Effects[potion_arguments[1]],
                              effect_chance=float(potion_arguments[2]), effect_amt=int(potion_arguments[3]))
        except FileNotFoundError:
            with open(cls._path_to_potion_preset_file_mac, 'r') as f:
                lines = f.read().splitlines()
                potion_arguments = []
                for line in lines:
                    potion_arguments.append(line.split(", "))
                first_item = [i[0] for i in potion_arguments]
                assert potion_name in first_item, \
                    f"{potion_name} does not exist in Character_Presets.txt"
                potion_arguments = potion_arguments[first_item.index(potion_name)]
                return Potion(potion_arguments[0], Effects[potion_arguments[1]],
                              effect_chance=float(potion_arguments[2]), effect_amt=int(potion_arguments[3]))
    @classmethod
    def stack_potions(cls, potions: list):
        """Turns a list of potions into a dictionary."""
        potion_dict = {}
        potion_list = potions
        while len(potion_list) > 0:
            amount = 1
            potion_temp = potion_list[0]
            del(potion_list[0])
            if len(potion_list) == 0:
                potion_dict.update([(potion_temp, amount)])
                return potion_dict
            i = 1
            for potion in potion_list:
                if potion_temp == potion:
                    del(potion_list[i])
                    amount += 1
                i += 1
            potion_dict.update([(potion_temp, amount)])
        return potion_dict

