from Constants import *
import os


class Item:
    """Item data type that holds all relevant information for misc. items"""
    def __init__(self, name: str, cost: int = 0):
        """Creates the Item instances
        """
        assert isinstance(name, str), f"Name expected to be string type, got: {type(name)}"
        assert isinstance(cost, int) and cost >= 0, f"Cost expected to be a positive Integer, " \
                                                    f"got: {type(cost)} with a value {cost}"
        self.name = name
        self.cost = cost


class Weapon:
    """Weapon data type that holds all the relevant information for all weapon items."""
    _path_to_character_preset_file = os.getcwd() + "\\Weapons.txt"

    def __init__(self, name: str, cost: int, job: Jobs, wpn_type: WpnTypes, phy_damage: int, mag_damage: int = 0,
                 effect: Effects = Effects.NONE, effect_chance: int = 100, effect_amt: int = 0):
        """Creates the Weapon instance.

        Keyword arguments:
        name -- the name of this item
        cost -- the value of this item in currency
        job -- the character class that this item is most effective for
        wpn_type -- the type of weapon it is
        damage -- the default damage this weapon does
        effect -- the specific effect this weapon causes (can't be applied to staffs)
        effect_chance -- the percentage of teh effect being activated
        effect_amt -- the amount of effect the effect causes
        """
        assert isinstance(name, str), f"Name expected to be string type, got: {type(name)}"
        assert isinstance(cost, int) and cost >= 0, f"Cost expected to be a positive Integer type, " \
                                                    f"got: {type(cost)} with a value {cost}"
        assert isinstance(job, Jobs), f"Job expected to be Jobs type, got: {type(job)}"
        assert isinstance(wpn_type, WpnTypes), f"Weapon_Type expected to be Wpn_Types type, got: {type(wpn_type)}"
        assert isinstance(phy_damage, int), f"Damage expected to be Integer type, got: {type(phy_damage)}"
        assert isinstance(effect, Effects), f"Effect expected to be Effects type, got: {type(effect)}"
        assert isinstance(effect_chance, float), f"Effect_Chance expected to be Float type, got: {type(effect_chance)}"
        assert isinstance(effect_amt, int), f"Effect_Amount expected to be integer type, got: {type(effect_amt)}"
        assert isinstance(mag_damage, int), f"Magical Damage expected to be integer type, got: {type(mag_damage)}"
        self.name = name
        self.cost = cost
        self.job = job
        self.wpn_type = wpn_type
        self.phy_damage = phy_damage
        self.effect = effect
        self.effect_chance = float(effect_chance) / 100
        self.effect_amt = float(effect_amt) / 100
        self.mag_damage = mag_damage

    @classmethod
    def load_weapon_from_file(cls, weapon_name: str):
        """Returns a weapon instance of the specified weapon."""
        # TODO


class Armor:
    """Weapon data type that holds all the relevant information for all weapon items."""
    _path_to_character_preset_file = os.getcwd() + "\\Armor_Pieces.txt"

    def __init__(self, name: str, cost: int, job: Jobs, phy_neg: int, magic_neg: int, armor_type: ArmorTypes,
                 armor_piece: ArmorPieces):
        """Creates the Armor Instance.

        Keyword arguments:
        name -- the name of this item
        cost -- the value of this item in currency
        job -- the character class that this item is most effective for
        phy_neg -- the amount of physical damage absorbed by the armor piece
        magic_neg -- the amount of magical damage absorbed by the armor piece
        armor_type -- the type of armor it is (Plated, chain, and leather)
        armor_piece -- the type of armor piece it is (Helmet, breastplate, and grieves)
        """
        assert isinstance(name, str), f"Name expected to be string type, got: {type(name)}"
        assert isinstance(cost, int), f"Cost expected to be Integer type, got: {type(cost)}"
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
        self.cost = cost
        self.job = job
        self.phy_neg = float(phy_neg / 100)
        self.magic_neg = float(magic_neg / 100)
        self.armor_type = armor_type

    @classmethod
    def load_armor_from_file(cls, armor_name: str):
        """Returns an armor instance of the specified armor."""
        # TODO


