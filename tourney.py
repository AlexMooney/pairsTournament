try:
    import numpy as np
    numpy = True
except ImportError:
    print("The module numpy was not found.  Probabilities will not be reported in results.")

import pairsClasses as p
from strategies.chrisStrategies import FoldLowWithHigh
from strategies.chrisStrategies import Expectation
from random import shuffle

strategies = [FoldLowWithHigh(3,1),
              FoldLowWithHigh(4,8),
              Expectation()]
strat_names = ["Folder_3", "Folder_4_8", "Expectation"]
n_strats = len(strategies)

for i in range(n_strats):
    strategies[i].tourney_index = i
    strategies[i].tourney_name = strat_names[i]

losers = []
for i in range(100):
    # defaults to 5 players that always hit
    d = p.Dealer(n_strats)
    shuffle(strategies)
    for i in range(n_strats):
        d.gameState.players[i].strategy = strategies[i]
    # play a game and get the index of the losing strategy
    lost = d.gameState.players[d.play()].strategy.tourney_index
    losers.append(lost)

data = []
for i in range(n_strats):
    data.append(losers.count(i))

print("Games Lost:")
for i in range(n_strats):
    print(strat_names[i] + ":\t" + str(data[i]))

if numpy:
    prior = np.repeat(10, n_strats)
    posterior = prior + np.array(data)
    N = 10000
    draws = np.random.dirichlet(posterior, N)
    best = np.bincount(np.argmin(draws, axis = 1), minlength = n_strats) / N
    worst = np.bincount(np.argmax(draws, axis = 1), minlength = n_strats) / N

    print("\n\n\t\tP(best)\tP(worst)")
    for i in range(n_strats):
        print(strat_names[i] + "\t" + '%.2f' % best[i] + "\t" + '%.2f' % worst[i])

