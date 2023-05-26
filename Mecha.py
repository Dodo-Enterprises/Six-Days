from Character import Character
from BattleSystem import BattleSystem
from Items import *
class Mecha:
    """"""

    def __init__(self, player: Character):
        self.player = player

    def start(self):
        """
  #IMPORTANT--- Also need to add specific weapons for the mage class after winning a fight
        # and all armor for both classes. Add whatever you think is appropriate.
        # Also change the range if need be. I don't know the numbers. This is for the rest going on
        :return: player
        """
        self.player.add_to_inventory([Potion.load_potion_from_file("Health (M)") for i in range(5)])
        print("Player received 5 Potions (L)")
        print("\nYou enter the Mecha Kingdom. "
            "\nYou see a huge plane with a beautiful sky. It was hard to believe that this is a land that no one leaves.")
        input()
        print("When you look around, you see a little town. "
            "\nSurprisingly, you see some people working on the land from a far distance. ")
        input()
        print("You: Didn’t Muriel say that the people evacuated due to the king’s order? "
            "\nYou walk to the town with little questions. ")
        input()
        print("By the time you reach the town, you are able to see people a lot closer. You are surprised at their appearance. "
            "\nThey are humans made out of metal! ")
        input()
        print("You: What is going on here??? ")
        input()
        print("One of the men who are working in the field sees you. ")
        input()
        print("Mecha man 1: You have real flesh! How did you survive the king’s artifact???")
        input()
        print("You: What do you mean by surviving the king's artifact? Didn’t all the citizens evacuate?")
        input()
        print("Mecha man 1: Yes, that is what is known to the public. "
            "\nBut the truth is that the king when the demon king attacked our kingdom, "
            "\nused his artifact to turn everyone in the kingdom into cyborgs. ")
        input()
        print("You: How dare he! What happened next?")
        input()
        print("Mecha Man 1: Then the king built a watch tower to look over everyone. "
            "\nWhen he sees something else than a cyborg, he strikes his magic to kill it. My name is James.")
        input()
        print("Come to my house you need to hide, or the king will find you and kill you! "
            "\nYou follow James, and James brings you to his house. At James’ house, you see two other mecha men.")
        input()
        print("James: This is Peter, the fisherman. Also, he is the strongest man in the town. You see Peter.")
        input()
        print("Peter is a man with a lot of hair and a curly mustache. Also, you are able to see his bulky muscles.")
        input()
        print("James: This other man is John. He is very smart. Probably the wisest man in the town.")
        input()
        print("John was a very tall skinny man.When you saw Peter and John, they looked very angry. "
            "\nSoon, realize the reason why.")
        input()
        print("Peter: What are you doing James?! Are you stupid? You brought a non-cyberized man. "
            "\nNo one is allowed to be organic except the king! Did you not see what happened to Andrew two years ago? "
            "\nWhen the king found out Andrew hid a normal man, the king killed the man with everyone in Andrew’s family! "
            "\nAndrew, his wife, children, and even the cousins were killed! Leave him out and let him die by himself.")
        input()
        print("John: James, don’t take Peter’s word in your heart. He said that since he cares about you. Please forgive him. "
            "\nHowever, Peter is right about bringing man into our house. We have family and friends, James. "
            "\nPlease leave the man alone. Let the king decide his fate. ")
        input()
        print("James: No I can’t let him go. I cannot let any more men die in this kingdom by the king. "
            "\nOkay, then I will bring him to the cabin at the top of the hill. I will be back soon. ")
        input()
        print("Peter: What is wrong with you James? Just leave him alone. ")
        input()
        print("John: Okay go and put him in the cabin. Then, you need to come back alone. Let’s live a normal life.")
        input()
        print("James: Thank you John, and I am sorry Peter. I cannot let anyone die anymore. James drags you out of the house. "
            "\nYou follow him and start to walk up to the hill. The hill was far away from the town. "
            "\nAt the top of the hill, you are able to see the town clearly. ")
        input()
        print("James: Isn’t it beautiful? I am sorry. As you heard from Peter, many died helping non-cyber people like you. "
            "\nPlease understand them. There are good people in their hearts.")
        input()
        print("You entered the cabin with James.")
        input()
        print("James: Here is some food to eat. You can stay here for about 20 days. "
            "\nMeanwhile, find a way to run away from the kingdom. Boom! You hear a loud sound nearby. "
            "\nWhen you exit the cabin, you see the town burned down by the king. ")
        input()
        print("James: No! Peter, John!")
        input()
        print("James starts to run down the hill. You follow James to the town. At James’s house, you see Peter injured. ")
        input()
        print("James: Peter! Peter! What happened? Where is John? What happened? ")
        input()
        print("Peter: It is all your fault! You killed John. You killed everyone in the town. Peter goes silent. "
            "\nJames mourns for his loss, but no tears came out from the machine’s eyes.")
        input()
        print("You: Are you okay? ")
        input()
        print("James: Leave me alone! You killed my friends. Why did you come here?! Everything is your fault! ")
        print("\nThat night, the rain came to the town. "
            "\nYou leave James alone and stay at one of the destroyed houses in the town. "
            "\nThe rain ran down James’s face.")
        input()
        print("The next day, when you wake up and start to pack up to leave the town, James comes to you.")
        input()
        print("James: I am sorry for yesterday. But I want to know the reason you came to this kingdom. ")
        input()
        print("You explained everything to James.  "
            "\nYou fought in the crystal kingdom, and your goal is to collect all the artifacts to kill the demon king. ")
        input()
        print("James: So you are trying to take the artifact from the king. Let me help you. "
            "\nI know the location of the entrance of the king's watch tower. I worked there before I came to this town")
        input()
        print("Let me help you so that I may avenge John and Peter. You started to walk with James to the king’s watch tower. "
            "\nYou are attacked by cyberized guards!")
        input()
        #Battle 4
        self.player.health = 200
        if BattleSystem.load_battle_from_file(self.player, 4).start():
            print("You Won")
            if self.player.job == Jobs.WARRIOR:
                self.player.add_to_inventory(Weapon.load_weapon_from_file("Electric Spear (M)"))
                print("Player received an Electric Spear(M)")
        else:
            print("You Lose")
            return False
        input()
        #Battle 5
        self.player.health = 200
        if BattleSystem.load_battle_from_file(self.player, 5).start():
            print("You Won")
        else:
            print("You Lose")
            return False
        input()
        print("After a while, you finally make it to the king’s tower. "
            "\nIn front of the tower, there are many guards protecting the watchtower.")
        input()
        print("James: There are too many guards. I will lure them. Go inside the watchtower and kill the guards.")
        input()
        print("James jumps into the middle of the guards. Then James starts to run away. "
            "\nMost of the guards start to follow James and only a few guards remain at the entrance.")
        input()
        print("After you leave John with the guards, "
            "\nyou evade the remaining guards and enter the king’s watch tower. "
            "\nThe tower is very tall that you cannot see the end of it. ")
        input()
        print("At the top of the tower, you finally meet the king.")
        input()
        print("Wingard Levioso: You are finally here the man with flesh. "
            "\nYou will die like everyone in the town who tried to help you! ")
        input()
        #Battle 6 (Boss)
        self.player.health = 200
        if BattleSystem.load_battle_from_file(self.player, 6).start():
            print("You Won, or did you?")
        else:
            print("You Lose")
            return False
        print("You stab your weapon into Wingard Levioso’s heart. However, Wingard Levioso remains alive. ")
        input()
        print("Wingard Levioso: Did you think you could kill me? There’s no flesh nor blood within this cloak to kill. "
            "\nThere is only one idea. And ideas are weapon-proof. The flesh cannot defeat my ideas. "
            "\nEverything needs to turn into machines for time is limited to flesh and machines are everlasting. "
            "\nYou cannot kill me you fool. You will also die like your friend here. ")
        input()
        print("Wingard Levioso brings James in front of you. ")
        input()
        print("James: Please, for John and for Peter…")
        input()
        print("Wingard Levioso squeezes James’ head. Soon, James’ head exploded. ")
        input()
        print("Wingard Levioso: You think your friend can run away from my army? "
            "\nEveryone who helps you will die along with you. ")
        input()
        #Boss. Battle #7
        self.player.health = 200
        if BattleSystem.load_battle_from_file(self.player, 7).start():
            print("You Won")
            self.player.add_to_inventory(Armor.load_armor_from_file("Magic Helmet"))
            self.player.add_to_inventory(Armor.load_armor_from_file("Magic Chest"))
            self.player.add_to_inventory(Armor.load_armor_from_file("Magic Legs"))
            print("Player received Magic armor set")
            if self.player.job == Jobs.MAGE:
                self.player.add_to_inventory(Weapon.load_weapon_from_file("Staff of Wingard Levioso (M)"))
                self.player.add_to_inventory(Spell.load_spell_from_file("Lazer"))
                print("Player received Staff of Wingard Levioso and the Lazer spell")
        else:
            print("You Lose")
            return False
        input()
        print("Wingard Levioso: No, no. Why was my idea not unstoppable? Why? ")
        input()
        print("You took The Armor of Construction from Wingard Levioso. ")
        input()
        print("You look at James’s lifeless body and mourn. You are then determined to bring an end to all of this.")
        input()
        'Go back to town and talk to NPCs'
        print("Muriel: Oh welcome back, [player]! "
            "\nWith that fire in your eyes, I can already tell that you conquered another kingdom. Which one was it?")
        input()
        print("Oh, it was the Mecha kingdom ")
        input()
        print("Please …tell me, what happened with the king")
        input()
        print("Player explains everything")
        input()
        print("Levioso, oh how far you’ve fallen.")
        input()
        print("Just when I thought he had only abandoned us for his own selfish pride, ")
        input()
        print("Muriel falls to the floor and starts the cry. Ragnar then comes downstairs.")
        input()
        print("Ragnar: Levioso was once a great friend of ours. "
            "\nWe had personally recommended him to the high deity in order to become the ruler of the mecha kingdom. "
            "\nAfter all this time, he had only gotten worse. ")
        input()
        print("I’m so sorry Muriel and you,JaJaWaWa, for having to deal with him. "
              "\nI should have been a better judge of character when you first arrived")
        input()
        print("That leaves only one kingdom left to go. Keep going kid, you're in the endgame now!")
        input()
        print("")

        return self.player



