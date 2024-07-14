from blackjack_game import BlackjackGame
from input_functions import get_dealer_card, get_player_hand, get_user_input


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