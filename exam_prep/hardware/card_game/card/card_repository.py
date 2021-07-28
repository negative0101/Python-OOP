from card_game.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        for c in self.cards:
            if c.name == card.name:
                raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card):
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        self.cards.remove(card)
        self.count -= 1

    def find(self, name):
        for c in self.cards:
            if c.name == name:
                return c.name
