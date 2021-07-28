from card_game.battle_field import BattleField
from card_game.card.card_repository import CardRepository
from card_game.card.magic_card import MagicCard
from card_game.card.trap_card import TrapCard
from card_game.player.beginner import Beginner
from card_game.player.player_repository import PlayerRepository
from card_game.player.advanced import Advanced


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, player_type, username):
        player = Beginner(username) if player_type == 'Beginner' else Advanced(username)
        self.player_repository.add(player)
        return f"Successfully added player of type {player_type} with username: {username}"

    def add_card(self, card_type, name):
        card = MagicCard(name) if card_type == 'Magic' else TrapCard(name)
        self.card_repository.add(card)
        return f"Successfully added card of type {card_type}Card with name: {name}"

    def add_player_card(self, username, card_name):
        user = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        user.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attacker_name, enemy_name):
        attacker = self.player_repository.find(attacker_name)
        enemy = self.player_repository.find(enemy_name)
        BattleField.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ''
        for player in self.player_repository.players:
            result += f'Username: {player.username} - Health: {player.health} - Cards {len(player.card_repository)}\n'
            for card in player.card_repository.cards:
                result += f'### Card: {card.name} - Damage: {card.damage_points}\n'
        return result
