from Crystal import Crystal
from Character import Character
from Mecha import Mecha
from Clock import Clock
from Items import *

while True:
      #Intro
      print("\nThe land of Ostrania. A wonderful, vibrant land made by a high deity, Kangmar. ")
      input()
      print("Kangmar gave this land to three kings to rule peacefully.\nIt gave them three unique artifacts that granted the "
            "kings the necessary power in order to lead their kingdoms.\nThe Crystal of Perpetuation, The Armor of "
            "Construction, and The Sword of Transcendence.")
      input()
      print("They had ruled the land for 20 years with none being able to even invade the land.")
      input()
      print("Peace was short-lived,however, as the evil demon king despised everything that the deity had done for what he "
            "\nthought were lowly humans.")
      input()
      print("So he invaded the land of Ostrania and brought chaos to all who called it home.")
      input()
      print("The three kings were terrified of the demon’s power! "
            "\nThey had not been threatened at all since gaining their power. "
            "\nSo they completely shut down their kingdoms never to be seen again while "
            "\nkeeping the artifacts with them.")
      input()
      print("The deity was enraged at the cowardice of the kings and tried to reach out to them but to no avail. "
            "\nIt then tried to stop the demon king itself, but it was overpowered just barely escaping.")
      input()
      print("Ever since the demon came to rule over the land with his tyrannical fist, Ostrania was made a hell on earth for "
            "\nits citizens. . .")
      input()
      print("Old man: That is the full history of this land. Ugh, thanks for making me explain it all kid! My throat is "
            "\nparched and I’m all out of the water! ")
      input()
      print("\nThat demon king has made all the food and water really expensive and it just ticks me off. ")
      input()
      print("I feel as though he’s trying to kill us off in the worst way possible. "
            "\nTrying to get anything nowadays has become too much of a hindrance to all of us.")
      input()
      print("Can’t an old man just sit back, be miserable, and with a glass of water?! "
            "\nExplaining the history of this land just makes me depressed!")
      input()
      print("Old woman: I apologize for his outburst. He’s been bitter since Ostrania has fallen from grace and . . . "
            "\nsome other personal matters.")
      input()
      print("Old man: Hey! No more history, especially mine. We talked about this Muriel! [Old man leaves the room]")
      input()
      print("Muriel: Oh dear! Sigh. Ragnar is a bit on the sensitive side. He hasn’t opened up to anyone "
            "\nsince the tragedy. . . ")
      input()
      print("Oh right, so Kangmar has chosen you to be its knight. The people have lived in fear long enough and it has "
            "\nsearched for so long to find someone worthy to take on this task.")
      input()
      print("I didn’t think the worthy one would emerge nearly 20 years later, but it’s better late than never!")
      input()
      print("I ask that you reclaim the 3 artifacts and defeat the demon king as the three artifacts combined will give you "
            "\nthe power to you overcome and defeat him.")
      input()
      print("This is the only way to bring peace back to our home! So please, lend us your strength!")
      input()
      print("Before you go, you will need a weapon.")
      input()
      #The player chooses a weapon that dictates the class.
      i = 1
      while True:
            print("Knife (1)")
            print("Staff (2)")
            try:
                  ans = input()
                  assert ans == "1" or ans == "2", "stuff"
                  if ans == "1":
                        print("You are now a Warrior!")
                        player = Character("JaJaWaWa", 200, Jobs.WARRIOR, [], {}, {},
                                           arm1=Weapon.load_weapon_from_file("Knife (L)"),
                                           helmet=Armor.load_armor_from_file("Leather Helmet"),
                                           breastplate=Armor.load_armor_from_file("Leather Tunic"),
                                           grieves=Armor.load_armor_from_file("Leather Trousers"), is_player=True)
                        break
      #Staff is not working
                  elif ans == "2":
                        print("You are a Mage!")
                        player = Character("JaJaWaWa", 200, Jobs.MAGE, [Spell.load_spell_from_file("Fireball")], {}, {},
                                          arm1=Weapon.load_weapon_from_file("Wooden Staff (L)"),
                                           helmet=Armor.load_armor_from_file("Leather Helmet"),
                                           breastplate=Armor.load_armor_from_file("Leather Tunic"),
                                           grieves=Armor.load_armor_from_file("Leather Trousers"), is_player=True)
                        break
            except AssertionError:
                  print("Invalid")

      print("\nRagnar: [Yells from upstairs] Don’t forget to tell him that there may be enemies in each of the kingdoms.")
      input()
      print("Muriel: (Sigh) Yes dear I didn’t forget! Jeez, he thinks I’m the forgetful one. He didn’t even tell you "
            "\nabout each of the three kingdoms specifically. ")
      input()
      print("I’ll quickly explain each of the kingdoms. Which one would you like to hear about?")
      input()
      #The Player can choose which kingdom for Muriel to describe or choose to skip the explanation.
      # Choices include the Crystal Kingdom, the Mecha Kingdom, the Clock Kingdom, or Skip.
      # After an explanation, Muriel will ask which kingdom to describe after she finishes explaining the chosen kingdom.
      # She will stop explaining and move on after all three kingdoms are described.
      while True:
            print("Crystal (1)")
            print("Mecha (2)")
            print("Clock (3)")
            print("skip")
            try:
                  ans = input()
                  assert ans == "1" or ans == "2" or ans == "3" or ans == "skip", "Invalid response"
            except AssertionError:
                  print("Invalid")
                  continue
            if ans == "skip":
                  print("Muriel: Oh so you are already pretty knowledgeable about these kingdoms. I see. Well, ok.")
                  break
            match ans:
                  case "1":
                        print("Muriel: The Crystal Kingdom is home to King Agðarsdotter. "
                              "\nHe was entrusted with the Crystal of Perpetuation which gave them the power to freeze "
                              "\nand preserve anything. When he heard the news of the demon king’s invasion, he quickly "
                              "\nput a crystal barrier around the kingdom trapping the townsfolk with him. "
                              "\nNo one has been able to contact anyone from the inside for a long time and all that can be "
                              "\nheard from the kingdom are some occasional loud roars. "
                              "\nRecently, the crystal barrier surrouding the kingdom weakened, "
                              "\nbut no one brave enough has stepped up "
                              "\nWho knows what twisted creations dwell"
                              "\nin that once great kingdom? but, I’m sure with your strength you’ll retrieve that artifact "
                              "\nwith a fair amount of effort. "
                              "\nWhich kingdom would you like me to explain? ")
                        input()
                        continue
                  case "2":
                        print("Muriel: The Mecha Kingdom is home to King Wingard Levioso who dawns with the Armor of "
                              "\nConstruction. This armor gave him fantastical mechanical powers which granted him the "
                              "\nengineering ability of a genius. The townspeople were ordered by his decree to evacuate "
                              "\nthe kingdom once news broke, leaving only him. King Levioso constructed a huge watchtower "
                              "\nthat allows him to see the potential danger he anticipates. That watchtower may be a bit of "
                              "\na challenge to scale, but I’m sure you can handle it. "
                              "\nInstead of lending his strength to oppose the evil forces, "
                              "\nhe commanded that everybody evacuate "
                              "\nand he stay alone to defend the kingdom. (Muriel gets emotional without realizing) "
                              "\nArgh, that man is a coward! How can he have been so selfish and leave his people like that? "
                              "\n(Muriel tears up a bit)... S-Sorry, I didn’t mean to get so worked up, please forgive me. "
                              "\nWhich kingdom would you like me to explain? ")
                        input()
                        continue
                  case "3":
                        print("Muriel: The Clock Kingdom is led by King Clockyll Tymdal who wields "
                              "\nthe Sword of Transcendence. "
                              "\nKing Tymdal has always been sort of frantic and does not take bad news very well. "
                              "\nHis kingdom was the first to be attacked by the demon king and in a frantic panic, "
                              "\nthe king used the sword and put the kingdom in a time loop. "
                              "\nI’m guessing he thought this would give him the advantage of being able to strategize "
                              "\nwhat to do to combat the demons, but all it did was cause the same event to repeat over and "
                              "\nover again with little to no change. No one has ever made an effort to step inside that "
                              "\nkingdom since it is infested with demons. "
                              "\nThis will surely be the toughest artifact to retrieve! ")
                        input()
                        break

      print("Oh and once you enter a kingdom you won’t be able to leave until you retrieve the artifact. "
            "\n So make sure you’re prepared before going into a kingdom. Please be careful and may Kangmar be with you always "
            "\n on your travels. (Muriel leaves).")
      input()
      player = Crystal(player).start()
      if not player:
            continue
      player = Mecha(player).start()
      if not player:
            continue
      if not Clock(player).start():
            continue
      else:
            break

