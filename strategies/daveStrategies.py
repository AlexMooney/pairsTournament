from __future__ import division
from copy import copy
from math import log

class expValue:
    """This strategy folds based on card counting expectation values."""
    def __init__(self):
        from collections import Counter
        self.Counter = Counter

    def play(self, info):
        cards = self.Counter(info.deck)
        if info.bestFold(self.player)[1] > sum([card*cards[card]/len(info.deck) for card in self.player.stack]):
            return 'Hit me'
        else:
            return 'fold'

class otherShoe:
    """This strategy folds based on card counting expectation values."""
    def __init__(self):
        from collections import Counter
        self.Counter = Counter

    def play(self, info):
        cards = self.Counter(info.deck)
        if info.bestFold(self.player)[1] > (1 + (len(info.inStacks())-\
                                                 len(self.player.stack))*-0.1) \
           * sum([card*cards[card]/len(info.deck) for card in self.player.stack]):
            return 'Hit me'
        else:
            return 'fold'

class otherShoe4:
    """This strategy folds based on card counting expectation values. \
            and decreases the likihood of folding proportional to the \
            probability that another player will pair"""
    def __init__(self):
        from collections import Counter
        self.Counter = Counter

    def play(self, info):
        cards = self.Counter(info.deck)
        try:
            stacks = info.inStacks().remove(self.player.stack) 
        except:
            stacks = info.inStacks()
        if info.bestFold(self.player)[1] > \
           (1 - sum([cards[s]/len(info.deck) for s in stacks]) ** (info.noPlayers-1)) \
           * sum([card*cards[card]/len(info.deck) for card in self.player.stack]): 
            return 'Hit me'
        else:
            return 'fold'

class otherShoe2:
    """This strategy folds based on card counting expectation values. \
            and decreases the likihood of folding proportional to the \
            probability that another player will pair"""
    def __init__(self):
        from collections import Counter
        self.Counter = Counter

    def play(self, info):
        cards = self.Counter(info.deck)
        try:
            stacks = info.inStacks().remove(self.player.stack) 
        except:
            stacks = info.inStacks()
        if info.bestFold(self.player)[1] > \
           (1 - sum([cards[s]/len(info.deck) for s in stacks]) ** (info.noPlayers-1)) \
           * sum([card*cards[card]/len(info.deck) for card in self.player.stack]) \
           + sum([card*cards[card]/len(info.deck) for card in self.player.stack]):
            return 'Hit me'
        else:
            return 'fold'

class otherShoe3:
    """This strategy folds based on card counting expectation values. \
            and decreases the likihood of folding proportional to the \
            probability that another player will pair\
            with a scaler reduction"""
    def __init__(self):
        from collections import Counter
        self.Counter = Counter

    def play(self, info):
        cards = self.Counter(info.deck)
        try:
            stacks = info.inStacks().remove(self.player.stack) 
        except:
            stacks = info.inStacks()
        if info.bestFold(self.player)[1] > \
           (1 - sum([cards[s]/len(info.deck) for s in stacks]) ** (info.noPlayers-1)) \
           * sum([card*cards[card]/len(info.deck) for card in self.player.stack])\
           * 0.8 \
           + sum([card*cards[card]/len(info.deck) for card in self.player.stack]):
            return 'Hit me'
        else:
            return 'fold'

class HMICL:
    """This strategy folds based on card counting expectation values."""
    def __init__(self, ra = -0.1):
        from collections import Counter
        self.Counter = Counter
        self.ra = ra

    def play(self, info):
        cards = self.Counter(info.deck)
        if info.bestFold(self.player)[1] > (1 + self.ra) * \
           sum([card*cards[card]/len(info.deck) for card in self.player.stack]):
            return 'Hit me'
        else:
            return 'fold'

class expValue3_ra:
    """This strategy folds based on card counting expectation values."""
    def __init__(self, ra = 0.1):
        from collections import Counter
        self.Counter = Counter
        self.ra = ra

    def play(self, info):
        cards = self.Counter(info.deck)
        if info.bestFold(self.player)[1] > (1 + self.ra) * \
           sum([card*cards[card]/len(info.deck) for card in self.player.stack]):
            return 'Hit me'
        else:
            return 'fold'


# this class is unfinished
class Terminator:
    """ This strategy modifies expValue to steal low value cards before 
        players with high points can get them """
    def __init__(self,safe_zone = 5):
        from collections import Counter
        self.Counter = Counter
        self.safe_zone = safe_zone

    def play(self, info):
        cards = self.Counter(info.deck)
        #hard to make stealing low cards work in standard pairs
        if info.bestFold + player.getScore() < safe_zone:
            return 'fold'           
        if info.bestFold(self.player)[1] > (1 + self.ra) * \
           sum([card*cards[card]/len(info.deck) for card in self.player.stack]):
            return 'Hit me'
        else:
            return 'fold'
