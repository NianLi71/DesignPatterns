from abc import ABC, abstractmethod

class Display(ABC):
	@abstractmethod
	def getColums(self):
		pass

	@abstractmethod
	def getRows(self):
		pass

	@abstractmethod
	def getRowText(self, row):
		pass

	def show(self):
		for i in range(self.getRows()):
			print(self.getRowText(i))