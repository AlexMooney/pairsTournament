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
        from random import shuffle

        shuffle(self.gameState.deck)
        self.gameState.deck = self.gameState.deck[N:]

    def deal(self):
        from random import shuffle
        shuffle(self.gameState.deck)

        player_tuples = []
        for player in self.gameState.players:
            new_card = self.gameState.deck.pop(0)
            player.hit(new_card)
            player_tuples.append([player, new_card])

        cardlist = [player_tuple[1] for player_tuple in player_tuples]
        while cardlist.count(min(cardlist)) != 1:
            for player_tuple in player_tuples:
                if player_tuple[1] == min(cardlist):
                    if self.gameState.deck[0] == min(cardlist):
                        
                    new_card = self.gameState.deck.pop(0)
                    player_tuple[0].hit(new_card)






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
