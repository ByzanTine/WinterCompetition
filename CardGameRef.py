# from array import *
import AI_JKL

	#AI
AI_GAME=AI_JKL.AI();
class Data:
	deck=[]
	decksum=0
	decknum=0
	opponentHandsum=0
	opponentHandNum=0
	selfTricks=0
	opponentTricks=0
	selfPoints=0
	opponentPoints=0
	#coefficients
	#*Base is how much it will change in the AI parameter floating
	HandDiffCoefficient=9.836290665392232
	HandDiffCoefficientBase=0.3
	TrickCoefficient=9.836290665392232
	TrickCoefficientBase=0.3
	ChallengeLowerBound=-9.462321304806025
	ChallengeLowerBoundBase=0.5
	ChallengeBoundLength= 19.57615855916059
	ChallengeBoundLengthBase=0.5
	indexfirstBound=0.7140976403820799
	indexfirstBoundBase=0.01
	indexsecondBound=0.7770826012818803
	indexsecondBoundBase=0.01
	decknumRatio=1.194497844125556
	decknumRatioBase=0.1
	def __init__(self):
		self.selfHand=[0,0,0,0,0]
	def updateCoefficientsGame(self, win):
		if AI_GAME.registerTournamentResult(win):
			newParams=AI_GAME.getNewParameters([Data.HandDiffCoefficient, Data.TrickCoefficient, Data.ChallengeLowerBound, Data.ChallengeBoundLength, Data.indexfirstBound,Data.indexsecondBound, Data.decknumRatio],
				[Data.HandDiffCoefficientBase, Data.TrickCoefficientBase, Data.ChallengeLowerBoundBase, Data.ChallengeBoundLengthBase, Data.indexfirstBoundBase, Data.indexsecondBoundBase, Data.decknumRatioBase])
			Data.HandDiffCoefficient=newParams[0]
			Data.TrickCoefficient=newParams[1]
			Data.ChallengeLowerBound=newParams[2]
			Data.ChallengeBoundLength=newParams[3]
			Data.indexfirstBound=newParams[4]
			Data.indexsecondBound=newParams[5]
			Data.decknumRatio=newParams[6]
	def printCoefficient(self):
		print "HandDiffCoefficient "+self.HandDiffCoefficient
		print "TrickCoefficient"+self.TrickCoefficient
		print "ChallengeLowerBound"+self.ChallengeLowerBound
		print "ChallengeBoundLength"+self.ChallengeBoundLength
		print "indexfirstBound"+self.indexfirstBound
		print "indexsecondBound"+self.indexsecondBound

	def getRank(self,val):
		rank=0
		for i in range (0,val-1):
			rank+=self.deck[i]
		rank+=self.deck[val-1]/2
		return rank
	def getTrickDiff(self):
		return self.selfTricks - self.opponentTricks
    #from 0 to 1, chance to win this round
	def challenge(self):
		print "dicknum is "+str(self.decknum)
		print "hand is %s" % self.selfHand
		print "hand rank sum is " + str(self.getHandRankSum())
		print "opp hand rank sum is " + str(self.getOpponentHandRankSum())
		if(len(self.selfHand)!=0):
			index=self.HandDiffCoefficient*1.0*(self.getHandRankSum()-self.getOpponentHandRankSum())/(self.decknum**self.decknumRatio) \
				+ self.TrickCoefficient*1.0*(self.selfTricks-self.opponentTricks)/(len(self.selfHand))
		else:
			index=self.HandDiffCoefficient*1.0*(self.getHandRankSum()-self.getOpponentHandRankSum())/(self.decknum**self.decknumRatio) \
				+ self.TrickCoefficient*1.0*(self.selfTricks-self.opponentTricks)
		
		print "card diff is "+str(1.0*(self.getHandRankSum()-self.getOpponentHandRankSum())/(self.decknum**2))
		print "trick diff is " + str(self.selfTricks-self.opponentTricks)
		ratio=(index-self.ChallengeLowerBound)/self.ChallengeBoundLength
		print "win chance is "+str(ratio)
		if ratio<0:
			return 0
		if ratio>1:
			return 1
		return ratio

	def getHandRankSum(self):
		for i in self.selfHand:
			self.deck[i-1]+=1
		rankValue = 0
		for i in self.selfHand:
			rankValue+=self.getRank(i)
		for i in self.selfHand:
			self.deck[i-1]-=1
		return rankValue

	def getOpponentHandRankSum(self):

		# print "cache is "+str(self.ohrs_cache)
		try:
			self.ohrs_cache
		except AttributeError:
			self.ohrs_cache=" "
		if self.ohrs_cache == " ":
			for i in self.selfHand:
				self.deck[i-1]+=1
			rankValue = 0
			for i in self.selfHand:
				rankValue+=self.getRank(i)
			oppRank=((self.decknum+len(self.selfHand)+1)*(self.decknum+len(self.selfHand))/2-rankValue)*self.opponentHandNum/self.decknum
			for i in self.selfHand:
				self.deck[i-1]-=1
			self.ohrs_cache=oppRank
			return oppRank
		else:
			return self.ohrs_cache
	def shuffle(self):
		self.decksum=0

		while(len(self.deck)!=0):
			self.deck.pop()

		
		for i in range(0,13):
			#self.decksum=i*8+8+self.decksum
			
			self.deck.append(8)
			self.decksum=(i+1)*8+self.decksum
			self.decknum=104
	def gameStart(self,hand):
		# console.log("gameStart")
		print "gameStart"
		self.selfTricks=0
		self.opponentTricks=0
		self.selfHand=[0,0,0,0,0]
		
		self.selfHand=sorted(hand)
		# self.getHandRankSum()=0
		for i in range(len(self.selfHand)):
			# self.getHandRankSum()+=self.selfHand[i]
			self.decksum-=self.selfHand[i]
		print "gameStart, decknum -5"
		self.decknum-=5
		self.opponentHandNum=5
		self.ohrs_cache=" "
	def gameEnd(self):
		self.selfTricks=0
		self.opponentTricks=0
		print "gameEnd, decknum -" +str(self.opponentHandNum)
		self.decknum-=self.opponentHandNum
		self.decksum-=(self.decksum/self.decknum)*self.opponentHandNum
		self.opponentHandNum=0
		if(self.decknum<10):
			self.shuffle()

		while(len(self.selfHand)!=0):
			self.selfHand.pop()
		self.selfHand=[0,0,0,0,0]
	#make sure handval exist
	def updateHand(self,handval):
		
		self.selfHand.remove(handval)
	def cardExposed(self,cardval):
		self.deck[cardval-1]-=1
		self.decksum-=cardval
		self.decknum-=1
		self.opponentHandNum-=1
		for i in self.selfHand:
			self.deck[i-1]+=1
		self.getOpponentHandRankSum()
		self.ohrs_cache-=self.getRank(cardval)
		for i in self.selfHand:
			self.deck[i-1]-=1
		
# x=Data()
# x.shuffle()
# print x.getRank(1)
# print len(x.deck)
# print x.decksum
# print x.deck[7]

# x.shuffle()
# print len(x.deck)
# x.gameStart([1,3,4,5,6])
# print x.selfHand
# print "getHandRankSum():"
# print x.getHandRankSum()
# x.selfTricks=x.selfTricks+1
# print x.selfTricks
# x.challenge()
# x.updateHand(5)
# print x.selfHand
# print x.getHandRankSum()
# x.gameEnd()
# print x.selfHand
# print "opponentHandsum: "
# print x.getOpponentHandRSum(5)
