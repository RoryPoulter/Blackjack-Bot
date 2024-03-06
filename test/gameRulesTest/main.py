from random import randint


class Hand:
    def __init__(self, card_1, card_2):
        """
        :param card_1: The first card drawn
        :type card_1: Card
        :param card_2: The second card drawn
        :type card_2: Card
        """
        self.total = [0, 0]
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
        return self.total > other.total

    def drawCard(self, new_card):
        """

        :param new_card: The last card drawn
        :type new_card: Card
        :return:
        """
        self.cards.append(new_card)

    def checkTotal(self):
        if self.total[1] > 21:
            print("Bust!")
            return False
        elif self.total[0] > 21:
            self.total[0] = self.total[1]
        return True


class Card:
    def __init__(self, card_number):
        self.suit = SUITS[card_number // 13]
        self.face = FACES[card_number % 13][0]
        self.value = 0

    def __str__(self):
        return f"{self.face} of {self.suit}"


if __name__ == "__main__":
    SUITS = ["Spades", "Hearts", "Clubs", "Diamonds"]
    FACES = {
        0: ["Ace", 1],
        1: ["2", 2],
        2: ["3", 3],
        3: ["4", 4],
        4: ["5", 5],
        5: ["6", 6],
        6: ["7", 7],
        7: ["8", 8],
        8: ["9", 9],
        9: ["10", 10],
        10: ["Jack", 10],
        11: ["Queen", 10],
        12: ["King", 10],
    }
    card_number = randint(0, 51)
    card_1 = Card(card_number)
    print(card_1)
    card_number = randint(0, 51)
    card_2 = Card(card_number)
    print(card_2)
    hand = Hand(card_1, card_2)
    print(hand)
