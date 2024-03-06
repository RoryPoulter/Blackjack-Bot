from random import randint
from numpy import array


class Hand:
    def __init__(self, card_1, card_2):
        """
        :param card_1: The first card drawn
        :type card_1: Card
        :param card_2: The second card drawn
        :type card_2: Card
        """
        self.total = card_1.value + card_2.value
        self.cards = [card_1, card_2]

    def __repr__(self):
        return ", ".join(list(map(str, self.cards)))

    def __gt__(self, other):
        """
        Compares the totals of the hands
        :param other: The other hand object
        :type other: Hand
        :return: whether the first hand has a greater total
        :rtype: bool
        """
        return self.total[1] > other.total[1]

    def drawCard(self, new_card):
        """

        :param new_card: The last card drawn
        :type new_card: Card
        :return:
        """
        self.cards.append(new_card)
        self.total += new_card.value
        self.checkTotal()

    def checkTotal(self):
        if self.total[0] > 21:
            print("Bust!")
            return False
        elif self.total[1] > 21:
            self.total[1] = self.total[0]
        return True


class Card:
    def __init__(self, card_number):
        """

        :param card_number: Random number to determine suit and face
        :type card_number: int
        """
        self.suit = SUITS[card_number // 13]
        self.face = FACES[card_number % 13][0]
        self.value = FACES[card_number % 13][1]

    def __str__(self):
        return f"{self.face} of {self.suit}"


if __name__ == "__main__":
    SUITS = ["Spades", "Hearts", "Clubs", "Diamonds"]
    FACES = {
        0: ["Ace", array([1, 11])],
        1: ["2", array([2, 2])],
        2: ["3", array([3, 3])],
        3: ["4", array([4, 4])],
        4: ["5", array([5, 5])],
        5: ["6", array([6, 6])],
        6: ["7", array([7, 7])],
        7: ["8", array([8, 8])],
        8: ["9", array([9, 9])],
        9: ["10", array([10, 10])],
        10: ["Jack", array([10, 10])],
        11: ["Queen", array([10, 10])],
        12: ["King", array([10, 10])],
    }

    card_1 = Card(2)
    print(card_1)
    card_2 = Card(11)
    print(card_2)
    hand = Hand(card_1, card_2)
    print(hand)
    print(hand.total)
    card_3 = Card(12)
    hand.drawCard(card_3)
    print(hand.total)