class Spell:
    """Spell data type that holds all the relevant information for all spells."""
    _path_to_character_preset_file = os.getcwd() + "\\Spells.txt"

    def __init__(self, name: str, cost: int, mana_cost: int, mag_damage: int, is_area_of_effect_damage: bool,
                 effect: Effects = Effects.NONE, effect_chance: int = 100, effect_amt: int = 0):
        """Creates the Spell instance.

        Keyword arguments:
        name -- the name of this item
        cost -- the value of this item in currency
        mana_cost -- the amount of mana expended in casting this spell
        damage -- the default damage this spell does
        is_AOE -- does the spell afflict damage over all enemies
        effect -- the specific effect this spell causes.
        effect_chance -- the percentage of teh effect being activated
        effect_amt -- the amount of effect the effect causes
        """
        assert isinstance(name, str), f"Name expected to be string type, got: {type(name)}"
        assert isinstance(cost, int), f"Cost expected to be Integer type, got: {type(cost)}"
        assert isinstance(mana_cost, int), f"Mana_cost expected to be Integer type, got: {type(mana_cost)}"
        assert isinstance(mag_damage, int), f"Damage expected to be Integer type, got: {type(mag_damage)}"
        assert isinstance(is_area_of_effect_damage, bool), f"Is_AOE expected to be Boolean type, " \
                                                           f"got: {type(is_area_of_effect_damage)}"
        assert isinstance(effect, Effects), f"Effect expected to be Effects type, got: {type(effect)}"
        assert isinstance(effect_chance, float), f"Effect_Chance expected to be Float type, got: {type(effect_chance)}"
        assert isinstance(effect_amt, int), f"Effect_Amount expected to be integer type, got: {type(effect_amt)}"
        self.name = name
        self.cost = cost
        self.mana_cost = mana_cost
        self.mag_damage = mag_damage
        self.is_AOE = is_area_of_effect_damage
        self.effect = effect
        self.effect_chance = float(effect_chance) / 100
        self.effect_amt = effect_amt

    @classmethod
    def load_spell_from_file(cls, spell_name: str):
        """Loads a spell from the spells.txt file and returns it as a spell instance."""
        # TODO


class Potion:
    """Potion data type that holds all the relevant information for all potions."""
    _path_to_character_preset_file = os.getcwd() + "\\Potions.txt"

    def __init__(self, name: str, cost: int, effect: Effects, effect_amt: int, effect_chance: int = 100):
        """Creates the Potion instance.

        Keyword arguments:
        name -- the name of this item
        cost -- the value of this item in currency
        effect -- the specific effect this potion causes
        effect_chance -- the percentage of teh effect being activated
        effect_amt -- the amount of effect the effect causes
        """
        assert isinstance(name, str), f"Name expected to be string type, got: {type(name)}"
        assert isinstance(cost, int), f"Cost expected to be Integer type, got: {type(cost)}"
        assert isinstance(effect, Effects), f"Effect expected to be Effects type, got: {type(effect)}"
        assert isinstance(effect_chance, float), f"Effect_Chance expected to be Float type, got: {type(effect_chance)}"
        assert isinstance(effect_amt, int), f"Effect_Amount expected to be integer type, got: {type(effect_amt)}"
        self.name = name
        self.cost = cost
        self.effect = effect
        self.effect_chance = float(effect_chance) / 100
        self.effect_amt = effect_amt

    @classmethod
    def load_potion_from_file(cls, potion_name: str):
        """Loads a potion from the potions.txt file and returns it as a potion instance."""
        # TODO

    @classmethod
    def stack_potions(cls, potions: list):
        """Turns a list of potions into a dictionary."""
        # TODO
