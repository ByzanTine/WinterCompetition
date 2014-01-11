import random
class AI:
	def __init__(self):
		self.shaking=2;
		self.shakDecreaseRatio=0.9;
		self.countPeriod=100;#change parameter after *
		self.totalCount=0;
		self.winCount=0;
	
	#returns true if there should be a new parameter assignment
	#false otherwise
	def registerTournamentResult(self, win):
		if win:
			self.winCount+=1;
		self.totalCount+=1;
		return self.totalCount >= self.countPeriod
	def getnewParameters(self, listOfParameters):
		for x in range(0, len(listOfParameters)):
			listOfParameters[x]=listOfParameters[x]*(1+self.shaking*(random.random()-0.5));
		self.shaking*=self.shakDecreaseRatio;
		return listOfParameters;
	