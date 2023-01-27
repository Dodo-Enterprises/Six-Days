from enum import Enum


class Jobs(Enum):
    ANY = -1
    WARRIOR = 0
    MAGE = 1


class WpnTypes(Enum):
    NONE = -1
    SLASH = 0
    BLUNT = 1
    PIERCE = 2
    STAFF = 3


class Effects(Enum):
    NONE = -1
    BURN = 0
    FREEZE = 1
    STUN = 2
    POISON = 3
    HEALTH = 4
    STRENGTH = 5
    DEFENSE = 6
    MAGIC = 7


class ArmorTypes(Enum):
    NONE = -1
    LEATHER = 0
    CHAIN = 1
    PLATE = 2


class ArmorPieces(Enum):
    NONE = -1
    HELMET = 0
    BREASTPLATE = 1
    GRIEVES = 2
    SHIELD = 3