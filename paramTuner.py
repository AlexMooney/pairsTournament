import sys
sys.path.append('./strategies')

from pairsClasses import Dealer
from pairsClasses import SimpletonStrategy
from alexStrategies import FixFoldStrategy
from alexStrategies import RatioFoldStrategy

PLAYERS = 2

for N in range(22,33,2):
    print("N = "+str(N))
    losses = [0]*PLAYERS
    for i in range(10000):
        d = Dealer(PLAYERS)
        d.verbose = False
        d.gameState.players[0].strategy = FixFoldStrategy(3)
        d.gameState.players[1].strategy = RatioFoldStrategy(N)
        losses[d.play()] += 1

    print(losses)
    print()
