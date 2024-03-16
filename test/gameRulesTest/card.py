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
    def __init__(self):
        card_number = randint(0, 51)
        self.suit: str = SUITS[card_number // 13]
        self.face: str = FACES[card_number % 13][0]
        self.value: array = FACES[card_number % 13][1]

    def __str__(self):
        return f"{self.face} of {self.suit}"


if __name__ == "__main__":
    card: Card = Card()
    print(card)
    print(card.value)