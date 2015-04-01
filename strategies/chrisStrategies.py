from __future__ import division
from math import ceil
from copy import copy

class FoldLowWithHigh:
    def __init__(self, fold, hand):
        ''' Strategy that folds when 'fold' is available if 'hand' or higher is in hand'''
        self.fold = fold
        self.hand = hand

    def play(self, info):
        # get best fold as tuple (playerIndex, card)
        best = info.bestFold(self.player)
        # get current hand
        stack = self.player.stack
        if best[1] <= self.fold and max(stack) >= self.hand:
            return best
        return "Hit"

class Expectation3:
    '''
    Determines optimal play by computing the expected points per turn
    until next points are earned.
    '''
    def __init__(self, tm = 5, high = 10, burn = 5):
        self.TURN_MAX = tm
        self.cards = tuple(range(1, high + 1))
        self.burn = burn

    def play(self, info):
        self.discards = info.discards
        deck = info.deck
        hand = tuple(self.player.stack)
        fold = info.bestFold(self.player)
        if(fold[1] <= 2):
            return fold
        play_to = max(11, 60 / info.noPlayers + 1)
        high_card = max(hand) if hand else 0
        scores = []
        for i in range(info.noPlayers):
            scores.append(info.players[i].getScore())
        if play_to - max(scores) < 6 and high_card + self.player.getScore() >= play_to:
            return fold
        ev_hit = self._turn(hand, deck, 1)

        if fold[1] / 2 < ev_hit:
             return fold
        return ev_hit

    def _p_deal(self, c, deck):
        return deck.count(c) / len(deck)

    def _p_fold(self, c, deck):
        return self._p_deal(c, deck)

    def _hit(self, hand, deck, trn):
        return sum([self._p_deal(c, deck) * c for c in hand]) / (trn+1)

    def _fold(self, ev_hit, deck, trn):
        prob = sum([self._p_fold(c, deck) for c in self.cards if c < ev_hit])
        ev = 0
        if prob > 0:
            ev = sum([self._p_fold(c, deck) * c for c in self.cards if c < ev_hit]) / prob / (trn+1)
        return (prob, ev)

    def _reshuffle(self, deck):
        return self.discards + deck

    def _turn(self, hand, deck, trn):
        ev_hit = self._hit(hand, deck, trn)
        if trn < self.TURN_MAX:
            for c in self.cards:
                if c not in hand and c in deck:
                    d = copy(deck)
                    d.remove(c)
                    if len(d) == self.burn:
                        d = self._reshuffle(d)
                    ev_hit += self._turn(hand + tuple([c]), d, trn+1) * self._p_deal(c, deck)

        if trn == 1:
            return ev_hit
        f = self._fold(ev_hit, deck, trn)
        p_fold = f[0]
        ev_fold = f[1]
        return p_fold * ev_fold + (1-p_fold) * ev_hit

class Heuristic:
    '''
    Determines optimal play according to 4 simple parameters.
    '''
    def __init__(self, ratio = 2.5, near_death = 3, always = 2, diff = 3):
        self.ratio = ratio
        self.nd = near_death
        self.always = always
        self.diff = diff

    def play(self, info):
        hand = self.player.stack
        fold = info.bestFold(self.player)
        if(fold[1] <= self.always):
            return fold
        if(sum(hand) / fold[1] > self.ratio and max(hand) - fold[1] >= self.diff):
            return fold
        play_to = max(11, 60 / info.noPlayers + 1)
        scores = []
        for i in range(info.noPlayers):
            scores.append(info.players[i].getScore())
        if play_to - max(scores) <= self.nd and max(hand) + self.player.getScore() >= play_to:
            return fold
        return "hit"

class SmartRatio:
    '''
    Determines optimal play with simple ratio intended to approximate
    Expectation with a full deck.
    '''
    def __init__(self, start = 1, inc = 1, near_death = 6, always = 2):
        self.start = start
        self.inc = inc
        self.nd = near_death
        self.always = always

    def play(self, info):
        hand = self.player.stack
        fold = info.bestFold(self.player)
        # cards always fold for
        if(fold[1] <= self.always):
            return fold
        play_to = max(11, 60 / info.noPlayers + 1)
        # when to start 'end-game' folding
        scores = []
        for i in range(info.noPlayers):
            scores.append(info.players[i].getScore())
        if play_to - max(scores) <= self.nd and max(hand) + self.player.getScore() >= play_to:
            return fold
        # general fold rule
        if sum(hand) / fold[1] >= (self.start + self.inc*len(hand)):
            return fold
        return "hit"

class Interactive:
    '''Allows interactive play with bots.'''

    def play(self, info):
        self._print_state(info)
        choice = input('Your play?')
        return choice

    def _print_state(self, info):
        for p in info.players:
            print('Player %d:\tstack: %s' % (p._index, str(p.stack)))
            print('\t\tpoints: %d' % (p.getScore()))
        print('You:\tstack:%s' % (str(self.player.stack)))
        print('\tpoints: %d' % (self.player.getScore()))



