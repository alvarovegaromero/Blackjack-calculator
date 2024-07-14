from actions import Action
from card import Card
from hand import Hand
from card_counter import CardCounter

MAXIMUM_VALUE = 21  

def suggest_action(player_hand: Hand, dealer_card: Card, card_counter: CardCounter, surrender_allowed: bool):
    player_value = player_hand.value()

    print("Value of the player: ", player_value)
    print("Value of the dealer: ", dealer_card.value())

    # Strategy
    if player_value >= 17:
        return Action.STAND
    elif player_value == 11:
        return Action.DOUBLE
    elif player_value == 10 and dealer_card.rank in ['4', '5', '6']:
        return Action.DOUBLE
    elif player_value <= 11:
        return Action.HIT
    elif surrender_allowed and player_value == 16 and dealer_card.rank in ['9', '10', 'A']:
        return Action.SURRENDER
    else: # value in [12, 16]
        dealer_prob = card_counter.get_probability(dealer_card.rank)
        if dealer_prob < 0.5:
            return Action.STAND
        else:
            return Action.HIT

def main():
    print("Welcome to Blackjack Advisor!")

    num_decks = int(input("Enter number of decks: "))
    card_counter = CardCounter(num_decks)
    surrender_allowed = input("Is surrender allowed? (y/n): ").lower() == 'y'

    while True:
        player_input = input("Enter player's hand (comma-separated values, e.g: A,10): ").split(',')
        dealer_input = input("Enter dealer's upcard (single value, e.g: 3): ")

        player_hand = Hand([Card(rank) for rank in player_input])
        dealer_card = Card(dealer_input)

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

        cont = input("Do you want to continue playing? (y/n): ").lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()