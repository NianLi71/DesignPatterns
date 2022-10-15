import random

from NumberGenerator import NumberGenerator

class RandomNumberGenerator(NumberGenerator):
	def __int__(self):
		super().__int__()
		self.number = 0

	def getNumber(self):
		return self.number

	def excute(self):
		for i in range(20):
			self.number = random.randint(1, 10)
			self.notifyObservers()