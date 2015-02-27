# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 16:15:30 2015

strategies = [Heuristic(near_death=4),
              Heuristic(ratio=2.75, near_death=4),
              Expectation3(),
              Heuristic(),
              Heuristic(ratio=2.25, near_death=4, always=3)]

--------------------------------
Games Played:   50000

                Lost    Percent
Heuristic ND    10175   0.20
Heuristic Agg   9965    0.20
Expectation3    9607    0.19
Heuristic Def   10155   0.20
Heuristic Cons  10098   0.20

                P(best) P(worst)
Heuristic ND    0.00    0.45
Heuristic Agg   0.01    0.02
Expectation3    0.99    0.00
Heuristic Def   0.00    0.36
Heuristic Cons  0.00    0.17

#############################################################

strategies = [Heuristic(near_death=4, always=3),
              Heuristic(ratio=2.75, near_death=4),
              Expectation3(),
              Heuristic(near_death=5, ratio=3),
              Heuristic(ratio=2.25, near_death=4, always=3)]

--------------------------------
Games Played:   50000

                Lost    Percent
Heuristic X     10328   0.21
Heuristic Agg   9962    0.20
Expectation3    9787    0.20
Heuristic Wait  9797    0.20
Heuristic Cons  10126   0.20

                P(best) P(worst)
Heuristic X     0.00    0.91
Heuristic Agg   0.04    0.00
Expectation3    0.51    0.00
Heuristic Wait  0.45    0.00
Heuristic Cons  0.00    0.08

#############################################################

strategies = [Heuristic(near_death=6, ratio=3),
              Heuristic(ratio=2.75, near_death=4),
              Expectation3(),
              Heuristic(near_death=5, ratio=3),
              Heuristic(ratio=3.25, near_death=6, always=3)]

Games Played:   50000

                Lost    Percent
Heur Wait More  9995    0.20
Heuristic Agg   10177   0.20
Expectation3    9914    0.20
Heuristic Wait  10034   0.20
Heuristic W X   9880    0.20

                P(best) P(worst)
Heur Wait More  0.11    0.07
Heuristic Agg   0.00    0.76
Expectation3    0.33    0.01
Heuristic Wait  0.06    0.14
Heuristic W X   0.50    0.01

#############################################################

(near_death threshold in Expectation3 set to 6)

strategies = [Heuristic(near_death=6, ratio=3),
              Heuristic(ratio=2.75, near_death=4),
              Expectation3(),
              Heuristic(near_death=5, ratio=3),
              Heuristic(ratio=3.25, near_death=6, always=3)]

Games Played:   39300

                Lost    Percent
Heur Wait More  7765    0.20
Heuristic Agg   8173    0.21
Expectation3    7551    0.19
Heuristic Wait  7863    0.20
Heuristic W X   7948    0.20

                P(best) P(worst)
Heur Wait More  0.04    0.00
Heuristic Agg   0.00    0.95
Expectation3    0.95    0.00
Heuristic Wait  0.01    0.01
Heuristic W X   0.00    0.04
Stopping early due to high probabilities of best and worst.  (Threshold set to 0.95)


@author: chris
"""

