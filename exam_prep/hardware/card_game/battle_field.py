from card_game.player.player import Player


class BattleField:
    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError('Player is dead')

        if attacker.__class__.__name__ == 'Beginner':
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        if enemy.__class__.__name__ == 'Beginner':
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        for card in attacker.card_repository.cards:
            attacker.health += card.health_points

        for card in enemy.card_repository.cards:
            enemy.health += card.health_points

        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            attacker.take_damage(card.damage_points)
