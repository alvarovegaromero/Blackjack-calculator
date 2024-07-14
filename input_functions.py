from card import Card
from hand import Hand

def get_num_decks():
    return int(input("Enter number of decks: "))

def is_surrender_allowed():
    return input("Is surrender allowed? (y/n): ").lower() == 'y'

def get_dealer_strategy():
    return input("Does the dealer HIT or STAND on soft 17? (hit/stand): ").lower() == 'hit'

def get_player_hand():
    player_input = input("Enter player's hand (comma-separated values, e.g: A,10): ").split(',')
    return Hand([Card(rank) for rank in player_input])

def get_dealer_card():
    dealer_input = input("Enter dealer's upcard (single value, e.g: 3): ")
    return Card(dealer_input)

def get_user_input(prompt, type_=str, valid_responses=None):
    while True:
        response = type_(input(prompt))
        if valid_responses and response not in valid_responses:
            print(f"Invalid response. Please enter one of the following: {valid_responses}")
        else:
            return response