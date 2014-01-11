import math
def responseToChallenge(gameData, isPlayingSecond):
    if gameData.getTrickDiff is 2:
        return False
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
	else :
		return gameData.selfHand[int(math.floor(len(gameData.selfHand)*(1-gameData.challenge())))]

