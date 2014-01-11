# from array import *

class Data:
	deck=[]
	decksum=0
	selfHandsum=0
	selfHand=[0,0,0,0,0]
	opponentHandsum=0
	selfTricks=0
	opponentTricks=0
	HandDiffCoefficient=0
	TrickCoefficient=0


	def getRank(self):
		return 1

	def challenge(self):
		index=self.HandDiffCoefficient*(self.selfHandsum-self.opponentHandsum) + self.TrickCoefficient*(self.selfTricks-self.opponentTricks)
		#print "challenge index: "
		#print a
		return index

	def shuffle(self):
		self.decksum=0
		while(len(self.deck)!=0):
			self.deck.pop()

		
		for i in range(0,13):
			#self.decksum=i*8+8+self.decksum
			self.deck.append(8)
			self.decksum=i*8+8+self.decksum

	def gameStart(self,hand):
		self.selfTricks=0
		self.opponentTricks=0
		self.selfHand=hand

	def gameEnd(self):
		self.selfTricks=0
		self.opponentTricks=0
		while(len(self.selfHand)!=0):
			self.selfHand.pop()
		self.selfHandsum=0
	def updateHand(handval):
		deck[handval-1]-=1

x=Data()
x.shuffle()
print x.getRank()
print len(x.deck)
print x.decksum
print x.deck[7]

x.shuffle()
print len(x.deck)
x.gameStart([1,3,4,5,6])
print x.selfHand
x.gameEnd()
print x.selfHand
x.selfTricks=x.selfTricks+1
print x.selfTricks
x.challenge()


