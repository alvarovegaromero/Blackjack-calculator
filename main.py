from blackjack_game import BlackjackGame
from input_functions import get_dealer_card, get_dealer_strategy, get_player_hand, get_user_input, get_player_new_card

MAXIMUM_VALUE = 21

def main():
    print("Welcome to Blackjack Advisor!")

    num_decks = get_user_input("Enter number of decks: ", int)
    surrender_allowed = get_user_input("Is surrender allowed? (y/n): ", valid_responses=['y', 'n']) == 'y'
    dealer_stands_on_soft_17 = get_dealer_strategy()

    game = BlackjackGame(num_decks, surrender_allowed, dealer_stands_on_soft_17)

    continue_playing = True

    while continue_playing:
        player_hand = get_player_hand()
        dealer_card = get_dealer_card()

        game.play_hand(player_hand, dealer_card)

        while player_hand.value() <= 21:
            add_card = get_user_input("Do you want to add a new card to you hand? (y/n): ", valid_responses=['y', 'n'])
            if add_card == 'y':
                new_card = get_player_new_card()
                game.add_card_to_player_hand(new_card)
                game.play_hand(player_hand, dealer_card)
            else:
                continue_playing = False
                break

    print("Your final hand value is: ", player_hand.value())

if __name__ == "__main__":
    main()
