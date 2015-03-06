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

#############################################################

(SmartRatio using > instead of >=)
(Heuristic using 3 for ratio and 6 for near_death)

strategies = [
              Expectation3(),
              SmartRatio(),
              Heuristic(),
              Heuristic(ratio=2.5, always=3)
              ]


Games Played:   14600

                Lost    Percent
Expectation3    3469    0.24
SmartRatio      3625    0.25
Heuristic Def   3672    0.25
Heuristic Alt   3834    0.26

                P(best) P(worst)
Expectation3    0.95    0.00
SmartRatio      0.04    0.01
Heuristic Def   0.01    0.04
Heuristic Alt   0.00    0.96
Stopping early due to high probabilities of best and worst.  (Threshold set to 0.95)

#############################################################

strategies = [
              #Expectation3(),
              SmartRatio(),
              Heuristic(near_death=6, ratio=3),
              Heuristic(near_death=7, ratio=2.5, always=3),
              SmartRatio(start = 1.1),
              SmartRatio(start = 1.1, inc = 0.9)
              ]

Games Played:   50000

                Lost    Percent
SmartRatio      9810    0.20
Heuristic Def   9914    0.20
Heuristic Alt   10651   0.21
SmartRatio 1.1  9709    0.19
SmartRatio Slow 9916    0.20

                P(best) P(worst)
SmartRatio      0.22    0.00
Heuristic Def   0.04    0.00
Heuristic Alt   0.00    1.00
SmartRatio 1.1  0.70    0.00
SmartRatio Slow 0.04    0.00

#############################################################

strategies = [
              #Expectation3(),
              SmartRatio(),
              Heuristic(near_death=6, ratio=3),
              Heuristic(near_death=5, ratio=3),
              SmartRatio(start = 1.1),
              SmartRatio(start = 1.2, inc = 1.2)
              ]

Games Played:   50000

                Lost    Percent
SmartRatio      10047   0.20
Heuristic Def   10173   0.20
Heuristic Alt   10225   0.20
SmartRatio 1.1  9727    0.19
SmartRatio Slow 9828    0.20

                P(best) P(worst)
SmartRatio      0.01    0.06
Heuristic Def   0.00    0.35
Heuristic Alt   0.00    0.60
SmartRatio 1.1  0.76    0.00
SmartRatio Slow 0.24    0.00

#############################################################

# Initalize strategies in list
strategies = [
              #Expectation3(),
              SmartRatio(start = 1.1, always = 3),
              Heuristic(near_death = 6, ratio = 3),
              Heuristic(near_death = 5, ratio = 3),
              SmartRatio(start = 1.1),
              SmartRatio(start = 1.1, inc = 1.1)
              ]

Games Played:   50000

                Lost    Percent
SmartRatio      10079   0.20
Heuristic Def   10272   0.21
Heuristic Alt   9974    0.20
SmartRatio 1.1  9773    0.20
SmartRatio Slow 9902    0.20

                P(best) P(worst)
SmartRatio      0.01    0.09
Heuristic Def   0.00    0.89
Heuristic Alt   0.06    0.01
SmartRatio 1.1  0.77    0.00
SmartRatio Slow 0.17    0.00

#############################################################

strategies = [
              Expectation3(),
              SmartRatio(start = 1.1, always = 3),
              Heuristic(near_death = 6, ratio = 3),
              Heuristic(near_death = 5, ratio = 3),
              SmartRatio(start = 1.1),
              SmartRatio(start = 1.1, inc = 1.1)
              ]

Games Played:   50000

                Lost    Percent
Expectation3    8283    0.17
SmartRatio      8417    0.17
Heuristic Def   8274    0.17
Heuristic Alt   8479    0.17
SmartRatio 1.1  8292    0.17
SmartRatio Slow 8255    0.17

                P(best) P(worst)
Expectation3    0.22    0.03
SmartRatio      0.02    0.28
Heuristic Def   0.24    0.02
Heuristic Alt   0.00    0.62
SmartRatio 1.1  0.19    0.03
SmartRatio Slow 0.33    0.02

#############################################################

strategies = [
              #Expectation3(),
              SmartRatio(start = 1.1, always = 3),
              Heuristic(near_death = 6, ratio = 3),
              #Heuristic(near_death = 5, ratio = 3),
              SmartRatio(start = 1.1),
              SmartRatio(start = 1.1, inc = 1.1)
              ]

Games Played:   50000

                Lost    Percent
SmartRatio      12545   0.25
Heuristic Def   12824   0.26
SmartRatio 1.1  12230   0.24
SmartRatio Slow 12401   0.25

                P(best) P(worst)
SmartRatio      0.02    0.04
Heuristic Def   0.00    0.95
SmartRatio 1.1  0.84    0.00
SmartRatio Slow 0.14    0.00


@author: chris
"""

