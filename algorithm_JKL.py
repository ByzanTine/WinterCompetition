import math
def responseToChallenge(gameData, isPlayingSecond):
    if gameData.selfPoints ==9:
        if len(gameData.selfHand) == 0 and gameData.opponentPoints == 9:
            return True
        elif sum(gameData.selfHand)/len(gameData.selfHand) > 7:
            return True 
        else:
            return False
    if gameData.getTrickDiff() >= 3:
        return True
    if gameData.getTrickDiff() <= -3:
        return False
    if gameData.getTrickDiff() ==2:
        return True
    if gameData.getTrickDiff() ==-2:
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
    if len(gameData.selfHand) ==5 and sum(gameData.selfHand) - gameData.selfHand[0] > 40:
        return True;
    if len(gameData.selfHand) ==4 and sum(gameData.selfHand) - gameData.selfHand[0] > 30:
        return True;
    if len(gameData.selfHand) ==3 and sum(gameData.selfHand) - gameData.selfHand[0] > 20 and gameData.getTrickDiff() > 0:
        return True;
    if len(gameData.selfHand) ==1 and gameData.getTrickDiff() > 0:
        return True;
    if gameData.opponentPoints == 9:
        if len(gameData.selfHand) ==5 and sum(gameData.selfHand) - gameData.selfHand[0] > 35:
            return True;
        if len(gameData.selfHand) ==4 and sum(gameData.selfHand) - gameData.selfHand[0] > 26:
            return True;
        if len(gameData.selfHand) ==3 and sum(gameData.selfHand) - gameData.selfHand[0] > 17 and gameData.getTrickDiff() > 0:
            return True;
        if len(gameData.selfHand) ==1 and gameData.getTrickDiff() > 0:
            return True;
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
    sub = gameData.selfHand[0]
    if isPlayingSecond :
        for i in gameData.selfHand:
            if i > opponentsCard:
                if i - opponentsCard <= 5:
                    return i
                elif sub == opponentsCard:
                    return sub
                else:
                    return gameData.selfHand[0]
            else:
                sub = i
		# if cannot find a bigger one return the least
		return gameData.selfHand[0]
	else :
		return gameData.selfHand[int(math.floor((len(gameData.selfHand) - 1)*(1-gameData.challenge())))]

