class Player:
    def __init__(self):
        self.__money = 100
        self.__hand = []
        self.__bet = 5

    def getMoney(self):
        return self.__money

    def updateMoney(self, amount):
        self.__money += amount

    def setBet(self, amount):
        self.__bet = amount

    def getBet(self):
        return self.__bet

    def addCard(self, card):
        self.__hand.append(card)

    def resetHand(self):
        self.__hand = []

    def getHand(self):
        return self.__hand

    def getHandValue(self):
        sum = 0
        for i in range(self.__hand.__len__()-1):
            sum += self.__hand[i].getCardValue()
        return sum