# from array import *

class Data:
    deck=[]
    decksum=0
    selfHandsum=0
    selfHand=[]
    opponentHandsum=0
    selfTricks=0
    opponentTricks=0
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
   	
    #originate Vals
    def shuffle(self):
    	for i in range(0,13):
 			#self.decksum=i*8+8+self.decksum
        	self.deck.append(8)
        	self.decksum=i*8+8+self.decksum


x=Data()
x.shuffle()
print x.getRank()
print len(x.deck)
print x.decksum
print x.deck[7]