"""Module storing custom Card class"""

from random import randint

SUITS: list[str] = ["Spades ♠", "Hearts ♥", "Clubs ♣", "Diamonds ♦"]
FACES: list[list[str, complex]] = [
        ["Ace", 1 + 11j],
        ["2", 2 + 2j],
        ["3", 3 + 3j],
        ["4", 4 + 4j],
        ["5", 5 + 5j],
        ["6", 6 + 6j],
        ["7", 7 + 7j],
        ["8", 8 + 8j],
        ["9", 9 + 9j],
        ["10", 10 + 10j],
        ["Jack", 10 + 10j],
        ["Queen", 10 + 10j],
        ["King", 10 + 10j]
]


class Card:
    """Class for the cards in play
    """
    def __init__(self):
        """Constructor method
        """
        card_number = randint(0, 51)
        self.suit: str = SUITS[card_number // 13]
        self.face: str = FACES[card_number % 13][0]
        self.value: complex = FACES[card_number % 13][1]

    def __str__(self):
        return f"{self.face} of {self.suit}"


if __name__ == "__main__":
    card: Card = Card()
    print(card)
    print(card.value)
