from card import Card

CARDS_PER_DECK = 52
SUITS_PER_DECK = 4
CARDS_AS_TEN = ['10','J', 'Q', 'K']

class CardCounter:
    def __init__(self, num_decks=6):
        self.num_decks = num_decks
        self.remaining_cards = {}

        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'A', 'T']
        for rank in ranks:
            if rank == 'T':
                self.remaining_cards[rank] = self.num_decks * SUITS_PER_DECK * len(CARDS_AS_TEN)
            else:
                self.remaining_cards[rank] = self.num_decks * SUITS_PER_DECK

    def record_card(self, card: Card):
        if card.rank in CARDS_AS_TEN:
            self.remaining_cards['T'] -= 1
        else:
            self.remaining_cards[card.rank] -= 1

    def reset(self):
        self.__init__(self.num_decks)

    def get_remaining(self, rank: str):
        return self.remaining_cards[rank]

    def get_probability(self, rank: str):
        total_cards = sum(self.remaining_cards.values())
        return self.remaining_cards[rank] / total_cards if total_cards > 0 else 0
    