from Character import Character
from Items import *
import os
import random


class BattleSystem:
    """
    An instance of this class is created for every battle. This class handles all interactions of players and allies
    against enemies.
    """
    _path_to_battle_instances_file = os.getcwd() + "\\Battle_Instances.txt"

    def __init__(self, players_team: list[Character], enemies: list[Character]):
        """"""
        assert isinstance(players_team, list), f"Players-team expected to be a list type, got: {type(players_team)}"
        assert isinstance(enemies, list), f"Enemies expected to be a list type, got: {type(enemies)}"
        for character in players_team:
            assert isinstance(character, Character), \
                f"There should only be character types in player_team, got: {type(character)}"
        for character in enemies:
            assert isinstance(character, Character), \
                f"There should only be character types in enemies, got: {type(character)}"
        assert players_team[0].is_player, f"The first character in players_team should be the player, " \
                                          f"got: {players_team[0].name}"

        self.players_team = players_team
        self.enemies = enemies
        self.player = players_team[0]
        self.round = 0

    def start(self):
        """"""
        player_won = False
        while True:
            print("Player's Turn")
            if Effects.STUN not in self.player.status.keys():
                match self._player_action():
                    case 2:
                        player_won = True
                        break
            else:
                del self.player.status[Effects.STUN]
            if len(self.players_team) > 1:
                print("Allies Turn")
                if not self._player_team_action():
                    player_won = True
                    break
            print("Enemy's Turn")
            if not self._enemies_action():
                break
            if self._effects_applied() == "Game Over":
                break
            if len(self.enemies) == 0:
                player_won = True
                break
        print("Battle Over")
        return player_won


    def _player_action(self):
        """"""
        action_undecided = True
        print(f"Your health is {self.player.health}")
        while action_undecided:
            while True:
                try:
                    print("Choose your action.")
                    action = input("Physical attack (a), Cast Spell (s), Access inventory (i)")
                    assert action == "a" or action == "s" or action == "i"
                    break
                except AssertionError:
                    print("The input was not recognized as a valid input. Please input a valid response. ry again...")
            match action:
                case "a":
                    value = self._attack()
                    if value == 2:
                        return 2
                    elif value == 3:
                        return 3
                case "s":
                    value = self._cast_spell()
                    if value == 2:
                        return 2
                    elif value == 3:
                        return 3
                case "i":
                    self.player.open_inventory()
        return 3

    def _attack(self):
        """"""
        while True:
            try:
                print("Which armament would you like to use?")
                armament = input(f"{self.player.arm1.name} (1) or {self.player.arm2.name} (2)")
                assert armament == "1" or armament == "2" or armament == "b"
                break
            except AssertionError:
                print("The input was not recognized as a valid input. Please input a valid response. try again...")
        if armament == "b":
            return 1
        armament = int(armament)
        while True:
            try:
                print("Which enemy would you like to attack?")
                enemy_team = ""
                i = 1
                for enemy in self.enemies:
                    enemy_team += f"{enemy.name} with {enemy.health}hp ({i}) "
                    i += 1
                print(enemy_team)
                target = input("")
                if target == "b":
                    return 1
                target = int(target) - 1
                assert target in range(i)
                break
            except AssertionError or ValueError:
                print("The input was not recognized as a valid input. Please input a valid response. try again...")
        if armament == 1:
            result = self.player.phy_attack(self.player.arm1, self.enemies[target])
            print(f"You dealt {int(result[0])} points of damage.")
            if result[1] <= 0:
                print(self.enemies[target].name + " was defeated.")
                self.enemies.remove(self.enemies[target])
        else:
            result = self.player.phy_attack(self.player.arm2, self.enemies[target])
            print(f"You dealt {int(result[0])} points of damage.")
            if result[1] <= 0:
                print(self.enemies[target].name + " was defeated.")
                self.enemies.remove(self.enemies[target])
        if len(self.enemies) == 0:
            return 2
        return 3

    def _cast_spell(self):
        """"""
        if not self.player.spells:
            print("You have no spells to cast.")
            return 1
        while True:
            try:
                print("Which spell would you like to cast?")
                i = 1
                spells = ''
                for spell in self.player.spells:
                    spells += f"{spell.name} ({i}) "
                    i += 1
                spell_to_cast = int(input(spells)) - 1
                assert spell_to_cast in range(i) or spell_to_cast == "b"
                break
            except AssertionError or ValueError:
                print("The input was not recognized as a valid input. Please input a valid response. try again...")
        if spell_to_cast == "b":
            return 1
        spell = self.player.spells[spell_to_cast]
        try:
            assert self.player.arm1.wpn_type == WpnTypes.STAFF or self.player.arm2.wpn_type == WpnTypes.STAFF, \
                "No staff equipped."
        except AssertionError:
            print("No staff equipped.")
            return 1
        if spell.is_AOE:
            msg = "You dealt "
            if self.player.arm1.wpn_type == WpnTypes.STAFF:
                armament = self.player.arm1
            else:
                armament = self.player.arm2
            for enemy in self.enemies:
                result = self.player.mag_attack(armament, spell,
                                                enemy)
                if enemy == self.enemies[0]:
                    msg += f"{result[0]} damage to {enemy.name}"
                else:
                    msg += f" and {result[0]} damage to {enemy.name}"
                if result[1] <= 0:
                    print(enemy.name + " was defeated.")
                    del enemy
            print(msg)
            if len(self.enemies) == 0:
                return 2
            return 3
        while True:
            try:
                print("Which enemy would you like to attack?")
                enemy_team = ""
                i = 1
                for enemy in self.enemies:
                    enemy_team += f"{enemy.name} with {enemy.health}hp ({i}) "
                    i += 1
                print(enemy_team)
                target = input("")
                if target == "b":
                    return 1
                target = int(target) - 1
                assert target in range(i)
                break
            except AssertionError or ValueError:
                print("The input was not recognized as a valid input. Please input a valid response. try again...")
        if self.player.arm1.wpn_type == WpnTypes.STAFF:
            result = self.player.mag_attack(self.player.arm1, spell,
                                   self.enemies[target])
            print(f"You have dealt {int(result[0])} points of damage.")
            if result[1] <= 0:
                print(self.enemies[target].name + " was defeated.")
        elif self.player.arm2.wpn_type == WpnTypes.STAFF:
            result = self.player.mag_attack(self.player.arm2, spell,
                                   self.enemies[target])
            print(f"You have dealt {int(result[0])} points of damage.")
            if result[1] <= 0:
                print(self.enemies[target].name + " was defeated.")
                del self.enemies[target]
        if len(self.enemies) == 0:
            return 2
        return 3

    def _player_team_action(self):
        """"""
        for ally in self.players_team:
            if ally.is_player:
                continue
            print(f"{ally.name} has {ally.health} health.")
            if Effects.STUN in ally.status.keys():
                print(f"{ally.name} was stunned.")
                continue
            armament = ally.arm2
            if random.randrange(1,2) == 1:
                armament = ally.arm1
            if armament.wpn_type == WpnTypes.STAFF:
                spell = ally.spells[0]
                if len(ally.spells) > 1:
                    spell = ally.spells[random.randrange(0, len(ally.spells))]
                if spell.is_AOE:
                    for enemy in self.enemies:
                        result = ally.mag_attack(armament, spell, enemy)
                        print(f"{ally.name} dealt {result[0]} points of damage to {enemy.name}")
                        if result[1] <= 0:
                            self.enemies.remove(enemy)
                        if len(self.enemies) == 0:
                            return False
                target = random.randrange(0, len(self.enemies))
                result = ally.mag_attack(armament, spell, self.enemies[target])
                print(f"{ally.name} dealt {result[0]} points of damage to {self.enemies[target].name}")
                if result[1] <= 0:
                    self.enemies.remove(self.enemies[target])
                if len(self.enemies) == 0:
                    return False
            target = random.randrange(0, len(self.enemies))
            result = ally.phy_attack(armament, self.enemies[target])
            print(f"{ally.name} dealt {result[0]} points of damage to {self.enemies[target].name}")
            if result[1] <= 0:
                self.enemies.remove(self.enemies[target])
            if len(self.enemies) == 0:
                return False
        enemy_team = ""
        i = 1
        for enemy in self.enemies:
            enemy_team += f"{enemy.name} with {enemy.health}hp ({i}) "
            i += 1
        print(enemy_team)
        return True

    def _enemies_action(self):
        """"""
        for enemy in self.enemies:
            if Effects.STUN in enemy.status.keys():
                print(f"{enemy.name} was stunned.")
                continue
            armament = enemy.arm2
            if random.randrange(1,2) == 1:
                armament = enemy.arm1
            if armament.wpn_type == WpnTypes.STAFF:
                spell = enemy.spells[0]
                if len(enemy.spells) > 1:
                    spell = enemy.spells[random.randrange(0, len(enemy.spells))]
                if spell.is_AOE:
                    for good_guy in self.players_team:
                        result = enemy.mag_attack(armament, spell, good_guy)
                        if result[1] <= 0:
                            if self.player.health <= 0:
                                print("Game Over")
                                return False
                            print(f"{good_guy.name} died.")
                            self.players_team.remove(good_guy)
                            continue
                    continue
                target = random.randrange(0, len(self.players_team))
                result = enemy.mag_attack(armament, spell, self.players_team[target])
                print(f"{enemy.name} dealt {result[0]} points of damage to {self.players_team[target].name}")
                if result[1] <= 0:
                    if self.player.health <= 0:
                        print("Game Over")
                        return False
                    print(f"{self.players_team[target].name} died.")
                    del self.players_team[target]
                    continue
            target = random.randrange(0, len(self.players_team))
            result = enemy.phy_attack(armament, self.players_team[target])
            print(f"{enemy.name} dealt {result[0]} points of damage to {self.players_team[target].name}")
            if result[1] <= 0:
                if self.player.health <= 0:
                    print("Game Over")
                    return False
                print(f"{self.players_team[target].name} died.")
                del self.players_team[target]
        return True

    def _effects_applied(self):
        """"""
        for team in [self.players_team, self.enemies]:
            for character in team:
                for effect, (amt, duration) in character.status.items():
                    if duration == Character.effect_duration:
                        match effect:
                            case Effects.BURN:
                                character.hurt(float(amt))
                                print(f"{character.name} had {amt} damage dealt from burns.")
                            case Effects.HEALTH:
                                character.hurt(-float(amt))
                                print(f"{character.name} had {amt} health restored.")
                                if character.is_player:
                                    print(f"Current health: {character.health}")
                            case Effects.STRENGTH:
                                character.arm1.phy_damage += amt
                                character.arm2.phy_damage += amt
                                print(f"{character.name}'s strength rose.")
                            case Effects.DEFENSE:
                                character.helmet.phy_neg += amt
                                character.helmet.magic_neg += amt
                                character.breastplate.phy_neg += amt
                                character.breastplate.magic_neg += amt
                                character.grieves.phy_neg += amt
                                character.grieves.magic_neg += amt
                                print(f"{character.name}'s defense rose.")
                            case Effects.MAGIC:
                                character.arm1.mag_damage += amt
                                character.arm2.mag_damage += amt
                                print(f"{character.name}'s magic rose.")
                            case Effects.DEATHTOUCH:
                                del character.status[(amt, duration)]
                                if character.hurt(2000) <= 0:
                                    print("DeathTouch!!!")
                                    print(character.name + " died.")
                                    if character.is_player:
                                        character.remove_effects()
                                        return "Game Over"
                                    team.remove(character)
                    character.status[effect] = (amt, duration - 1)
                    if duration == 0:
                        character.remove_effects(effect)
                        del character.status[(amt, duration + 1)]
                if character.health <= 0:
                    print(character.name + " was defeated.")
                    if character.is_player:
                        character.remove_effects()
                        return "Game Over"
                    team.remove(character)
        return True

    @classmethod
    def load_battle_from_file(cls, player: Character, battle_index: int):
        assert isinstance(player, Character), f"Player expected to be a Character type, got: {type(player)}"
        assert player.is_player, "Player expected to be the main player not a character."
        assert isinstance(battle_index, int) and battle_index >= 0, f"Battle_index expected to be a positive integer " \
                                                                    f"type, got: {type(battle_index)}"

        allies = [player]
        enemies = []

        with open(cls._path_to_battle_instances_file, 'r') as f:
            data = f.read().splitlines()[battle_index - 1]
            data = data.split(" ")
            allies_present = False
            if data[0] != "NONE":
                allies_str_list = data[0].split(",")
                allies_present = True
            enemies_str_list = data[1].split(",")
            if allies_present:
                for ally in allies_str_list:
                    allies.append(Character.load_character_from_file(ally))
            for enemy in enemies_str_list:
                enemies.append(Character.load_character_from_file(enemy))

            return BattleSystem(allies, enemies)
