from __future__ import division
from math import ceil
from copy import copy
import numpy

class FoldLowWithHigh:
    def __init__(self, fold, hand):
        ''' Strategy that folds when 'fold' is available if 'hand' or higher is in hand'''
        self.fold = fold
        self.hand = hand

    def play(self, info):
        # get best fold as tuple (playerIndex, card)
        best = info.bestFold(self.player)
        self.discards = info.discards
        deck = info.deck
        hand = tuple(self.player.stack)
        # get current hand
        stack = self.player.stack
        if best[1] <= self.fold and max(stack) >= self.hand:
            return best
        return "Hit"

class pickoff:
    '''
    takes low cards.
    '''
    def __init__(self, high = 10, burn = 5):
        self.cards = tuple(range(1, high + 1))
        self.burn = burn

    def play(self, info):
        best = info.bestFold(self.player)
        if best[1] <= 2:
             return best
        elif best[1] <= 4 and (max(self.player.stack) == 10 or (max(self.player.stack) >= 8 and len(self.player.stack) >= 3)):
             return best
        elif ((10-max(info.inStacks())) > best[1] and (info.inPoints()))/info.noPlayers > 6:
             return best
        else:
             return "booger"

class simpleExp:
    '''
    takes low cards.
    '''
    def __init__(self, high = 10, burn = 5):
        self.cards = tuple(range(1, high + 1))
        self.burn = burn

    def play(self, info):
        self.discards = info.discards
        deck = info.deck
        hand = tuple(self.player.stack)
        best = info.bestFold(self.player)
        if best[1] <= 2:
             return best
        elif best[1] <= sum([self._p_deal(c, deck) * c for c in hand]) and (11-sum(info.inPoints()))/info.noPlayers > best[1] :
             return best
        else:
             return "booger"

    def _p_deal(self, c, deck):
        return deck.count(c) / len(deck)

class simpleExp2:
    '''
    takes low cards.
    '''
    def __init__(self, high = 10, burn = 5):
        self.cards = tuple(range(1, high + 1))
        self.burn = burn

    def play(self, info):
        self.discards = info.discards
        deck = info.deck
        hand = tuple(self.player.stack)
        best = info.bestFold(self.player)
        if best[1] <= 2:
             return best
        elif best[1] <= sum([self._p_deal(c, deck) * c for c in hand]):
             return best
        elif sum(info.inPoints())/info.noPlayers > 6 and best[1] < 6:
             return best
        else:
             return "booger"

    def _p_deal(self, c, deck):
        return deck.count(c) / len(deck)

class noPeek:
    '''
    strategy not requiring deck
    '''
    def play(self, info):
        self.discards = info.discards
        deck = info.deck
        hand = tuple(self.player.stack)
        best = info.bestFold(self.player)
        if (sum(hand) > 15 or max(hand)>7) and best[1] < 5:
             return best
        elif (sum(hand) > 16 or max(hand)>9) and best[1] < 6:
             return best
        elif sum([1 if sum(p.points)>4 and len(p.stack)>0 and max(p.stack) > (11 - sum(p.points)) else 0 for p in info.players]) > 2:
             return best
        else:
             return "booger"

class trad:
    '''
    takes low cards.
    '''

    def play(self, info):
        deck = info.deck
        hand = tuple(self.player.stack)
        best = info.bestFold(self.player)
        points = tuple(self.player.points)
        opp = [pl for pl in info.players if pl != self.player]
        if sum(points) + max(hand) < 11:
            return "booger"
        elif sum([self._p_deal(c, deck) * c for c in hand]) > best[1] + 1 and sum([1 if sum([self._p_deal(c, deck) * c for c in hand]) > sum([self._p_deal(c, deck) * c for c in p.stack])  else 0 for p in opp] ) >= (info.noPlayers - 1):
            return best
        elif sum([self._p_deal(c, deck) * (c + sum(points) >=11) for c in hand]) > 1 - numpy.product([ 1 - sum([self._p_deal(c, deck) * (c + sum(p.points) >=11) for c in p.stack])  for p in opp] ):
            return best
        else:
            return "booger"

    def _p_deal(self, c, deck):
        return deck.count(c) / len(deck)

