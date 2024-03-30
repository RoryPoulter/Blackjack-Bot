from numpy import array
from card import Card


class Hand:
    def __init__(self, dealer=False):
        """Constructor method
        :param dealer: If the hand belongs to the dealer, `False` by default
        :type dealer: bool
        """
        self.total: array = array([0, 0])
        self.cards: list[Card] = []
        for _ in range(2):
            self.drawCard()
        self.in_play: bool = True
        self.blackjack: bool = self == 21
        self.five_card: bool = False
        self.dealer: bool = dealer

    def __repr__(self):
        """
        :return: Formatted string with cards in hand and highest total
        :rtype: str
        """
        return "|"+", ".join(list(map(str, self.cards)))+"| "+f"({self.total[1]})"

    def __int__(self):
        """Returns the total of the hand, higher value if there is an ace
        :return: The higher total
        :rtype: int
        """
        return int(self.total[1])

    def __gt__(self, other):
        """Compares the totals of the hands
        :param other: The other hand object or a number
        :type other: Hand | int
        :return: whether the first hand has a greater total
        :rtype: bool
        """
        if type(other) is int:
            return self.total[1] > other
        else:
            return self.total[1] > other.total[1]

    def __lt__(self, other):
        """Compares the totals of the hands
        :param other: The other hand object or a number
        :type other: Hand | int
        :return: whether the first hand has a greater total
        :rtype: bool
        """
        if type(other) is int:
            return self.total[1] < other
        else:
            return self.total[1] < other.total[1]

    def __eq__(self, other):
        """Compares the totals of the hands
        :param other: The other hand object or a number
        :type other: Hand | int
        :return: whether the first hand has an equal total
        :rtype: bool
        """
        if type(other) is int:
            return self.total[1] == other
        else:
            return self.total[1] == other.total[1]

    def __len__(self):
        """Finds the number cards in the hand
        :return: The number of cards in the hand
        :rtype: int
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
        """Checks if the hand is still valid
        :return: Whether the player is still in the game
        :rtype: bool
        """
        if self.total[0] > 21:  # If the min total > 21
            return False
        elif self.total[1] > 21:  # If the player has an ace and the max total > 21
            self.total[1] -= 10  # Sets the max total == min total

        if len(self) == 5:
            self.five_card = True
        return True

    def displayHand(self):
        """Displays the cards drawn at the start of the game, hides second card for dealer's hand
        """
        if self.dealer:
            print("|" + str(self.cards[0]) + "|")
        else:
            print("|"+", ".join(list(map(str, self.cards)))+"| "+f"({self.total[1]})")


if __name__ == "__main__":
    player_hand: Hand = Hand()
    player_hand.displayHand()
    player_hand.drawCard()
    print(player_hand)

    dealer_hand: Hand = Hand(dealer=True)
    dealer_hand.displayHand()
    dealer_hand.drawCard()
    print(dealer_hand)
