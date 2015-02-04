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
        self.verbose = False
        for n in range(self.gameState.noPlayers):
            self.gameState.players.append(Player(n))

        for i in range(1, 11):
            self.gameState.deck += [i] * i

    def deal(self):
        for player in self.gameState.players:
            newCard = self.gameState.draw()
            player.stack = [newCard]
            player.strategy.player = player

        cardList = [sum(player.stack) for player in self.gameState.players]
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
            minPlayers = [player for player in minPlayers
                           if sum(player.stack) == min(cardList)]

        startPlayer = minPlayers[0]
        self.gameState.startIndex = self.gameState.players.index(startPlayer)

        i = 0
        for player in self.gameState.players:
            i += 1
            self.vPrint('Player ' + str(i) + '\'s stack: ' + str(player.stack))

    def play(self):
        from copy import deepcopy
        self.deal() # should be called by Tournament?
        highestScore = max(int(60 / self.gameState.noPlayers) + 1, 11)

        allScores = [player.getScore() for player in self.gameState.players]
        currentIndex = self.gameState.startIndex

        while max(allScores) < highestScore:
            currentPlayer = self.gameState.players[currentIndex]
            info = deepcopy(self.gameState)
            inStacks = self.gameState.inStacks()
            if inStacks == [] or \
             len(currentPlayer.stack) == 0 or \
             (min(inStacks) + currentPlayer.getScore()) >= highestScore:
                reply = 'hit.'
                self.vPrint('Player '+str(currentIndex+1)+' was forced to hit.')
            else:
                reply = currentPlayer.strategy.play(info)
                self.vPrint('Player '+str(currentIndex+1)+' decided to '+str(reply))

            if reply == 'fold':
                foldFrom = self.gameState.bestFold(currentPlayer)
                self.gameState.players[foldFrom[0]].steal(foldFrom[1])
                currentPlayer.catch(foldFrom[1])
                self.vPrint('You just folded for ' + str(foldFrom[1]) +
                    ' Your stack: ' + str(currentPlayer.stack) +
                    ' Your score: ' + str(currentPlayer.getScore()))
            else:
                try:
                    self.gameState.players[reply[0]].steal(reply[1])
                    currentPlayer.catch(reply[1])
                    self.vPrint('You just folded for ' + str(reply[1]) +
                           ' Your stack: ' +
                           str(currentPlayer.stack) +
                            ' Your score: ' +
                            str(currentPlayer.getScore()))
                except TypeError:
                    hitCard = self.gameState.draw()
                    currentPlayer.hit(hitCard)
                    whichPair = currentPlayer.whichPair()
                    if whichPair:
                        currentPlayer.catch(hitCard)
                        self.vPrint('You just paired for ' + str(hitCard) +
                               ' Your stack: ' +
                               str(currentPlayer.stack) +
                                ' Your score: ' +
                                str(currentPlayer.getScore()))
                    else:
                        self.vPrint('You just hit for ' + str(hitCard) +
                               ' Your stack: ' +
                               str(currentPlayer.stack) +
                                ' Your score: ' +
                                str(currentPlayer.getScore()))


            allScores = [player.getScore() for player in self.gameState.players]
            currentIndex = (currentIndex + 1) % self.gameState.noPlayers

        return ((currentIndex - 1) % self.gameState.noPlayers)+1

    def vPrint(self, *args):
        if self.verbose:
            print(*args)

class Information:
    """This the the game state information provided to Strategy classes to make
    decisions with.
    """
    def __init__(self):
        self.deck = []
        self.discards = []
        self.players = []
        self.burn = 5
        self.startIndex = 0 # Dealer.deal will set this properly
        self.noPlayers = 0 # Dealer.__init__ will set this properly

    def bestFolds(self):
        """
        Gets a list of tuples with the player index and smallest card for each player.
        """
        best = []
        for i in range(len(self.players)):
            low = 10
            for card in self.players[i].stack:
                if low>card:
                    low = card
            best += [(i, low)]
        return best

    def bestFold(self, player):
        """
        Return the "best" fold, for a nondiscriminating sort of strategy.
        """
        best = min([fold[1] for fold in self.bestFolds()])
        index = (player.index()-1)%self.noPlayers # player to right
        while True:
            if min([11]+self.players[index].stack) == best:
                return (index, best)
            else:
                index = (index - 1)%self.noPlayers


    def draw(self):
        from random import choice
        if len(self.deck) <= self.burn: # time to shuffle
            self.deck = []
            for i in range(1, 11):
                self.deck += [i] * i
            for i in self.inPoints() + self.inStacks():
                self.deck.remove(i)
            self.discards = []
        card = choice(self.deck)
        self.deck.remove(card)
        return card

    def inPoints(self):
        self.allPoints = []
        for player in self.players:
            self.allPoints += player.points
        return self.allPoints

    def inStacks(self):
        self.allStacks= []
        for player in self.players:
            self.allStacks += player.stack
        return self.allStacks

class Player:
    """This holds information about the cards that a player has.
    """
    def __init__(self, index):
        self.stack = []
        self.points = []
        self.strategy = SimpletonStrategy()
        self._index = index

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
