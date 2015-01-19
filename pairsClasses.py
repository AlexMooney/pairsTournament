# -*- coding: utf-8 -*-
# Classes used by the tournament program to run computer continuous Pairs

class Dealer:
    """This asks Strategy classes to play the game and tracks the game state.

    >>> d = Dealer()


    >>> d.gameState.deck
    [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

    """

    def __init__(self):

        self.gameState = Information()
        for i in range(1, 11):
            self.gameState.deck += [i] * i

    def burn(self, N=5):
        """
        >>> d = Dealer()


        >>> d.burn()


        >>> len(d.gameState.deck)
        50

        """
        from random import choice
        for i in range(N):
            self.gameState.deck.remove(choice(self.gameState.deck))

    def deal(self):

        self.burn()
        for player in self.gameState.players:
            self.gameState.discards.append(player.stack)
            new_card = self.gameState.deck.draw()
            player.stack = [new_card]

        cardlist = [sum(player.stack) for player in min_players]
        min_players = [player for player in self.gameState.players
                       if sum(player.stack) == min(cardlist)]


        while len(min_players) != 1:
            for player in list(min_players):
                if sum(player.stack) != min(cardlist):
                    min_players.remove(player)
                else:
                    player.hit(self.gameState.draw())
                    while player.whichPair() != False:
                        self.gameState.discards.append(player.stack.pop(-1))
                        player.hit(self.gameState.draw())
            cardlist = [sum(player.stack) for player in min_players]

        global start_player
        start_player = min_player[0]

    def play(self):
        highest_score = max(int(60 / N) + 1, 11)








class Information:
    """This the the game state information provided to Strategy classes to make
    decisions with.
    """
    def __init__(self):
        self.deck = []
        self.discards = []
        self.players = []

    def bestFold(self):
        smallest = min(self.inStacks())
        best = []
        for i in range(len(self.players)):
            if smallest in self.Players[i].inStack():
                best += (i, smallest)
        return best

    def draw(self):
        from random import choice
        if len(self.deck) == 0: # shuffle
            self.deck = []
            for i in range(1, 11):
                self.deck += [i] * i
            for i in self.inPoints() + self.inStacks():
                self.deck.remove(i)
            self.deck.burn()
            self.discards = []
        card = choice(deck)
        deck.remove(card)
        return card

    def inPoints(self):
        try:
            return self.allPoints
        except NameError:
            self.allPoints = []
            for player in self.Players:
                self.allPoints += player._pointsList
            return self.allPoints

    def inStacks(self):
        try:
            return self.allStacks
        except NameError:
            self.allStacks= []
            for player in self.Players:
                self.allPoints += list(player._stackSet)
            return self.allPoints

class Player:
    """This holds information about the cards that a player has.
    """
    def __init__(self):
        self.stack = []
        self.points = []

    def catch(self, card):
        self.stack = []
        self.points.append(card)

    def hit(self, card):
        self.stack.append(card)

    def index(self, newIndex=None):
        if newIndex == None:
            return self._index
        self._index = newIndex

    def getScore(self):
        return sum(self.points)

    def getSmallest(self):
        return min(self.stack)

    def steal(self, card):
        self.stack.remove(card)

    def whichPair(self):
        if self.stack == []:
            return False
        from collections import Counter
        mostCommon = Counter(self.stack).most_common(1)[0]
        if mostCommon[1] > 1:
            return mostCommon[0]
        else:
            return False

class SimpletonStrategy:
    """This is an example strategy"""
    def __init__(self):
        self.shouldIHit = True
    def play(self, info):
        if self.shouldIHit:
            return "Hit me; I can't lose!"
        else:
            return "fold"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
