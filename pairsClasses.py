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
