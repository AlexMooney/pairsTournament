class FixFoldStrategy:
    """This strategy folds every time there is a small card available."""
    def __init__(self, N=3):
        self.N = N
    def play(self, info):
        if info.bestFold(self.player)[1] > self.N:
            return 'Hit me'
        else:
            return 'fold'

class RatioFoldStrategy:
    """This strategy folds more readily as their stack grows worse"""
    def __init__(self, N=4):
        self.N = N
    def play(self, info):
        if info.bestFold(self.player)[1]*self.N > sum([s*s for s in self.player.stack]):
            return 'Hit me'
        else:
            return 'fold'

class CardCounter:
    """This strategy folds based on card counting expectation values."""
    def __init__(self, scared=0.23):
        from collections import Counter
        self.Counter = Counter
        self.scared = scared
    def play(self, info):
        c = self.Counter(info.deck)
        if info.bestFold(self.player)[1] > self.scared*sum([s*c[s] for s in c])/len(info.deck) + sum([s*c[s]/len(info.deck) for s in self.player.stack]):
            return 'Hit me'
        else:
            return 'fold'
