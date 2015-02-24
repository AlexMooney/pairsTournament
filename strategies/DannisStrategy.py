from collections import Counter

class LowCardFold:
	def __init__(self):
		'''Strategy that folds when 'fold' is available if 'hand' or higher is in hand'''

	def play(self, info):
		# get the number of players
		NumPlayers = info.noPlayers
		highestScore = max(int(60 / NumPlayers) + 1, 11)
		# get best fold as tuple (playerIndex, card)
		best = info.bestFold(self.player)
		# get current hand
		stack = self.player.stack
		if best[1]<4 and sum(stack) != (highestScore-best[1]):
			return best
		return "Hit"

class DannisStrategy:
	def __init__(self, PercentHit):
		from collections import Counter
		self.Counter = Counter
		self.PercentHit = PercentHit
	def play(self, info):
		# current deck list
		deck = self.Counter(info.deck)
		#best fold as tuple (playerIndex, card)
		best = info.bestFold(self.player)
		# list of current hand
		stack = self.player.stack
		# if best fold is greater than expected value of points (based on cards in deck), hit
		if (best[1] > self.PercentHit * sum([card*deck[card] for card in deck])/len(info.deck) + sum([card*deck[card]/len(info.deck) for card in stack])):
			return "hit"
		# if best fold is less than expected value of points (based on cards in deck), fold
		return best

class NoCardKnowledge:
#This class uses the suggested strategy available on the pairs website (no knowledge of cards in deck or discards)
	def play(self, info):
		# get the number of players
		NumPlayers = info.noPlayers
		highestScore = max(int(60 / NumPlayers) + 1, 11)
		# get best fold as tuple (playerIndex, card)
		best = info.bestFold(self.player)
		# get current hand
		stack = self.player.stack
		if best[1]==1 and (sum(stack) < (highestScore-1)):
			return best
		if (sum(stack)/len(stack)) >= (highestScore - sum(stack)):
			return best
		if sum(stack) > 18*best[1]:
			return best
		if best[1] + sum(stack) >= highestScore:
			return "Hit"
		return "Hit"

