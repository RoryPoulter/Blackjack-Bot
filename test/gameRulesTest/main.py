from card import Card
from hand import Hand


def decideWinner(player_hand, dealer_hand):
    """
    Determines the winner of the game
    :param player_hand: The cards the player finished with
    :type player_hand: Hand
    :param dealer_hand: The cards the dealer finished with
    :type dealer_hand: Hand
    :return: Boolean value for if the player won
    :rtype: bool
    """
    if len(dealer_hand) == 5:
        return False
    elif len(player_hand) == 5:
        return True
    else:
        return player_hand > dealer_hand


def main():
    print("---------------------")
    player_hand: Hand = Hand()
    dealer_hand: Hand = Hand()
    print(player_hand)
    if dealer_hand.blackjack:
        print("Dealer wins")
        return
    elif player_hand.blackjack:
        print("You win!")
        return

    in_play = True
    while (player_hand < 21) and in_play and (len(player_hand) < 5):
        in_play = input("Draw card? [Y/N]: ").upper() == "Y"
        if in_play:
            player_hand.drawCard(Card())
            print(player_hand)
            if player_hand > 21:
                print("Dealer wins")
                return

    print(dealer_hand)
    while (dealer_hand < 16) and (len(dealer_hand) < 5):
        dealer_hand.drawCard(Card())
        print(dealer_hand)
        if dealer_hand > 21:
            print("You win!")
            return

    player_won = decideWinner(player_hand, dealer_hand)
    if player_won:
        print("You win!")
    else:
        print("Dealer won")


if __name__ == "__main__":
    main()
