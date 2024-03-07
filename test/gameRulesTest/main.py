from random import randint
from numpy import array


class Hand:
    def __init__(self, *cards):
        """
        :param card_1: The cards drawn
        :type cards: Card
        """
        self.total: array = array([0, 0])
        for card in cards:
            self.total += card.value
            self.checkTotal()
        self.cards: list[Card] = [*cards]

    def __repr__(self):
        return ", ".join(list(map(str, self.cards)))

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
        self.checkTotal()

    def checkTotal(self):
        """
        Checks if the hand is still valid
        :return: Whether the player is still in the game
        :rtype: bool
        """
        if self.total[0] > 21:  # If the min total > 21
            print("Bust!")
            return False
        elif self.total[1] > 21:  # If the player has an ace and the max total > 21
            self.total[1] = self.total[0]  # Sets the max total == min total
        return True

    def split(self):
        if (self.cards[0].face == self.cards[1].face) and (len(self) == 2):
            second_hand: Hand = Hand(self.cards[1])
            self.total = self.cards[0].value
            self.cards = self.cards[:1]
            return second_hand

    def burn(self):
        if self.total[1] == 14:
            no_of_cards: int = len(self)
            new_cards: dict[int, Card] = {}
            for i in range(no_of_cards):
                new_cards[i] = Card(randint(0, 51))
            self.__init__(*new_cards.values())


class Card:
    def __init__(self, card_number):
        """
        :param card_number: Random number to determine suit and face
        :type card_number: int
        :raise ValueError: If card_number is out of range
        """
        if card_number > 51 or card_number < 0:
            raise ValueError("card_number must be between 0 and 51 inclusive")
        self.suit: str = SUITS[card_number // 13]
        self.face: str = FACES[card_number % 13][0]
        self.value: array = FACES[card_number % 13][1]

    def __str__(self):
        return f"{self.face} of {self.suit}"


if __name__ == "__main__":
    SUITS: list[str] = ["Spades", "Hearts", "Clubs", "Diamonds"]
    FACES: list[list[str, array]] = [
        ["Ace", array([1, 11])],
        ["2", array([2, 2])],
        ["3", array([3, 3])],
        ["4", array([4, 4])],
        ["5", array([5, 5])],
        ["6", array([6, 6])],
        ["7", array([7, 7])],
        ["8", array([8, 8])],
        ["9", array([9, 9])],
        ["10", array([10, 10])],
        ["Jack", array([10, 10])],
        ["Queen", array([10, 10])],
        ["King", array([10, 10])],
    ]

    card_1: Card = Card(1)  # 2 of Spades
    card_2: Card = Card(12)  # King of Spades
    card_3: Card = Card(1)  # 2 of Spades
    hand: Hand = Hand(card_1, card_2, card_3)
    print(hand, hand.total)
    hand.burn()
    print(hand, hand.total)
