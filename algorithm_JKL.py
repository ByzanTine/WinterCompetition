def responseToChallenge(gameData, isPlayingSecond):
	return False;
def issueChanllenge(gameData, isPlayingSecond, opponentsCard=0):
	return False;
#return the index of card to play
def playCard(gameData, isPlayingSecond, opponentsCard=0):
	if isPlayingSecond :
		for i in gameData.selfHand:
			if i > opponentsCard:
				return i
		# if cannot find a bigger one return the least
		return gameData.selfHand[0]
	