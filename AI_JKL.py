import random
class AI:
	shaking=2
	shakDecreaseRatio=0.9
	countPeriod=100
	totalCount=0
	winCount=0
	#returns true if there should be a new parameter assignment
	#false otherwise
	def registerTournamentResult(self, win):
		if win:
			self.winCount+=1;
		self.totalCount+=1;
		return self.totalCount >= self.countPeriod
	def getnewParameters(self, listOfParameters, listOfBases):
		for x in range(0, len(listOfParameters)):
			listOfParameters[x]=listOfParameters[x]*(1+self.shaking*(random.random()-0.5));
		self.shaking*=self.shakDecreaseRatio;
		totalCount=0
		winCount=0
		return listOfParameters;
# ai = AI();
# for i in range(10000):
# 