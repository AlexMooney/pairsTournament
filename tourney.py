'''
Tourney.py
Runs a tournament of continuous pairs.
Dealer class and other game mechanics imported from pairsClasses.
Strategies to play in the tournament need to be imported, initialized,
and passed to tournament function.
'''
from __future__ import division
from itertools import chain, combinations
import pairsClasses as p
from random import shuffle
try:
    import numpy as np
    numpy = True
except ImportError:
    print("The module numpy was not found."
          "Probabilities will not be reported in results.")
    numpy = False



# Specify strategies to import here
from strategies.chrisStrategies import PureExp
from strategies.DannisStrategy import NoCardKnowledge
from strategies.michaelStrategies import OverThinker
from strategies.alexStrategies import CruelFoldNoCount
from strategies.brianStrategies import noPeek
from strategies.chrisStrategies import HitMe 
from strategies.chrisStrategies import Weights

# Initalize strategies in dict
strategies = {"Champ": PureExp(0.9, 8),
              "Weights": Weights(0.6),
              "Weights": Weights(1),
              "Weights": Weights(1.6),
              "Hit": HitMe()
              }

for key, value in strategies.items():
    value.tourney_key = key

class Tourney:

    def __init__(self, strategies, games = 50000, check = 100, prob = 0.95,
                 prior = 500):
        self.strats = strategies
        self.n = len(strategies)
        self.games = games
        self.check = check
        self.prob = prob
        self.prior = prior
        self.lost = dict.fromkeys(list(strategies.keys()), 0)
        self.early = False
        self.interactive = False
        self.nw = max(len(k) for k in strategies.keys()) + 5
        self.rw = 10

    def play(self):
        for g in range(self.games):
            d = p.Dealer(self.n, verbose = False, standard = True,
                         calamity = False)
            keys = list(self.strats.values())
            shuffle(keys)
            for j, s in enumerate(keys):
                d.gameState.players[j].strategy = s
            # play a game and get the key of the losing strategy
            loser = d.gameState.players[d.play()].strategy.tourney_key
            self.lost[loser] += 1
            if not (g+1) % self.check:
                self._summary(g+1)
            if self.interactive:
                print('%s lost.' % (loser))
                try:
                    input('Press Enter to continue.')
                except SyntaxError:
                    pass
            if self.early:
                break
        return self.lost

    def _summary(self, g):
        print("--------------------------------")
        print("Games Played:\t" + str(g) + "\n")
        row = "{:<%d}{:<%d}{:<%d}" % (self.nw, self.rw, self.rw)
        print(row.format("", "Lost", "Percent"))
        for key in self.strats:
            print(row.format(key, str(self.lost[key]), 
                             '%.2f' % (self.lost[key] / g)))
    
        if numpy:
            self._report_probs()
    
    def _report_probs(self):
            prior = np.repeat(self.prior, self.n)
            posterior = prior + np.array(list(self.lost.values()))
            keys = list(self.lost.keys())
            N = 10000
            draws = np.random.dirichlet(posterior, N)
            best = np.bincount(np.argmin(draws, axis = 1),
                               minlength = self.n) / N
            worst = np.bincount(np.argmax(draws, axis = 1),
                                minlength = self.n) / N
    
            print()
            row = "{:<%d}{:<%d}{:<%d}" % (self.nw, self.rw, self.rw)
            print(row.format("", "P(best)", "P(worst)"))
            for i, key in enumerate(self.strats):
                print(row.format(key,'%.2f' % best[keys.index(key)],
                                 '%.2f' % worst[keys.index(key)]))
            if max(best) > self.prob and max(worst) > self.prob:
                print("Stopping early due to high probabilities "
                      "of best and worst. (Threshold set to %s)" % 
                      str(self.prob))
                self.early = True
            

class GrandTourney:

    def __init__(self, strategies, games = 100, check = 500, prob = 0.95,
                 prior = 500):
        self.strats = strategies
        self.n = len(strategies)
        self.games = games
        self.check = check
        self.prob = prob
        self.prior = prior
        self.results = {}
        for strat in self.strats:
            self.strats[strat].gt_indices = {}
            for i in range(2, self.n+1):
                self.strats[strat].gt_indices[i] = []
            self.strats[strat].gt_games = 0
            self.strats[strat].gt_losses = 0
        self.nw = max(len(name) for name in self.strats) + 5
        self.rw = 10
            
    def _create_subsets(self):
        keys = list(self.strats.keys())
        return chain.from_iterable(combinations(keys, n)
                                   for n in range(2, len(keys)+1))
        
    def play(self, stop = False):
        subsets = self._create_subsets()
        for subset in subsets:
            self.results[subset] = Tourney({s:self.strats[s]
                for s in self.strats if s in subset}, 
                self.games, self.check, self.prob, self.prior).play()
            if stop:
                try:
                    input("Tourney ended. Press Enter to continue.")
                except:
                    pass
        self._grand_tourney_report()
    
    def _tourney_report(self, results):
        row = "{:<%d}"*4 % (self.nw, self.rw, self.rw, self.rw)
        print(row.format("","Losses","Percent","Index"))
        total = sum(results.values())
        for key in results:
            losses = results[key]
            percent = (results[key] / total)
            index = (results[key] / total * len(results))
            self.strats[key].gt_games += total
            self.strats[key].gt_losses += losses
            self.strats[key].gt_indices[len(results)].append(index)
            print(row.format(key, str(losses), '%.2f' % percent,
                             '%.2f' % index))
        print('\n')
        
    def _grand_tourney_report(self):
        print("-------------------------------------------------------------")
        print("|                    Grand Tourney Results                  |")
        print("-------------------------------------------------------------")
        print("Total Tournaments Played: " + str(len(self.results)))
        
        for i in range(2, self.n+1):
            print("--------------------------------------------")
            print(str(i) + "-Player Tournaments:")
            for result in self.results.values():
                if len(result) == i:
                    self._tourney_report(result)
                    
        print("-------------------------------------------------------------")
        print("|                       Final Indices                       |")
        print("-------------------------------------------------------------")
        
        overall = {}
        row = "{:<%d}"*4 % (self.nw, self.rw, self.rw, self.rw)
        for key in self.strats:
            strat = self.strats[key]
            strat.gt_means = []
            for i in range(2, self.n+1):
                strat.gt_means.append(sum(strat.gt_indices[i]) /
                                      len(strat.gt_indices[i]))
            overall[key] = sum(strat.gt_means) / len(strat.gt_means)
            strat.gt_means.append(overall[key])
            for i in range(len(strat.gt_means)):
                strat.gt_means[i] = '%.2f' % strat.gt_means[i]
                
        
        order = sorted(overall, key=overall.get)
        lengths = tuple([self.nw] + [self.rw] * self.n) 
        row = "{:<%d}"*(self.n+1) % lengths 
        headers = tuple(['Player'] + [str(i) for i in range(2, self.n+1)] +
                        ['Overall'])
        print(row.format(*headers))
        for s in order:
            print(row.format(*tuple([s] + self.strats[s].gt_means)))
            

if __name__ == "__main__":
    log = False
    if(log):
        import sys
    
        class Tee(object):
            def __init__(self, *files):
                self.files = files
            def write(self, obj):
                for f in self.files:
                    f.write(obj)
    
        f = open('tourney_log.txt', 'w')
        original = sys.stdout
        sys.stdout = Tee(sys.stdout, f)
    
    tourney = GrandTourney(strategies, games = 5000, check = 1000)
    tourney.play()
    
    if(log):
        f.close()
        sys.stdout = original
