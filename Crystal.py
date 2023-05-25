import Character
class Crystal:
    """"""

    def __init__(self, player: Character):
        self.player = player

    def start(self):
        """

        :return: player
        """
        # All the code for the crystal arc

        print("You enter the Crystal Kingdom."
              "The crystals are everywhere and they are bright, "
              "fluorescent purple and it feels cold and lifeless inside. "
              "As you enter you are shocked to see that there are plenty of townspeople frozen inside "
              "the crystals. "
              "You feel a swell of sorrow and anger toward the king for allowing this to happen to his kingdom." 
              "You then come across bigger crystals that then come alive and attack you. "
              "They seem to be possessed by the demon king’s minions.")
        input()
        print("It seems these demons are pretty weak. Anyone with decent skills could get past these.")
        print("???: ROOOAAAARRRR!!!")
        print("You then hear a loud roar. "
              "You have no idea what thing made that sound but with your courage, you continue forward. ")
        print("After a bit more walking, you then make your way to the castle and enter it. "
              "You see a bright glow coming from the throne room and make your way to it."
              "You then are shocked to see the king frozen in his throne with the Crystal of Perpetuation.")
        print("You make your way to grab it-")
        print("???: ROOOAAAARRRR!!!")
        print("You turn around and you see a giant crystal golem ready to fight.")
        print("After a victorious cheer, you make your way to the king still frozen, "
              "and take the crystal from his cold hands.")
        print("It seem the king had perished while being frozen by his own hand. "
              "After you take the artifact you use its power to revert the townspeople back to normal and "
              "then they evacuate to another kingdom.  ")
        print("The player goes back to town and talks to Muriel and Ragnar. ")
        # If the player defeated the first kingdom
        print("Muriel: Oh why if it isn’t [player], it has been a while. How’ve you been?")
        #Options
        print("Muriel: Oh you got the Crystal of Perpetuation! This is marvelous! I just knew you could do it! "
              "Ragnar come see this!")
        print("Ragnar: Hmm call me impressed [player] it seems I’ve underestimated you. "
              "Yes, it seems you may really have the tenacity to defeat the demon king. "
              "Don’t get too comfortable though, you’ve still got more kingdoms to do. "
              "Don’t lose that fire of yours, we’ll need it till the very end! ")
        print("Ragnar then goes to sit in his chair by the fire")
        print("Muriel: It seems Ragnar is starting to warm up to you. If you keep it up, "
              "I’m sure you’ll become good friends! ")
        self.player.add_to_inventory(self, )
        print("Muriel: So now you have only two kingdoms left! Keep it up! ")
        print("")

        return self.player