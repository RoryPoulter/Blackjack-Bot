from card import Card


class Hand:
    """The hand to store the cards.
    """
    def __init__(self, dealer=False):
        """Constructor method

        Args:
            dealer (bool, optional): If the hand belongs to the dealer. Defaults to False.
        """
        self.total: complex = 0 + 0j
        self.cards: list[Card] = []
        for _ in range(2):
            self.drawCard()
        self.in_play: bool = True
        self.blackjack: bool = self == 21
        self.five_card: bool = False
        self.dealer: bool = dealer

    def __repr__(self):
        """Formats the cards in the hand and the total in a string representation

        Returns:
            str: The formatted string
        """
        return "|"+", ".join(list(map(str, self.cards)))+"| "+f"({self.total.imag})"

    def __int__(self):
        """Returns the higher total of the hand

        Returns:
            int: The total of the hand
        """
        return int(self.total.imag)

    def __gt__(self, other):
        """Checks if the value of the hand is greater than a given value

        Args:
            other (int, Hand): The value being compared with the hand

        Returns:
            bool: True if greater than the other value, else False
        """
        if isinstance(other, int):
            return self.total.imag > other
        return self.total.imag > other.total.imag

    def __lt__(self, other):
        """Checks if the value of the hand is less than a given value

        Args:
            other (int, Hand): The value being compared with the hand

        Returns:
            bool: True if less than the other value, else False
        """
        if isinstance(other, int):
            return self.total.imag < other
        return self.total.imag < other.total.imag

    def __eq__(self, other):
        """Checks if the value of the hand is equal to a given value

        Args:
            other (int, Hand): The value being compared with the hand

        Returns:
            bool: True if equal to the other value, else False
        """
        if isinstance(other, int):
            return self.total.imag == other
        return self.total.imag == other.total.imag

    def __len__(self):
        """Returns the size of the hand

        Returns:
            int: The number of cards in the hand
        """
        return len(self.cards)

    def drawCard(self):
        """Adds a card to the hand
        """
        new_card: Card = Card()
        self.cards.append(new_card)
        self.total += new_card.value
        self.in_play = self.checkTotal()

    def checkTotal(self):
        """Checks if the player has bust

        Returns:
            bool: True if the hand is still in play, else False
        """
        if self.total.real > 21:  # If the min total > 21
            return False
        elif self.total.imag > 21:  # If the player has an ace and the max total > 21
            self.total -= 10j  # Sets the max total == min total

        if len(self) == 5:
            self.five_card = True
        return True

    def displayHand(self):
        """Displays the cards drawn at the start of the game, hides second card for dealer's hand
        """
        if self.dealer:
            print("|" + str(self.cards[0]) + "|")
        else:
            print("|"+", ".join(list(map(str, self.cards)))+"| "+f"({self.total.imag})")


if __name__ == "__main__":
    player_hand: Hand = Hand()
    player_hand.displayHand()
    player_hand.drawCard()
    print(player_hand)

    dealer_hand: Hand = Hand(dealer=True)
    dealer_hand.displayHand()
    dealer_hand.drawCard()
    print(dealer_hand)
