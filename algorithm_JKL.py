import math
def responseToChallenge(gameData, isPlayingSecond):
    if gameData.selfPoints is 9:
        if isPlayingSecond and gameData.challenge() > gameData.indexsecondBound:
            return True 
        elif gameData.challenge() > gameData.indexfirstBound:
            return True
    if gameData.opponentPoints is 9:
        return True
    if gameData.getTrickDiff() >= 3:
        return True
    if gameData.getTrickDiff() <= -3:
        return False
    if gameData.getTrickDiff() is 2:
        return True
    if gameData.getTrickDiff() is -2:
        return False
    if len(gameData.selfHand)==0:
        if gameData.getTrickDiff()==0 :
            return False
        return gameData.getTrickDiff()>0
    if isPlayingSecond:
        if gameData.challenge() > gameData.indexsecondBound:
            return True
    elif gameData.challenge() > gameData.indexfirstBound:
        return True
    return False;
def issueChallenge(gameData, isPlayingSecond, opponentsCard=0):
    print "issueChallenge: "+str(gameData.getTrickDiff())
    if len(gameData.selfHand) is 5 and sum(gameData.selfHand) > 50:
        return True;
    if len(gameData.selfHand) is 4 and sum(gameData.selfHand) > 40:
        return True;
    if len(gameData.selfHand) is 3 and sum(gameData.selfHand) > 30:
        return True;
    if gameData.opponentPoints is 9:
        if isPlayingSecond and gameData.challenge() > gameData.indexsecondBound:
            return True 
        elif gameData.challenge() > gameData.indexfirstBound:
            return True
    if gameData.getTrickDiff() >= 3:
        return False
    if gameData.getTrickDiff() <= -3:
        return False
    allBigger = True
    if isPlayingSecond:
        for i in gameData.selfHand:
            if i < opponentsCard:
                allBigger = False
        if allBigger and gameData.getTrickDiff() > 0:
            return True
        if gameData.challenge() > gameData.indexsecondBound:
            return True
    else: 
        if gameData.getTrickDiff() < -1:
            return False
        if gameData.challenge() > gameData.indexfirstBound:
            return True
    return False;
#return the index of card to play
def playCard(gameData, isPlayingSecond, opponentsCard=0):
	print "play card"
	if isPlayingSecond:
		print "opponentsCard: " + str(opponentsCard)
	print "selfHand: "
	print gameData.selfHand
	if isPlayingSecond :
		for i in gameData.selfHand:
			if i > opponentsCard:
				return i
		# if cannot find a bigger one return the least
		return gameData.selfHand[0]
	else :
		return gameData.selfHand[int(math.floor((len(gameData.selfHand) - 1)*(1-gameData.challenge())))]

