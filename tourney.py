import pairsClasses as p
from strategies.chrisStrategies import FoldLowWithHigh
from strategies.chrisStrategies import Expectation

losers = []
for i in range(50):
    # defaults to 5 players that always hit
    d = p.Dealer(4)
    # replace some strategies
    d.gameState.players[0].strategy = FoldLowWithHigh(3, 8)
    d.gameState.players[1].strategy = FoldLowWithHigh(4, 8)
    d.gameState.players[2].strategy = Expectation()
    # play a game and append the loser index
    losers.append(d.play())

# changed this in anticipation index change from Alex
# may need +1 to work correctly
for i in range(len(d.gameState.players)):
    print("Player " + str(i) + ": " + str(losers.count(i)))
