# from array import *
import AI_JKL

class Data:
	deck=[]
	decksum=0
	decknum=0
	selfHand=[0,0,0,0,0]
	opponentHandsum=0
	opponentHandNum=0
	selfTricks=0
	opponentTricks=0
	#coefficients
	#*Base is how much it will change in the AI parameter floating
	HandDiffCoefficient=10
	HandDiffCoefficientBase=0
	TrickCoefficient=10
	TrickCoefficientBase=0
	ChallengeLowerBound=-10
	ChallengeLowerBoundBase=0
	ChallengeBoundLength=20
	ChallengeBoundLengthBase=0
	indexfirstBound=0.7
	indexfirstBoundBase=0
	indexsecondBound=0.8
	indexsecondBoundBase=0

	#AI
	AI_GAME=AI_JKL.AI();
	def updateCoefficientsGame(self, win):
		if self.AI_GAME.registerTournamentResult(win):
			newParams=self.AI_GAME.getNewParameters([self.HandDiffCoefficient, self.TrickCoefficient, self.ChallengeLowerBound, self.ChallengeBoundLength, self.indexfirstBound, self.indexsecondBound],
				[self.HandDiffCoefficientBase, self.TrickCoefficientBase, self.ChallengeLowerBoundBase, self.ChallengeBoundLengthBase, self.indexfirstBoundBase, self.indexsecondBoundBase])
			self.HandDiffCoefficient=newParams[0]
			self.TrickCoefficient=newParams[1]
			self.ChallengeLowerBound=newParams[2]
			self.ChallengeBoundLength=newParams[3]
			self.indexfirstBound=newParams[4]
			self.indexsecondBound=newParams[5]
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
		index=self.HandDiffCoefficient*1.0*(self.getHandRankSum()-self.getOpponentHandRankSum())/(self.decknum**2) \
			+ self.TrickCoefficient*1.0*(self.selfTricks-self.opponentTricks)/(len(self.selfHand))
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
