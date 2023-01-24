from enum import Enum


class Jobs(Enum):
    WARRIOR = 0
    MAGE = 1


class WpnTypes(Enum):
    SHARP = 0
    BLUNT = 1
    SHIELD = 2
    RANGED = 3
    STAFF = 4


class Effects(Enum):
    BURNED = 0
    FROZEN = 1
    SHOCKED = 2
    POISONED = 3
    HEALTH = 4
    STRENGTH = 5
    DEFENSE = 6
    MAGIC = 7


class ArmorTypes(Enum):
    LEATHER = 0
    CHAIN = 1
    PLATE = 2


class ArmorPieces(Enum):
    HELMET = 0
    BREASTPLATE = 1
    GRIEVES = 2