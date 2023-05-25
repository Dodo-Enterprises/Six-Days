from Crystal import Crystal
from Character import Character
from Mecha import Mecha
from Clock import Clock
from Items import *


#Intro
print("The land of Ostrania. A wonderful, vibrant land made by a high deity, Kangmar. ")
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
      print("Sword (1)")
      print("Staff (2)")
      try:
            ans = input()
            assert ans == "1" or ans == "2"
            if ans == "1":
                  print("You are now a Warrior!")
                  player = Character("JaJaWaWa", 100, Jobs.WARRIOR, [], {}, {},
                                     arm1=Weapon.load_weapon_from_file("Knife (L)"), is_player=True)
                  break
            print("You are a Mage!")
            player = Character("JaJaWaWa", 100, Jobs.MAGE, [Spell.load_spell_from_file("Fireball")], {}, {},
                               arm1=Weapon.load_weapon_from_file("Wooden Staff"), is_player=True)
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
i = 1
while True:
      print("Crystal (1)")
      print("Mecha (2)")
      print("Clock (3)")
      try:
            ans = input()
            assert ans == "1" or ans == "2" or ans == "3" or ans == "exit" or ans == "skip", "Invalid response"
      except AssertionError:
            print("Invalid")
            continue
      if ans == "skip" and i == 1:
            print("Muriel: Oh so you are already pretty knowledgeable about these kingdoms. I see. Well, ok.")
      break
      i += 1
      match ans:
            case "1":
                  print("Muriel: The Crystal Kingdom is home to King Agðarsdotter. "
                        "He was entrusted with the Crystal of Perpetuation which gave them the power to freeze "
                        "and preserve anything. When he heard the news of the demon king’s invasion, he quickly "
                        "put a crystal barrier around the kingdom trapping the townsfolk with him. "
                        "No one has been able to contact anyone from the inside for a long time and all that can be "
                        "heard from the kingdom are some occasional loud roars. "
                        "Recently, the crystal barrier surrouding the kingdom weakened, "
                        "but no one brave enough has stepped up "
                        "Who knows what twisted creations dwell"
                        "in that once great kingdom? but, I’m sure with your strength you’ll retrieve that artifact "
                        "with a fair amount of effort. "
                        "Which kingdom would you like me to explain? ")
                  input()
            case "exit":
                  break
            case "2":
                  print("Muriel: The Mecha Kingdom is home to King Wingard Levioso who dawns with the Armor of "
                        "Construction. This armor gave him fantastical mechanical powers which granted him the "
                        "engineering ability of a genius. The townspeople were ordered by his decree to evacuate "
                        "the kingdom once news broke, leaving only him. King Levioso constructed a huge watchtower "
                        "that allows him to see the potential danger he anticipates. That watchtower may be a bit of "
                        "a challenge to scale, but I’m sure you can handle it. "
                        "Instead of lending his strength to oppose the evil forces, "
                        "he commanded that everybody evacuate "
                        "and he stay alone to defend the kingdom. (Muriel gets emotional without realizing) "
                        "Argh, that man is a coward! How can he have been so selfish and leave his people like that? "
                        "(Muriel tears up a bit)... S-Sorry, I didn’t mean to get so worked up, please forgive me. "
                        "Which kingdom would you like me to explain? ")
                  input()
            case "3":
                  print("Muriel: The Clock Kingdom is led by King Clockyll Tymdal who wields "
                        "the Sword of Transcendence. "
                        "King Tymdal has always been sort of frantic and does not take bad news very well. "
                        "His kingdom was the first to be attacked by the demon king and in a frantic panic, "
                        "the king used the sword and put the kingdom in a time loop. "
                        "I’m guessing he thought this would give him the advantage of being able to strategize "
                        "what to do to combat the demons, but all it did was cause the same event to repeat over and "
                        "over again with little to no change. No one has ever made an effort to step inside that "
                        "kingdom since it is infested with demons. "
                        "This will surely be the toughest artifact to retrieve ")
                  input()


print("Oh and once you enter a kingdom you won’t be able to leave until you retrieve the artifact. "
      "\nSo make sure you’re prepared before going into a kingdom. Please be careful and may Kangmar be with you always "
      "\n"
      "on your travels. (Muriel leaves).")
input()

player = Mecha(player).start()
#player = Crystal(player).start()






