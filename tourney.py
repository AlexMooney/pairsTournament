'''
Tourney.py
Runs a tournament of continuous pairs.
Dealer class and other game mechanics imported from pairsClasses.
Strategies to play in the tournament need to be imported, initialized,
and passed to tournament function.
'''
numpy = False
try:
    import numpy as np
    numpy = True
except ImportError:
    print("The module numpy was not found.  Probabilities will not be reported in results.")
import pairsClasses as p
from random import shuffle

# Specify strategies to import here
from strategies.chrisStrategies import FoldLowWithHigh
from strategies.chrisStrategies import Expectation

# Initalize strategies in list
strategies = [FoldLowWithHigh(3,1),
              FoldLowWithHigh(4,8),
              Expectation()]
              
# name strategies for reporting
strat_names = ["Folder_3", "Folder_4_8", "Expectation"]

# Remaining code does not need to change between tourneys
n_strats = len(strategies)

for i in range(n_strats):
    strategies[i].tourney_index = i
    strategies[i].tourney_name = strat_names[i]

losers = []

def tourney(strategies, games = 500, check = 50, prob = 0.95, prior = 500):
    early = False
    for i in range(games):
        if not i % check:
            if summary(i, prob, prior):
                early = True                
                break
        d = p.Dealer(n_strats)
        shuffle(strategies)
        for j in range(n_strats):
            d.gameState.players[j].strategy = strategies[j]
        # play a game and get the index of the losing strategy
        lost = d.gameState.players[d.play()].strategy.tourney_index
        losers.append(lost)
    if not early:
        summary(games, 1, prior)

def summary(games, prob, prior):
    print("--------------------------------")
    print("Games Played:\t" + str(games))
    print("\n\t\tLost\tPercent")
    data = []
    for i in range(n_strats):
        data.append(losers.count(i))
        if games == 0:
            games = 1
        print(strat_names[i] + "\t" + str(data[i]) + "\t" + '%.2f' % (data[i] / games))
    
    if numpy:
        prior = np.repeat(prior, n_strats)
        posterior = prior + np.array(data)
        N = 10000
        draws = np.random.dirichlet(posterior, N)
        best = np.bincount(np.argmin(draws, axis = 1), minlength = n_strats) / N
        worst = np.bincount(np.argmax(draws, axis = 1), minlength = n_strats) / N
    
        print("\n\t\tP(best)\tP(worst)")
        for i in range(n_strats):
            print(strat_names[i] + "\t" + '%.2f' % best[i] + "\t" + '%.2f' % worst[i])
        if max(best) > prob and max(worst) > prob:
            print("Stopping early due to high probabilities of best and worst.  (Threshold set to " + str(prob) + ")")
            return True
    
tourney(strategies)
