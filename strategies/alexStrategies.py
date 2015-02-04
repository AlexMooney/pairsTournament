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
