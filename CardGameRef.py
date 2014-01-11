# from array import *

class Data:
    deck=[]
    decksum=0
    selfHandsum=0
    selfHand=[0,0,0,0,0]
    opponentHandsum=0
    selfTricks=0
    opponentTricks=0
    HandDiffCoefficient=0;
    TrickCoefficient=0;


    def getRank(self):
        return 1


    def getDecksum(self):
    	return decksum
    def getSelfHandSum(self):
    	return selfHandsum
    def getOpponentHandSum(self):
    	return opponentHandsum
   	def getSelfTricks(self):
   		return selfTricks
   	def getOpponentTricks(self):
   		return opponentTricks
   	def getHandDiffCofficient(self):
   		return HandDiffCoefficient
   	def getTrickCoefficient(self):
   		return TrickCoefficient
   	def getTrickDiff(self):
   		return selfTricks-opponentTricks
    #originate Vals
    def shuffle(self):
    	decksum=0
    	while(len(self.deck)!=0):
			self.deck.pop()

		
    	for i in range(0,13):
 			#self.decksum=i*8+8+self.decksum
        	self.deck.append(8)
        	self.decksum=i*8+8+self.decksum

    def gameStart(self,hand):
    	selfTricks=0
    	opponentTricks=0
    	self.selfHand=hand

    def gameEnd(self):
    	selfTricks=0
    	opponentTricks=0
    	while(len(self.selfHand)!=0):
    		self.selfHand.pop()
    	selfHandsum=0

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