from Character import Character


class BattleSystem:
    """
    An instance of this class is created for every battle. This class handles all interactions of players and allies
    against enemies.
    """
    def __init__(self, players_team, enemies):
        """"""
        assert isinstance(players_team, list), f"Playerr-team expected to be a list type, got: {type(players_team)}"
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


class BattleLoader:
    """
    This class will load preset scenarios from file to create battle instances.
    """