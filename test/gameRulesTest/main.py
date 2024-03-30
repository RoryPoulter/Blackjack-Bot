from time import sleep
from hand import Hand


class Game:
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
            self.gameOver("dealer", "blackjack")
        elif self.player_hand.blackjack:
            self.gameOver("player", "blackjack")
        else:
            self.playerTurn()

    def gameOver(self, winner, win_condition):
        messages = {
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
            self.gameOver("dealer", "5 card")
        elif len(self.player_hand) == 5:
            self.gameOver("player", "5 card")
        elif self.player_hand > self.dealer_hand:
            self.gameOver("player", "greater")
        else:
            self.gameOver("dealer", "greater")

    def playerTurn(self):
        draw = input("Draw card? [y/n]: ").upper()
        if draw == "Y":
            sleep(0.5)
            self.player_hand.drawCard()
            print(self.player_hand)
            if not self.player_hand.in_play:
                print(self.dealer_hand)
                self.gameOver("dealer", "bust")
            elif (len(self.player_hand) == 5) or (self.player_hand == 21):
                self.dealerTurn()
            else:
                self.playerTurn()
        else:
            self.dealerTurn()

    def dealerTurn(self):
        print(self.dealer_hand)
        while self.dealer_hand < 17:
            sleep(0.5)
            self.dealer_hand.drawCard()
            print(self.dealer_hand)
        if self.dealer_hand == 21:
            self.gameOver("dealer", "21")
        elif self.dealer_hand > 21:
            self.gameOver("player", "bust")
        else:
            self.decideWinner()


def main():
    Game()


if __name__ == "__main__":
    main()
