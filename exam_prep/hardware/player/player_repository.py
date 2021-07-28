from card_game.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        for p in self.players:
            if p.username == player.username:
                raise ValueError(f'Player {player.username} already exists!')
        self.players.append(player)
        self.count += 1

    def remove(self, player_name):
        if player_name == '':
            raise ValueError("Player cannot be an empty string!")
        for p in self.players:
            if p.username == player_name:
                self.players.remove(p)
                self.count -= 1

    def find(self, username):
        for p in self.players:
            if p.username == username:
                return p.username
