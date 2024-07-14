from blackjack_game import BlackjackGame
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

def main():
    print("Welcome to Blackjack Advisor!")

    num_decks = get_user_input("Enter number of decks: ", int)
    surrender_allowed = get_user_input("Is surrender allowed? (y/n): ", valid_responses=['y', 'n']) == 'y'
    dealer_hits_on_soft_17 = get_user_input("Does the dealer HIT or STAND on soft 17? (hit/stand): ", valid_responses=['hit', 'stand']) == 'hit'

    game = BlackjackGame(num_decks, surrender_allowed, dealer_hits_on_soft_17)

    while True:
        player_hand = get_player_hand()
        dealer_card = get_dealer_card()

        game.play_hand()

        cont = get_user_input("Do you want to continue playing? (y/n): ", valid_responses=['y', 'n'])
        if cont != 'y':
            break

if __name__ == "__main__":
    main()