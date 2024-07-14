from card_counter import CardCounter
from strategy import suggest_action
from card import Card

MAXIMUM_VALUE = 21

def get_user_input(prompt, type_=str, valid_responses=None):
    while True:
        response = type_(input(prompt))
        if valid_responses and response not in valid_responses:
            print(f"Invalid response. Please enter one of the following: {valid_responses}")
        else:
            return response

class BlackjackGame:
    def __init__(self, num_decks, surrender_allowed, dealer_hits_on_soft_17):
        self.num_decks = num_decks
        self.surrender_allowed = surrender_allowed
        self.dealer_hits_on_soft_17 = dealer_hits_on_soft_17
        self.card_counter = CardCounter(num_decks)
        self.player_hand = None
        self.dealer_card = None

    def play_hand(self):
        for card in self.player_hand.cards:
            self.card_counter.record_card(card)
        self.card_counter.record_card(self.dealer_card)

        while self.player_hand.value() <= MAXIMUM_VALUE:
            action = suggest_action(self.player_hand, self.dealer_card, self.card_counter, self.surrender_allowed, self.dealer_hits_on_soft_17)
            print(f"Suggested action: {action}")

            add_card = get_user_input("Do you want to add a new card to you hand? (y/n): ", valid_responses=['y', 'n'])
            if add_card == 'y':
                new_card_input = get_user_input("Enter your new card (single value, e.g: 3): ")
                new_card = Card(new_card_input)
                self.player_hand.add_card(new_card)
                self.card_counter.record_card(new_card)
            else:
                break
