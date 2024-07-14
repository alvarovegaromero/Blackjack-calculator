from actions import Action
from hand import Hand
from card import Card
from card_counter import CardCounter

def suggest_action(player_hand: Hand, 
                   dealer_card: Card, 
                   card_counter: CardCounter, 
                   surrender_allowed: bool
                   ) -> Action:
    
    player_value = player_hand.value()

    print("Value of the player: ", player_value)
    print("Value of the dealer: ", dealer_card.value())

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
    else: # [12, 16]
        dealer_prob = card_counter.get_probability(dealer_card.rank)
        if dealer_prob < 0.5:
            return Action.STAND
        else:
            return Action.HIT