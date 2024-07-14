from card import Card
from hand import Hand
from card_counter import CardCounter
from strategy import suggest_action

MAXIMUM_VALUE = 21

def get_num_decks():
    return int(input("Enter number of decks: "))

def is_surrender_allowed():
    return input("Is surrender allowed? (y/n): ").lower() == 'y'

def get_player_hand():
    player_input = input("Enter player's hand (comma-separated values, e.g: A,10): ").split(',')
    return Hand([Card(rank) for rank in player_input])

def get_dealer_card():
    dealer_input = input("Enter dealer's upcard (single value, e.g: 3): ")
    return Card(dealer_input)

def play_hand(player_hand, dealer_card, card_counter, surrender_allowed):
    for card in player_hand.cards:
        card_counter.record_card(card)
    card_counter.record_card(dealer_card)

    while player_hand.value() <= MAXIMUM_VALUE:
        action = suggest_action(player_hand, dealer_card, card_counter, surrender_allowed)

        print(f"Suggested action: {action}")

        add_card = input("Do you want to add a new card to you hand? (y/n): ").lower()
        if add_card == 'y':
            new_card_input = input("Enter your new card (single value, e.g: 3): ")
            new_card = Card(new_card_input)
            player_hand.add_card(new_card)
            card_counter.record_card(new_card)
        else:
            break

def main():
    print("Welcome to Blackjack Advisor!")

    num_decks = get_num_decks()
    card_counter = CardCounter(num_decks)
    surrender_allowed = is_surrender_allowed()

    while True:
        player_hand = get_player_hand()
        dealer_card = get_dealer_card()

        play_hand(player_hand, dealer_card, card_counter, surrender_allowed)

        cont = input("Do you want to continue playing? (y/n): ").lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()