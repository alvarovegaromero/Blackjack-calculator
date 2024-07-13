class Hand:
    def __init__(self, cards):
        self.cards = cards

    def value(self):
        total = sum(card.value() for card in self.cards)
        # If total value is over 21 and there's an Ace in the hand, reduce total by 10
        if total > 21 and any(card.rank == 'A' for card in self.cards):
            return total - 10
        return total

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)