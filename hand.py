from typing import List
from card import Card
from constants import MAXIMUM_HAND_VALUE

class Hand:
    def __init__(self, cards: List[Card]):
        self.cards = cards

    def value(self) -> int:
        total = sum(card.value() for card in self.cards)
        aces = sum(card.rank == 'A' for card in self.cards)

        while total > MAXIMUM_HAND_VALUE and aces:
            total -= 10
            aces -= 1

        return total
    
    def add_card(self, card: Card):
        self.cards.append(card)
    
    def __str__(self) -> str:
        return ', '.join(str(card) for card in self.cards)
    