#The Ending
print("\nWith all three artifacts at your disposal, "
      "\nyou make your way to the demon kings lair killing off every servant of him in the process")
input()
print("The Demon King taunts you")
input()
print("Demon King: What! How did a lowly human get in here!"
      "\nDo you have a death wish!"
      "\nI will feed you to my dogs, "
      "\nyou worthless little nothing!")
input()
print("\nWait! A-Are those Ragmar's Artifacts!"
      "\nNO! WAIT! STOP! DON'T KILL ME!")
input()
print("YOU DEFEAT THE DEMON KING!")
input()
print("You hear a loud voice")
input()
print("???:YOU DID IT!")
input()
print("After vanquishing the demon king, JajaWawa became a legendary hero in the nation of Ostrania."
      "\nThe High Deity, Kangmar even returned back to its great land. ")
input()
print("Muriel and Ragnar couldn’t believe their eyes as they could see a bright blue sky among the whole land.")
input()
print("Everyone celebrated as the demon king was no more!")
input()
print("After returning to town you find a note in Muriel and Ragnar’s house")
input()
print("Dear [player],"
        "\nWe cannot thank you enough for all the hard work you put into saving the nation and its people! "
        "\nWe would like to thank you from the bottom of our hearts. "
        "\nThere is one more thing we forgot to mention to you in person. "
        "\nWe planned to tell you in person but our time ran short. "
        "\nTogether, I and Muriel are also deities that serve the high deity. "
        "\nWe took refuge and hid in this small town in order to be undetected by the demon king. "
        "\nWe’re sorry we kept this a secret but we couldn’t risk it. I hope you can forgive us. "
        "\nI’m sure we’ll see each other again soon. And again thank you for everything. "
		"\nSincerely," 
		"\nRagnar and Muriel :)   ")









