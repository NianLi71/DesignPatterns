from abc import ABC, abstractmethod

class Entry(ABC):
	@abstractmethod
	def getName(self):
		pass

	@abstractmethod
	def getSize(self):
		pass

	# @abstractmethod
	# def add(self, entry):
	# 	pass

	@abstractmethod
	def printList(self, prefix=''):
		pass

	def __str__(self):
		return self.getName() + ' (' + str(self.getSize()) + ')' 