import random
import sys
class AI:
	winCount=0
	#returns true if there should be a new parameter assignment
	#false otherwise
	lastWinPercentage=0
	lastListOfParameters=[]
	def __init__(self, totalCount = 6000, shakDecreaseRatio=0.95, countPeriod=100, shaking=2):
		print "new AI created"
		self.totalCount=totalCount;
		self.shakDecreaseRatio=shakDecreaseRatio;
		self.countPeriod=countPeriod;
		self.shaking=shaking;
	
	def registerTournamentResult(self, win):
		if win:
			self.winCount+=1
		self.totalCount+=1
		return self.totalCount >= self.countPeriod
	def getNewParameters(self, listOfParameters, listOfBases):
		sys.stderr.write(("for %s" % listOfParameters)+", winRate is "+str(self.winCount*1.0/self.totalCount)+" "+str(self.lastWinPercentage)+"\n")
		if self.lastWinPercentage > self.winCount*1.0/self.totalCount :
			print "fallback"
			listOfParameters=self.lastListOfParameters
		else :
			self.lastListOfParameters=listOfParameters
			self.lastWinPercentage=self.winCount*1.0/self.totalCount
		for x in range(0, len(listOfParameters)):
			listOfParameters[x]=listOfParameters[x]+listOfBases[x]*self.shaking*(random.random()-0.5);
		self.shaking*=self.shakDecreaseRatio;
		self.totalCount=0
		self.winCount=0
		print "new parameter is %s" % listOfParameters
		return listOfParameters;
# for i in range(10000):
# 
