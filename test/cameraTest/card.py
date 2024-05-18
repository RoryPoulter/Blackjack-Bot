from numpy import array


SUITS: dict[str, str] = {
    "♠": "Spades ♠",
    "♥": "Hearts ♥",
    "♣": "Clubs ♣",
    "♦": "Diamonds ♦"
}
FACES: dict[str, list[str, array]] = {
        "A": ["Ace", array([1, 11])],
        "2": ["2", array([2, 2])],
        "3": ["3", array([3, 3])],
        "4": ["4", array([4, 4])],
        "5": ["5", array([5, 5])],
        "6": ["6", array([6, 6])],
        "7": ["7", array([7, 7])],
        "8": ["8", array([8, 8])],
        "9": ["9", array([9, 9])],
        "10": ["10", array([10, 10])],
        "J": ["Jack", array([10, 10])],
        "Q": ["Queen", array([10, 10])],
        "K": ["King", array([10, 10])]
}


class Card:
    def __init__(self, face, suit):
        """Constructor method
        :param face: The face of the card
        :type face: str:
        :param suit: The suit of the card
        :type suit: str
        """
        self.suit: str = SUITS.get(suit)
        self.face: str = FACES.get(face)[0]
        self.value: array = FACES.get(face)[1]

    def __str__(self):
        return f"{self.face} of {self.suit}"


if __name__ == "__main__":
    card: Card = Card("A", "♣")
    print(card)
    print(card.value)
