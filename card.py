class Card:
    def __init__(self, rank: str):
        self.rank = rank

    def value(self) -> int:
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # 1 or 11, decided in Hand class
        else:
            return int(self.rank)

    def __str__(self) -> str:
        return f'{self.rank}'