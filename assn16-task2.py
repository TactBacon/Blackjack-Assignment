from player import Player
from deck import Deck
import time


def main():
    print("Welcome to Blackjack")

    playerCount = eval(input("Please enter the amount of players (1-5): ").strip())
    playerCount = playerCount < 1 and 1 or playerCount > 5 and 5 or playerCount

    print()

    deck = Deck()

    players = []
    for i in range(playerCount):
        players.append(Player())
    dealer = Player()

    playing = True
    while playing:
        # Bet
        for i in range(playerCount):
            if players[i].getMoney() > 0:
                print("Player" + str(i) + ", you have $" + str(players[i].getMoney()))
                betAmount = eval(input("Please enter your amount to bet (minimum: 5): $").strip())
                if players[i].getMoney() <= 5 or betAmount > players[i].getMoney():
                    betAmount = players[i].getMoney()
                elif betAmount < 5:
                    betAmount = 5

                players[i].setBet(betAmount)
                print("You bet $" + str(betAmount) + "\n")

        # Deal the cards

        print()

        deck.shuffle()
        for i in range(playerCount):
            players[i].resetHand()
        dealer.resetHand()

        for i in range(2):
            for j in range(playerCount+1):
                if j < playerCount:
                    if players[j].getMoney() > 0:
                        players[j].addCard(deck.draw())
                else:
                    dealer.addCard(deck.draw())

        print("The dealer's second card is the " + str(dealer.getHand()[1]))

        # Ask players if they'd like to hit or hold

        for i in range(playerCount):
            if players[i].getMoney() > 0:
                hold = False
                while not hold:
                    print("\nIt's your turn, Player" + str(i) + ", you have these cards:")
                    print(*players[i].getHand(), sep=", ")
                    choice = input("\nWould you like to hit or hold: ").strip()

                    if choice == "hit":
                        card = deck.draw()
                        print("You were given the " + str(card))
                        players[i].addCard(card)
                        sum = players[i].getHandValue()
                        if sum > 21:
                            print("You have busted, your cards' value: " + str(sum))
                            hold = True

                    elif choice == "hold":
                        print("You have decided to hold")
                        hold = True
            print()

        # Dealer's turn

        print("\nIt's the dealer's turn, the dealer has these cards:")
        print(*dealer.getHand(), sep="\n")
        print()

        hold = False
        while not hold:
            sum = dealer.getHandValue()

            if sum > 21:
                print("The dealer has busted with a total sum of " + str(sum))
                hold = True

            elif sum <= 21 and sum >= 17:
                print("The dealer has decided to hold.")
                hold = True

            elif sum < 17:
                print("The dealer is drawing another card...")
                time.sleep(1)
                card = deck.draw()
                print("The dealer was given the " + str(card))
                dealer.addCard(card)
                sum = dealer.getHandValue()
                if sum <= 21 and sum > 17:
                    hold = True
                    print("The dealer has decided to hold.")
                elif sum > 21:
                    hold = True
                    print("The dealer has busted with a total sum of " + str(sum))

        # Determine winners

        print()

        for i in range(playerCount):
            if players[i].getMoney() > 0:
                if players[i].getHandValue() < 22:
                    if dealer.getHandValue() < players[i].getHandValue() or dealer.getHandValue() > 21:
                        print("Player" + str(i) + ", you have won!  You have received $" + str(players[i].getBet()))
                        players[i].updateMoney(players[i].getBet())
                    elif dealer.getHandValue() == players[i].getHandValue():
                        print("Player" + str(i) + ", you have tied with the dealer and have neither gained nor \
                            lost money.")
                    else:
                        print("Player" + str(i) + ", you have been beaten!  You have lost $" + str(players[i].getBet()))
                        players[i].updateMoney(-players[i].getBet())
                else:
                    print("Player" + str(i) + ", you have busted!  You have lost $" + str(players[i].getBet()))
                    players[i].updateMoney(-players[i].getBet())

        # Display scores

        print()

        canPlay = False
        for i in range(playerCount):
            if players[i].getMoney() > 0:
                canPlay = True
            print("Player" + str(i) + " has $" + str(players[i].getMoney()))

        # Ask to play again

        print()

        if canPlay:
            playAgain = input("Would you like to play again? (y/n): ").strip()
            if playAgain == "n":
                playing = False
        else:
            print("All players have run out of money.")
            playing = False

    # End of game

    for i in range(playerCount):
        for j in range(0, playerCount - 1):
            if players[j].getMoney() > players[j + 1].getMoney():
                players[j], players[j + 1] = players[j + 1], players[j]

    print("\n\nThanks for playing!\nSCORES:")

    for i in range(playerCount):
        print("Player" + str(i) + ": $" + str(players[i].getMoney()))


main()
