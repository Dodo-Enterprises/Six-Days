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

    def __init__(self, players_team: list[Character], enemies: list[Character], loot: list[Item] = None,
                 run_difficulty: int = 50):
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
        assert isinstance(run_difficulty, int), f"Run_difficulty expected to be int type, got: {type(run_difficulty)}"
        assert 100 >= run_difficulty >= 0, f"Run_difficulty expected to be inbetween " \
                                           f"the number 0 to 100, got: {run_difficulty}"

        self.players_team = players_team
        self.enemies = enemies
        self.player = players_team[0]
        self.round = 0
        self.battle_ongoing = True
        self.run_difficulty = float(run_difficulty / 100)
        self.loot = loot

    def start(self):
        """"""
        while self.battle_ongoing:
            print("Player's Turn")
            match self._player_action():
                case 1:
                    self.battle_ongoing = False
                case 2:
                    self.battle_ongoing = False
            if len(self.players_team) > 1:
                print("Allies Turn")
                if not self._player_team_action():
                    self.battle_ongoing = False
            print("Enemy's Turn")
            if not self._enemies_action():
                self.battle_ongoing = False
            self._effects_applied()
        print("Battle Over")

    def _player_action(self):
        """"""
        action_undecided = True

        while action_undecided:
            while True:
                try:
                    print("Choose your action.")
                    action = input("Physical attack (a), Cast Spell (s), Access inventory (i), or Run (r)")
                    assert action == "a" or action == "s" or action == "i" or action == "r"
                    break
                except AssertionError:
                    print("The input was not recognized as a valid input. Please input a valid response. ry again...")
            match action:
                case "a":
                    value = self._attack()
                    if value == 2:
                        return 1
                    elif value == 3:
                        return 3
                case "s":
                    self._cast_spell()
                case "i":
                    self.player.open_inventory()
                case "r":
                    if self._run():
                        return 2
                    action_undecided = False
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
            return
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
            if self.player.phy_attack(self.player.arm1, self.enemies[target])[1] <= 0:
                self.enemies.remove(self.enemies[target - 1])
        if self.player.phy_attack(self.player.arm2, self.enemies[target])[1] <= 0:
            self.enemies.remove(self.enemies[target - 1])
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
                    spells += f"{spell.name} ({i})"
                    i += 1
                spell_to_cast = input()
                assert int(spell_to_cast) - 1 in range(i) or spell_to_cast == "b"
                break
            except AssertionError or ValueError:
                print("The input was not recognized as a valid input. Please input a valid response. try again...")
        if spell_to_cast == "b":
            return 1
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
            self.player.mag_attack(self.player.arm1, Spell.load_spell_from_file(spell_to_cast), self.enemies[target])
        elif self.player.arm2.wpn_type == WpnTypes.STAFF:
            self.player.mag_attack(self.player.arm2, Spell.load_spell_from_file(spell_to_cast), self.enemies[target])
        if len(self.enemies) == 0:
            return 2
        return 3

    def _run(self):
        """"""
        if random.random() <= self.run_difficulty:
            return True
        return False

    def _player_team_action(self):
        """"""
        for ally in self.players_team:
            if ally.job == Jobs.WARRIOR:
                target = random.randrange(0, len(self.enemies))
                if ally.phy_attack(ally.arm1, self.enemies[target])[1] <= 0:
                    self.enemies.remove(self.enemies[target])
                if len(self.enemies) == 0:
                    return False
            else:
                target = random.randrange(0, len(self.enemies))
                if ally.mag_attack(ally.arm1, ally.spells[0], self.enemies[target])[1] <= 0:
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
            if enemy.job == Jobs.WARRIOR:
                target = random.randrange(0, len(self.players_team))
                enemy.phy_attack(enemy.arm1, self.players_team[target])
                if self.player.health <= 0:
                    print("Game Over")
                    return False
            else:
                target = random.randrange(0, len(self.players_team))
                enemy.mag_attack(enemy.arm1, enemy.spells[0], self.players_team[target])
                if self.player.health <= 0:
                    print("Game Over")
                    return False
        return True

    def _effects_applied(self):
        """"""
        # TODO

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
            if data[0] != "null":
                allies_str_list = data[0].split(",")
                allies_present = True
            enemies_str_list = data[1].split(",")
            if allies_present:
                for ally in allies_str_list:
                    allies.append(Character.load_character_from_file(ally))
            for enemy in enemies_str_list:
                enemies.append(Character.load_character_from_file(enemy))
            run_difficulty = int(data[2])

            return BattleSystem(allies, enemies, run_difficulty=run_difficulty)
