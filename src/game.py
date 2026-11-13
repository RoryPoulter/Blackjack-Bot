"""The code for the rules of the game.
"""


import random


SUITS = ["Hearts", "Spades", "Diamonds", "Clubs"]
FACES = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]


class Card:
    """Class for card objects. The value is stored as a `complex` type, where the real component
    corresponds to when an 'Ace' is worth 1, and the imaginary component corresponds to when an
    'Ace' is worth 11; if there are no 'Aces' in the hand, these are the same .
    """
    def __init__(self, suit: str, face: str):
        self.suit = suit
        self.face = face
        # Ace
        if self.face == "Ace":
            self.value = 1+11j
        # 2 - 10
        elif self.face.isnumeric():
            self.value = int(self.face) * (1+1j)
        # Face cards
        else:
            self.value = 10+10j

    def __str__(self):
        return f"{self.face} of {self.suit}"

    def get_value(self) -> complex:
        """Getter for value attribute.

        Returns:
            complex: The value of the card.
        """
        return self.value


class Hand:
    """Class for hand objects, which contain cards.
    """
    def __init__(self, first_card: Card, second_card: Card):
        self.cards: list = []
        self.total = 0+0j
        self.add_card(first_card)
        self.add_card(second_card)
        self.bust = False
        self.blackjack = self.total.imag == 21

    def __repr__(self):
        return ", ".join(map(str, self.cards))

    def get_total(self) -> complex:
        """Getter for the total value of the hand.

        Returns:
            complex: The total value of the hand.
        """
        return self.total

    def add_card(self, card: Card) -> None:
        """Adds a card to the hand and updates the total value.

        Args:
            card (Card): The new card to add to the hand.
        """
        self.cards.append(card)
        # If the hand already has an 'Ace', adding another will have no affect at value of 11.
        if self.total.real != self.total.imag and card.face == "Ace":
            self.total += 1+1j
        # All other cases.
        else:
            self.total += card.value
        # Check if the hand is bust.
        if self.total.real > 21:
            self.bust = True

    def is_bust(self) -> bool:
        """Returns boolean value for if the hand has bust.

        Returns:
            bool: If the value of the hand exceeds 21.
        """
        return self.bust

    def is_blackjack(self) -> bool:
        """Returns boolean value for if the hand is a blackjack.

        Returns:
            bool: If the initial value is 21.
        """
        return self.blackjack


def draw_random_card() -> Card:
    """Factory method for generating a random card.

    Returns:
        Card: A card with a random suit and face.
    """
    rand_suit = random.choice(SUITS)
    rand_face = random.choice(FACES)
    return Card(rand_suit, rand_face)


def draw_card(suit: str, face: str) -> Card:
    """Factory method for generating a specific card.

    Args:
        suit (str): The suit of the card.
        face (str): The face of the card.

    Raises:
        ValueError: If the suit is not in `SUITS`.
        ValueError: If the face is not in `FACES`.

    Returns:
        Card: The specified card object.
    """
    if suit not in SUITS:
        raise ValueError(f"{suit} is not a valid suit")
    if face not in FACES:
        raise ValueError(f"{face} is not a valid face")
    return Card(suit, face)


if __name__ == "__main__":
    # card_1 = draw_random_card()
    # card_2 = draw_random_card()
    card_1 = draw_card("Clubs", "Ace")
    card_2 = draw_card("Clubs", "5")
    hand = Hand(card_1, card_2)
    print(hand.get_total(), hand)
    if hand.is_blackjack():
        print("Blackjack!")

    while hand.get_total().imag < 17 and hand.get_total().real < 17:
        new_card = draw_random_card()
        hand.add_card(new_card)
        print(hand.get_total(), hand)
    if hand.is_bust():
        print("Bust!")
