from enum import Enum


class Commands(Enum):
    HELP = "help"
    OPEN_INVENTORY = "inv"
    EQUIP = "equip"
    UNEQUIP = "unequip"
    ATTACK = "atk"
    TRASH = "trash"
    USE = "use"
    EXIT = "exit"
