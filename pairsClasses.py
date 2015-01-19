# -*- coding: utf-8 -*-
# Classes used by the tournament program to run computer continuous Pairs

class Dealer:
    """This asks Strategy classes to play the game and tracks the game state.

    >>> d = Dealer()


    >>> d.gameState.deck
    [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

    """

    def __init__(self, noPlayers = 5):

        self.gameState = Information()
        self.gameState.noPlayers = noPlayers
        for n in range(self.gameState.noPlayers):
            self.gameState.players.append(Player())

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

        cardList = [sum(player.stack) for player in minPlayers]
        minPlayers = [player for player in self.gameState.players
                       if sum(player.stack) == min(cardList)]


        while len(minPlayers) != 1:
            for player in list(minPlayers):
                if sum(player.stack) != min(cardList):
                    minPlayers.remove(player)
                else:
                    player.hit(self.gameState.draw())
                    while player.whichPair() != False:
                        self.gameState.discards.append(player.stack.pop(-1))
                        player.hit(self.gameState.draw())
            cardList = [sum(player.stack) for player in minPlayers]

        startPlayer = minPlayers[0]
        self.gameState.currentIndex = self.gameState.players.index(startPlayer)

    def play(self):
        from copy import deepcopy
        self.deal() # should be called by Tournament?
        highestScore = max(int(60 / self.gameState.players) + 1, 11)

        allScores = [player.getScore() for player in self.gameState.players]

        while max(allScores) < highestScore:
            info = deepcopy(self.gameState)
            reply = self.gameState.players[currentIndex].strategy.play(info)
            if reply == 'fold':
                foldFrom = self.gameState.bestFold()
                self.gameState.players[foldFrom(0)].steal(foldFrom[1])
                self.gameState.players[currentIndex].catch(foldFrom[1])

            else:
                try:
                    self.gameState.players[reply[0]].steal(reply[1])
                    self.gameState.players[currentIndex].catch(reply[1])
                except TypeError:
                    self.gameState.players[currentIndex].hit(self.gameState.deck.draw())

            allScores = [player.getScore() for player in self.gameState.players]
            currentIndex = (currentIndex + 1) % self.gameState.noPlayers

        return [player in self.gameState.players
               if player.getScore() >= highestScore][0]


class Information:
    """This the the game state information provided to Strategy classes to make
    decisions with.
    """
    def __init__(self):
        self.deck = []
        self.discards = []
        self.players = []
        self.currentIndex = 0 # Dealer.deal will set this properly

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
                self.allPoints += player.points
            return self.allPoints

    def inStacks(self):
        try:
            return self.allStacks
        except NameError:
            self.allStacks= []
            for player in self.Players:
                self.allPoints += list(player.stack)
            return self.allPoints

class Player:
    """This holds information about the cards that a player has.
    """
    def __init__(self):
        self.stack = []
        self.points = []
        self.strategy = SimpletonStrategy()

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
            return 'Hit me; I can\'t lose!'
        else:
            return 'fold'

if __name__ == "__main__":
    import doctest
    doctest.testmod()
