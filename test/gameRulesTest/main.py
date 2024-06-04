"""Example code for how the rules of the game will be applied.
Real code will need to be different as cards will not be generated randomly but instead drawn from 
a physical deck and read by a camera. `Game` class will need to have 3 parameters for the revealed 
dealer card and the 2 player cards.
"""
from time import sleep

from hand import Hand

class Game:
    """The game
    """
    def __init__(self):
        """Constructor method
        """
        self.player_hand: Hand = Hand()
        self.dealer_hand: Hand = Hand(dealer=True)

        print("Player hand:")
        self.player_hand.displayHand()
        print("Dealer hand:")
        self.dealer_hand.displayHand()

        if self.dealer_hand.blackjack:
            print(self.dealer_hand)
            self.gameOver("Dealer", "blackjack")
        elif self.player_hand.blackjack:
            self.gameOver("Player", "blackjack")
        else:
            self.playerTurn()

    def gameOver(self, winner, win_condition):
        """Displays the game over message

        Args:
            winner (Literal["Player", "Dealer"]): Who won the game
            win_condition (Literal["blackjack", "5 card", "21", "greater", "bust"]): How the game was won
        """
        messages: dict[str, str] = {
            "blackjack": f"{winner} won with blackjack!",
            "5 card": f"{winner} won with 5 cord trick!",
            "21": f"{winner} won with 21!",
            "greater": f"{winner} won with {max(int(self.player_hand), int(self.dealer_hand))}!",
            "bust": f"{winner} won by bust!"
        }
        print(messages[win_condition])

    def decideWinner(self):
        """Determines the winner of the game
        """
        if len(self.dealer_hand) == 5:
            self.gameOver("Dealer", "5 card")
        elif len(self.player_hand) == 5:
            self.gameOver("Player", "5 card")
        elif self.player_hand > self.dealer_hand:
            self.gameOver("Player", "greater")
        else:
            self.gameOver("Dealer", "greater")

    def playerTurn(self):
        """Allows the player to draw a card or end their turn
        """
        draw: str = input("Draw card? [y/n]: ").upper()
        if draw == "Y":
            sleep(0.5)
            self.player_hand.drawCard()
            print(self.player_hand)
            if not self.player_hand.in_play:
                print(self.dealer_hand)
                self.gameOver("Dealer", "bust")
            elif (len(self.player_hand) == 5) or (self.player_hand == 21):
                self.dealerTurn()
            else:
                self.playerTurn()
        elif draw == "N":
            self.dealerTurn()
        else:
            print("Invalid input: enter either 'y' or 'n'")
            self.playerTurn()

    def dealerTurn(self):
        """Dealer draws cards until their total is equal to or greater than 17
        """
        print(self.dealer_hand)
        while self.dealer_hand < 17:
            sleep(0.5)
            self.dealer_hand.drawCard()
            print(self.dealer_hand)
        if self.dealer_hand == 21:
            self.gameOver("Dealer", "21")
        elif self.dealer_hand > 21:
            self.gameOver("Player", "bust")
        else:
            self.decideWinner()


if __name__ == "__main__":
    Game()
