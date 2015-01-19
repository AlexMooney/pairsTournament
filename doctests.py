"""This is a series of doctests for objects in pairClasses

#############################
# This tests the Player class
>>> from pairsClasses import Player

>>> p = Player()

>>> p.hit(5)

>>> p.hit(10)

>>> p.stack
[5, 10]

>>> p.whichPair()
False

>>> p.hit(10)

>>> p.whichPair()
10

>>> p.catch(10)

>>> p.points
[10]

>>> p.stack
[]

>>> p.getScore()
10

>>> p.hit(9)

>>> p.hit(3)

>>> p.getSmallest()
3

>>> p.steal(3)

>>> p.stack
[9]

>>> p.hit(9)

>>> p.catch(9) # normally hit and check whichPair before calling catch

>>> p.getScore()
19

>>> p.points
[10, 9]

>>> from pairsClasses import Dealer

>>> d = Dealer()

>>> d.vPrint('Hi there') # verbose false by default

>>> d.verbose = True

>>> d.vPrint('Hi there') # print arguments when verbose is true
Hi there

>>> d.play()


"""

import doctest
result = doctest.testmod()
print('Ran '+str(result[1])+' tests; '+
      str(result[1]-result[0])+' passed.')
