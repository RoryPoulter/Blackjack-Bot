"""Example code for how the rules of the game will be applied.
Real code will need to be different as cards will not be generated randomly but instead drawn from 
a physical deck and read by a camera. `Game` class will need to have 3 parameters for the revealed 
dealer card and the 2 player cards.
"""
from time import sleep
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


class Game:
    """The game
    """
    def __init__(self):
        """Constructor method
        """
        self.player_hand: Hand = Hand()
        self.dealer_hand: Hand = Hand(dealer=True)

        print("Player hand:")
        self.player_hand.display_hand()
        print("Dealer hand:")
        self.dealer_hand.display_hand()

        if self.dealer_hand.blackjack:
            print(self.dealer_hand)
            self.game_over("Dealer", "blackjack")
        elif self.player_hand.blackjack:
            self.game_over("Player", "blackjack")
        else:
            self.player_turn()

    def game_over(self, winner, win_condition):
        """Displays the game over message

        Args:
            winner (Literal["Player", "Dealer"]): Who won the game
            win_condition (Literal["blackjack", "5 card", "21", "greater", "bust"]): Win method
        """
        messages: dict[str, str] = {
            "blackjack": f"{winner} won with blackjack!",
            "5 card": f"{winner} won with 5 cord trick!",
            "21": f"{winner} won with 21!",
            "greater": f"{winner} won with {max(int(self.player_hand), int(self.dealer_hand))}!",
            "bust": f"{winner} won by bust!"
        }
        print(messages[win_condition])

    def decide_winner(self):
        """Determines the winner of the game
        """
        if len(self.dealer_hand) == 5:
            self.game_over("Dealer", "5 card")
        elif len(self.player_hand) == 5:
            self.game_over("Player", "5 card")
        elif self.player_hand > self.dealer_hand:
            self.game_over("Player", "greater")
        else:
            self.game_over("Dealer", "greater")

    def player_turn(self):
        """Allows the player to draw a card or end their turn
        """
        draw: str = input("Draw card? [y/n]: ").upper()
        if draw == "Y":
            sleep(0.5)
            self.player_hand.draw_card()
            print(self.player_hand)
            if not self.player_hand.in_play:
                print(self.dealer_hand)
                self.game_over("Dealer", "bust")
            elif (len(self.player_hand) == 5) or (self.player_hand == 21):
                self.dealer_turn()
            else:
                self.player_turn()
        elif draw == "N":
            self.dealer_turn()
        else:
            print("Invalid input: enter either 'y' or 'n'")
            self.player_turn()

    def dealer_turn(self):
        """Dealer draws cards until their total is equal to or greater than 17
        """
        print(self.dealer_hand)
        while self.dealer_hand < 17:
            sleep(0.5)
            self.dealer_hand.draw_card()
            print(self.dealer_hand)
        if self.dealer_hand == 21:
            self.game_over("Dealer", "21")
        elif self.dealer_hand > 21:
            self.game_over("Player", "bust")
        else:
            self.decide_winner()


class Hand:
    """The hand to store the cards.
    """
    def __init__(self, dealer=False):
        """Constructor method

        Args:
            dealer (bool, optional): If the hand belongs to the dealer. Defaults to False.
        """
        self.total: complex = 0 + 0j
        self.cards: list[Card] = []
        for _ in range(2):
            self.draw_card()
        self.in_play: bool = True
        self.blackjack: bool = self == 21
        self.five_card: bool = False
        self.dealer: bool = dealer

    def __repr__(self):
        """Formats the cards in the hand and the total in a string representation

        Returns:
            str: The formatted string
        """
        return "|"+", ".join(list(map(str, self.cards)))+"| "+f"({self.total.imag})"

    def __int__(self):
        """Returns the higher total of the hand

        Returns:
            int: The total of the hand
        """
        return int(self.total.imag)

    def __gt__(self, other):
        """Checks if the value of the hand is greater than a given value

        Args:
            other (int, Hand): The value being compared with the hand

        Returns:
            bool: True if greater than the other value, else False
        """
        if isinstance(other, int):
            return self.total.imag > other
        return self.total.imag > other.total.imag

    def __lt__(self, other):
        """Checks if the value of the hand is less than a given value

        Args:
            other (int, Hand): The value being compared with the hand

        Returns:
            bool: True if less than the other value, else False
        """
        if isinstance(other, int):
            return self.total.imag < other
        return self.total.imag < other.total.imag

    def __eq__(self, other):
        """Checks if the value of the hand is equal to a given value

        Args:
            other (int, Hand): The value being compared with the hand

        Returns:
            bool: True if equal to the other value, else False
        """
        if isinstance(other, int):
            return self.total.imag == other
        return self.total.imag == other.total.imag

    def __len__(self):
        """Returns the size of the hand

        Returns:
            int: The number of cards in the hand
        """
        return len(self.cards)

    def draw_card(self):
        """Adds a card to the hand
        """
        new_card: Card = Card()
        self.cards.append(new_card)
        self.total += new_card.value
        self.in_play = self.check_total()

    def check_total(self):
        """Checks if the player has bust

        Returns:
            bool: True if the hand is still in play, else False
        """
        if self.total.real > 21:  # If the min total > 21
            return False
        if self.total.imag > 21:  # If the player has an ace and the max total > 21
            self.total -= 10j  # Sets the max total == min total

        if len(self) == 5:
            self.five_card = True
        return True

    def display_hand(self):
        """Displays the cards drawn at the start of the game, hides second card for dealer's hand
        """
        if self.dealer:
            print("|" + str(self.cards[0]) + "|")
        else:
            print("|"+", ".join(list(map(str, self.cards)))+"| "+f"({self.total.imag})")


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

    def __int__(self):
        return self.value.imag


if __name__ == "__main__":
    Game()
