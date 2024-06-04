"""Module for storing custom Card class"""
from random import choice


FACES: dict[str, list[str, complex]] = {
        "A": ["Ace", 1 + 11j],
        "2": ["2", 2 + 2j],
        "3": ["3", 3 + 3j],
        "4": ["4", 4 + 4j],
        "5": ["5", 5 + 5j],
        "6": ["6", 6 + 6j],
        "7": ["7", 7 + 7j],
        "8": ["8", 8 + 8j],
        "9": ["9", 9 + 9j],
        "10": ["10", 10 + 10j],
        "J": ["Jack", 10 + 10j],
        "Q": ["Queen", 10 + 10j],
        "K": ["King", 10 + 10j]
}


class Card:
    """Class for the cards in play
    """
    def __init__(self, face):
        """Constructor method

        Args:
            face (str): the face of the card
        """
        self.face: str = FACES.get(face)[0]
        self.value: complex = FACES.get(face)[1]

    def __str__(self):
        return self.face

    def __add__(self, card):
        """
        :param card: The other card
        :type card: Card
        """
        return self.value + card.value


if __name__ == "__main__":
    card_1: Card = Card(choice(list(FACES.keys())))
    print(card_1)
    print(card_1.value)
    card_2: Card = Card(choice(list(FACES.keys())))
    print(card_2)
    print(card_2.value)
    print(card_1 + card_2)
