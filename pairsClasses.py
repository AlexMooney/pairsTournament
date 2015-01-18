# -*- coding: utf-8 -*-
# Classes used by the tournament program to run computer continuous Pairs

class Dealer:
    """This asks Strategy classes to play the game and tracks the game state.
    """
    def __init__(self):
        self.gameState = Information()

class Information:
    """This the the game state information provided to Strategy classes to make
    decisions with.
    """
    def __init__(self):
        self.deck = []
        self.discards = []
        self.players = []

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

    def bestFold(self):
        smallest = min(self.inStacks())
        best = []
        for i in range(len(self.players)):
            if smallest in self.Players[i].inStack():
                best += (i, smallest)
        return best

class Player:
    """This holds information about the cards that a player has.
    """
    def __init__(self):
        self._stackSet = set()
        self._pointsList = []

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
