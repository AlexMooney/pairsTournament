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

class CruelFold:
    def __init__(self, scared=0.23, malice=0.5):
        from collections import Counter
        self.Counter = Counter
        self.scared = scared
        self.malice = malice

    def play(self, info):
        numPlayers = info.noPlayers
        hitPoints = [(60/numPlayers) - p.getScore() for p in info.players]
        folds = sorted(info.bestFolds(), key=lambda t: t[1])
        if folds[0][0] == self.player.index():
            folds = folds[:1] + [f for f in folds[1:] if f[0] != self.player.index]
        else:
            folds = [f for f in folds if f[0] != self.player.index()]
        pkill = 0
        c = self.Counter(info.deck)
        for i, hp in enumerate(hitPoints):
            if i == self.player.index():
                continue
            if hp >= folds[0][1] and hp < folds[1][1]:
                pkill += sum([s*c[s]/len(info.deck) for s in info.players[i].stack])

        if info.bestFold(self.player)[1] - self.malice*pkill > self.scared*sum([s*c[s] for s in c])/len(info.deck) + sum([s*c[s]/len(info.deck) for s in self.player.stack]):
            return 'Hit me'
        else:
            return 'fold'

