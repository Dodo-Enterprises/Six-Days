from Character import Character
from BattleSystem import BattleSystem
from Items import *
class Crystal:
    """"""

    def __init__(self, player: Character):
        self.player = player

    def start(self):
        """

        #IMPORTANT Also need to add specific weapons for the mage class after winning a fight
        # and all armor for both classes. Add whatever you think is appropriate.
        #Also change the range if need be. I don't know the numbers. This is for the rest going on

        :return: player
        """
        #All the code for the crystal arc
        self.player.add_to_inventory([Potion.load_potion_from_file("Health (L)") for i in range(5)])
        print("Player received 5 Potions (L)")
        print("You enter the Crystal Kingdom."
            "The crystals are everywhere and they are bright, "
            "fluorescent purple and it feels cold and lifeless inside. "
            "\nAs you enter you are shocked to see that there are plenty of townspeople frozen inside "
            "\nthe crystals. "
            "\nYou feel a swell of sorrow and anger toward the king for allowing this to happen to his kingdom." 
            "\nYou then come across bigger crystals that then come alive and attack you. "
            "\nThey seem to be possessed by the demon king’s minions.")
        #Battle 1
        self.player.health = 200
        if BattleSystem.load_battle_from_file(self.player, 1).start():
            print("You Won")
            if self.player.job == Jobs.WARRIOR:
                self.player.add_to_inventory(Weapon.load_weapon_from_file("Sword (L)"))
                print("Player received a Sword (L)")
            else:
                self.player.add_to_inventory(Weapon.load_weapon_from_file("Nice Wooden Staff (L)"))
                print("Player received a Nice Wooden Staff (L)")
        else:
            print("You Lose")
            return False
        input()
        #Battle 2
        self.player.health = 200
        if BattleSystem.load_battle_from_file(self.player, 2).start():
            print("You Won")
        else:
            print("You Lose")
            return False
        input()
        print("It seems these demons are pretty weak. Anyone with decent skills could get past these.")
        input()
        print("???: ROOOAAAARRRR!!!")
        input()
        print("You then hear a loud roar. "
            "You have no idea what thing made that sound but with your courage, you continue forward. ")
        input()
        print("After a bit more walking, you then make your way to the castle and enter it. "
            "\nYou see a bright glow coming from the throne room and make your way to it."
            "\nYou then are shocked to see the king frozen in his throne with the Crystal of Perpetuation.")
        input()
        print("You make your way to grab it-")
        input()
        print("???: ROOOAAAARRRR!!!")
        input()
        print("You turn around and you see a giant crystal golem ready to fight.")
        input()
        #Battle 3 (Boss)
        self.player.health = 200
        if BattleSystem.load_battle_from_file(self.player, 3).start():
            print("You Won")
            self.player.add_to_inventory(Armor.load_armor_from_file("Stone Head"))
            self.player.add_to_inventory(Armor.load_armor_from_file("Stone Chest"))
            self.player.add_to_inventory(Armor.load_armor_from_file("Stone Legs"))
            print("Player received the stone set of armor")
            if self.player.job == Jobs.WARRIOR:
                self.player.add_to_inventory(Weapon.load_weapon_from_file("Stone Hammer (L)"))
                print("Player received a Stone Hammer (L)")
            else:
                self.player.add_to_inventory(Spell.load_spell_from_file("Icespear"))
                print("Player received Icespear spell")
        else:
            print("You Lose")
            return False
        input()
        input()
        print("After a victorious cheer, you make your way to the king still frozen, "
            "\n and take the crystal from his cold hands.")
        input()
        print("It seem the king had perished while being frozen by his own hand. "
            "\n After you take the artifact you use its power to revert the townspeople back to normal and "
            "\n then they evacuate to another kingdom.  ")
        input()
        print("Jajawawa goes back to town and talks to Muriel and Ragnar. ")
        input()
        #The player defeated the first kingdom
        print("Muriel: Oh why if it isn’t JajaWawa, it has been a while. How’ve you been?")
        input()
        print("Muriel: Oh you got the Crystal of Perpetuation! This is marvelous! I just knew you could do it! "
            "\nRagnar come see this!")
        input()
        print("Ragnar: Hmm call me impressed JajaWawa it seems I’ve underestimated you. "
            "\nYes, it seems you may really have the tenacity to defeat the demon king. "
            "\nDon’t get too comfortable though, you’ve still got more kingdoms to do. "
            "\nDon’t lose that fire of yours, we’ll need it till the very end! ")
        input()
        print("Ragnar then goes to sit in his chair by the fire")
        input()
        print("Muriel: It seems Ragnar is starting to warm up to you. If you keep it up, "
            "\nI’m sure you’ll become good friends! ")
        input()
        print("Muriel: So now you have only two kingdoms left! Keep it up! ")
        input()
        print("")

        return self.player