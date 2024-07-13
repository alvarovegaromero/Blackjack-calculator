from card import Card
from hand import Hand
from card_counter import CardCounter

def suggest_action(player_hand: Hand, dealer_card: Card, card_counter: CardCounter):
    player_value = player_hand.value()

    # simple strategy
    if player_value >= 17:
        return 'STAND'
    elif player_value <= 11:
        return 'HIT'
    else: # value in [12, 16]
        # more advanced
        dealer_prob = card_counter.get_probability(dealer_card.rank)
        if dealer_prob < 0.5:
            return 'STAND'
        else:
            return 'HIT'

def main():
    print("Welcome to Blackjack Advisor!")

    num_decks = int(input("Enter number of decks: "))
    card_counter = CardCounter(num_decks)

    while True:
        player_input = input("Enter player's hand (comma-separated values, e.g: A,10): ").split(',')
        dealer_input = input("Enter dealer's upcard (single value, e.g: 3): ")

        player_hand = Hand([Card(rank) for rank in player_input])
        dealer_card = Card(dealer_input)

        for card in player_hand.cards:
            card_counter.record_card(card)
        card_counter.record_card(dealer_card)

        action = suggest_action(player_hand, dealer_card, card_counter)

        print(f"Suggested action: {action}")

        cont = input("Do you want to continue? (y/n): ").lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()
