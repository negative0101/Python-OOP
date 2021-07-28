from card_game.card.card import Card


class MagicCard(Card):
    def __init__(self, name):
        super().__init__(name, 5, 80)
