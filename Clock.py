from Character import Character
from BattleSystem import BattleSystem
from Items import *


class Clock:
    """"""

    def __init__(self, player: Character):
        self.player = player

    def start(self):
        """
  #IMPORTANT Also need to add specific weapons for the mage class after winning a fight
        # and all armor for both classes. Add whatever you think is appropriate.
        #Also change the range if need be. I don't know the numbers. This is for the rest going on
            :return: True if beat game
            """

        # All the code for the clock arc
        print("\nYou enter the Clock Kingdom. Everything looks peaceful and no demons are attacking the kingdom. "
              "\nYou see a city in the distance. You walk towards the city doubting what is going on here. ")
        input()
        print("In the city, all the people are happy and in the marketplace, "
              "\nthere are no poor or disabled people begging for money. ")
        input()
        print("At the marketplace, a man with a black coat bumps into you. "
              "\nThe man smelled like a dead body and had bandages everywhere on his body. "
              "\nHe just walked away not even saying sorry to you.")
        input()
        print("While you are still walking through the marketplace thinking how it contradicts what "
              "\nMuriel explained about this kingdom, you saw three children playing, praising the name of their king.")
        input()
        # Player and kid interation
        print("Do you want to talk to them? ")
        input()
        i = 1
        while True:
            print("Talk (1)")
            print("Walk (2)")
            try:
                ans = input()
                assert ans == "1" or ans == "2"
            except AssertionError:
                print("Invalid command try again.")
                continue
            if ans == "1":
                print("You go talk with children about their king")
                input()
                print("Player: Mind if I join you?")
                input()
                print("Boy 1: Sure! You can be Gavriel Utterson and I will be mighty Clockyll Tymdal")
                input()
                print("Boy 2: I want to be Clockyll Tymdal!")
                print("\nI want to be Clockyll Tymdal!")
                print("Girl 1: I will be the princess ")
                input()
                print("Player (stopping the fight between boys 1 and 2): Kids, who is Gavriel Utterson? ")
                input()
                print("Girl 1: You don’t know Gavriel Utterson?")
                input()
                print("Boy 2: Gavriel Utterson is a friend of Clockyll Tymdal! "
                      "\nHe is a hunter who hunts down demons. "
                      "\nHe always wears a black coat and uses weapons from other continents. "
                      "\nIt blasts fire without using magic! ")
                input()
                break
            else:
                print("Ignore children and keep walking")
                input()
                break

        print("With many doubts, you visit the nearest hotel and spend a night there."
              "\nThe next day, as you walk down the street, you see the sky turn dark and blood starts to rain. "
              "\nDemons rush into the city and start to kill the citizens.")
        input()
        print("Boy 1: Help!"
              "\nCitizen 1: I don’t want to die!"
              "\nCitizen 2: Leave me alone!")
        input()
        print("Soon, screaming and sorrow fill every corner of the city. "
              "\nEvery street of the city turns into a river of blood. "
              "\nWith rage, you decided to kill every demon. ")
        input()
        # Battle 8
        # Three demons at the same time
        if BattleSystem.load_battle_from_file(self.player, 8).start():
            self.player.add_to_inventory([Potion.load_potion_from_file("Health (M)") for i in range(5)])
            print("You Won")
            print("Player received 5 Potions(M)")
        else:
            print("You Lose")
            return False
        print("Knights and wizards of Clock Kingdom also start to fight against demons. "
              "\nAll the knights and wizards were so strong that they were able "
              "\nto kill every demon that invaded the kingdom. "
              "\nThe knights made a defense line to protect the citizens "
              "\nand the wizards created traps for upcoming attacks.")
        input()
        print("The next day, you see more demons charging into the Clock Kingdom along with dragons from the sky. "
              "\nAmong them, you see a gigantic dragon with three heads on it. "
              "\nOne of its heads was cut out and its skin was ruined by unknown magic.")
        input()
        # Battle 9 against 2 dragons
        if BattleSystem.load_battle_from_file(self.player, 9).start():
            self.player.add_to_inventory(Weapon.load_weapon_from_file("Dragon Claw (M)"))
            print("You Won")
            print("Player received a Dragon Claw (M)")
        else:
            print("You Lose")
            return False
        print("Player received Dragon Scale Armor")
        input()
        print("The dragons were so strong that knights and wizards of the clock kingdom died one by one. "
              "\nThe gigantic dragon attacks the player ")
        # Battle 10 ???
        # Battle
        input()
        # Loses this battle
        print("You see the man with the black coat with a weird magic wand that you didn’t see before. "
              "\nThe man used his magic wand and blasted fire toward the gigantic dragon.")
        input()
        print("Man: Fortissax! I am here to take your other heads!")
        input()
        print("The gigantic dragon, Fortissax, created enormous lightning bolts. "
              "\nFortissax throws the black and dark yellow lightning bolt at the man.")
        input()
        print("As soon as the lightning touched the ground, it created a gray ominous fog. "
              "\nAnything that touched the fog lost its life. "
              "\nThe man jumped at Fortissax and blasted one of its remaining heads.")
        input()
        print("However, the man lost his arm in an attack on the last head and fell to the ground")
        input()
        print("Man: I… I cannot stop the loop… or I cannot die… he does not allow me to… I need the dragon heart… "
              "\nI need it to defeat everything… ")
        input()
        print("You see Fortissax fly in for the  kill the man")
        input()
        print("???: Disappear.")
        input()
        print("At once, Fortissax exploded leaving nothing left.")
        input()
        print("???: You cannot die now, my friend. You need to save this kingdom with me forever. ")
        input()
        print("Man: Please just kill me…")
        input()
        print("???: Okay, I will.")
        input()
        print("The man’s body explodes, but you see the man regenerate immediately. ")
        input()
        print("???: You haven’t forgotten have you? You cannot die, my friend. "
              "\nI changed you with my power and my power is over everything. Let’s start again.")
        input()
        print("??? takes his sword out and it shines with bright blue light. "
              "\nThe light started to devour everything nearby.")
        input()
        print("When the light starts to devour you, you see Muriel and she teleports you out of the kingdom.")
        input()
        print("Muriel: What are you doing? Two years already passed since you entered the kingdom.")
        input()
        print("I cannot sneak into the kingdom anymore without Clockyll Tymdal knowing. That was the only chance. ")
        input()
        print("Next time you enter the kingdom, you must take the artifact from the king, "
              "\nor else you will stay in the loop forever.")
        input()
        print("Now you re-enter the kingdom")
        input()
        print("You enter the Clock Kingdom. "
              "\nEverything looks peaceful and none of the demons are attacking the kingdom. "
              "\nYou see the city from a far distance. "
              "\nYou walk towards the city hoping the peace last forever…")
        input()
        print("In the city, all people are happy and in the marketplace, "
              "\nthere are no poor or disabled begging for money. ")
        input()
        print("At the marketplace, a man with a black coat bumps into you. "
              "\nThe man smells like a dead body and has bandages everywhere on his body. "
              "\nHe just works away, not even saying sorry to you. "
              "\nYou stopped him from walking away.")
        input()
        # Talk to Mysterious Man
        while True:
            print("End loop (1)")
            print("Kill Dragon(2)")
            try:
                ans = input()
                assert ans == "1" or ans == "2"
            except AssertionError:
                print("Invalid command. try again.")
                continue
            match ans:
                case "1":
                    print("“I can help you to kill the dragon")
                    input()
                    break
                case "2":
                    print("I will help you end the loop")
                    input()
                    print("Man: You don’t know what you are talking about. "
                          "\nIf you know anything about this loop, prove it to me.")
                    input()
                    break
        # Battle 11 Fight against man
        if BattleSystem.load_battle_from_file(self.player, 11).start():
            print("You Won")
        else:
            print("You Lose")
            return False
        input()
        print("Man: You have the artifacts of the kings. Interesting, you want the artifact of Clockyll Tymdal. "
              "\nWell, then you can at least survive his magic.")
        input()
        print("The only way to kill him is by using the dragon's heart which gives "
              "\nthe special power of the dragon to whoever eats it. But whoever eats it will die in an hour.")
        input()
        print("Help me kill the dragon then we can end to loop. If so, the artifact will be yours eventually."
              "\nHere take this sword")
        self.player.add_to_inventory(Weapon.load_weapon_from_file("Death Sword (H)"))
        print("Player received a Death Sword")
        input()
        print("By the way, my name is Gavriel Utterson. See you in two days. ")
        input()
        print("After meeting Gavriel Utterson, you visited the nearest hotel and spend a night there.")
        input()
        print("The next day, as you were walking down the street, "
              "\nyou see the sky turn dark and blood started to rain. "
              "\nDemons rush into the city and start to kill every person.")
        input()
        print("Boy 1: Help! "
              "\nCitizen 1: I don’t want to die "
              "\nCitizen 2: Leave me alone! ")
        input()
        print("Soon, the screaming and sorrow fill the city. Every street in the city turns into a river of blood. "
              "\nYou see many bodies of people everywhere in the city. ")
        # Battle 12 (Grab 8th battle)
        # Three demons at the same time
        if BattleSystem.load_battle_from_file(self.player, 12).start():
            print("You Won")
        else:
            print("You Lose")
            return False
        input()
        print("Knights and wizards of the Clock Kingdom also start to fight against demons. "
              "\nAll the knights and wizards were strong enough that "
              "\nthey were able to kill every demon that invaded the kingdom. ")
        input()
        print("The Knights made a defense line to protect citizens and the "
              "\nwizards created traps for upcoming attacks.")
        print("\nThe next day, you see more demons charging to the Clock Kingdom along with dragons from the sky. "
              "\nFortissax also appeared with other dragons.")
        input()
        print("Gavriel Utterson joins and Fortissax flies down to you "
              "/nthrowing lightning bolts that have the power of death.")
        input()
        # 2nd Battle against Fortissax this time with ally (Battle 13)
        if BattleSystem.load_battle_from_file(self.player, 13).start():
            self.player.add_to_inventory(Weapon.load_weapon_from_file("Lightning Claw (H)"))
            print("Player received a Lightning Claw (H)")
        else:
            print("You Lose")
            return False
        print("\nPlayer received Staff of Dragon Lord and"
              "\nLightning Claw!")
        input()
        print("Fortissax falls down to the ground.")
        input()
        print("Gavriel Utterson: I… I… made it happen. "
              "\nGavriel Utterson eats the dragon heart. "
              "\nThe power of Fortissax came to Gavriel Utterson.")
        input()
        print("???: Amazing, you finally made it. But what does that change?")
        input()
        print("Gavriel Utterson: Clockyll Tymdal…")
        input()
        # Batte (14) It's the Boss with ally
        if BattleSystem.load_battle_from_file(self.player, 14).start():
            self.player.add_to_inventory(Weapon.load_weapon_from_file("Sword of Kangmar (H)"))
            print("You Won")
            print("Player received a Sword of Kangmar (H)")
        else:
            print("You Lose")
            return False
        input()
        print("Gavriel Utterson used the power of Fortissax.")
        input()
        print("Clockyll: That may kill me but can you even attack me? ")
        input()
        print("Gavriel Utterson jumps to tackle Tymdal. "
              "\nTymdal makes Gavriel Utterson’s legs disappear. "
              "\nHe falls to the ground.")
        input()
        print("Clockyll: It is over!")
        input()
        print("Gavriel: No it’s not over yet… I am not alone this time.")
        input()
        print("You charge Tymdal for the last attack. "
              "\nHe tries to attack you with his magic but the power of artifacts protected you from it. ")
        input()
        print("Clockyll: What, no! NOOO!!!")
        input()
        print("Gavriel: Everything is over… Everyone in the clock kingdom can live peacefully…")
        input()
        print("Good job kid. You saved everyone in this kingdom. I cannot believe that my dream had come true.")
        input()
        print("You walk away from the Clock Kingdom to your next destination. "
              "\nYou hear a banging sound from far away, it’s the sound of Gavriel Utterson’s foreign magic wand.")
        input()
        print("On the ground near the remains of Tymdall You have obtained the last artifact, "
              "\nThe Sword of Transcendence!")
        input()
        # Player goes back to town for the last time
        print("Muriel: Oh JajaWawa! Wait don’t tell me"
              "\nYou conquered the last kingdom, didn’t you?")
        input()
        print("Oh, I’m so proud of you, you’ve gotten so strong! Ragnar come, come!")
        input()
        print("Ragnar: Oh I can’t believe it. A hero has finally risen up and collected all of the artifacts!")
        input()
        print("That just leaves one last thing to do. ")
        input()
        print("Defeat the demon king!")
        input()
        print("Our fate is in your hands JajaWawa!")
        input()
        print("Muriel: Good luck and save Ostrania!")
        input()

        return True
