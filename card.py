class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # This can also be 1, depending on the Hand's total
        else:
            return int(self.rank)

    def __str__(self):
        return f'{self.rank} of {self.suit}'