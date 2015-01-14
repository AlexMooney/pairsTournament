# Pairs Tournament

This program runs a tournament of AIs which play Continuous Pairs.
  Each player is a Python class which is given the state of the game and decides to hit or fold.

## Pairs
Pairs is a pub game for 2 to 8 players designed by James Ernest and Paul Peterson.
  For rules, variants, alternate decks, and more, please visit the
  [official website](www.playpairs.com).
  Pairs is :copyright: and :tm: 2014 James Ernest and Hip Pocket Games.

## API
The tournament creates a `Dealer` and sets up things like dealing cards and burning cards and then tells the dealer to run the game.

Cards are simply stored as integers.

### `Dealer`
The `Dealer` class asks the `Strategy` classes if they want to *hit* or *fold* and manipulates the cards held by the `Player` classes.
Dealer methods are invoked by the main loop to set up a game and play it out.
##### `Dealer` methods
- `burn(N=5)` burns `N` cards off the deck and does not reveal them.
- `deal()` gives all `Player` classes their first cards and determines playing order then attaches the `Strategy` classes to the `Player` classes.
- `discards()` returns list of all seen cards in the discard pile.
- `play()` runs an entire game and returns the scores of all participants at the end.
- `players()` returns the list of players in play order.
- `timeLimit()` asks for the time limit for a `Strategy` to decide on its move, in ms.
- `turn(Strategy)` invokes the `Strategy.play()` method and resolves the changes to the `Player` classes involved.

### `Player`
The `Player` class holds the lists of *stack* and *points* cards.
  ##### `Player` methods
  - `catch(card)` adds the passed card to their *points* and clears their *stack*
  - `hit(card)` adds the card to their *stack*
  - `points()` returns the list of the cards in their *points*
  - `score()` returns the sum of their *points*
  - `smallest()` returns the smallest card in their *stack*
  - `stack()` returns the list of the cards in their *stack*
  - `steal(card)` removes the card from their *stack*

### `Strategy`
You write a `Strategy` class to compete with those written by other players.  The `Strategy` is initialized with its own `Player` as the sole argument.  The `Strategy` should probably ask the `Dealer` some questions about the state of the game and the decide to hit or which card it would like to fold for.
  ##### `Strategy` methods
  - `play(dealer)` should return `(playerIndex, card)` to fold for a specific card, `"fold"` to take the "best" card available, and any other value to hit.
