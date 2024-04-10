from numpy import array
from random import randint


SUITS: list[str] = ["Spades ♠", "Hearts ♥", "Clubs ♣", "Diamonds ♦"]
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
        ["King", array([10, 10])]
]


class Card:
    def __init__(self, value):
        """Constructor method
        :param value: The value to identify the card, 0-51
        :type value: int
        """
        self.suit: str = SUITS[value // 13]
        self.face: str = FACES[value % 13][0]
        self.value: array = FACES[value % 13][1]

    def __str__(self):
        return f"{self.face} of {self.suit}"


if __name__ == "__main__":
    card: Card = Card(randint(0, 51))
    print(card)
    print(card.value)
