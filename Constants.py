from enum import Enum


class Jobs(Enum):
    ANY = "ANY"
    NONE = "NONE"
    WARRIOR = "WARRIOR"
    MAGE = "MAGE"


class WpnTypes(Enum):
    NONE = "NONE"
    SLASH = "SLASH"
    BLUNT = "BLUNT"
    PIERCE = "PIERCE"
    STAFF = "STAFF"


class Effects(Enum):
    NONE = "NONE"
    BURN = "BURN"
    STUN = "STUN"
    HEALTH = "HEALTH"
    STRENGTH = "STRENGTH"
    DEFENSE = "DEFENSE"
    MAGIC = "MAGIC"
    DEATHTOUCH = "DEATHTOUCH"
    LIFESTEAL = "LIFESTEAL"


class ArmorTypes(Enum):
    NONE = "NONE"
    LEATHER = "LEATHER"
    CHAIN = "CHAIN"
    PLATE = "PLATE"


class ArmorPieces(Enum):
    # NONE = "NONE"
    HELMET = "HELMET"
    BREASTPLATE = "BREASTPLATE"
    GRIEVES = "GRIEVES"
    # SHIELD = "SHIELD"
