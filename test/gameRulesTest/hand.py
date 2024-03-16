from numpy import array
from card import Card


class Hand:
    def __init__(self):
        self.total: array = array([0, 0])
        self.cards: list[Card] = []
        for _ in range(2):
            card: Card = Card()
            self.drawCard(card)
        self.in_play: bool = True
        self.blackjack: bool = self == 21
        self.five_card: bool = False

    def __repr__(self):
        return "|"+", ".join(list(map(str, self.cards)))+"| "+f"({self.total[1]})"

    def __int__(self):
        return self.total[1]

    def __gt__(self, other):
        """
        Compares the totals of the hands
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
        """
        Compares the totals of the hands
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
        """
        Compares the totals of the hands
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
        """
        Finds the number cards in the hand
        :return: The number of cards in the hand
        :rtype: int
        """
        return len(self.cards)

    def drawCard(self, new_card):
        """
        Adds a card to the hand
        :param new_card: The last card drawn
        :type new_card: Card
        """
        self.cards.append(new_card)
        self.total += new_card.value
        self.in_play = self.checkTotal()

    def checkTotal(self):
        """
        Checks if the hand is still valid
        :return: Whether the player is still in the game
        :rtype: bool
        """
        if self.total[0] > 21:  # If the min total > 21
            return False
        elif self.total[1] > 21:  # If the player has an ace and the max total > 21
            self.total[1] = self.total[0]  # Sets the max total == min total

        if len(self) == 5:
            self.five_card = True
        return True


if __name__ == "__main__":
    hand: Hand = Hand(Card(), Card())
    print(hand)
    print(hand.total)
    hand.drawCard(Card())
    print(hand)
    print(hand.total)
