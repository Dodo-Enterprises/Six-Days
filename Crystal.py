import Character
class Crystal:
    """"""

    def __init__(self, player: Character):
        self.player = player

    def start(self):
        """

        :return: player
        """
        #All the code for the crystal arc

        print("You enter the Crystal Kingdom."
            "The crystals are everywhere and they are bright, "
            "fluorescent purple and it feels cold and lifeless inside. "
            "\nAs you enter you are shocked to see that there are plenty of townspeople frozen inside "
            "\nthe crystals. "
            "\nYou feel a swell of sorrow and anger toward the king for allowing this to happen to his kingdom." 
            "\nYou then come across bigger crystals that then come alive and attack you. "
            "\nThey seem to be possessed by the demon king’s minions.")
        #Tis is supposed to be
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
        print("After a victorious cheer, you make your way to the king still frozen, "
            "\nand take the crystal from his cold hands.")
        input()
        print("It seem the king had perished while being frozen by his own hand. "
            "\nAfter you take the artifact you use its power to revert the townspeople back to normal and "
            "\nthen they evacuate to another kingdom.  ")
        input()
        print("The player goes back to town and talks to Muriel and Ragnar. ")
        input()
        # If the player defeated the first kingdom
        print("Muriel: Oh why if it isn’t JajaWawa, it has been a while. How’ve you been?")
        input()
        #Options
        print("Muriel: Oh you got the Crystal of Perpetuation! This is marvelous! I just knew you could do it! "
            "\nRagnar come see this!")
        input()
        print("Ragnar: Hmm call me impressed [player] it seems I’ve underestimated you. "
            "\nYes, it seems you may really have the tenacity to defeat the demon king. "
            "\nDon’t get too comfortable though, you’ve still got more kingdoms to do. "
            "\nDon’t lose that fire of yours, we’ll need it till the very end! ")
        input()
        print("Ragnar then goes to sit in his chair by the fire")
        input()
        print("Muriel: It seems Ragnar is starting to warm up to you. If you keep it up, "
            "\nI’m sure you’ll become good friends! ")
        input()
        self.player.add_to_inventory(self, )
        print("Muriel: So now you have only two kingdoms left! Keep it up! ")
        input()
        print("")

        return self.player()