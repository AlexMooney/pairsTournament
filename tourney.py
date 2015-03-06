'''
Tourney.py
Runs a tournament of continuous pairs.
Dealer class and other game mechanics imported from pairsClasses.
Strategies to play in the tournament need to be imported, initialized,
and passed to tournament function.
'''
from __future__ import division
numpy = False
try:
    import numpy as np
    numpy = True
except ImportError:
    print("The module numpy was not found.  Probabilities will not be reported in results.")
import pairsClasses as p
from random import shuffle

# Specify strategies to import here
from strategies.chrisStrategies import Expectation3
from strategies.chrisStrategies import SmartRatio
from strategies.chrisStrategies import Heuristic

# Initalize strategies in list
strategies = [
              #Expectation3(),
              SmartRatio(start = 1.1, always = 3),
              Heuristic(near_death = 6, ratio = 3),
              #Heuristic(near_death = 5, ratio = 3),
              SmartRatio(start = 1.1),
              SmartRatio(start = 1.1, inc = 1.1)
              ]

# name strategies for reporting
strat_names = [
               #"Expectation3",
               "SmartRatio",
               "Heuristic Def",
               #"Heuristic Alt",
               "SmartRatio 1.1",
               "SmartRatio Slow"
            ]

# Remaining code does not need to change between tourneys



def tourney(strategies, names, games = 50000, check = 100, prob = 0.95, prior = 500):
    losers = []
    n_strats = len(strategies)    
    for i in range(len(strategies)):
        strategies[i].tourney_index = i
        strategies[i].tourney_name = strat_names[i]
    early = False
    for i in range(games):
        if not i % check:
            if summary(i, prob, prior, n_strats, losers, names):
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
        summary(games, 1, prior, n_strats, losers, names)
    return losers

def summary(games, prob, prior, n_strats, losers, names):
    print("--------------------------------")
    print("Games Played:\t" + str(games))
    print("\n\t\tLost\tPercent")
    data = []
    for i in range(n_strats):
        data.append(losers.count(i))
        if games == 0:
            games = 1
        print(names[i] + "\t" + str(data[i]) + "\t" + '%.2f' % (data[i] / games))

    if numpy:
        prior = np.repeat(prior, n_strats)
        posterior = prior + np.array(data)
        N = 10000
        draws = np.random.dirichlet(posterior, N)
        best = np.bincount(np.argmin(draws, axis = 1), minlength = n_strats) / N
        worst = np.bincount(np.argmax(draws, axis = 1), minlength = n_strats) / N

        print("\n\t\tP(best)\tP(worst)")
        for i in range(n_strats):
            print(names[i] + "\t" + '%.2f' % best[i] + "\t" + '%.2f' % worst[i])
        if max(best) > prob and max(worst) > prob:
            print("Stopping early due to high probabilities of best and worst.  (Threshold set to " + str(prob) + ")")
            return True

def grand_tourney(strategies, games = 10000, check = 100, prob = 0.95, prior = 100):
    s = len(strategies)
    played = [0] * s
    shame = [0] * s
    wins = [0] * s
    for i in range(0, s):
        for j in range(i+1, s):
            sub_strat = [strategies[i], strategies[j]]
            sub_names = [strat_names[i], strat_names[j]]
            losses = tourney(sub_strat, sub_names, games, check, prob, prior)
            shame[i] += losses.count(0) * 2
            shame[j] += losses.count(1) * 2
            played[i] += len(losses)
            played[j] += len(losses)
            if(losses[0] < losses[1]):
                wins[i] += 1
            else:
                wins[j] += 1
    losses = tourney(strategies, strat_names, games, check, prob, prior)
    data = []
    for i in range(s):
        data.append(losses.count(i))
    for i in range(s):
        shame[i] += data[i] * s
        played[i] += sum(data)
        wins[i] += len([d for d in data if d > data[i]])
    
    print("--------------------------------")
    print("Grand Tourney Results")
    print("--------------------------------")
    print("\n\t\tGames\tShame\tIndex\tTourney Points")
    for i in range(0, s):
        print(strat_names[i] + "\t" + str(played[i]) + "\t" + str(shame[i]) + "\t" + '%.2f' % (shame[i] / played[i]) + "\t" + str(wins[i]))
        
grand_tourney(strategies)
