class Hand:
    def __init__(self, cards):
        self.cards = cards

    def value(self):
        total = sum(card.value() for card in self.cards)
        aces = sum(card.rank == 'A' for card in self.cards)

        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total
    
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)