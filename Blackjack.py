import random

class Player:
    score = 0

    def choose_action(self):
        # Get the players input.
        decision = input(f"Your at {self.score}, do you want to hit or stand?")

        # We convert it to lower case for easier checking.
        decision = decision.lower()

        # Is the deicision stand?
        if decision == "stand":
            return self.stand()

        if decision == "hit":
            return self.hit()
        print("Ahemm.. maybe you had a bit too much to drink, sir..")
        return self.choose_action()

    def draw(self):
        pass

    def stand(self):
        pass

    def hit(self):
        pass

def main():
    human_player = Player()


if __name__ == "__main__":
    main()


class Hand:

    def __init__(self, human: Player, dealer=None):
        self.human = human
        self.dealer = dealer

    def new(self):
        # While the human can act.
        self.human.choose_action()
        score = self.human.score
        if score > 21:
            print("You went bust!")
        elif score == 21:
            # TODO check if dealer has blackjack
            print("You win")
        else:
            return self.new()

def main():
    print("Welcome to our humble casino!")
    human_player = Player()
    while True:
        hand = Hand(human=human_player)
        print("A new game has been started")
        hand.new()

