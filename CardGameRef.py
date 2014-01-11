# from array import *

class Data:
	deck=[]
	decksum=0
	decknum=0
	selfHandsum=0
	selfHand=[0,0,0,0,0]
	opponentHandsum=0
	selfTricks=0
	opponentTricks=0

  #coefficients
	HandDiffCoefficient=0
  HandDiffCoefficientBase=2
	TrickCoefficient=0
  TrickCoefficientBase=10
  ChallengeLowerBound=-10
  ChallengeLowerBoundBase=-10
  ChallengeBoundLength=20
  ChallengeBoundLengthBase=10
	indexfirstBound=0
	indexsecondBound=0
	def getRank(self,val):
		rank=0
		for i in range (0,val-1):
			rank+=self.deck[i]
		rank+=self.deck[val-1]/2
		return rank

#from 0 to 1, chance to win this round
	def challenge(self):
		index=self.HandDiffCoefficient*(self.selfHandsum-self.opponentHandsum) + self.TrickCoefficient*(self.selfTricks-self.opponentTricks)
		ratio=(index-ChallengeLowerBound)/ChallengeBoundLength
    if ratio<0:
      return 0
    if ratio>1:
      return 1
    return ratio

	def getOpponentHandSum(self,cardnum):
		self.opponentHandsum = (self.decksum/self.decknum)*cardnum
		return self.opponentHandsum
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
		self.selfHand=hand
		self.selfHandsum=0
		for i in range(len(self.selfHand)):
			self.selfHandsum+=self.selfHand[i]
		self.decknum-=5

	def gameEnd(self):
		self.selfTricks=0
		self.opponentTricks=0

		while(len(self.selfHand)!=0):
			self.selfHand.pop()
		self.selfHandsum=0
	#make sure handval exist
	def updateHand(self,handval):
		self.deck[handval-1]-=1
		self.decksum-=handval
		self.decknum-=1
		self.selfHand.remove(handval)
		self.selfHandsum-=handval
	def cardExposed(self,cardval):
		self.deck[cardval-1]-=1
		self.decksum-=cardval
		self.decknum-=1
		
x=Data()
x.shuffle()
print x.getRank(1)
print len(x.deck)
print x.decksum
print x.deck[7]

x.shuffle()
print len(x.deck)
x.gameStart([1,3,4,5,6])
print x.selfHand
print "selfHandsum:"
print x.selfHandsum
x.selfTricks=x.selfTricks+1
print x.selfTricks
x.challenge()
x.updateHand(5)
print x.selfHand
print x.selfHandsum
x.gameEnd()
print x.selfHand
print "opponentHandsum: "
print x.getOpponentHandSum(5)
