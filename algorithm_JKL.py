import math
def responseToChallenge(gameData, isPlayingSecond):
    if gameData.getTrickDiff() >= 3:
        return True
    if gameData.getTrickDiff() <= -3:
        return False
    if gameData.getTrickDiff() is 2:
        return False
    if gameData.getTrickDiff() is -2:
        return True
    if isPlayingSecond:
        if gameData.challenge() > gameData.indexsecondBound:
            return True
    elif gameData.challenge() > gameData.indexfirstBound:
        return True
	return False;
def issueChallenge(gameData, isPlayingSecond, opponentsCard=0):
    if gameData.getTrickDiff() >= 3:
        return True
    if gameData.getTrickDiff() <= -3:
        return False
    if isPlayingSecond:
        for i in selfHand:
            if i < opponentsCard:
                return False
        return True
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

