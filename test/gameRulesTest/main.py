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
        self.in_play: bool = True

    def __repr__(self):
        return "|"+", ".join(list(map(str, self.cards)))+"|"

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
        return True

    def split(self):
        """
        Splits the hand if the faces of the two cards are the same
        :return: The hand with the second card
        :rtype: Hand
        :raise ValueError: If the hand does not have 2 cards of the same face
        """
        if (self.cards[0].face == self.cards[1].face) and (len(self) == 2):
            second_hand: Hand = Hand(self.cards[1])
            self.total = self.cards[0].value
            self.cards = self.cards[:1]
            return second_hand
        else:
            raise ValueError("Hand must be 2 cards with the same face to split")

    def burn(self):
        """
        Draws a new hand of the same number of cards if the total is 14
        :raise ValueError: If the total is not 14
        """
        if self.total[1] == 14:
            no_of_cards: int = len(self)
            new_cards: dict[int, Card] = {}
            for i in range(no_of_cards):
                new_cards[i] = Card()
            self.__init__(*new_cards.values())
        else:
            raise ValueError("Total must be 14 to burn")


class Card:
    def __init__(self):
        card_number = randint(0, 51)
        self.suit: str = SUITS[card_number // 13]
        self.face: str = FACES[card_number % 13][0]
        self.value: array = FACES[card_number % 13][1]

    def __str__(self):
        return f"{self.face} of {self.suit}"


class Player:
    def __init__(self):
        self.in_play: bool = True
        card_1: Card = Card()
        print(card_1)
        card_2: Card = Card()
        print(card_2)
        first_hand: Hand = Hand(card_1, card_2)
        self.hands: list[Hand] = [first_hand]
        self.hand_index: int = 0
        self.max = self.hands[0].total[1]
        if self.max == 21:
            print("Blackjack!")

    def maxTotal(self):
        player_max = 0
        for hand in self.hands:
            player_max = max(player_max, hand.total[1])
        self.max = player_max

    def twist(self):
        new_card: Card = Card()
        print(new_card)
        self.hands[self.hand_index].drawCard(new_card)
        if self.hands[self.hand_index] > 21:
            print("Bust!")
            self.hands.pop(self.hand_index)
            if self.hand_index >= len(self.hands):
                self.hand_index = 0

        if not self.hands:
            print("Out of play!")
            self.in_play = False
        else:
            print(self.hands)
            self.maxTotal()
            print(self.max)

    def stick(self):
        self.in_play = False

    def burn(self):
        self.hands[self.hand_index].burn()
        print(self.hands)
        self.maxTotal()
        print(self.max)

    def split(self):
        new_hand: Hand = self.hands[self.hand_index].split()
        self.hands.append(new_hand)
        print(self.hands)
        self.maxTotal()
        print(self.max)

    def changeHand(self):
        self.hand_index = int(input("Which hand? "))

    def turn(self):
        print(self.hands)
        choice: int = int(input("""Enter move: 
    1. Twist
    2. Stick
    3. Burn
    4. Split
    5. Change hand
"""))
        moves: dict = {
            1: self.twist,
            2: self.stick,
            3: self.burn,
            4: self.split,
            5: self.changeHand
        }
        moves.get(choice)()


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

    user_player: Player = Player()
    while user_player.in_play:
        user_player.turn()
